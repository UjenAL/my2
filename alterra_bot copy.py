import random
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

# Заглушка токена
BOT_TOKEN = "8056580496:AAFhRMKQF5E1cdqODpxQ_LCSnOd6w926TQo"

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Путь к папке с мемами
MEMES_DIR = "memes"

# Создаем папку для мемов, если она не существует
if not os.path.exists(MEMES_DIR):
    os.makedirs(MEMES_DIR)

# Примеры цитат на українській
quotes = [
    "Життя — це не очікування, коли буря пройде. Це навчання танцювати під дощем.",
    "Коли здається, що все йде не так — пам'ятай, зірки світять лише в темряві.",
    "Навіть найтемніша ніч закінчується світанком.",
    "Ти сильніший, ніж думаєш. Вір у себе.",
    "Не зупиняйся, поки не буде гордості за результат.",
    "Кожен день — новий шанс змінити своє життя.",
    "Посмішка — найкоротший шлях до щастя.",
    "Зміни — це початок чогось великого.",
    "Все, що нас не вбиває — робить нас сильнішими.",
    "Твоя енергія — твоя суперсила!"
]

# Ключові слова для визначення настрою
sad_keywords = ['сум', 'грусть', 'печаль', 'втома', 'злість', 'погано', 'поганий', 'стрес']

@dp.message()
async def handle_message(message: types.Message):
    text = message.text.lower()
    if any(word in text for word in sad_keywords):
        # Случайно выбрать мем или цитату
        if random.choice([True, False]):
            # Отправка мема
            memes = [f for f in os.listdir(MEMES_DIR) if f.endswith(('.jpg', '.png', '.jpeg', '.gif'))]
            if memes:
                meme_path = os.path.join(MEMES_DIR, random.choice(memes))
                await message.answer_photo(InputFile(meme_path))
            else:
                await message.answer("Наразі немає мемів 😢")
        else:
            # Отправка цитаты
            await message.answer(random.choice(quotes))
    else:
        await message.answer("Напиши мені, як ти себе почуваєш 😊")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
