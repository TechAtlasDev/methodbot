from pyrogram import Client, filters
import pyrogram
from moduls.utils.database import UserOperations
from moduls.utils.utils import loading_message
from moduls.utils.buttons import keymakers

@Client.on_message(filters.command(["info", "me"], "/"))
async def info_user(clientC:pyrogram.client.Client, responseR:pyrogram.types.messages_and_media.message.Message, postdata=0):
    ID_USER = responseR.from_user.id if not postdata else postdata

    sticker = await loading_message(responseR, 3)
    # Verificando si está registrado en la base de datos
    status = UserOperations().is_registered(ID_USER)

    if status:
        # Si está registrado, se obtienen los datos del usuario
        user_data = UserOperations().get_user_data(ID_USER)

        mensaje = f"""
[🪪] Tu id: <code>{user_data["id"]}</code>
[👤] Tu username: <code>{user_data["username"]}</code>
[💳] Tus tokens: <code>{user_data["tokens_user"]}</code>
"""
        botones = keymakers(["❌ Cerrar"], ["rm-0"], add_basics=False)

        await sticker.delete()
        await responseR.reply_text(mensaje, reply_markup=botones)
    else:
        botones = keymakers(["❌ Cerrar"], ["rm-0"], add_basics=False)
        await sticker.delete()
        await responseR.reply_text("[😱] No estás registrado en la base de datos.", reply_markup=botones)