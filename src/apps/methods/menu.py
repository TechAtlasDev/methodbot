from pyrogram import Client, filters
import pyrogram
from moduls.utils.utils import loading_message
from moduls.utils.database import MethodOperations
from moduls.utils.buttons import keymakers

@Client.on_message(filters.command(['methods', "metodos", "menu"], "/"))
async def get_metodos(clientC:pyrogram.client.Client, responseR:pyrogram.types.messages_and_media.message.Message, postdata=0):

    # LA POSTDATA SE RECIBE CON LOS SIGUIENTES DATOS:
    """    
    postdata = {
        "user": {
            "_": "User",
            "id": 1601204657,
            "is_self": false,
            "is_contact": false,
            "is_mutual_contact": false,
            "is_deleted": false,
            "is_bot": false,
            "is_verified": false,
            "is_restricted": false,
            "is_scam": false,
            "is_fake": false,
            "is_support": false,
            "is_premium": false,
            "first_name": "z2ppbwvuzxpkzxphh",
            "status": "UserStatus.RECENTLY",
            "username": "z2ppbwvuzxpkzxphh",
            "language_code": "es"
        },
        "postdata": "1" -> Numero de metodo a buscar
    }
    """

    sticker = await loading_message(responseR, 3)

    metodo = MethodOperations().obtener_metodos(postdata["postdata"], postdata["postdata"]+1)[0]
    datos_metodos = """[🪪] ID: <code>{}</code>
[📘] Título: <b>{}</b>
[📚] Descripción: {}
[💰] Costo: {} Tokens"""

    text = f"<b>[🔍] Información del método {postdata["postdata"]+1}:</b>\n\n"
    text += f"{datos_metodos.format(metodo["id"], metodo["titulo"], metodo["descripcion"], metodo["costo"])}\n\n"


    botones = keymakers([f"[✅] Obtener método", f"⏭ Método {postdata["postdata"]+2}"],
                        [f"buy_method-{metodo["id"]}_{postdata["user"].id}", f"get_metodo_info-{postdata["postdata"]+1}"], add_basics=True, lote=2)

    await sticker.delete()
    await clientC.send_photo(responseR.chat.id, photo=metodo["urlIMG"], caption=text, reply_markup=botones)