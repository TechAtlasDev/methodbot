# Importando los modulos
from pyrogram import Client, filters
from moduls.utils.utils import loading_message
from moduls.utils import utils
import pyrogram
from moduls.utils.buttons import keymakers

# Operaciones de bases de datos
from moduls.utils.database import UserOperations

# Controlando el mensaje con las siguientes características
@Client.on_message(filters.command(["start", "iniciar", "inicio"], prefixes=["!", "/", "."]) & filters.text)
async def start(clientC:pyrogram.client.Client, responseR:pyrogram.types.messages_and_media.message.Message, postdata=0):

    sticker = await loading_message(responseR, 1)

    ID_USER = responseR.from_user.id
    USERNAME = responseR.from_user.username

    User = UserOperations()

    # Verificando si está registrado en la base de datos
    if User.is_registered(ID_USER):
        await sticker.delete()

        botones = keymakers(["❌ Cerrar", "📘 Mis datos", "[👀] Ver métodos disponibles", "[🏁] Ver ofertas disponibles"],
                            ["rm-0", f"info-{ID_USER}", "get_metodo_info-0", "verOfertas-0"], lote=2)
        await responseR.reply_text(f"[👋] Hola de nuevo!.", reply_markup=botones)
    
    # Si no está registrado en la base de datos
    else:
        await sticker.delete()
        User.create_user(ID_USER, USERNAME, 0)
        botones = keymakers(["❌ Cerrar", "📘 Mis datos", "[👀] Ver métodos disponibles", "[🏁] Ver ofertas disponibles"],
                            ["rm-0", f"info-{ID_USER}", "get_metodo_info-0", "verOfertas-0"], lote=2)
        await responseR.reply_text(f"[👋] Bienvenido al bot donde encontrarás los mejores métodos.", reply_markup=botones)