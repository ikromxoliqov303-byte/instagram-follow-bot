#!/usr/bin/env python3
"""
Avtomatik Bot Launcher - HAMMASI AVTOMATIK!
Bu script barcha kerakli qadamlarni avtomatik bajaradi
"""

import subprocess
import sys
import os
import platform

def run_command(cmd, description):
    """Buyruqni ishga tushirish"""
    print(f"\n{'='*50}")
    print(f"🔄 {description}...")
    print(f"{'='*50}\n")
    try:
        if isinstance(cmd, str):
            subprocess.check_call(cmd, shell=True)
        else:
            subprocess.check_call(cmd)
        print(f"✅ {description} tugadi!\n")
        return True
    except Exception as e:
        print(f"❌ Xato: {e}\n")
        return False

def main():
    print("\n" + "="*60)
    print("🚀 INSTAGRAM FOLLOW BOT - AVTOMATIK LAUNCHER")
    print("="*60 + "\n")
    
    # 1. pip ni yangilash
    print("BOSQICH 1: pip yangilash")
    run_command(
        [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
        "pip yangilash"
    )
    
    # 2. requirements.txt o'rnatish
    print("BOSQICH 2: Kutubxonalar o'rnatish")
    if not os.path.exists("requirements.txt"):
        print("❌ requirements.txt topilmadi!")
        sys.exit(1)
    
    run_command(
        [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
        "Python kutubxonalari o'rnatish"
    )
    
    # 3. .env tekshirish
    print("BOSQICH 3: .env tekshirish")
    if not os.path.exists(".env"):
        print("❌ .env fayli topilmadi!")
        print("⚠️ .env.example ni .env ga nomi o'zgarting!")
        sys.exit(1)
    print("✅ .env fayli topildi!\n")
    
    # 4. Bot ishga tushirish
    print("BOSQICH 4: BOT ISHGA TUSHIRISH")
    print("\n" + "="*60)
    print("🤖 BOT ISHGA TUSHDI!")
    print("="*60)
    print("\n💡 Telegram: @instagram_maining_bot")
    print("📝 Buyruqlar: /start, /follow, /status, /stop\n")
    print("="*60 + "\n")
    
    # Bot ishga tushir
    try:
        subprocess.call([sys.executable, "main.py"])
    except KeyboardInterrupt:
        print("\n⏹️ Bot to'xtatildi.")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Xato: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
