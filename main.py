import asyncio
import logging
import random
from datetime import datetime, timedelta
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from instagrapi import Client
import os
from dotenv import load_dotenv

load_dotenv()

# ================= SOZLAMALAR =================
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
INSTA_USERNAME = os.getenv("INSTA_USERNAME")
INSTA_PASSWORD = os.getenv("INSTA_PASSWORD")

DAILY_LIMIT = int(os.getenv("DAILY_LIMIT", "50"))
MIN_DELAY = int(os.getenv("MIN_DELAY", "30"))
MAX_DELAY = int(os.getenv("MAX_DELAY", "120"))
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()
cl = Client()
cl.delay_range = [MIN_DELAY, MAX_DELAY]

# Global o'zgaruvchilar
is_running = False
today_followed = 0
last_reset = datetime.now()

# ================= YORDAMCHI FUNKSIYALAR =================
async def reset_daily_count():
    global today_followed, last_reset
    if datetime.now().date() > last_reset.date():
        today_followed = 0
        last_reset = datetime.now()

def is_admin(user_id: int) -> bool:
    return user_id == ADMIN_ID

# ================= ASOSIY FUNKSIYA =================
async def follow_users(count: int, message: Message):
    global is_running, today_followed
    
    if not is_admin(message.from_user.id):
        await message.answer("❌ Sizga ruxsat yo'q! Faqat admin.")
        return
    
    if is_running:
        await message.answer("⚠️ Bot allaqachon ishlamoqda!")
        return
    
    await reset_daily_count()
    
    if today_followed >= DAILY_LIMIT:
        await message.answer(f"⏳ Bugungi limit ({DAILY_LIMIT}) tugadi. Ertaga urinib ko'ring.")
        return
    
    is_running = True
    followed_today = 0
    errors = 0
    
    try:
        await message.answer("🔐 Instagram bilan bog'lanmoqda...")
        cl.login(INSTA_USERNAME, INSTA_PASSWORD)
        await message.answer("✅ Instagram login muvaffaqiyatli!")
        
        await message.answer(
            f"🚀 {count} ta follow boshlandi!\n"
            f"⏱ Har bir follow orasida: {MIN_DELAY}-{MAX_DELAY} soniya\n"
            f"📊 Bugungi limit: {today_followed}/{DAILY_LIMIT}"
        )
        
        # Hashtag orqali odamlarni topish
        medias = cl.hashtag_medias_recent("f4f", amount=count*3)
        
        for media in medias:
            if followed_today >= count or today_followed >= DAILY_LIMIT:
                break
            
            # Xato limiti
            if errors >= 5:
                await message.answer("⚠️ 5 ta xato ketdi. Jarayon to'xtatilmoqda...")
                break
                
            user = media.user
            
            # O'zimizni follow qilmaymiz
            if user.username == INSTA_USERNAME:
                continue
            
            try:
                cl.user_follow(user.pk)
                followed_today += 1
                today_followed += 1
                
                await message.answer(
                    f"✅ Follow qilindi: @{user.username}\n"
                    f"📊 Jami: {today_followed}/{DAILY_LIMIT}"
                )
                
                # Random kutish (xavfsizlik uchun)
                wait_time = random.randint(MIN_DELAY, MAX_DELAY)
                await asyncio.sleep(wait_time)
                
            except Exception as e:
                errors += 1
                error_msg = str(e)[:100]
                await message.answer(f"❌ Xato: @{user.username} — {error_msg}")
                await asyncio.sleep(random.randint(60, 120))  # Xatoda uzoq kutish
                
    except Exception as e:
        await message.answer(f"❌ Kritik xato: {str(e)[:200]}")
    finally:
        is_running = False
        await message.answer(
            f"🏁 Jarayon tugadi!\n"
            f"✅ Bugun: {today_followed}/{DAILY_LIMIT}\n"
            f"❌ Xatolar: {errors}"
        )

# ================= BUYRUQLAR =================
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 Instagram Follow Botga xush kelibsiz!\n\n"
        "📋 Buyruqlar:\n"
        "/follow 50 — 50 ta follow boshlash (faqat admin)\n"
        "/status — Bot holatini ko'rish\n"
        "/stop — Jarayonni to'xtatish\n\n"
        "⚠️ Instagram qoidalarini buzish xavflidir!"
    )

@dp.message(Command("follow"))
async def cmd_follow(message: Message):
    if not is_admin(message.from_user.id):
        await message.answer("❌ Faqat admin foydalanishi mumkin!")
        return
        
    try:
        count = int(message.text.split()[1])
        count = min(count, 100)  # Bir martada maks 100
        await follow_users(count, message)
    except IndexError:
        await message.answer("❌ Foydalanish: /follow 50")
    except ValueError:
        await message.answer("❌ Son kiriting: /follow 50")

@dp.message(Command("status"))
async def status(message: Message):
    await reset_daily_count()
    await message.answer(
        f"📊 Bot Holati:\n"
        f"📈 Bugun follow: {today_followed}/{DAILY_LIMIT}\n"
        f"⏱ Kutish: {MIN_DELAY}-{MAX_DELAY} soniya\n"
        f"🤖 Holat: {'🟢 Ishlamoqda' if is_running else '🔴 Kutmoqda'}"
    )

@dp.message(Command("stop"))
async def stop_bot(message: Message):
    global is_running
    if not is_admin(message.from_user.id):
        await message.answer("❌ Faqat admin!")
        return
    
    is_running = False
    await message.answer("🛑 Bot to'xtatildi!")

# ================= BOTNI ISHGA TUSHIRISH =================
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("🚀 Bot ishga tushdi...")
    asyncio.run(main())
