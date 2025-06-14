import telebot
import random
import os

# جلب التوكن من متغير البيئة المسمي BOT_TOKEN
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# قائمة أسئلة الصراحة
saraha_list = [
    "متى شعرت بأقوى شهوة تجاهي؟",
    "هل مرّ في بالك تخونني؟",
    "ما أكثر شيء يثيرك فيّ؟",
    # زيد الأسئلة هنا حسب ذوقك
]

# قائمة التحديات المثيرة والرومانسية
tahadi_list = [
    "سجّل ڤويس تقول فيه 'اشتقتلك' وكأنك تبكي.",
    "أرسل لي صورة من كاميرتك الآن، بدون تعديل.",
    "أغمض عيونك، وتخيلني، ثم قل بصوت عالي: 'أريدك الآن'.",
    # زيد التحديات هنا حسب ما تحب
]

# التعامل مع الأمر /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🎯 صراحة", "🔥 تحدي", "🎲 عشوائي")
    bot.send_message(message.chat.id, "هلا حبي جعفر ❤️ اختار نوع اللعبة 😘", reply_markup=markup)

# التعامل مع ضغط المستخدم على الأزرار
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

# تشغيل البوت بشكل مستمر
bot.infinity_polling()
