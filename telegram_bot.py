import telebot
import config
import sqlite3

#bot
bot = telebot.TeleBot(config.TOKEN)

# with sqlite3.connect('users.db') as connect:
@bot.message_handler(commands=['start'])
def start(message):
    print("here")
    bot.send_message(message.chat.id, message.chat.id)
    
    if message.chat.type == "group":
        bot.send_message(message.chat.id, 'Это группа')
    else: 
        bot.send_message(message.chat.id, 'Нет')
    
    
    # amount = bot.get_chat_member_count(message.chat.id)
    # bot.send_message(message.chat.id, amount)


    # connect = sqlite3.connect('users.db')
    # cursor = connect.cursor()
    # cursor.execute(""" CREATE TABLE IF NOT EXISTS login_id(
    #     id INTEGER
    # ) """)
    # connect.commit()
    
    # #check id in fields
    # people_id = message.chat.id
    # cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
    # data = cursor.fetchone()
    # if data is None:
    #     #add values in fields
    #     user_id = [message.chat.id]
    #     cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
    #     connect.commit()
    # else:
    #     bot.send_message(message.chat.id, 'Такой пользователь уже существует')
        
    # connect.close()
            

    # @bot.message_handler(commands=['delete'])
    # def delete(message):
    #     cursor = connect.cursor()
    #     people_id = message.chat.id
    #     cursor.execute(f"DELETE FROM login_id WHERE id = {people_id};")
    #     connect.commit()
        


@bot.message_handler(commands=['info1'])
def people(message):
    # member = bot.get_chat_member(message.chat.id, message.from_user.id)
    member = bot.get_chat_member(message.chat.id, "689759837")
    #then member added to chat
    bot.send_message(message.chat.id, member)
    #person status
    # bot.send_message(message.chat.id, member.status)
    #kick person
    bot.kick_chat_member(message.chat.id, "689759837")

#polling
bot.polling()