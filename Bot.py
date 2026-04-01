import asyncio
import logging
import sys
import json

from aiogram.types import URLInputFile
from RedditFetcher import reddit
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types.reaction_type_emoji import ReactionTypeEmoji
from aiogram.types import ReactionType

TOKEN = "8492197672:AAFAuGZh4nzGqVppoO2Rpe9UFkO6fA5uP8k"
bot = Bot(token=TOKEN)

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    if message.chat.id == 1278478311:
        await message.answer(f"Valar Morghulis!")
    else:
        await message.answer("U r not Citizen, so i dont give u access to use this bot!")

user_memes = {}

@dp.message(lambda message: message.text.lower() == "memes")
async def memes(message: Message):
    if message.chat.id == 1278478311:
        title, url = reddit()
        user_memes['me'] = (title, url)
        for i in range(len(title)):
            photo_url = url[i]
            photo = URLInputFile(photo_url, filename=f"picture{i}.png")
            await message.answer_photo(photo, caption=title[i])

@dp.message()
async def number(message: Message):
    if message.text.isdigit():
        try:
            num = int(message.text)
            title, url = user_memes['me']
            photo_url = url[num]
            photo = URLInputFile(photo_url, filename=f"picture{num}.png")
            channel_id = -1002112088417
            memed: Message = await bot.send_photo(chat_id=channel_id, photo=photo, caption=title[num])
            await message.answer("Done✅")
            last_message_id = memed.message_id
            reactions = [ReactionTypeEmoji(emoji="😁")]
            await bot.set_message_reaction(chat_id=channel_id, message_id=last_message_id, reaction=reactions)
        except:
            await message.answer("There's no such an index nigga!?")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())