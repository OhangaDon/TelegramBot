import telegram.ext

Token = "6176609952:AAEo8MBXcBIM8ezhIRvt0osAHgP1oG4E_bg"
updater = telegram.ext.Updater("6180720326:AAESDUsihjQQ4ZFj9_-rrpt9x1XqJj1EVU4", use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    update.message.reply_tet("Hello! Welcome to Simplilearn")


def help(update, context):
    update.message.reply_tet(
        """
        /start -> Welcome to the channel
        /help -> This practicular message
        /context -> About various Playlists of Simplilearn
        /Python -> The first video from Python playlist
        /SQL -> The first video from SQL playlist
        /Java -> The first video from java Playlist
        /Skillup -> Free platform for certification by Simplilearn
        /contact -> contact information
        """
    )


def content(update, context):
    update.message.reply_text("We have various playlists and articles available!")


def Python(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/Tm5u97I7OrM")


def SQL(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/pFq1pgli0OQ")


def Java(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/i6AZdFxTK9I")


def Skillup(update, context):
    update.message.reply_text(
            "tutorial link : https://www.simplilearn.com/?&utm_source=google&utm_medium=cpc&utm_term=%2Bwww%20"
            "%2Bsimplilearn%20%2Bcom&utm_content=803350713-40537012023-467574577661&utm_device=c&utm_campaign=Search"
            "-Brand-Broad-IN-AllDevice-adgroup-brand-navigation&gclid"
            "=Cj0KCQjw0oyYBhDGARIsAMZEuMv5mA9EysZZ5NfhK65Cb5OU0Q0TVC4con6DQzHF502-dfgA7QQFCgQaAu5sEALw_wcB")


def contact(update, context):
    update.message.reply_text("You can contact on the official mail id")


def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}, use the commands using /")


dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.CommandHandler('content', content))
dispatcher.add_handler(telegram.ext.CommandHandler('Python', Python))
dispatcher.add_handler(telegram.ext.CommandHandler('SQL', SQL))
dispatcher.add_handler(telegram.ext.CommandHandler('Java', Java))
dispatcher.add_handler(telegram.ext.CommandHandler('Skillup', Skillup))
dispatcher.add_handler(telegram.ext.CommandHandler('contact', contact))
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()
