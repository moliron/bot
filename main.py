from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)
async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='start', description='запуск бота'),
        types.BotCommand(command='hellp', description='блабла'),
        types.BotCommand(command='you', description='я'),
        types.BotCommand(command='game', description='игра'),
        types.BotCommand(command='hello', description='привет')
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands='start')
async def start(messege: types.Message):
    await messege.reply('hi')


@dp.message_handler(commands='hellp')
async def start(messege: types.Message):
    await messege.reply('blabla')

@dp.message_handler(commands='you')
async def start(messege: types.Message):
    await messege.reply('u')

@dp.message_handler(commands='game')
async def start(messege: types.Message):
    await messege.reply('diablo')

@dp.message_handler(commands='hello')
async def start(messege: types.Message):
    await messege.reply('hi')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)


if __name__ != '__name__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)