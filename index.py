import os
import asyncio
from telegram import Bot
from dotenv import load_dotenv

# ---------
#   CONFIGURAÇÕES 
# --------
load_dotenv()

# Carrega variáveis de ambiente
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Converter chat_id para inteiro
CHAT_ID = int(CHAT_ID)

# Func. MSG
async def enviar_mensagem(texto):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=texto)

# Função principal
async def main():
    await enviar_mensagem("🔥 PROMOÇÕES MANO PEPA!")

# Roda o bot
if __name__ == "__main__":
    asyncio.run(main()) 