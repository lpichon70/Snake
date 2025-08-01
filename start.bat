@echo off
chcp 65001 > nul
IF NOT EXIST "env\" (
    echo Création de l'environnement virtuel...
    python -m venv env
)

call env\Scripts\activate.bat

IF EXIST requirements.txt (
    echo Installation des dépendances...
    pip install -r requirements.txt
)

python main.py
pause