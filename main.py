from aiogram import Bot, Dispatcher, filters, types
import asyncio


bot = Bot(token='7434111701:AAG_lTOzGnTcoLOWqf2pY42jnYZFmashBSg')
dp = Dispatcher(bot=bot)


@dp.message(filters.Command('start'))
async def start_function(message: types.Message):
    await message.answer("Xush kelibsiz")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())