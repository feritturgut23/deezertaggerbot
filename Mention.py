import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

emoji_calisan = []

anlik_calisan = []

tekli_calisan = []

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("●** Merhaba 🇹🇷**\n\n● **Grubunuzdaki tüm kullanıcılara etiket atabilirim,Beni grubunuza ekleyip yetki vermeniz gerekir.** \n\n● **ᴛᴜᴍ ᴋᴏᴍᴜᴛʟᴀʀɪ ᴏɢʀᴇɴᴍᴇᴋ ɪᴄɪɴ /help ᴋᴏᴍᴜᴛᴜɴᴜ ᴋᴜʟʟᴀɴɪɴ . . !**",
                    buttons=(
                   
		      [Button.url('🎉  Beni Gruba Ekle  🎉', 'https://t.me/Electrataggerbot?startgroup=a')],
                      [Button.url('📝  Destek Grubu  📝',  'https://t.me/SohbetGaribanlarTr')], 
                      [Button.url('😎  Developer  😎', 'https://t.me/magandasahip')],
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "📝 **Etiket Komutları **\n\n**» /utag < mesajınız > \Gruptaki kullanıcılara 5-li etiket atar.!**\n\n**» /tag  < ᴍᴇsᴀᴊɪɴɪᴢ > \nɢʀᴜʙᴛᴀᴋɪ ᴋᴜʟʟᴀɴɪᴄɪʟᴀʀᴀ ᴛᴇᴋ ᴛᴇᴋ ᴇᴛɪᴋᴇᴛ ᴀᴛᴀʀ . . !**\n\n**» /cancel => ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪɴɪ ᴅᴜʀᴅᴜʀᴜʀ . . !**"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('🎉  Beni Gruba Ekle  🎉', 'https://t.me/ElectraTaggerbot?startgroup=a')],
                      [Button.url('📝  Destek Grubu  📝',  'https://t.me/SohbetGaribanlarTr')],
                      [Button.url('😎  Developer  😎', 'https://t.me/Magandasahip')],
                      [Button.url('😎  Kanal  😎', 'https://t.me/Magandasahip')],
                    ),
                    link_preview=False
                   )
	
@client.on(events.NewMessage(pattern="^/reklam$"))
async def help(event):
  helptext = "**📝 Etiket Komutları\n\n» /utag < Mesajınız > => Gruptaki kullanıcılara 5-li etiket atar. !\n» /tag  < Mesajınız > => Gruptaki kullanıcılara tek tek etiket atar!\n» /cancel => Etiketleme işlemini durdurur!\n\n✵ Bir çok özelliğe sahip @ElectraTaggerbot 'u grububuza ekleyip rahatlıkla kullanabilirsiniz ! **"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('🎉  Botu Gruba Ekle  🎉', 'https://t.me/ElectraTaggerbot?startgroup=a')],
                    ),
                    link_preview=False
                   )
	
	

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)


emoji = " ❤️ 🧡 💛 💚 💙 💜 🖤 🤍 🤎 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 😋 😛 😝 😜 🤪 🤨 🧐 🤓 😎 🤩 🥳 😏 😒 " \
        "😞 😔 😟 😕 🙁 😣 😖 😫 😩 🥺 😢 😭 😤 😠 😡  🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 " \
        "😻 😼 😽 🙀 😿 😾 🔞 🌹 ".split (" ")


