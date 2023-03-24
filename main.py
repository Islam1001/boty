from pyromod import listen
from random import choice, randint 
from pyrogram import Client, filters 
from pyrogram.types import (
  InlineKeyboardMarkup,
  InlineKeyboardButton,
  CallbackQuery
)

api_id = 7311907
api_hash = "7a63b6b87d7a0f43a9e4b686eb2c4ca1"
token = "5336215402:AAFbE6MNguIIk-r7mJ--ozNYain1by24gnA"
app = Client(
   "@HssHH - Games",
    api_id=api_id,
  api_hash=api_hash,
  bot_token=token
)

EMOJIS = list("😭🤣😂😅😆😁😄😃😀🥳🤩🤩😍🥰😘😚😙😗😉🤪😜😝😛😋🥲🙂🙃😶😐😑🫣🤭")
@app.on_message(filters.regex("^الاسرع$") & filters.group)
@app.on_edited_message(filters.regex("^الاسرع$") & filters.group)
async def game_1(client, message):
   emoji = choice(EMOJIS)
   re = f"^{emoji}$"
   ASK = await app.ask(
     message.chat.id,
     "اسرع واحد يرسل الايموجي : `{}`".format(emoji),
     reply_to_message_id=message.id,
     filters=filters.regex(re)
   )
   await app.send_message(
      message.chat.id,
      "المستخدم {} كفو اجابتك صح".format(ASK.from_user.mention),
      reply_to_message_id=ASK.id
   )
   
AUT = [
  "https://telegra.ph/file/5c0875dfcffe3e9a5df8b.jpgZAIDاصالة",
  "https://telegra.ph/file/6eb251808382289632226.jpgZAIDتامر حسني",
  "https://telegra.ph/file/94131da89e97781e08772.jpgZAIDنانسي عجرم",
  "https://telegra.ph/file/eed0d7ff96194a8f8c2d7.jpgZAIDاليسا",
  "https://telegra.ph/file/79de290d7131bd2343c50.jpgZAIDهيفاء وهبي",
  "https://telegra.ph/file/47b584756e5c7c84e0bad.jpgZAIDشيرين",
  "https://telegra.ph/file/56def78a3f3b78b3515ac.jpgZAIDحسين الجسمي",
  "https://telegra.ph/file/478423ba1b724269b71ab.jpgZAIDعمرو دياب",
  "https://telegra.ph/file/2364efe0dd00116830480.jpgZAIDكاظم الساهر",
  "https://telegra.ph/file/5f0de633a64e7b28d2b46.jpgZAIDناصيف زيتون",
  "https://telegra.ph/file/5b3abd2874d41d8d3bbc8.jpgZAIDتامر عاشور",
  "https://telegra.ph/file/a06b89e8e3a9c66707e78.jpgZAIDمحمد صلاح",
  "https://telegra.ph/file/6f6622b0e345a624e94e9.jpgZAIDكرستيانو رونالدو",
  "https://telegra.ph/file/2c11bfdab09589eddb542.jpgZAIDمحمد رمضان",
  "https://telegra.ph/file/10f7ddbd1779f6bcc9df8.jpgZAIDوائل جسار"
]

@app.on_message(filters.regex("^مشاهير$") & filters.group)
@app.on_edited_message(filters.regex("^مشاهير$") & filters.group)
async def game_2(client, message):
   photoo = choice(AUT)
   photo = photoo.split("ZAID")[0]
   print(photo)
   author = photoo.split("ZAID")[1]
   print(author)
   x = await message.reply_photo(
     photo
   )
   re = f"^{author}$"
   ASK = await app.ask(
     message.chat.id,
     "اسرع واحد يرسل أسم الفنان",
     reply_to_message_id=x.id,
     filters=filters.regex(re)
   )
   await ASK.reply(
    f"كفو {ASK.from_user.mention} اجابتك صحيحة"
   )
   
