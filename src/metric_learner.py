# metric_learner.py - Metric Learning & FaceID-style Vector Database
import os
import json
import time
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from torchvision.models import mobilenet_v2, MobileNet_V2_Weights
from PIL import Image
import numpy as np

from src.config import CLASS_NAMES, CLASS_INFO

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
DATABASE_PT = os.path.join(DATA_DIR, 'metric_database.pt')
DATABASE_JSON = os.path.join(DATA_DIR, 'metric_database.json')
DATASET_TRAIN_DIR = os.path.join(BASE_DIR, 'dataset', 'train')

_EMBEDDER_MODEL = None
_TRANSFORMS = None

def get_embedder():
    global _EMBEDDER_MODEL, _TRANSFORMS
    if _EMBEDDER_MODEL is None:
        weights = MobileNet_V2_Weights.DEFAULT
        full_model = mobilenet_v2(weights=weights)
        full_model.eval()
        
        class FeatureExtractor(nn.Module):
            def __init__(self, m):
                super().__init__()
                self.features = m.features
                self.pool = nn.AdaptiveAvgPool2d((1, 1))
            def forward(self, x):
                x = self.features(x)
                x = self.pool(x)
                x = torch.flatten(x, 1)
                return F.normalize(x, p=2, dim=1)
                
        _EMBEDDER_MODEL = FeatureExtractor(full_model)
        _TRANSFORMS = weights.transforms()
        
    return _EMBEDDER_MODEL, _TRANSFORMS

def extract_embedding(pil_img):
    model, tf = get_embedder()
    tensor = tf(pil_img.convert('RGB')).unsqueeze(0)
    with torch.no_grad():
        emb = model(tensor)[0]
    return emb

class MetricDatabase:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = MetricDatabase()
        return cls._instance
        
    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        self.prototypes = {}
        self.metadata = {}
        self.samples = []
        self.load()
        
    def load(self):
        if os.path.exists(DATABASE_PT):
            try:
                data = torch.load(DATABASE_PT, map_location='cpu', weights_only=False)
                self.prototypes = data.get('prototypes', {})
                self.metadata = data.get('metadata', {})
                self.samples = data.get('samples', [])
                return
            except Exception:
                pass
        self._initialize_baseline()
        self.save()

    def save(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        torch.save({
            'prototypes': self.prototypes,
            'metadata': self.metadata,
            'samples': self.samples
        }, DATABASE_PT)
        
        summary = {}
        for k, v in self.metadata.items():
            summary[k] = {
                'vn_name': v.get('vn_name', k),
                'icon': v.get('icon', '🍏'),
                'sample_count': v.get('count', 1),
                'last_updated': v.get('last_updated', '')
            }
        with open(DATABASE_JSON, 'w', encoding='utf-8') as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)

    def _initialize_baseline(self):
        for c_name in CLASS_NAMES:
            c_info = CLASS_INFO.get(c_name, {'vn_name': c_name, 'icon': '🍏'})
            self.metadata[c_name] = {
                'vn_name': c_info.get('vn_name', c_name),
                'icon': c_info.get('icon', '🍏'),
                'count': 1,
                'last_updated': 'init'
            }
            c_dir = os.path.join(DATASET_TRAIN_DIR, c_name)
            embs = []
            if os.path.exists(c_dir):
                for f in os.listdir(c_dir)[:5]:
                    if f.lower().endswith(('.jpg', '.png', '.jpeg')):
                        try:
                            im = Image.open(os.path.join(c_dir, f))
                            embs.append(extract_embedding(im))
                        except Exception:
                            pass
            if len(embs) > 0:
                mean_emb = torch.stack(embs).mean(dim=0)
                self.prototypes[c_name] = F.normalize(mean_emb, p=2, dim=0)
            else:
                torch.manual_seed(abs(hash(c_name)) % 100000)
                rand_vec = torch.randn(1280)
                self.prototypes[c_name] = F.normalize(rand_vec, p=2, dim=0)

    def predict(self, pil_cropped_img, top_k=3, temperature=0.08):
        query_emb = extract_embedding(pil_cropped_img)
        classes = list(self.prototypes.keys())
        if not classes:
            return None
            
        proto_tensor = torch.stack([self.prototypes[c] for c in classes])
        similarities = torch.matmul(proto_tensor, query_emb)
        
        logits = similarities / temperature
        probs = F.softmax(logits, dim=0)
        
        top_probs, top_indices = torch.topk(probs, min(top_k, len(classes)))
        
        results = []
        for p, idx in zip(top_probs, top_indices):
            c_name = classes[idx.item()]
            meta = self.metadata.get(c_name, {})
            sim_score = similarities[idx.item()].item()
            results.append({
                'class_name': c_name,
                'vn_name': meta.get('vn_name', c_name),
                'icon': meta.get('icon', '🍏'),
                'probability': float(p.item() * 100.0),
                'cosine_sim': float(sim_score)
            })
            
        best = results[0]
        sim = best['cosine_sim']
        if sim > 0.75:
            conf = min(99.9, max(92.0, 85.0 + sim * 15.0))
        elif sim > 0.50:
            conf = min(90.0, max(70.0, 50.0 + sim * 40.0))
        else:
            conf = max(20.0, min(65.0, sim * 80.0))
            
        return {
            'best_class': best['class_name'],
            'best_vn_name': best['vn_name'],
            'icon': best['icon'],
            'confidence': float(conf),
            'cosine_similarity': float(sim),
            'top_predictions': results
        }

    def learn_fruit(self, pil_cropped_img, class_name, vn_name=None, icon='🍎', user_note=''):
        new_emb = extract_embedding(pil_cropped_img)
        ts = time.strftime('%Y-%m-%d %H:%M:%S')
        
        if class_name in self.prototypes:
            old_proto = self.prototypes[class_name]
            updated = F.normalize(old_proto * 0.4 + new_emb * 0.6, p=2, dim=0)
            self.prototypes[class_name] = updated
            self.metadata[class_name]['count'] = self.metadata[class_name].get('count', 1) + 1
            self.metadata[class_name]['last_updated'] = ts
        else:
            self.prototypes[class_name] = new_emb
            self.metadata[class_name] = {
                'vn_name': vn_name if vn_name else class_name,
                'icon': icon,
                'count': 1,
                'last_updated': ts
            }
            if class_name not in CLASS_NAMES:
                CLASS_NAMES.append(class_name)
            CLASS_INFO[class_name] = {
                'vn_name': vn_name if vn_name else class_name,
                'icon': icon,
                'calories': 'Khoảng 50-60 kcal/100g',
                'vitamins': 'Vitamin C và khoáng chất',
                'benefits': 'Tăng cường sức đề kháng tự nhiên',
                'tips': 'Chọn quả tươi ngon, không dập nát',
                'avg_price_per_kg': 60000
            }

        self.samples.append({
            'class_name': class_name,
            'learned_at': ts,
            'note': user_note
        })
        
        self.save()
        
        f_dir = os.path.join(DATASET_TRAIN_DIR, class_name)
        os.makedirs(f_dir, exist_ok=True)
        img_path = os.path.join(f_dir, f'learned_{int(time.time())}.jpg')
        try:
            pil_cropped_img.convert('RGB').save(img_path, 'JPEG', quality=95)
        except Exception:
            pass
            
        return True

