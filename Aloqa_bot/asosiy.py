from multiprocessing import context
from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
from telebot import types

def start(update, context):
    user=update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"<b>Здравствуйте @{user.username},это бот автомойка Karcher!!!</b>\n"
        "Пожалуйста, присылайте мне любые предложения или жалобы",parse_mode="HTML")#,reply_markup=tashqitugma
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Пожалуйста, укажите в своей жалобе дату и время, когда вы приехали в нашу мойку, а также марку и номер вашего автомобиля.",parse_mode="HTML")
    #tashqitugma=types.ReplyKeyboardMarkup(resize_keyboard=True)
    #tugma=types.KeyboardButton('Мы в социальных сетях🌐')
    
    #tashqitugma.add(tugma)
    
    
#def but(update,context):
    #if context.text=="Мы в социальных сетях🌐":
     #   context.bot.send_message(chat_id=update.effective_chat.id,text='Наш Инстаграм профиль 👉👉👉https://www.instagram.com/karcher_moykauz/?hl=ru')   
    
def xabar(update, context):
    matn=update.message.text
    user=update.message.from_user
    print(user)
    user_id=5075053188
    matn +=f"\n @{user.username} У вас новый сообщение"
    context.bot.send_message(chat_id=user_id,
        text=matn)
    context.bot.send_message(chat_id=update.effective_chat.id,
    text="Спасиба за вашу мнения!!! 🤝",
    parse_mode="HTML")


updater=Updater(token="5229668966:AAGQ1_Wi_2w2rxt1r1bd7hMyRFONRRXeHK4", use_context=True)
dispatcher=updater.dispatcher
start_handler=CommandHandler('start',start)
xabar_handler=MessageHandler(Filters.text,xabar)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(xabar_handler)

updater.start_polling()
print("bot ishladi")