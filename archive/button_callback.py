










from aiogram import Router
from aiogram.filters import Command

router = Router()

@router.message()
async def button_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button callbacks"""
    query = update.callback_query
    await query.answer()

    if query.data == "practice_start":
        await self.practice_command(update, context)
    elif query.data == "progress":
        await self.progress_command(update, context)
    elif query.data == "leaderboard":
        await self.leaderboard_command(update, context)
    elif query.data.startswith("practice_part_"):
        part = int(query.data.split("_")[-1])
        await self.send_question(update, context, part=part)
    elif query.data == "practice_random":
        await self.send_question(update, context, part=None)
    elif query.data.startswith("answer_"):
        question_id = int(query.data.split("_")[-1])
        await self.handle_question_response(update, context, question_id)


