# Instagram Auto-Follow Telegram Bot 🤖

Instagram bilan Telegram orqali avtomatik follow qilish uchun bot.

## ⚠️ MUHIM OGOHLANTIRISH

**Bu bot Instagram Terms of Service qoidalarini buzadi!**

- Instagram avtomatik follow/unfollow qilishni taqiqlab qo'ygan
- Ushbu botni foydalanish akkauntingizni bloklanishiga olib kelishi mumkin
- Shaxsiy xavfda foydalanish uchun

## 📋 Talablar

- Python 3.8+
- pip (paket menejeri)
- Telegram Bot Token (@BotFather dan)
- Instagram akkaunt (login/parol)

## 🚀 O'rnatish

### 1. Repository klonlash
```bash
git clone https://github.com/ikromxoliqov303-byte/instagram-follow-bot.git
cd instagram-follow-bot
```

### 2. Virtual Environment yaratish
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# yoki
venv\\Scripts\\activate  # Windows
```

### 3. Dependencies o'rnatish
```bash
pip install -r requirements.txt
```

### 4. .env faylini sozlash

`.env.example` ni `.env` ga nomi o'zgarting va ma'lumotlarni kiriting:

```bash
cp .env.example .env
```

`.env` faylini to'ldiring:
```
TELEGRAM_TOKEN=your_token_here
INSTA_USERNAME=shunchaki0209
INSTA_PASSWORD=elbek1234
ADMIN_ID=7492481933
DAILY_LIMIT=10000
MIN_DELAY=30
MAX_DELAY=10000
```

## 🎮 Ishga Tushirish

```bash
python main.py
```

## 📖 Buyruqlar

| Buyruq | Tavsifi |
|--------|----------|
| `/start` | Botga salom va yordam |
| `/follow 50` | 50 ta follow boshlash (faqat admin) |
| `/status` | Bot holatini ko'rish |
| `/stop` | Jarayonni to'xtatish |

## ⚙️ Sozlamalar

| O'zgaruvchi | Qiymati | Tavsifi |
|------------|---------|----------|
| `TELEGRAM_TOKEN` | - | Telegram bot tokeni |
| `INSTA_USERNAME` | `shunchaki0209` | Instagram username |
| `INSTA_PASSWORD` | `elbek1234` | Instagram parol |
| `ADMIN_ID` | `7492481933` | Admin Telegram ID |
| `DAILY_LIMIT` | `10000` | Kunlik follow limiti |
| `MIN_DELAY` | `30` | Minimal kutish (soniya) |
| `MAX_DELAY` | `10000` | Maksimal kutish (soniya) |

## 🔒 Xavfsizlik

- `.env` faylini hech qachon GitHub'ga supmang
- `.gitignore` faylida `.env` mavjud
- Parol va tokenlarni hech kimga aytmang
- Regular password almashtirishni o'ylang

## 🛠️ Troubleshooting

### Instagram Login xatosi
```
LoginError: 400 Bad Request
```
- Username va parolni tekshiring
- Instagram akkauntni tekshiring (bloklanmagan bo'lsin)

### Telegram bot javob bermayapti
```
BadRequest: CHAT_NOT_FOUND
```
- ADMIN_ID to'g'ri ekanligini tekshiring
- Bot'ni /start bilan ishga tushiring

## 📝 Litsenziya

MIT License - Shaxsiy foydalanish uchun

## ⚖️ Javobgarchilik

Bu botni foydalanish orqali oralgan barcha natijalarga siz javob berasiz. Instagram qoidalarini buzish uchun meni javobgarch emas.

---

**Savollar?** GitHub Issues orqali yozib qo'ying 💬
