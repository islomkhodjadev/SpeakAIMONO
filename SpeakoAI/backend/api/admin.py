# from typing import List
#
# from fastapi import APIRouter, HTTPException, Path
#
#
#
#
# router = APIRouter(prefix="api/admin", tags=["Admin"])
#
# #
# # class Admin(Filter):
# #     async def      __call__(self, message):
# #         return message.from_user.id in admin
#
#
# @router.message(Admin(), Command("newsletter"))
# async def chad(message: Message, state: FSMContext):
#     await state.set_state(NewsLetter.message)
#     await message.answer("Enter message you want to share:")
#
#
# @router.message(NewsLetter.message)
# async def chad(message: Message, state: FSMContext):
#     await state.clear()
#     await message.answer("start")
#     users = await get_all_users()
#     for user in users:
#         try:
#
#             await message.send_copy(chat_id=user.tg_id)
#
#
#         except Exception as e:
#             print(e)
#     await message.answer("success")