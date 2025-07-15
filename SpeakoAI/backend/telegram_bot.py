import asyncio
import logging
import os

from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
# Import your routers (grouped handlers)
from bot.handlers import start, admin, price  # if you split them

# Or import a single router if you're not modular yet

load_dotenv()
TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")

# Setup logger
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def main():
    bot = Bot(token=TELEGRAM_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
              )
    dp = Dispatcher(storage=MemoryStorage())

    # ⛓ Register routers here
    dp.include_router(start.router)  # user commands like /start, /help, messages
    dp.include_router(admin.router)  # admin stuff like /adminpanel
    dp.include_router(price.router)  # optional - e.g., /progress

    logger.info("🚀 SpeakoAI Bot is starting...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