@client.on(events.NewMessage(pattern="^/jssjejs ?(.*)"))
async def mentionall(event):
  global emoji_calisan
  if event.is_private:
    return await event.respond("**Bu komutu gruplar ve kanallar için geçerli**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadace yoneticiler kullana bilir😐**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Geçmiş mesajlar için etiket atabilmiyorum.**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**𝖤𝗍𝗂𝗄𝖾𝗍 𝗒𝖺𝗉𝗆𝖺𝗄 𝗂çin 𝗌𝖾𝖻𝖾𝗉 𝗒𝗈𝗄**")
  else:
    return await event.respond("**𝖤𝗍𝗂𝗄𝖾𝗍𝖾 𝖻𝖺ş𝗅𝖺𝗆𝖺𝗄 𝗂𝖼𝗂𝗇 sebep 𝗒𝖺𝗓ı𝗇...!**")
  
  if mode == "text_on_cmd":
    emoji_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in emoji_calisan:
        await event.respond("** 𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖻𝖺şarıyla 𝖽𝗎𝗋𝖽𝗎𝗋𝗎𝗅𝖽𝗎 **")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    emoji_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in emoji_calisan:
        await event.respond("**𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖻𝖺şarıyla 𝖽𝗎𝗋𝖽𝗎𝗋𝗎𝗅𝖽𝗎 ...**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**● ʙᴜ ᴋᴏᴍᴜᴛᴜ ʏᴀʟɴɪᴢᴄᴀ ɢʀᴜʙᴛᴀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀsɪɴɪᴢ . . !**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**● ʙᴜ ᴋᴏᴍᴜᴛᴜ ʏᴀʟɴɪᴢᴄᴀ ʏᴏɴᴇᴛɪᴄɪʟᴇʀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀ . . !**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki Mesajlara Cevap vermeyin")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**𝖤𝗍𝗂𝗄𝖾𝗍 𝗂𝗌𝗅𝖾𝗆𝗂𝗇𝗂 𝖻𝖺ş 𝗂𝖼𝗂𝗇 𝗌𝖾𝖻𝖾𝗉 𝗒𝗈𝗄**")
  else:
    return await event.respond("**● ᴇᴛɪᴋᴇᴛ ɪsʟᴇᴍɪɴɪ ʙᴀsʟᴀᴛᴍᴀᴋ ɪᴄɪɴ \n< sᴇʙᴇᴘ > ɢɪʀɪɴ ʏᴀᴅᴀ ʙɪʀ ᴍᴇsᴀᴊɪ ʏᴀɴɪᴛʟᴀʏɪɴ . . !**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id})** , "
      if event.chat_id not in anlik_calisan:
        await event.respond("**● ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ᴅᴜʀᴅᴜʀᴜʟᴅᴜ . . !**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id})** , "
      if event.chat_id not in anlik_calisan:
        await event.respond("**● ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ᴅᴜʀᴅᴜʀᴜʟᴅᴜ . . !**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**● ʙᴜ ᴋᴏᴍᴜᴛᴜ ʏᴀʟɴɪᴢᴄᴀ ɢʀᴜʙᴛᴀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀsɪɴɪᴢ . . !**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**● ʙᴜ ᴋᴏᴍᴜᴛᴜ ʏᴀʟɴɪᴢᴄᴀ ʏᴏɴᴇᴛɪᴄɪʟᴇʀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀ . . !**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**önceki mesajı etiketleye bilmerim*")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**● ᴇᴛɪᴋᴇᴛ ɪsʟᴇᴍɪɴɪ ʙᴀsʟᴀᴛᴍᴀᴋ ɪᴄɪɴ \n< sᴇʙᴇᴘ > ɢɪʀɪɴ ʏᴀᴅᴀ ʙɪʀ ᴍᴇsᴀᴊɪ ʏᴀɴɪᴛʟᴀʏɪɴ . . !**")
  else:
    return await event.respond("**● ᴇᴛɪᴋᴇᴛ ɪsʟᴇᴍɪɴɪ ʙᴀsʟᴀᴛᴍᴀᴋ ɪᴄɪɴ \n< sᴇʙᴇᴘ > ɢɪʀɪɴ ʏᴀᴅᴀ ʙɪʀ ᴍᴇsᴀᴊɪ ʏᴀɴɪᴛʟᴀʏɪɴ . . !**")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"• [{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in tekli_calisan:
        await event.respond("**● ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ᴅᴜʀᴅᴜʀᴜʟᴅᴜ . . !**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} \n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"• [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("**● ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ᴅᴜʀᴅᴜʀᴜʟᴅᴜ . . !**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	


@client.on(events.NewMessage(pattern="^/admin ?(.*)"))
async def mentionall(tagadmin):

	if admintag.pattern_match.group(1):
		seasons = tagadmin.pattern_match.group(1)
	else:
		seasons = ""

	chat = await tagadmin.get_input_chat()
	a_=0
	await tagadmin.delete()
	async for i in client.iter_participants(chat, filter=cp):
		if a_ == 500:
			break
		a_+=5
		await tagadmin.client.send_message(tagadmin.chat_id, "**[{}](tg://user?id={}) {}**".format(i.first_name, i.id, seasons))
		sleep(0.5)


print(">> Bot Başlatıldı. Üyelere etiket atabilirim. <<")
client.run_until_disconnected()
