import telegram


class TelegramBot:

    def __init__(self, token):
        self.token = token
        self.bot = telegram.Bot(token=self.token)

    def sendMessage(self, chat_id, message):
        self.bot.sendMessage(chat_id=chat_id, text=message)


if __name__ == "__main__":
    token = ''  # your token
    bot = TelegramBot(token)
    receiver_id = ''  # your id

    bot.sendMessage(receiver_id, "Start")
