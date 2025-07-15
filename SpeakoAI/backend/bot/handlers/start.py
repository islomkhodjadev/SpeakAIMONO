from aiogram import types, Router
from aiogram.filters import Command
from backend.models.schemas.schemas import UserCreateSchema
from backend.services.requests.user import create_user, get_user
from backend.bot.keyboards import start_keyboard  # <- actual InlineKeyboardMarkup
import logging

router = Router()
logger = logging.getLogger(__name__)

@router.message(Command("start"))
async def start_command(message: types.Message):
    user = message.from_user

    try:
        # Check if user exists before creating
        existing_user = await get_user(user.id)
        if not existing_user:
            user_data = UserCreateSchema(
                tg_id=user.id,
                first_name=user.first_name,
                username=user.username,
            )
            await create_user(user_data=user_data)

        welcome_message = f"""
🎉 Welcome to SpeakoAI, {user.first_name}!

I'm your IELTS Speaking practice assistant. I can help you:
• Practice with real IELTS speaking questions
• Get AI-powered scoring and feedback
• Track your progress over time
• Compare your performance with others

Use these commands:
/start - Show this welcome message

/price - Get pricing
/adminpanel - Admin panel
/checkadmin - Check if you're admin
        """

        await message.answer(welcome_message, reply_markup=start_keyboard)

    except Exception as e:
        logger.error(f"Error in /start command: {e}")
        await message.answer("Sorry, an error occurred. Please try again later.")
