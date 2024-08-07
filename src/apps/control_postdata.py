from pyrogram import Client
from moduls.utils.utils import getVAR, load_json

from apps.basics import welcome

from apps.users.get_info import info_user

from apps.methods.menu import get_metodos
from apps.methods.see_menu import ver_metodo

from apps.llm import iaUse

# Tipos de datos
from pyrogram.client import Client
from pyrogram.types.bots_and_keyboards.callback_query import CallbackQuery

CONFIG_LLM = load_json("llmConfig")

@Client.on_callback_query()
async def controler(cliente:Client, data_response:CallbackQuery):
    
    data = data_response.data
    USER_INFO = data_response.from_user
    CHAT_INFO = data_response.message.chat

    function_name, postdata = data.split("-")[0], 0 if len(data.split("-")) == 1 else "-".join(data.split("-")[1:])

    if postdata.startswith("VAR"):
        postdata = getVAR(postdata)

    else:
        postdata = int(postdata) if str(postdata).isdigit() else postdata

    if function_name == "start":
        await welcome.start(cliente, data_response.message, postdata)

    if function_name == "info":
        await info_user(cliente, data_response.message, postdata)
    
    elif function_name == "get_metodo_info":
        postdata = {
            "user": USER_INFO,
            "chat": CHAT_INFO,
            "postdata": postdata
        }
        await get_metodos(cliente, data_response.message, postdata)

    elif function_name == "buy_method":
        postdata = {
            "user": USER_INFO,
            "chat": CHAT_INFO,
            "postdata": postdata
        }
        await ver_metodo(cliente, data_response.message, postdata)

    elif function_name == "rm":
        await data_response.message.delete()

    elif function_name == CONFIG_LLM["COMMAND"]:
        await iaUse.llmUse(cliente, data_response.message, postdata)

    else:
        await cliente.answer_callback_query(
            callback_query_id=data_response.id,
            text=f"""⚠️ Function not set.\nFunction: {function_name}, postdata: {postdata}""",
            show_alert="true"
        )