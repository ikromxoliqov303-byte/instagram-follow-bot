#!/usr/bin/env python3
import subprocess
import sys
import os

print("🚀 Instagram Follow Bot ishga tushirilmoqda...\n")

# 1. pip ni yangilash
print("📦 pip yangilanmoqda...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
print("✅ pip yangilandi!\n")

# 2. requirements.txt o'rnatish
print("📥 Kutubxonalar o'rnatilmoqda...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
print("✅ Barcha kutubxonalar o'rnatildi!\n")

# 3. .env tekshirish
print("🔍 .env fayli tekshirilmoqda...")
if os.path.exists(".env"):
    print("✅ .env fayli topildi!\n")
else:
    print("❌ .env fayli topilmadi! .env.example ni .env ga nomi o'zgarting.\n")
    sys.exit(1)

# 4. Bot ishga tushirish
print("🤖 Bot ishga tushirilmoqda...\n")
print("=" * 50)
subprocess.call([sys.executable, "main.py"])
