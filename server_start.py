#!/usr/bin/env python3
"""
🚀 INSTAGRAM FOLLOW BOT - SERVER VERSION
Bu bot Telegram'da 24/7 ishlaydi!
"""

import os
import sys
from pathlib import Path

# .env fayli yaratish (agar mavjud bo'lmasa)
env_content = """# 🤖 INSTAGRAM FOLLOW BOT SETTINGS

# Telegram Bot Token
TELEGRAM_TOKEN=8701515072:AAHALF8PMu33Xh95xfmK8JMmHnjw2cQ38uU

# Instagram hissobi
INSTA_USERNAME=shunchaki0209
INSTA_PASSWORD=elbek1234

# Admin ID (sizning Telegram ID)
ADMIN_ID=7492481933

# Sozlamalar
DAILY_LIMIT=10000
MIN_DELAY=30
MAX_DELAY=10000
"""

# .env yaratish
if not os.path.exists(".env"):
    print("📝 .env fayli yaratilmoqda...\n")
    with open(".env", "w") as f:
        f.write(env_content)
    print("✅ .env fayli yaratildi!\n")

# Requirements o'rnatish
print("📦 Kutubxonalar o'rnatilmoqda...\n")
import subprocess
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "-q"])
print("✅ Kutubxonalar o'rnatildi!\n")

# Bot ishga tushirish
print("="*60)
print("🚀 BOT SERVER'DA ISHGA TUSHDI!")
print("="*60)
print("\n✨ Bot 24/7 ishlaydi!")
print("💡 Telegram: @instagram_maining_bot")
print("📝 Buyruqlar: /start, /follow 50, /status, /stop")
print("\n" + "="*60 + "\n")

# Main bot code
subprocess.call([sys.executable, "main.py"])
