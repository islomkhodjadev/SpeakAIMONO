from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import LabeledPrice, CallbackQuery

router = Router()

PAYMENT_TOKEN = '398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065'


@router.message(Command("payment"))
async def pay(message: types.Message):
    chat_id = message.chat.id
    total_price = 10000

    await message.bot.send_invoice(
        chat_id=chat_id,
        title="Upgrading to Premium",
        description="Get full access to all features of our botgit ",
        payload="bot-defined invoice payload",
        provider_token=PAYMENT_TOKEN,
        currency="UZS",
        prices=[
            LabeledPrice(label="Total: ", amount=int(total_price * 100)),
        ],
        start_parameter="start_parameter",
    )


@router.pre_checkout_query(lambda query: True)
async def checkout(pre_checkout_query: types.PreCheckoutQuery):
    await pre_checkout_query.bot.answer_pre_checkout_query(
        pre_checkout_query.id,
        ok=True,
        error_message="Transaction was declined, check if everything is alright"
    )


@router.message(lambda message: message.successful_payment)
async def get_payment(message: types.Message):
    chat_id = message.chat.id  # Fixed typo
    await message.answer("Payment successful!")
