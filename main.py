# Bu telegram keyboard-lar
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

# Bu-lar handler-lar
from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters)
print('BOT ISHLAYABDI...😎')

# Bu javob-so`zlar button-ni, va methodi -> ( ReplyKeyboardMarkup )
BTN_TODAY, BTN_TOMORROW, BTN_MONTH, BTN_REGION, BTN_DUA = ('⌛ Bugun', '⏳ Ertaga', '📆 To`liq taqvim', '🇺🇿 Mintaqa', '🤲 Duo')
main_buttons = ReplyKeyboardMarkup([
    [BTN_TODAY],[BTN_TOMORROW, BTN_MONTH],[BTN_REGION],[BTN_DUA]
], resize_keyboard=True)

# STATE-lar
STATE_REGION = 1
STATE_CALENDAR = 1

# start() funksiya
def start(update, context):
    # USER id-si
    user = update.message.from_user
    # BU KEYBOARD buyuriq-lar -> ( InlineKeyboardButton )
    buttons = [
        [
            InlineKeyboardButton('Namangan', callback_data='region_1'),
        ],
        [
            InlineKeyboardButton('Andijon', callback_data='region_2'),
            InlineKeyboardButton('Farg`ona', callback_data='region_3'),
        ]
    ]
    # START bosilsa javob-berish va bu method xam ishlaydi -> ( InlineKeyboardMarkup )
    update.message.reply_html('Assalamu alaykum <b>{} 😎</b>'
                              '\n \n<b>Ramazon oyi muborak bo`lsin...👏</b>'
                              '\n \nSizga qaysi mintaqa buyicha ma`lumot berish kerak '
                              .format(user.first_name ), reply_markup=InlineKeyboardMarkup(buttons))
    return STATE_REGION

# INLINE button-ga function
def inline_callback(update, context):
    try:
        query = update.callback_query
        query.message.delete()
        query.message.reply_html(text='<b>Ramazon taqvim</b> 2️⃣0️⃣2️⃣3️⃣'
                                      '\n \nQuyidagilardan birini tanlang 👇',
                                 reply_markup=main_buttons)
        return STATE_CALENDAR
    except Exception as e:
        print('error', str(e))

#---------> TUGMA-LAR BOSILGANDAGI FUNCTION
def calendar_today(update, context):
    update.message.reply_text('Bugun belgilandi')

def calendar_tomorrow(update, context):
    update.message.reply_text('Ertaga belgilandi')

def calendar_month(update, context):
    update.message.reply_text('To`liq taqvim belgilandi')

def calendar_region(update, context):
    update.message.reply_text('Mintaqa belgilandi')

def select_dua(update, context):
    update.message.reply_text('Duo belgilandi')

def main():
    # UPDATER-ni o`rnatib olish
    updater = Updater('5777882903:AAGG7dUI9BSr-YWVQm3ooVpIl60Sp0vfKug', use_context=True)
    # Dispatcher event-larni aniqlash uchun
    dispatcher = updater.dispatcher
    # START -> 1-chi KOMANDA-NOMI, 2-chi qaysi function-ga-murojati
    # dispatcher.add_handler(CommandHandler('start', start))

    # INLINE button-ga query (so`rov-yuborish)
    dispatcher.add_handler(CallbackQueryHandler(inline_callback))

# ---------> TUGMA-LAR BOSILGANDAGI JAVOB-LAR, methodi ->ConversationHandler
    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start)],
        states={
            STATE_REGION:[CallbackQueryHandler(inline_callback)],
            STATE_CALENDAR:[
                MessageHandler(Filters.regex('^(' + BTN_TODAY + ')$'), calendar_today),
                MessageHandler(Filters.regex('^(' + BTN_TOMORROW + ')$'), calendar_tomorrow),
                MessageHandler(Filters.regex('^(' + BTN_MONTH + ')$'), calendar_month),
                MessageHandler(Filters.regex('^(' + BTN_REGION + ')$'), calendar_region),
                MessageHandler(Filters.regex('^(' + BTN_DUA + ')$'), select_dua)
            ],
        },
        # BU ERROR BO`LSA START-GA QAYTARADI
        fallbacks=[CommandHandler('start', start)]
    )
    # BU BUYRUQ-LARNI DISPECHIR-GA BERILADI
    dispatcher.add_handler(conv_handler)

    # BU TELEGRAM method
    updater.start_polling()
    updater.idle()

main()







