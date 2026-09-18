@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul
cd /d "%~dp0"
title HE THONG NHAN DIEN 100 LOAI TRAI CAY - DE TAI 22 (AI)

echo ======================================================================
echo   CHUONG TRINH NHAN DIEN VA PHAN LOAI TRAI CAY (TRI TUE NHAN TAO)
echo   De tai so 22 - Deep Learning MobileNetV2 / YOLOv8 + Active Learning
echo ======================================================================
echo.

:: 1. Kiem tra Python tren may tinh
python --version >nul 2>&1
if %errorlevel% neq 0 (
    if exist "C:\Program Files\Python313\python.exe" (
        set "PATH=C:\Program Files\Python313;C:\Program Files\Python313\Scripts;!PATH!"
    ) else if exist "C:\Program Files\Python312\python.exe" (
        set "PATH=C:\Program Files\Python312;C:\Program Files\Python312\Scripts;!PATH!"
    ) else if exist "C:\Program Files\Python311\python.exe" (
        set "PATH=C:\Program Files\Python311;C:\Program Files\Python311\Scripts;!PATH!"
    ) else if exist "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" (
        set "PATH=%LOCALAPPDATA%\Programs\Python\Python313;%LOCALAPPDATA%\Programs\Python\Python313\Scripts;!PATH!"
    ) else if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
        set "PATH=%LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Python312\Scripts;!PATH!"
    ) else (
        echo [LOI NGHIEP TRONG] May tinh nay chua cai dat Python hoac chua them vao PATH!
        echo.
        echo Huong dan:
        echo 1. Cai dat Python 3.10 tro len tai https://www.python.org/downloads/
        echo 2. Khi cai dat, NHO TICH VAO O: [x] Add python.exe to PATH
        echo 3. Sau do mo lai file run_app.bat nay!
        echo ======================================================================
        pause
        exit /b 1
    )
)

:: 2. Tu dong kiem tra va cai dat thu vien con thieu (Khi mang sang may khac)
python -c "import streamlit, cv2, PIL, numpy, matplotlib" >nul 2>&1
if %errorlevel% neq 0 (
    echo [*] Phat hien may tinh moi chua co du thu vien can thiet!
    echo [*] Dang tu dong cai dat thu vien tu requirements.txt - Vui long cho 1-2 phut...
    echo.
    python -m pip install -r requirements.txt
    if !errorlevel! neq 0 (
        echo.
        echo [CANH BAO] Khong the tu dong tai thu vien do chua ket noi Internet.
        echo Hay dam bao may tinh co ket noi mang va chay lenh: pip install -r requirements.txt
        echo ======================================================================
        pause
    )
)

echo [*] Moi truong Python va thu vien da san sang!
echo [*] Dang khoi dong Web App tai: http://localhost:8501 ...
echo.

:: 3. Mo trinh duyet sau 1 giay
start "" http://localhost:8501

:: 4. Khoi chay Streamlit
python -m streamlit run app.py --server.port 8501 --server.headless false

if %errorlevel% neq 0 (
    echo.
    echo [THONG BAO] Streamlit da dung hoac gap su co.
    pause
)
