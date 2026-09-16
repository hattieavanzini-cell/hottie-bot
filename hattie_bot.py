
import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message

BOT_TOKEN = os.getenv(8859954684:AAF8N_gIaT6Rcifo4DucWKAhh6WsYlPxlvw)

AUTO_REPLY = """𐙚₊˚⊹ 𝐰𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐡𝐚𝐭𝐭𝐢𝐞 𝐬𝐡𝐨𝐩 ⊹˚₊𐙚

୨୧・𝐰𝐞𝐥𝐜𝐨𝐦𝐞, 𝐝𝐞𝐚𝐫! ♡
please check our sections below before purchasing.

╭──────────────୨୧
• ୨୧・ʚɞ 𝐫𝐮𝐥𝐞𝐬 & 𝐫𝐞𝐠𝐮𝐥𝐚𝐭𝐢𝐨𝐧𝐬
└ t.me/rnrbyhattie

• ୨୧・ʚɞ 𝐚𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐚𝐜𝐜𝐨𝐮𝐧𝐭𝐬
└ t.me/vlblcntsbyhattie

• ୨୧・ʚɞ 𝐬𝐨𝐥𝐝 𝐚𝐜𝐜𝐨𝐮𝐧𝐭𝐬
└ t.me/sldcntsbyhattie

• ୨୧・ʚɞ 𝐭𝐫𝐚𝐧𝐬𝐚𝐜𝐭𝐢𝐨𝐧 𝐩𝐫𝐨𝐨𝐟𝐬
└ t.me/prfsbyhattie

• ୨୧・ʚɞ 𝐥𝐞𝐠𝐢𝐭𝐢𝐦𝐚𝐜𝐲
└ t.me/lgtmcybyhattie
╰──────────────୨୧

𐙚₊˚⊹ 𝐫𝐞𝐚𝐝𝐲 𝐭𝐨 𝐛𝐮𝐲? ♡
୨୧・check our available accounts, then dm for price & details!

♡・𝐦𝐚𝐢𝐧 : @snthttvnzn
♡・𝐛𝐚𝐜𝐤𝐮𝐩 : @nmnngvnzn

thank you for choosing & trusting 𝐡𝐚𝐭𝐭𝐢𝐞 𝐬𝐡𝐨𝐩 ♡"""

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.business_message()
async def on_business_message(message: Message):
    if message.business_connection_id:
        await bot.send_message(
            chat_id=message.chat.id,
            text=AUTO_REPLY,
            business_connection_id=message.business_connection_id
        )

async def main():
    print("Hattie Shop auto-reply is now running...")
    await dp.start_polling(
        bot,
        allowed_updates=["business_message", "business_connection"]
    )

if __name__ == "__main__":
    asyncio.run(main())
