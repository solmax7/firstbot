import os, asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


dp = Dispatcher()

@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer(f"Привет, {msg.from_user.first_name}! Я готов ✨")

@dp.message()
async def echo(msg: types.Message):
    await msg.answer(f"Ты написал: <code>{msg.text}</code>")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
