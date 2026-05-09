#!/usr/bin/env python3
"""
🚀 INSTAGRAM FOLLOW BOT - SUPER AVTOMATIK LAUNCHER
Buning ichida HAMMASI bor - faqat ishga tushir va XO'ZI ISHLAYDI!
"""

import subprocess
import sys
import os
import shutil

print("\n" + "="*60)
print("🚀 INSTAGRAM FOLLOW BOT - AVTOMATIK SETUP & LAUNCH")
print("="*60 + "\n")

try:
    # BOSQICH 1: Repository klonlash (agar mavjud bo'lmasa)
    if not os.path.exists("main.py"):
        print("📥 BOSQICH 1: Repository yuklab olinmoqda...\n")
        subprocess.check_call([
            "git", "clone", 
            "https://github.com/ikromxoliqov303-byte/instagram-follow-bot.git",
            "."
        ])
        print("\n✅ Repository yuklab olindi!\n")
    
    # BOSQICH 2: pip yangilash
    print("="*60)
    print("📦 BOSQICH 2: pip yangilash...\n")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "-q"])
    print("✅ pip yangilandi!\n")
    
    # BOSQICH 3: requirements.txt o'rnatish
    print("="*60)
    print("📥 BOSQICH 3: Kutubxonalar o'rnatish...\n")
    if os.path.exists("requirements.txt"):
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "-q"])
        print("\n✅ Barcha kutubxonalar o'rnatildi!\n")
    else:
        print("❌ requirements.txt topilmadi!\n")
        sys.exit(1)
    
    # BOSQICH 4: .env tekshirish
    print("="*60)
    print("🔍 BOSQICH 4: .env tekshirish...\n")
    if not os.path.exists(".env"):
        print("❌ .env topilmadi!")
        print("📝 .env.example ni .env ga nomi o'zgarting!\n")
        sys.exit(1)
    print("✅ .env fayli topildi!\n")
    
    # BOSQICH 5: BOT ISHGA TUSHIRISH
    print("="*60)
    print("🤖 BOSQICH 5: BOT ISHGA TUSHIRILMOQDA!\n")
    print("="*60)
    print("\n✨ Bot ishga tushdi!")
    print("💡 Telegram: @instagram_maining_bot")
    print("📝 Buyruqlar: /start, /follow 50, /status, /stop")
    print("\n" + "="*60 + "\n")
    
    # Bot ishga tushir
    subprocess.call([sys.executable, "main.py"])

except KeyboardInterrupt:
    print("\n\n⏹️ Bot to'xtatildi.")
    sys.exit(0)
except Exception as e:
    print(f"\n❌ XATO: {e}\n")
    sys.exit(1)
