import asyncio
from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor

API_Token = '5791637720:AAG2lKP27A2NH_fdWwS8ipSg4l5RtfS6TPM'
admin_id=888881913

bot = Bot(API_Token, parse_mode="HTML")
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)