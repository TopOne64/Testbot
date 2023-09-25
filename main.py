import aiogram
import asyncio
from aiogram import Bot, Dispatcher
import database as db
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import State, StatesGroup
from aiogram.context import FSMContext
import environ
from admin import router

env = environ.Env()



async def on_startup(dp: Dispatcher):
    await db.db_start(dp)



async def main():
    storage = aiogram.fsm.storage.memory.MemoryStorage()
    env.read_env()
    bot = Bot(env('TOKEN'))
    dp = Dispatcher(bot=bot, storage=storage, loop=asyncio.get_event_loop())
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
        except KeyboardInterrupt
            print('Exit')
