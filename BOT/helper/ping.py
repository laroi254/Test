from FUNC.defs import *
from pyrogram import Client, filters
import time


@Client.on_message(filters.command("ping", [".", "/"]))
async def cmd_ping(client, message):
    try:
        start = time.perf_counter()
        resp  = """<b>
🤖 Checking ª𝗠𝗸𝗨𝘀𝗛𝘅𝗖𝗵𝗞 Ping...
        </b>"""
        edit  = await message.reply_text(resp, quote=True)
        end   = time.perf_counter()
        
        textb = f"""<b>
🤖 Bot Name: ª𝗠𝗸𝗨𝘀𝗛𝘅𝗖𝗵𝗞 
✅ Bot Status: Running
📶 Ping: {(end-start)*1000:.2f} ms
        </b>"""
        await client.edit_message_text(message.chat.id, edit.id, textb)

    except Exception:
        import traceback
        await error_log(traceback.format_exc())
