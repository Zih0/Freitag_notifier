import telegram


class TelegramBot:

    def __init__(self, token):
        self.token = token
        self.bot = telegram.Bot(token=self.token)

    def sendMessage(self, chat_id, message):
        self.bot.sendMessage(chat_id=chat_id, text=message)


if __name__ == "__main__":
    token = '1167349229:AAHFdxH4pEDCBFtsGTtngjiD7fDSfaluiBA'  # your token
    bot = TelegramBot(token)
    receiver_id = '1083114017'  # your id

    bot.sendMessage(receiver_id, "Start")
