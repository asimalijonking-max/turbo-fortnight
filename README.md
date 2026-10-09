# Aizen-style Telegram Bot

یہ bot فراہم کردہ screen recording کے menu style سے متاثر ہو کر بنایا گیا ایک نیا standalone Python bot ہے۔

## شامل options

- numbers — فی الحال صرف coming soon message
- status
- traffic
- balance
- Refer & Earn

## جان بوجھ کر شامل نہیں کیے گئے

- stock option
- Create Session option
- numbers کے اندر countries
- numbers کے اندر apps
- numbers کے اندر actual phone numbers

## GitHub پر upload

GitHub پر ایک نئی repository بنائیں، پھر اس folder کی files upload کریں:

- `bot.py`
- `requirements.txt`
- `Procfile`
- `README.md`
- `.gitignore`

## Railway deployment

1. Railway کھولیں اور **New Project** منتخب کریں۔
2. **Deploy from GitHub Repo** پر کلک کریں۔
3. اپنی GitHub repository منتخب کریں۔
4. Railway کے **Variables** میں یہ variable شامل کریں:

```text
BOT_TOKEN=BotFather سے ملا ہوا Telegram token
```

5. Deploy کریں۔ `Procfile` کی وجہ سے bot `python bot.py` سے run ہوگا۔
6. Logs میں `Aizen-style bot شروع ہو گیا ہے` نظر آئے تو deployment کامیاب ہے۔

## Local test

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export BOT_TOKEN="آپ کا token"
python bot.py
```

Windows PowerShell:

```powershell
$env:BOT_TOKEN="آپ کا token"
python bot.py
```

## اہم بات

Telegram کے عام message text کا اصل رنگ اپنی مرضی سے تبدیل نہیں کیا جا سکتا۔ اس لیے buttons میں emojis اور status labels استعمال کیے گئے ہیں۔ یہ code کسی دوسرے bot کا private code نہیں ہے؛ یہ آپ کے لیے نیا اور الگ implementation ہے۔
