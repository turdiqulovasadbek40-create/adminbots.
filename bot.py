import telebot

# BotFather'dan olgan tokeningizni shu yerga yozasiz
TOKEN = "SIZNING_BOT_TOKENINGIZ"
bot = telebot.TeleBot(TOKEN)

# /start buyrug'i (4 ta asosiy menyu ko'rinishida)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = (
        "Assalomu alaykum!\n\n"
        "Asosiy menyu:\n"
        "/diskord - 🎓 Diskord live – To'liq bank sistema (31 ta mavzu)\n"
        "/malumot - ℹ️ Ma'lumot\n"
        "/kurs - 📚 Kurs haqida ma'lumot olish\n"
        "/admin - 👤 Admin bilan bog'lanish"
    )
    bot.reply_to(message, text)

# 1. 🎓 Diskord live – To'liq bank sistema (31 ta mavzu)
@bot.message_handler(commands=['diskord'])
def send_diskord(message):
    text = (
        "🎓 **Diskord live – To'liq bank sistema:**\n\n"
        "1. Cendlar\n"
        "2. Afu,sfu,fu,self fu,inside fu\n"
        "3. negationlar\n"
        "4. x2 va x3 negation\n"
        "5. first,third\n"
        "6. likvidlik\n"
        "7. major minor doji\n"
        "8. doji\n"
        "9. lal\n"
        "10. imbalans\n"
        "11. inside fu\n"
        "12. self fu\n"
        "13. Hcs madeli\n"
        "14. hcs x1 x2 x3\n"
        "15. hcs negation\n"
        "16. hcs+ negation madeli\n"
        "17. true stop loss\n"
        "18. True stop loss bilan ishlash\n"
        "19. Time Frame Stretch\n"
        "20. Tfs established,fresh,closed\n"
        "21. Self negation\n"
        "22. Entry maddellar\n"
        "23. special candle\n"
        "24. 0.1 apart\n"
        "25. laol negation\n"
        "26. x3 negation\n"
        "27. x2 manipulation\n"
        "28. x3 manipulation\n"
        "29. x2 negation\n"
        "30. true hcs\n"
        "31. yonalish topish"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

# 2. ℹ️ Ma'lumot
@bot.message_handler(commands=['malumot'])
def send_malumot(message):
    text = "ℹ️ Ma'lumot"
    bot.send_message(message.chat.id, text)

# 3. 📚 Kurs haqida ma'lumot olish (mavzular va narxi 500$)
@bot.message_handler(commands=['kurs'])
def send_kurs(message):
    text = (
        "📚 **Kurs haqida ma'lumot:**\n\n"
        "**Narxi:** 500$\n\n"
        "**O'qish bo'yicha mavzular:**\n"
        "1. Cendlar\n"
        "2. Afu,sfu,fu,self fu,inside fu\n"
        "3. negationlar\n"
        "4. x2 va x3 negation\n"
        "5. first,third\n"
        "6. likvidlik\n"
        "7. major minor doji\n"
        "8. doji\n"
        "9. lal\n"
        "10. imbalans\n"
        "11. inside fu\n"
        "12. self fu\n"
        "13. Hcs madeli\n"
        "14. hcs x1 x2 x3\n"
        "15. hcs negation\n"
        "16. hcs+ negation madeli\n"
        "17. true stop loss\n"
        "18. True stop loss bilan ishlash\n"
        "19. Time Frame Stretch\n"
        "20. Tfs established,fresh,closed\n"
        "21. Self negation\n"
        "22. Entry maddellar\n"
        "23. special candle\n"
        "24. 0.1 apart\n"
        "25. laol negation\n"
        "26. x3 negation\n"
        "27. x2 manipulation\n"
        "28. x3 manipulation\n"
        "29. x2 negation\n"
        "30. true hcs\n"
        "31. yonalish topish"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

# 4. 👤 Admin bilan bog'lanish (@laa_admin)
@bot.message_handler(commands=['admin'])
def send_admin(message):
    text = "👤 Admin bilan bog'lanish: @laa_admin"
    bot.send_message(message.chat.id, text)

# Botni ishga tushirish
print("Bot ishga tushdi...")
bot.infinity_polling()
