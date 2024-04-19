from config import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ContentType
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
import logging

admins = ADMINS
storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


class Help(StatesGroup):
    waiting_message = State()

def menu():
    buttons = [
        types.InlineKeyboardButton(text='Купить игру', callback_data='magaz2'),
        types.InlineKeyboardButton(text='Убрать меню', callback_data='poka')
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def menu2():
    buttons = [
        types.InlineKeyboardButton(text='Action', callback_data='Action'),
        types.InlineKeyboardButton(text='Mmo', callback_data='Mmo'),
        types.InlineKeyboardButton(text='Rpg', callback_data='Rpg'),
        types.InlineKeyboardButton(text='Simulator', callback_data='Simulator'),
        types.InlineKeyboardButton(text='<-Вернутся назад', callback_data='nazad')
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def Action_game():
    buttons = [
        types.InlineKeyboardButton(text='Rust', callback_data='game'),
        types.InlineKeyboardButton(text='ELDEN RING', callback_data='game'),
        types.InlineKeyboardButton(text='<-Вернутся назад', callback_data='nazad')
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def Mmo_game():
    buttons = [
        types.InlineKeyboardButton(text='DayZ', callback_data='game'),
        types.InlineKeyboardButton(text='STALCRAFT', callback_data='game'),
        types.InlineKeyboardButton(text='<-Вернутся назад', callback_data='nazad')
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard



def Rpg_game():
    buttons = [
        types.InlineKeyboardButton(text='Warframe', callback_data='game'),
        types.InlineKeyboardButton(text='Guild Wars 2', callback_data='game'),
        types.InlineKeyboardButton(text='<-Вернутся назад', callback_data='nazad')
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard



def Simulator_game():
    buttons = [
        types.InlineKeyboardButton(text='Arma 3', callback_data='game'),
        types.InlineKeyboardButton(text=' BeamNG.drive', callback_data='game'),
        types.InlineKeyboardButton(text='<-Вернутся назад', callback_data='nazad')
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    await bot.send_photo(message.from_user.id, photo='https://cdn.cgmagonline.com/wp-content/uploads/2018/12/media-brief-gamestore-brings-capcoms-mega-man-to-gamestore-for-android-3.png', caption='Привет это бот по продажи игр🎮🎮🎮\n\n--этот бот создан для продажи игр--\nобратится к меню можно по команде:-/menu\n\nПиятного пользования ботом')
@dp.message_handler(commands='menu')
async def command_start(message: types.Message):
    await message.answer('Ты попал в меню вибирай что хочешь купить!!!\n\n🧾Menu🧾',reply_markup=menu())

@dp.callback_query_handler(Text(equals='nazad'))
async def command_start(cd: types.CallbackQuery):
   await cd.answer()
   await cd.message.answer('Ты попал в меню вибирай что хочешь купить!!!\n\n🧾Menu🧾',reply_markup=menu())

@dp.callback_query_handler(Text(equals='magaz2'))
async def kupit_odezdu(cd: types.CallbackQuery):
   await cd.answer()
   await cd.message.answer('---Выбирай жанр игры---',reply_markup=menu2())

@dp.callback_query_handler(Text(equals='Action'))
async def kupit_odezdu(cd: types.CallbackQuery):
   await cd.answer()
   await cd.message.answer('---Игр на жанра "Экшен"---',reply_markup=Action_game())


@dp.callback_query_handler(Text(equals='Mmo'))
async def kupit_odezdu(cd: types.CallbackQuery):
   await cd.answer()
   await cd.message.answer('---Игр на жанра "Ммо"---',reply_markup=Mmo_game())


@dp.callback_query_handler(Text(equals='Rpg'))
async def kupit_odezdu(cd: types.CallbackQuery):
   await cd.answer()
   await cd.message.answer('---Игр на жанра "Рпг"---',reply_markup=Rpg_game())


@dp.callback_query_handler(Text(equals='Simulator'))
async def kupit_odezdu(cd: types.CallbackQuery):
   await cd.answer()
   await cd.message.answer('---Игр на жанра "Симулятор"---',reply_markup=Simulator_game())
@dp.callback_query_handler(text ='game')
async def payment(callback: types.CallbackQuery):
    await bot.send_invoice(chat_id=callback.from_user.id, title='Покупка', description='игра',
                           payload='payment', provider_token=YKASSA_TOKEN, currency='RUB', start_parameter='test_bot',
                           prices=[{'label': 'Руб', "amount": 20000}])

@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: types.Message):
    await bot.send_message(message.from_user.id, "Вы купили игру на ПК")

@dp.callback_query_handler(Text(equals='poka'))
async def goodbuy(cd: types.CallbackQuery):
   await cd.answer()
   await cd.message.answer('Досвидание')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)