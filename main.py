# HENRIQUE
import asyncio
from telegram import Bot  # Biblioteca oficial do Telegram para Python

# ================================================
# 1️⃣ Token do bot
# ================================================
TOKEN = "//"

# ================================================
# 2️⃣ CHAT_ID
# ================================================
CHAT_ID = 1  # substitua pelo seu CHAT_ID real

# ================================================
# 3️⃣ Função principal que envia a mensagem
# ================================================
async def main():
    bot = Bot(token=TOKEN)

    # ================================================
    # 4️⃣ Mensagem organizada com links curtos
    # ================================================
    mensagem = f"""
<b>🔥 Notebook X DO MEGATOKIO SAFADO E MARCOS NEGROMOM </b>
<b>💳 Parcelas:</b> 10000000x SEM JUROS
<b>🎟️ Cupom:</b> <code>MEUCUPOM10</code>
<b>🏷️ De:</b> <s>R$ 3.500</s>
<b>💸 Por:</b> <b>R$ 2.199</b>
──────────────────────────
👉<b>LINK DO PRODUTO</b>
 <a href="https://s.shopee.com.br/9AF6RytJ53?share_channel_code=1">https://s.shopee.com.br/airfryer</a>
📢 <b>Grupo de Ofertas</b>
<a href="https://t.me/linkdogrupo">https://t.me/linkdogrupo</a>
"""

    try:
        # ================================================
        # 5️⃣ Envia a mensagem com foto
        # ================================================
        await bot.send_photo(
            chat_id=CHAT_ID,
            photo="https://vaiobr.vtexassets.com/arquivos/ids/162506-1200-1200?v=638556269494370000&width=1200&height=1200&aspect=true",
            caption=mensagem,
            parse_mode="HTML"
        )
        print("Mensagem enviada com sucesso!")
    except Exception as e:
        print("Erro ao enviar mensagem:", e)

# ================================================
# 6️⃣ Executa a função principal
# ================================================
asyncio.run(main())