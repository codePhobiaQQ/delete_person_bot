import telebot
import config
import sqlite3

#bot
bot = telebot.TeleBot(config.TOKEN)


# with sqlite3.connect('users.db') as connect:
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat_id, message.chat_id)
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
        


#polling
bot.polling()