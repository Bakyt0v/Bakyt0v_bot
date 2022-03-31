from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
URL = "https://bakytov.herokuapp.com/"
URI = "postgres://tnnayhqnpxaiep:11a13995d29231b136013e206477f6a279cc9cd3927b4f67863bf2633cc7f500@ec2-34-246-227-219.eu-west-1.compute.amazonaws.com:5432/d2tk2gf37l5p0i"
