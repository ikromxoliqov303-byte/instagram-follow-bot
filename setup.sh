#!/bin/bash

echo "🚀 Instagram Follow Bot o'rnatilmoqda..."
echo ""

# 1. Git clone
echo "📥 Repository yuklab olinmoqda..."
git clone https://github.com/ikromxoliqov303-byte/instagram-follow-bot.git
cd instagram-follow-bot

echo "✅ Repository yuklab olindi!"
echo ""

# 2. Virtual Environment (ixtiyoriy, lekin tavsiya etiladi)
echo "🐍 Virtual Environment yaratilmoqda..."
python -m venv venv

# Aktivlashtirish
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows
    source venv/Scripts/activate
else
    # Linux/Mac
    source venv/bin/activate
fi

echo "✅ Virtual Environment aktivlashtirildi!"
echo ""

# 3. Dependencies o'rnatish
echo "📦 Python kutubxonalari o'rnatilmoqda..."
pip install -r requirements.txt

echo "✅ Barcha kutubxonalar o'rnatildi!"
echo ""

# 4. Bot ishga tushirish
echo "🤖 Bot ishga tushirilmoqda..."
echo ""
python main.py
