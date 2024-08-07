import pyrogram
import pyrogram.mime_types
from moduls.utils.utils import loading_message
from moduls.utils.database import MethodOperations
from moduls.utils.buttons import keymakers

# TIPOS DE OBJETOS
chat_privado = pyrogram.enums.ChatType.PRIVATE
grupo = pyrogram.enums.ChatType.GROUP

async def ver_metodo(clientC:pyrogram.client.Client, responseR:pyrogram.types.messages_and_media.message.Message, postdata=0):
    print (postdata)
    metodoID, userID = postdata["postdata"].split("_")[0], postdata["postdata"].split("_")[1]

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
        "postdata": metodoID_userID -> Numero de metodo a buscar
    }
    """

    sticker = await loading_message(responseR, 5)

    # Verificando si el usuario tiene permisos
    if True:
        if responseR.chat.type != chat_privado:
            await clientC.send_message(postdata["chat"].id, "[✅] El método se enviará en tu chat privado.")

        metodo = MethodOperations().get_metodo(metodoID)
        print (metodo)
        text = f"<b>[✅] Información del método <code>{metodoID}</code>:</b>\n\n<b>Contenido:</b> {metodo["contenido"]}"
        botones = keymakers([f"❌ CERRAR VENTANA"],
                            ["rm-0"])
        await clientC.send_photo(userID, metodo["urlIMG"], caption=text, reply_markup=botones)

    else:
        await responseR.reply("No tienes permisos para ver este método.")

    await sticker.delete()
