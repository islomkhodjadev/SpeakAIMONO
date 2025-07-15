from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("price"))
async def price_command(message: types.Message):
    welcome_message = """
💸 Pricing Plans for IELTS Mock Speaking App

🧢 Free Plan
Target: Casual users, first-timers
Price: 0 UZS / month

Features:
✅ 1 mock exam per day
✅ AI Band Score (overall only)
❌ No PDF report
❌ No retry option
❌ No answer comparison
❌ No history tracking
❌ No personalized tips

"Just enough to feel guilty for not upgrading."

🥈 Gold Plan – Affordable Premium
Target: Serious students
Price: 15,000–20,000 UZS / month ($1.25–$1.7)

Features:
✅ 5 mocks per day
✅ Full detailed feedback in PDF
✅ 1 retry per mock (per day)
✅ AI-generated 7-day study plan
✅ Access to Band 9 sample answer (text only)
❌ No voice comparison
❌ No full progress analytics

"Students trying hard, but still on a budget."

💎 Platinum Plan – Full IELTS Warrior Mode
Target: Teachers, advanced students
Price: 35,000–50,000 UZS / month ($3–$4)

Features:
✅ Unlimited mocks
✅ Unlimited retries
✅ All detailed PDF feedback
✅ AI study plans tailored to your weakest criteria
✅ Full score breakdown history + analytics dashboard
✅ Band 9 voice and transcript comparison
✅ Leaderboards & practice challenges
✅ Telegram notifications & reminders

"Go from Band 5.5 to 7+ and prove it."
    """
    await message.answer(welcome_message)
