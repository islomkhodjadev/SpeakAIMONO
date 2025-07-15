from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

start_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    # [
    #     InlineKeyboardButton(
    #         text="🎯 Start Practice", callback_data="practice_start"
    #     )
    # ],
    # [InlineKeyboardButton(text="📊 My Progress", callback_data="progress")],
    # [InlineKeyboardButton(text="🏆 Leaderboard", callback_data="leaderboard")],
    [
        InlineKeyboardButton(
            text="Open Miniapp",
            web_app=WebAppInfo(url="https://502afd9bf74c.ngrok-free.app")
        )
    ]
])
#
# practice_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(
#             text="Part 1 - Personal Info", callback_data="practice_part_1"
#         )
#     ],
#     [
#         InlineKeyboardButton(
#             text="Part 2 - Long Turn", callback_data="practice_part_2"
#         )
#     ],
#     [
#         InlineKeyboardButton(
#             text="Part 3 - Discussion", callback_data="practice_part_3"
#         )
#     ],
#     [InlineKeyboardButton(text="Random Question", callback_data="practice_random")],
# ])
