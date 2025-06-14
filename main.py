import telebot
import random
import os

# هنا نجيب التوكن من البيئة الخارجية
TOKEN = os.environ.get("7277421640:AAGgtZrEI3qqwZXJZSL0LYRMbJh0neGayLE")
bot = telebot.TeleBot(TOKEN)

# أسئلة الصراحة
saraha_list = [
    "متى شعرت بأقوى شهوة تجاهي؟",
    "هل مرّ في بالك تخونني؟",
    "ما أكثر شيء يثيرك فيّ؟",
    # زيد الأسئلة هنا حسب ذوقك
]

# تحديات مثيرة ورومانسية
tahadi_list = [
    "سجّل ڤويس تقول فيه 'اشتقتلك' وكأنك تبكي.",
    "أرسل لي صورة من كاميرتك الآن، بدون تعديل.",
    "أغمض عيونك، وتخيلني، ثم قل بصوت عالي: 'أريدك الآن'.",
    # زيد التحديات هنا حسب ما تحب
]

# لما أحد يكتب /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🎯 صراحة", "🔥 تحدي", "🎲 عشوائي")
    bot.send_message(message.chat.id, "هلا حبي جعفر ❤️ اختار نوع اللعبة 😘", reply_markup=markup)

# لما المستخدم يضغط أي زر
@bot.message_handler(func=lambda m: True)
def reply(message):
    if message.text == "🎯 صراحة":
        bot.send_message(message.chat.id, random.choice(saraha_list))
    elif message.text == "🔥 تحدي":
        bot.send_message(message.chat.id, random.choice(tahadi_list))
    elif message.text == "🎲 عشوائي":
        bot.send_message(message.chat.id, random.choice(saraha_list + tahadi_list))
    else:
        bot.send_message(message.chat.id, "اضغط أحد الخيارات من الأزرار فوق ⬆️")

# هذا السطر يخلي البوت يشتغل طول الوقت
bot.infinity_polling()
