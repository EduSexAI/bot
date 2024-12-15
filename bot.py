import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Cài đặt API Key của OpenAI
openai.api_key = "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"

# Cài đặt API Token của Telegram Bot
TELEGRAM_TOKEN = "7796882295:AAGmhLjduszWUQ0war7tNjFmblWyVKMVlXU"

# Hàm để gọi OpenAI API và nhận phản hồi
def get_gpt_response(question):
    response = openai.Completion.create(
        engine="gpt-4o-mini",  # Hoặc GPT-4 nếu bạn sử dụng GPT-4
        prompt=question,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Hàm xử lý tin nhắn
def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    bot_response = get_gpt_response(user_message)
    update.message.reply_text(bot_response)

# Hàm để bắt đầu bot
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Chào bạn! Tôi là bot giáo dục giới tính EduSexBot. Bạn có thể hỏi tôi bất cứ câu hỏi nào về giáo dục giới tính.")

# Cài đặt và chạy bot
def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