EMO = [
  "👞:حذاء",
  "⭐:نجمة",
  "🕞:ساعة",
  "🍑:خوخ",
  "🛢️:نفط",
  "🎂:كيكة",
  "⚽:كورة",
  "🩳:شورت",
  "📒:دفتر",
  "🌹:وردة",
  "✏️:قلم",
  "🔥:نار",
  "💸:فلوس",
  "💻:لاب"
]
@app.on_message(filters.regex("^معاني$") & filters.group)
@app.on_edited_message(filters.regex("^معاني$") & filters.group)
async def game_3(client, message):
   A = choice(EMO)
   emo = A.split(":")[0]
   print(emo)
   ans = A.split(":")[1]
   print(ans)
   re = f"^{ans}$"
   ASK = await app.ask(
     message.chat.id,
     "اسرع واحد يرسل معنى الايموجي {}".format(emo),
     reply_to_message_id=message.id,
     filters=filters.regex(re)
   )
   await ASK.reply(
    f"كفو {ASK.from_user.mention} اجابتك صحيحة"
   )
   
FLAGS = [
  "🇦🇪:الامارات",
  "🇧🇭:البحرين",
  "🇪🇬:مصر",
  "🇮🇶:العراق",
  "🇱🇧️:لبنان",
  "🇱🇺:لوكسمبورغ",
  "🇵🇰:باكستان",
  "🇹🇷:تركيا",
  "🇾🇪:اليمن",
  "🇸🇩:السودان",
  "🇸🇦:السعودية",
  "🇵🇸:فلسطين",
  "🇴🇲:سلطنة عمان",
  "🇯🇵:اليابان"
]
@app.on_message(filters.regex("^اعلام دول$") & filters.group)
@app.on_edited_message(filters.regex("^اعلام دول$") & filters.group)
async def game_4(client, message):
   A = choice(FLAGS)
   emo = A.split(":")[0]
   print(emo)
   ans = A.split(":")[1]
   print(ans)
   re = f"^{ans}$"
   ASK = await app.ask(
     message.chat.id,
     "اسرع واحد يرسل اسم الدولة {}".format(emo),
     reply_to_message_id=message.id,
     filters=filters.regex(re)
   )
   await ASK.reply(
    f"كفو {ASK.from_user.mention} اجابتك صحيحة"
   )
@app.on_message(filters.regex("^اقتباس$") & filters.group)
@app.on_edited_message(filters.regex("^اقتباس$") & filters.group)
async def game_5(client, message):
   f = "quotes555v"
   t = message.chat.id
   d = randint(2,190)
   await app.copy_message(
      t,
      f,
      d,
      reply_to_message_id=message.id,
      reply_markup=InlineKeyboardMarkup(
      [
      [
      InlineKeyboardButton("Dev", user_id=5117901887)
      ]
      ]
      )
   )
   
@app.on_message(filters.regex("^كت$") & filters.group)
@app.on_edited_message(filters.regex("^كت$") & filters.group)
async def game_6(client, message):
   f = "rancutt"
   t = message.chat.id
   r = randint(2, 141)
   a = await app.get_messages("rancutt", r)
   id = message.from_user.id
   await message.reply(
      f"- ‹ {message.from_user.mention} ›\n{a.text}",
      reply_markup=InlineKeyboardMarkup(
      [
      [
      InlineKeyboardButton("التالي", callback_data=f"cut:{id}")
      ]
      ]
      )
   )
   
@app.on_message(filters.regex("^افتار انمي$") & filters.group)
@app.on_edited_message(filters.regex("^افتار انمي$") & filters.group)
async def anime(c,m):
    rl = randint(3,201)
    url = f"https://t.me/foravaanime/{rl}"
    user = m.from_user.mention
    await m.reply_photo(url, caption=f"༄ {user}\n༄ تم اختيار افتار لك")     
    
@app.on_message(filters.regex("^افتار عيال$") & filters.group)
@app.on_edited_message(filters.regex("^افتار عيال$") & filters.group)
async def boys(c,m):
    rl = randint(3,446)
    url = f"https://t.me/foravaboys/{rl}"
    user = m.from_user.mention
    await m.reply_photo(url, caption=f"༄ {user}\n༄ تم اختيار افتار لك")  

@app.on_callback_query(filters.regex("cut:"))
async def next_cut(_, query: CallbackQuery):
    id = int(query.data.split(":")[1])
    if not query.from_user.id == id:
      return await query.answer("هذا الأمر لايخصك", show_alert=True)
    else:
      idd = query.from_user.id
      r = randint(2, 141)
      a = await app.get_messages("rancutt", r)
      await query.edit_message_text(
        f"- ‹ {query.from_user.mention} ›\n{a.text}",
        reply_markup=InlineKeyboardMarkup(
          [
          [
          InlineKeyboardButton("التالي", callback_data=f"cut:{idd}")
          ]
          ]
        )
      )
   

app.run()