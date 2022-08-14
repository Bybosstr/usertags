#SNEHABHI USERTAGGER BOT
#Seni Seviyorum İstanbul Yakışıklısı😘

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

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

moment_worker = []

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global moment_worker
  moment_worker.remove(event.chat_id)
  
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("Merhaba Ben İstanbul Yakışıklsı Tarafından Yaratıldım @istanbulyakisiklisii ",
                    buttons=(
                      [Button.url('🙃 Grubunuza Almak için Basın bana  🥺✨', 'https://t.me/UserTags_Bot?startgroup=true')],
                      [Button.url('Destek için', 'https://t.me/istanbulyakisiklisii')],
                      [Button.url('Kanalımıza Katılın', 'https://t.me/GuvenceKanalimiz')]
                      ),
                    link_preview=False
                    )



@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "***𝚂𝙽𝙴𝙷𝙰𝙱𝙷𝙸 𝚄𝚂𝙴𝚁𝚃𝙰𝙶𝙶𝙴𝚁 𝙱𝙾𝚃'𝚂 𝙷𝙴𝙻𝙿 𝙼𝙴𝙽𝚄**\n\nCommand: /tag \n 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚆𝙸𝚃𝙷 𝚃𝙴𝚇𝚃 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝚃𝙴𝙻𝙻 𝙾𝚃𝙷𝙴𝚁𝚂. \n`𝙴𝚇𝙰𝙼𝙿𝙻𝙴: /tag 𝙶𝙾𝙾𝙳 𝙼𝙾𝚁𝙽𝙸𝙽𝙶!` \n𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝙰𝚂 𝙰𝙽 𝙰𝙽𝚂𝚆𝙴𝚁. 𝙰𝙽𝚈 𝙼𝚂𝙶 𝙱𝙾𝚃 𝚆𝙸𝙻𝙻 𝚃𝙰𝙶 𝚄𝚂𝙴𝚁𝚂 𝚃𝙾 𝚁𝙴𝙿𝙻𝙸𝙴𝙳 𝙼𝚂𝙶"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('🙃Grubunuza Almak için Basın bana 🥺✨', 'https://t.me/UserTags_Bot?startgroup=true')],
                      [Button.url('Destek için', 'https://t.me/istanbulyakisiklisii')],
                      [Button.url('Kanalımıza Katılın', 'https://t.me/GuvenceKanalimiz')]
                      ),
                    link_preview=False
                    )
  
@client.on(events.NewMessage(pattern="^/Reklam$"))
async def repository(event):
  snehabhitext = "**Kendi Reklamını Ver @istanbulyakisiklisii**"
  await event.reply(snehabhitext,
                    buttons= [Button.url('Para Kazanma Grubu', 'http://t.me/guvenilirsistemler')]
                      ),
                    link_preview=False
                    )
  
#𝚆𝙰𝙰𝙷 𝙱𝙷𝙰𝙸𝙼𝚈𝙰 𝙵𝚄𝙻𝙻 𝙸𝙼𝙶𝙽𝙾𝚁𝙴𝙱𝙰𝚉𝙸

#𝙲𝚁𝙴𝙳𝙸𝚃 𝙳𝙴 𝙳𝙴𝙽𝙰 𝚆𝙰𝚁𝙽𝙰 𝙼𝙰 𝙲𝙷𝙾𝙳 𝙳𝙴𝙽𝙶𝙴

@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global moment_worker
  if event.is_private:
    return await event.reply("Grup veya Kanallarda kullan!")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.reply("Bunu Sadece Yöneticiler Kullanabilir.")
    
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.reply("Üyeleri Etiketleyemem")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.reply("𝙶𝙸𝚅𝙴 𝙼𝙴 𝙲𝙰𝙽 𝙰𝙽 𝙰𝚁𝙶𝚄𝙼𝙴𝙽𝚃. 𝙴𝚇𝙰𝙼𝙿𝙻𝙴: `/tag 𝙺𝙰𝙷𝙰 𝙼𝙰𝚁 𝚁𝙰𝙷𝙴 𝙷𝙾 𝚂𝙰𝙱`")
  else:
    return await event.reply("𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙼𝚂𝙶 𝙾𝚁 𝙶𝙸𝚅𝙴 𝚂𝙾𝙼𝙴 𝚃𝙴𝚇𝚃 𝚃𝙾 𝙼𝙴𝙽𝚃𝙸𝙾𝙽!")
  if mode == "text_on_cmd":
    moment_worker.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.respond("Durduruldu Grubumuza Katılın @GuvenilirSistemler")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
        
  if mode == "text_on_reply":
    moment_worker.append(event.chat_id)
    
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.reply("Durduruldu @guvenilirsistemler")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
        
print("USERTAGGER BOT BAŞLATILDI")
print("¯\_(ツ)_/¯ YARDIM İÇİN @istanbulyakisiklisii")
client.run_until_disconnected()
