from telebot import types
import telebot
from telebot import *
import requests

bot = telebot.TeleBot("5073409435:AAGyWexh98nBJsnjeOWtDaT4w_h4xwiN2VU")

@bot.message_handler(commands=["start"])
def start(message):
    if message.chat.type == 'private':
        first = message.from_user.first_name
        mas = types.InlineKeyboardMarkup(row_width=1)
        z222 = types.InlineKeyboardButton(f'• نسألكم الدعاء •', url=f'https://t.me/hsshh')
        mas.add(z222)
        bot.send_message(message.chat.id,text=f"""اهلا بك عزيزي في بوت القرآن الكريم 
------‐------------------------
• يقوم البوت بجلب صفحات القرآن صفحة صفحة
- كل ما عليك هوه ارسال رقم الصفحة لاقوم بجلبه بشكل صورة لك .،
- ارسل الارقام باللغة الانكليزية (1.2..4..الخ)
- تستطيع ايضاً الضغط على زر ( تصفح القرآن الكريم ) وسيكون بإمكانك التصفح عن طريق الأزرار 

• يمكنك الاستماع الى السور ايضاً
- ارسل اسم السورة وسيتم ارسالها بشكل بصمه صوتيه للأستماع لها
- يمكنك ايضاً الضغط على زر ( ° الأستماع الى القرآن الكريم ° ) وسيتم اظهار رسالة تحتوي على كل سور القرآن الكريم """,reply_markup=mas)

@bot.message_handler(func=lambda m: True)
def fael(message):
    if str(message.chat.type) not in ['private']:return
    try:
        mas = types.InlineKeyboardMarkup(row_width=2)
        back = types.InlineKeyboardButton(text='° التالي °', callback_data=f'back:{message.text}')
        page = types.InlineKeyboardButton(f'• نسألكم الدعاء •', url=f'https://t.me/hsshh')
        url = f"https://www.daily-quran.com/static/pages/page-{message.text}.jpg"
        mas.add(back,next)
        mas.add(page)
        bot.send_photo(message.chat.id,url,reply_markup=mas)
    except:
        bot.send_message(message.chat.id,text=f'**• يجب إرسال رقم الصفحة بشكل صحيح:**

- 1,2,3... ترسل : **001 , 002 , 003...**
- 10,11,12... ترسل : **010 , 011 , 012...**')

@bot.callback_query_handler(func=lambda call: True)
def calling(call):
    data = str(call.data)
    chat = call.message.chat.id
    if (data).count("next:"):
        try:
            bot.delete_message()
            msg = int(data.split("next:")[1])-1
            mas = types.InlineKeyboardMarkup(row_width=2)
            back = types.InlineKeyboardButton(text='° التالي °', callback_data=f'back:{msg}')
            page = types.InlineKeyboardButton(f'• نسألكم الدعاء •', url=f'https://t.me/hsshh')
            url = f"https://www.daily-quran.com/static/pages/page-{msg}.jpg"
            mas.add(back,next)
            mas.add(page)
            bot.send_photo(call.message.chat.id,url,reply_markup=mas)
        except:
            pass
    if (data).count("back:"):
        try:
            msg = int(data.split("back:")[1])+1
            mas = types.InlineKeyboardMarkup(row_width=2)
            back = types.InlineKeyboardButton(text='° التالي °', callback_data=f'back:{msg}')
            page = InlineKeyboardButton(f'• نسألكم الدعاء •', url=f'https://t.me/hsshh')
            url = f"https://www.daily-quran.com/static/pages/page-{msg}.jpg"
            mas.add(back,next)
            mas.add(page)
            bot.send_photo(call.message.chat.id,url,reply_markup=mas)
        except:
            pass

bot.polling(True)