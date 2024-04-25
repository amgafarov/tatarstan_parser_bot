import os
from aiogram import Bot, Dispatcher, types, Router
from aiogram.enums import ParseMode
from secure import __telegram_api_key__
from tat_min_parser import start_min_parser

dp = Dispatcher()
bot = Bot(token=__telegram_api_key__, parse_mode=ParseMode.HTML)
r = Router()
__rss_chat_id__ = '-1002000518192'
__rss_chan_id__ = None


async def send_message_func(title: str, min_name: str, date: str, content: str, link: str):
    global bot

    file_name = title[:50].strip() + '.txt'
    file_path = 'files/' + file_name

    with open(file_path, 'w') as file:
        text = title + '\n' + content + '\n\n' + f'Источник: {min_name}'
        file.write(text)

    await bot.send_document(
        chat_id=__rss_chat_id__,
        document=types.FSInputFile(file_path),
        caption=min_name + '\n\n' + title + '\n\n' + date + '\n\n' + link,
        message_thread_id=__rss_chan_id__
    )

    os.remove(file_path)


async def start() -> None:
    dp.include_router(r)

    await start_min_parser(send_message_func)