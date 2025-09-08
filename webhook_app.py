import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.environ["BOT_TOKEN"]
PUBLIC_URL = os.environ.get("PUBLIC_URL", "")
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET", "whsec")
WEBHOOK_PATH = f"/tg/{WEBHOOK_SECRET}"

# ✅ новый стиль aiogram >= 3.7
bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(CommandStart())
async def start(msg: types.Message):
    await msg.answer("Я на вебхуках и жив!")

@dp.message()
async def echo(msg: types.Message):
    await msg.answer(f"Эхо (webhook): <code>{msg.text}</code>")

async def on_startup(app):
    if not PUBLIC_URL:
        raise RuntimeError("PUBLIC_URL is not set")
    await bot.set_webhook(PUBLIC_URL + WEBHOOK_PATH)

async def on_shutdown(app):
    await bot.delete_webhook()

async def health(request):
    return web.Response(text="ok")

def main():
    app = web.Application()
    app.router.add_get("/healthz", health)
    SimpleRequestHandler(dp, bot).register(app, path=WEBHOOK_PATH)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    setup_application(app, dp, bot=bot)
    port = int(os.environ.get("PORT", 8080))  # Railway подставляет $PORT
    web.run_app(app, host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
