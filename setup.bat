@echo off
chcp 65001 >nul
echo 🚀 Instagram Follow Bot o'rnatilmoqda...
echo.

REM 1. Git clone
echo 📥 Repository yuklab olinmoqda...
git clone https://github.com/ikromxoliqov303-byte/instagram-follow-bot.git
cd instagram-follow-bot

echo ✅ Repository yuklab olindi!
echo.

REM 2. Virtual Environment
echo 🐍 Virtual Environment yaratilmoqda...
python -m venv venv
call venv\Scripts\activate.bat

echo ✅ Virtual Environment aktivlashtirildi!
echo.

REM 3. Dependencies o'rnatish
echo 📦 Python kutubxonalari o'rnatilmoqda...
pip install -r requirements.txt

echo ✅ Barcha kutubxonalar o'rnatildi!
echo.

REM 4. Bot ishga tushirish
echo 🤖 Bot ishga tushirilmoqda...
echo.
python main.py
pause
