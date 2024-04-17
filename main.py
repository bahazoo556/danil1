from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_message(msg: types.Message):
   await bot.send_message(msg.chat.id, msg.text)


if __name__ == '__main__':
   executor.start_polling(dp)
