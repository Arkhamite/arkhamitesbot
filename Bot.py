import asyncio
import logging
import sys

from History import history
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from Fact import fact
from Gemini import gemini
from aiogram.types import URLInputFile
from RedditFetcher import reddit
from aiogram import F, Router
from aiogram.types import Message
from aiogram import Bot, Dispatcher, html, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types.reaction_type_emoji import ReactionTypeEmoji
from aiogram.types import ReactionType

TOKEN = ""
channel_id = -1002112088417
bot = Bot(token=TOKEN)
citizen = 1278478311
scheduler = AsyncIOScheduler(timezone="Asia/Tashkent")

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    if message.chat.id == 1278478311:
        await message.answer(f"Valar Morghulis!")
    else:
        await message.answer("U r not Citizen, so i dont give u access to use this bot!")

user_memes = {}

@dp.message(lambda message: message.chat.id == 1278478311 and message.text.lower().startswith("ask"))
async def ai(message: Message) -> None:
    text = message.text.lower()
    await message.answer(gemini(text[4:len(text)]))

@dp.message(lambda message: message.chat.id == 1278478311 and message.text.lower().startswith("post"))
async def post(message: Message) -> None:
    title, link = history()
    if len(message.text) == 4:
        for i in range(2):
            await message.answer(title[i])
    else:
        if message.text[5:len(message.text)].isdigit():
            index = int(message.text[5:len(message.text)])
            if index < 3:
                linkk = f"https://www.history.com/{link[index]}"
                prompt = f"""Menga quyidagi havola {linkk} asosida Telegram kanalim uchun o'zbek tilida post tayyorlab ber. Postni tayyorlashda ushbu qoidalarga amal qil:


    Insoniy til: Quruq faktlar emas, jonli va qiziqarli hikoya ko'rinishida yoz.

    Yaxlit matn: Ro'yxat (nuqta yoki chiziqchalar) ishlatma, faqat abzaslar bilan ajrat.

    Soddalik: Murakkab terminlarsiz, oddiy va tushunarli tilda bo'lsin.

    Struktura: - Title

    Kirish: Voqeani qiziqarli jumlalar bilan boshla.

    Asosiy qism: Eng muhim voqealar va dramatik jarayonni tushuntir.

    Xulosa: Mazmunli va ta'sirli yakun yasa.

    Faqat matn: Ortiqcha kirish-chiqish gaplarsiz, faqat postning tayyor variantini b"""
                postiy = gemini(prompt)
                posti: Message = await bot.send_message(chat_id=channel_id, text=postiy)
                await message.answer("Posted✅")
                last_message_id = posti.message_id
                reactions = [ReactionTypeEmoji(emoji="❤️")]
                await bot.set_message_reaction(chat_id=channel_id, message_id=last_message_id, reaction=reactions)
            else:
                await message.answer("Theres no such an index nigger")
        else:
            await message.answer("Only number nigga")

@dp.message(lambda message: message.text.lower() == "memes" and message.chat.id == 1278478311)
async def memes(message: Message):
    data = reddit()
    print(type(data))
    if type(data) == tuple:
        title, url = data
        user_memes['me'] = (title, url)
        for i in range(len(title)):
            photo_url = url[i]
            caption=title[i]
            photo = URLInputFile(photo_url, filename=f"picture{i}.png")
            await message.answer_photo(photo, caption=caption)
    else:
        await message.answer(str(data))

@dp.message(lambda message: message.text.isdigit())
async def number(message: Message):
    try:
        num = int(message.text)
        title, url = user_memes['me']
        photo_url = url[num]
        photo = URLInputFile(photo_url, filename=f"picture{num}.png")
        memed: Message = await bot.send_photo(chat_id=channel_id, photo=photo, caption=title[num])
        await message.answer("Done✅")
        last_message_id = memed.message_id
        reactions = [ReactionTypeEmoji(emoji="😁")]
        await bot.set_message_reaction(chat_id=channel_id, message_id=last_message_id, reaction=reactions)
    except:
        await message.answer("There's no such an index nigga!?")

async def send_remind():
    prompt = f"translate this {fact()} into uzbek and send me the only translation"
    translation = gemini(prompt)
    xabar = f"Kun fakti\n\n{translation}"
    fakt: Message = await bot.send_message(chat_id=channel_id, text=xabar)
    await bot.send_message(chat_id=1278478311, text="Today's Fact sent✅")
    last_message_id = fakt.message_id
    reactions = [ReactionTypeEmoji(emoji="❤️")]
    await bot.set_message_reaction(chat_id=channel_id, message_id=last_message_id, reaction=reactions)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    scheduler.add_job(send_remind, "cron", hour=7, minute=0)
    scheduler.start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
