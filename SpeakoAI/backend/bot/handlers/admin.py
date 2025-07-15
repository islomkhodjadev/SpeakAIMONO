from aiogram import types, Router
from aiogram.filters import Command
from backend.services.requests.user import create_user, get_user, get_all_users
import logging

logger = logging.getLogger(__name__)
ADMINS = {5514429658, 1099766821}

router = Router()

@router.message(Command("checkadmin"))
async def check_admin(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("🚫 get out of here")
    else:
        await message.answer("✅ You are admin.")
@router.message(Command("adminpanel"))
async def admin_panel_command(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("🚫 Access denied.")
        return

    try:
        users = await get_all_users()  # import this properly
        table = (
            "👤 Registered Users:\n\n" +
            "\n".join(
                f"{i+1}. {u.first_name or 'Unknown'} — `{u.tg_id}`"
                for i, u in enumerate(users)
            )
            if users else
            "⚠️ No users have practiced yet."
        )
        await message.answer(table, parse_mode="Markdown")

    except Exception as e:
        logger.error(f"Error in admin panel: {e}")
        await message.answer("⚠️ Error fetching admin data.")
