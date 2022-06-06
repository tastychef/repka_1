from aiogram import Bot, Dispatcher
from aiogram.utils import executor
bot = Bot(token="5393953243:AAEgydRql-P3YNYHY7uBLIxUIXqC3BBsIrQ")
dp = Dispatcher(bot)

executor.start_polling()