import telebot
from telebot import types

# التوكن الخاص ببوتك MAXNT
TOKEN = "8831291246:AAHrDeXjKM3qw-huqPndNFCcivDgIckqXVc"
bot = telebot.TeleBot(TOKEN)

# 1. الترحيب بالأعضاء الجدد
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    for member in message.new_chat_members:
        first_name = member.first_name
        welcome_text = f"أهلاً وسهلاً بك يا **{first_name}** في مجتمع **MAXNT**! ⚔️🔥\n\nاضغط على الزر أدناه أو اكتب /scripts للحصول على السكربتات."
        
        # زر سريع للمشاهدة
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("📜 قائمة السكربتات", callback_data="show_scripts")
        markup.add(btn)
        
        bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=markup)

# 2. أمر عرض السكربتات (/scripts أو /script)
@bot.message_handler(commands=['scripts', 'script', 'start'])
def send_scripts_menu(message):
    show_menu(message.chat.id)

def show_menu(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # قائمة السكربتات (تقدر تعدل أو تضيف أزرار زيادة)
    btn1 = types.InlineKeyboardButton("🏴‍☠️ Blox Fruits Script", callback_data="blox_fruits")
    btn2 = types.InlineKeyboardButton("⚔️ King Legacy Script", callback_data="king_legacy")
    btn3 = types.InlineKeyboardButton("🔥 Blade Ball Script", callback_data="blade_ball")
    
    markup.add(btn1, btn2, btn3)
    bot.send_message(chat_id, "اختر اللعبة للحصول على السكربت الخاص بها 🎯:", reply_markup=markup)

# 3. الاستجابة عند الضغط على الأزرار
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "show_scripts":
        show_menu(call.message.chat.id)
        
    elif call.data == "blox_fruits":
        script = "```lua\n-- MAXNT Blox Fruits Script\nloadstring(game:HttpGet('[https://raw.githubusercontent.com/MAXNT/BloxFruits/main/script.lua](https://raw.githubusercontent.com/MAXNT/BloxFruits/main/script.lua)'))()\n```"
        bot.send_message(call.message.chat.id, f"**سكربت Blox Fruits:** ⚔️\n\n{script}\n\n*اضغط على الكود لنخسه مباشرة!*", parse_mode='Markdown')
        
    elif call.data == "king_legacy":
        script = "```lua\n-- MAXNT King Legacy Script\nloadstring(game:HttpGet('[https://raw.githubusercontent.com/MAXNT/KingLegacy/main/script.lua](https://raw.githubusercontent.com/MAXNT/KingLegacy/main/script.lua)'))()\n```"
        bot.send_message(call.message.chat.id, f"**سكربت King Legacy:** 👑\n\n{script}\n\n*اضغط على الكود لنخسه مباشرة!*", parse_mode='Markdown')

    elif call.data == "blade_ball":
        script = "```lua\n-- MAXNT Blade Ball Script\nloadstring(game:HttpGet('[https://raw.githubusercontent.com/MAXNT/BladeBall/main/script.lua](https://raw.githubusercontent.com/MAXNT/BladeBall/main/script.lua)'))()\n```"
        bot.send_message(call.message.chat.id, f"**سكربت Blade Ball:** ⚽\n\n{script}\n\n*اضغط على الكود لنخسه مباشرة!*", parse_mode='Markdown')

print("بوت MAXNT جاهز للعمل والترحيب ونشر السكربتات! 🚀")
bot.infinity_polling()
