# Local setup on Windows

## 1. Create the repository on GitHub

Suggested name:

```text
BotTradeNC-AI-Native
```

Suggested visibility at the beginning:

```text
Private
```

## 2. Clone or initialize locally

From the folder where this starter was extracted:

```powershell
git init
git add .
git commit -m "Initial AI-native BotTradeNC repository structure"
git branch -M main
git remote add origin https://github.com/MauroPresso/BotTradeNC-AI-Native.git
git push -u origin main
```

If you use GitHub CLI:

```powershell
gh repo create MauroPresso/BotTradeNC-AI-Native --private --source . --remote origin --push
```

## 3. Create virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

## 4. Initialize database

```powershell
python scripts/init_db.py
```

## 5. Run tests

```powershell
pytest
```
