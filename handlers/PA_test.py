from aiogram import types
from dispatcher import dp
import config
import re
from bot import BotDB
from datetime import datetime, date, time

homework = ''
users = []
ban_list = [1234567890, 809737708]
administrators = [1010912506, 624844200, 1144754121]
users_i = 23
anarchy = True
password = '250706'

def check_date(date, now):
    if(date < now):
        date += 7
    return date

def check_date_i(date, now_m, num):
    if (now_m == 1 or now_m == 3 or now_m == 5 or now_m == 7 or now_m == 8 or now_m == 10 or now_m == 12):
        if(date > 31):
            date = 1 + num
    elif (now_m == 4 or now_m == 6 or now_m == 9 or now_m == 11):
        if(date > 30):
            date = 1 + num
    elif (now_m == 2):
        if(date > 28):
            date = 1 + num
    return date

def check_month(date, month):
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        if(date > 31):
            month = month + 1
            if(month == 13): month = 1
    elif (month == 4 or month == 6 or month == 9 or month == 11):
        if(date > 30):
            month = month + 1
            if(month == 13): month = 1
    elif (month == 2):
        if(date > 28):
            month = month + 1
            if(month == 13): month = 1
    return month

def date_to_str(date):
    if(len(str(date)) == 1):
        date_str = "0" + str(date)
    else:
        date_str = str(date)
    return date_str

def main_menu():
    menu = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Получить ДЗ")
    item2 = types.KeyboardButton("Загрузить ДЗ")
    item3 = types.KeyboardButton("Расписание")
    item4 = types.KeyboardButton("Узнать ДЗ на дату")
    menu.add(item1, item2, item3, item4)
    return menu

class User():
    date_hw = ''
    subject = ''
    first_name = ''
    last_name = ''

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.stage_hw = 0
        self.stage_get_hw = 0
        self.stage_get_hw_gf = 0

@dp.message_handler(commands = "start")
async def start(message: types.Message):
    global users
    global users_i
    if(not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id)
    
    menu = main_menu()
    user = User(message.from_user.id, message.from_user.first_name, message.from_user.last_name)
    users.append(user)
    if(user.first_name is None or user.first_name == 'None' or user.first_name == 'none'):
        first = 'None'
    else:
        first = user.first_name
    if(user.last_name is None or user.last_name == 'None' or user.last_name == 'none'):
        last = 'None'
    else:
        last = user.last_name
    if(user.id is None or user.id == 'None' or user.id == 'none'):
        uid = 'None'
    else:
        uid = user.id
    cmd = 'User' + str(users_i) + ':\n' + '\tID: ' + str(uid) + '\n' + '\tFirst name: ' + first + '\n' + '\tLast name: ' + last + '\n\n'
            

    users_txt = open('files/users.txt', 'r')
    tmp = users_txt.read()
    users_txt.close()
    if (str(user.id) not in tmp):
        users_txt = open('files/users.txt', 'a')
        users_txt.write(cmd)
        users_i += 1

    if(str(message.from_user.first_name) != 'None'):
        name = message.from_user.first_name
    elif(str(message.from_user.last_name) != 'None'):
        name = message.from_user.last_name
    else:
        name = 'пользователь'
    
    await message.bot.send_message(message.chat.id, ('Привет, ' + str(name) + '!').format(message.from_user), reply_markup = menu) 

@dp.message_handler(content_types = ["text"])
async def start(message):
    global homework
    global users
    global users_i
    global administrators
    global anarchy
    global ban_list

    isuser = False
    for user_i in users:
        if(user_i.id == message.from_user.id):
            user = user_i
            isuser = True
            
    if (isuser == False):

        user = User(message.from_user.id, message.from_user.first_name, message.from_user.last_name)
        users.append(user)
        if(user.first_name is None or user.first_name == 'None' or user.first_name == 'none'):
            first = 'None'
        else:
            first = user.first_name
        if(user.last_name is None or user.last_name == 'None' or user.last_name == 'none'):
            last = 'None'
        else:
            last = user.last_name
        if(user.id is None or user.id == 'None' or user.id == 'none'):
            uid = 'None'
        else:
            uid = user.id
        cmd = 'User' + str(users_i) + ':\n' + '\tID: ' + str(uid) + '\n' + '\tFirst name: ' + first + '\n' + '\tLast name: ' + last + '\n\n'

        users_txt = open('files/users.txt', 'r')
        tmp = users_txt.read()
        users_txt.close()
        if (str(user.id) not in tmp):
            users_txt = open('files/users.txt', 'a')
            users_txt.write(cmd)
            users_i += 1

    if message.text == 'anarchy' or message.text == 'Anarchy':
        await message.bot.send_message(message.chat.id, "Пожалуйста введите пароль".format(message.from_user))
    elif message.text == '250706' and anarchy == False:
        anarchy = True
        await message.bot.send_message(message.chat.id, "Режим анархии активирован".format(message.from_user))
    elif message.text == '250706' and anarchy == True:
        anarchy = False
        await message.bot.send_message(message.chat.id, "Режим анархии отключён".format(message.from_user))

    elif 'unbanned' in message.text or 'Unbanned' in message.text:
        user_b = ''
        for i in range(9, len(message.text)):
            if(message.text[i] != ' '):
                user_b += message.text[i]
        ban_list.remove(int(user_b))
        await message.bot.send_message(message.chat.id, ("Пользователь " + str(user_b) + " разбанен").format(message.from_user))

    elif 'banned' in message.text or 'Banned' in message.text:
        user_b = ''
        for i in range(7, len(message.text)):
            if(message.text[i] != ' '):
                user_b += message.text[i]
        ban_list.append(int(user_b))
        await message.bot.send_message(message.chat.id, ("Пользователь " + str(user_b) + " забанен").format(message.from_user))

    elif 'unadmin' in message.text or 'Unadmin' in message.text:
        user_b = ''
        for i in range(8, len(message.text)):
            if(message.text[i] != ' '):
                user_b += message.text[i]
        administrators.remove(int(user_b))
        await message.bot.send_message(message.chat.id, ("Пользователь " + str(user_b) + " лишён прав администратора").format(message.from_user))

    elif ('admin' in message.text or 'Admin' in message.text) and 'list' not in message.text:
        user_b = ''
        for i in range(6, len(message.text)):
            if(message.text[i] != ' '):
                user_b += message.text[i]
        administrators.append(int(user_b))
        await message.bot.send_message(message.chat.id, ("Пользователю " + str(user_b) + " выданы права администратора").format(message.from_user))
    
    elif message.from_user.id in ban_list:
        await message.bot.send_message(message.chat.id, 'Вы забанены!\nЕсли есть вопросы обратитесь к администратору'.format(message.from_user)) 

    elif message.text == 'Назад ↩️':
        menu = main_menu()
        user.stage_hw = 0
        user.stage_get_hw = 0
        await message.bot.send_message(message.chat.id, 'Назад ↩️'.format(message.from_user), reply_markup = menu) 

    elif message.text == 'Расписание':
        photo = open('files/timetable.jpeg', 'rb')
        await message.bot.send_photo(message.chat.id, photo = photo)

    elif message.text == 'Загрузить ДЗ':

        if(message.from_user.id in administrators or anarchy):
            await message.bot.send_message(message.chat.id, 'Доступ разрешён'.format(message.from_user)) 

            menu = types.ReplyKeyboardMarkup(resize_keyboard = True)

            now = datetime.now()
            weekday = datetime.weekday(now)
            date = str(datetime.date(now))
            today = date[8] + date[9]
            monday = int(today) - int(weekday)
            num_day = 0

            today_date = check_date(monday, int(today))
            today_date = check_date_i(today_date, now.month, num_day)
            if (int(today_date) < 10):
                num_day += 1
            today_date_str = date_to_str(today_date)
            month_n = check_month(today_date, now.month)
            month_n_str = date_to_str(month_n)

            user.date_hw = "Понедельник\n(" + today_date_str + "." + month_n_str + ")"
            item1 = types.KeyboardButton(user.date_hw)

            today_date = check_date(monday + 1, int(today))
            month_n = check_month(today_date, now.month)
            today_date = check_date_i(today_date, now.month, num_day)
            if (int(today_date) < 10):
                num_day += 1
            today_date_str = date_to_str(today_date)
            month_n_str = date_to_str(month_n)

            user.date_hw = "Вторник\n(" + today_date_str + "." + month_n_str + ")"
            item2 = types.KeyboardButton(user.date_hw)

            today_date = check_date(monday + 2, int(today))
            month_n = check_month(today_date, now.month)
            today_date = check_date_i(today_date, now.month, num_day)
            if (int(today_date) < 10):
                num_day += 1
            today_date_str = date_to_str(today_date)
            month_n_str = date_to_str(month_n)

            user.date_hw = "Среда\n(" + today_date_str + "." + month_n_str + ")"
            item3 = types.KeyboardButton(user.date_hw)

            today_date = check_date(monday + 3, int(today))
            month_n = check_month(today_date, now.month)
            today_date = check_date_i(today_date, now.month, num_day)
            if (int(today_date) < 10):
                num_day += 1
            today_date_str = date_to_str(today_date)
            month_n_str = date_to_str(month_n)

            user.date_hw = "Четверг\n(" + today_date_str + "." + month_n_str + ")"
            item4 = types.KeyboardButton(user.date_hw)

            today_date = check_date(monday + 4, int(today))
            month_n = check_month(today_date, now.month)
            today_date = check_date_i(today_date, now.month, num_day)
            if (int(today_date) < 10):
                num_day += 1
            today_date_str = date_to_str(today_date)
            month_n_str = date_to_str(month_n)

            user.date_hw = "Пятница \n(" + today_date_str + "." + month_n_str + ")"
            item5 = types.KeyboardButton(user.date_hw)
            
            back = types.KeyboardButton("Назад ↩️")
            menu.add(item1, item2, item3, item4, item5, back)
            user.stage_hw = 1
            await message.bot.send_message(message.chat.id, 'Выберите дату'.format(message.from_user), reply_markup = menu) 
        else:
            await message.bot.send_message(message.chat.id, 'Недостаточно прав доступа'.format(message.from_user)) 

    elif user.stage_hw == 3:
        homework_db = user.date_hw + user.subject + "%&%" + message.text
        first = '...'
        last = '...'
        if(str(message.from_user.first_name) != 'None'):
            first = str(message.from_user.first_name)
        if(str(message.from_user.last_name) != 'None'):
            last = str(message.from_user.last_name)
        user_hw = str(message.from_user.id) + " | " + first + " | " + last
        BotDB.add_homework(message.from_user.id, user_hw, homework_db)
        user.stage_hw = 0
        menu = main_menu()
        if(str(message.from_user.first_name) != 'None'):
            name = message.from_user.first_name
        elif(str(message.from_user.last_name) != 'None'):
            name = message.from_user.last_name
        else:
            name = 'пользователь'
        await message.bot.send_message(message.chat.id, ('Домашнее задание загружено \nСпасибо, ' + name + '!').format(message.from_user), reply_markup = menu)

    elif user.stage_hw == 2:
        user.subject = message.text
        user.stage_hw = 3
        await message.bot.send_message(message.chat.id, 'Напишите задание'.format(message.from_user))
        
    elif user.stage_hw == 1:
        date_hf = message.text
        lend = len(date_hf)
        user.date_hw = date_hf[lend - 6] + date_hf[lend - 5] + date_hf[lend - 4] + date_hf[lend - 3] + date_hf[lend - 2] + "." + str(datetime.today().year)
        user.stage_hw = 2

        menu = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton("Русский 🇷🇺")
        item2 = types.KeyboardButton("Литература📕")
        item3 = types.KeyboardButton("История 📜")
        item4 = types.KeyboardButton("Право 👨‍⚖")
        item5 = types.KeyboardButton("Общество 📋")
        item6 = types.KeyboardButton("Алгебра 📈")#3^2x-1 3^2x
        item7 = types.KeyboardButton("Геометрия 📐")
        item8 = types.KeyboardButton("Астрономия🔭")
        item9 = types.KeyboardButton("ОБЖ 🪖")
        item10 = types.KeyboardButton("Информатика🖥")
        item11 = types.KeyboardButton("Английский язык 🇬🇧")
        item12 = types.KeyboardButton("Биология 🔬")
        item13 = types.KeyboardButton("География 🌍")
        item14 = types.KeyboardButton("Проект 📊")
        back = types.KeyboardButton("Назад ↩️")
        menu.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, back)
        await message.bot.send_message(message.chat.id, 'Выберите предмет'.format(message.from_user), reply_markup = menu)

    elif message.text == 'Узнать ДЗ на дату':
        user.stage_get_hw_gf = 1
        await message.bot.send_message(message.chat.id, 'Напишите дату, на которую хотите узнать ДЗ\nВ формате dd.mm.yyyy'.format(message.from_user)) 

    elif user.stage_get_hw_gf == 1:
        user.stage_get_hw_gf = 0
        date_hf = message.text
        if(date_hf[1] == '.'):
            date_hf = "0" + date_hf
        isodate = int(date_hf[0] + date_hf[1])
        isomonth = int(date_hf[3] + date_hf[4])
        isoyear = int(date_hf[6] + date_hf[7] + date_hf[8] + date_hf[9])
        user.stage_get_hw = 0

        records = BotDB.get_homeworks(message.from_user.id)

        menu = main_menu()
        if(len(records)):
            answer = f"🕘 Домашнее задание на {date_hf}\n\n"

            for r in records:
                cmd = r[3]
                if(cmd != '' and r[0] > 0):
                    date_out = int(cmd[0] + cmd[1])
                    month_out = int(cmd[3] + cmd[4])
                    year_out = int(cmd[6] + cmd[7] + cmd[8] + cmd[9])
                    user.subject_out = ''
                    for i in range(10, len(cmd)):
                        if(cmd[i] == '%'):
                            break
                        user.subject_out += cmd[i]     
                                       
                    homework_out = ''
                    score = 0
                    for i in range(5, len(cmd)):
                        if (score >= 3):
                            homework_out += cmd[i] 
                        if (cmd[i] == '%' or cmd[i] == '&' or cmd[i] == '/'):
                            score += 1

                    if (date_out == isodate and month_out == isomonth and year_out == isoyear):
                        answer += "<b>" + (user.subject_out) + "</b>\n"
                        answer += f" - {homework_out}\n\n"

            await message.reply(answer, reply_markup = menu)
        else:
            await message.reply("Записей не обнаружено!")
    
    elif message.text == 'Получить ДЗ':
        menu = types.ReplyKeyboardMarkup(resize_keyboard = True)

        now = datetime.now()
        weekday = datetime.weekday(now)
        date = str(datetime.date(now))
        today = date[8] + date[9]
        monday = int(today) - int(weekday)
        num_day = 0

        today_date = check_date(monday, int(today))
        month_n = check_month(today_date, now.month)
        today_date = check_date_i(today_date, now.month, num_day)
        if (int(today_date) < 10):
            num_day += 1
        today_date_str = date_to_str(today_date)
        month_n_str = date_to_str(month_n)

        user.date_hw = "Понедельник\n(" + today_date_str + "." + month_n_str + ")"
        item1 = types.KeyboardButton(user.date_hw)

        today_date = check_date(monday + 1, int(today))
        month_n = check_month(today_date, now.month)
        today_date = check_date_i(today_date, now.month, num_day)
        if (int(today_date) < 10):
            num_day += 1
        today_date_str = date_to_str(today_date)
        month_n_str = date_to_str(month_n)

        user.date_hw = "Вторник\n(" + today_date_str + "." + month_n_str + ")"
        item2 = types.KeyboardButton(user.date_hw)

        today_date = check_date(monday + 2, int(today))
        month_n = check_month(today_date, now.month)
        today_date = check_date_i(today_date, now.month, num_day)
        if (int(today_date) < 10):
            num_day += 1
        today_date_str = date_to_str(today_date)
        month_n_str = date_to_str(month_n)

        user.date_hw = "Среда\n(" + today_date_str + "." + month_n_str + ")"
        item3 = types.KeyboardButton(user.date_hw)

        today_date = check_date(monday + 3, int(today))
        month_n = check_month(today_date, now.month)
        today_date = check_date_i(today_date, now.month, num_day)
        if (int(today_date) < 10):
            num_day += 1
        today_date_str = date_to_str(today_date)
        month_n_str = date_to_str(month_n)

        user.date_hw = "Четверг\n(" + today_date_str + "." + month_n_str + ")"
        item4 = types.KeyboardButton(user.date_hw)

        today_date = check_date(monday + 4, int(today))
        month_n = check_month(today_date, now.month)
        today_date = check_date_i(today_date, now.month, num_day)
        if (int(today_date) < 10):
            num_day += 1
        today_date_str = date_to_str(today_date)
        month_n_str = date_to_str(month_n)

        user.date_hw = "Пятница \n(" + today_date_str + "." + month_n_str + ")"
        item5 = types.KeyboardButton(user.date_hw)
        
        back = types.KeyboardButton("Назад ↩️")
        menu.add(item1, item2, item3, item4, item5, back)
        user.stage_get_hw = 1
        await message.bot.send_message(message.chat.id, 'Выберите дату'.format(message.from_user), reply_markup = menu) 

    elif user.stage_get_hw == 1:
        date_hf = message.text
        lend = len(date_hf)
        date = date_hf[lend - 6] + date_hf[lend - 5] + date_hf[lend - 4] + date_hf[lend - 3] + date_hf[lend - 2] 
        isoyear = datetime.today().year
        isodate = int(date[0] + date[1])
        isomonth = int(date[3] + date[4])
        user.stage_get_hw = 0

        records = BotDB.get_homeworks(message.from_user.id)

        menu = main_menu()
        if(len(records)):
            answer = f"🕘 Домашнее задание на {date}\n\n"

            for r in records:
                cmd = r[3]
                if(cmd != '' and r[0] > 0):
                    date_out = int(cmd[0] + cmd[1])
                    month_out = int(cmd[3] + cmd[4])
                    year_out = int(cmd[6] + cmd[7] + cmd[8] + cmd[9])
                    user.subject_out = ''
                    for i in range(10, len(cmd)):
                        if(cmd[i] == '%'):
                            break
                        user.subject_out += cmd[i]     
                                       
                    homework_out = ''
                    score = 0
                    for i in range(5, len(cmd)):
                        if (score >= 3):
                            homework_out += cmd[i] 
                        if (cmd[i] == '%' or cmd[i] == '&' or cmd[i] == '/'):
                            score += 1

                    if (date_out == isodate and month_out == isomonth and year_out == isoyear):
                        answer += "<b>" + (user.subject_out) + "</b>\n"
                        answer += f" - {homework_out}\n\n"

            await message.reply(answer, reply_markup = menu)
        else:
            await message.reply("Записей не обнаружено!")
    elif message.text == 'full users' or message.text == 'Full users':
        users_txt = open('files/users.txt', 'r')
        cmd = users_txt.read()
        users_txt.close()
        await message.reply(cmd)
    
    elif message.text == 'users' or message.text == 'Users':
        cmd = ''
        i = 1
        for user_i in users:
            if(user_i.first_name is None or user_i.first_name == 'None' or user_i.first_name == 'none'):
                first = 'None'
            else:
                first = user_i.first_name
            if(user_i.last_name is None or user_i.last_name == 'None' or user_i.last_name == 'none'):
                last = 'None'
            else:
                last = user_i.last_name
            if(user_i.id is None or user_i.id == 'None' or user_i.id == 'none'):
                uid = 'None'
            else:
                uid = user_i.id
            cmd += 'User' + str(i) + ':\n' + '\t\t\t\tID: ' + str(uid) + '\n' + '\t\t\t\tFirst name: ' + first + '\n' + '\t\t\t\tLast name: ' + last + '\n\n'
            i += 1
        # users_txt = open("users.txt", 'r')
        # cmd = users_txt.read()
        # users_txt.close()
        await message.reply(cmd)
    
    elif message.text == 'Ban list' or message.text == 'ban list':
        cmd = ''
        for i in ban_list:
            cmd += str(i) + '\n'
        await message.bot.send_message(message.chat.id, cmd.format(message.from_user)) 

    elif message.text == 'Admin list' or message.text == 'admin list':
        cmd = ''
        for i in administrators:
            cmd += str(i) + '\n'
        await message.bot.send_message(message.chat.id, cmd.format(message.from_user)) 



@dp.message_handler(commands = ("spent", "earned", "s", "e"), commands_prefix = "/!")
async def start(message: types.Message):
    cmd_variants = (('/spent', '/s', '!spent', '!s'), ('/earned', '/e', '!earned', '!e'))
    operation = '-' if message.text.startswith(cmd_variants[0]) else '+'

    value = message.text
    for i in cmd_variants:
        for j in i:
            value = value.replace(j, '').strip()

    if(len(value)):
        x = re.findall(r"\d+(?:.\d+)?", value)
        if(len(x)):
            value = float(x[0].replace(',', '.'))

            BotDB.add_record(message.from_user.id, operation, value)

            if(operation == '-'):
                await message.reply("✅ Запись о <u><b>расходе</b></u> успешно внесена!")
            else:
                await message.reply("✅ Запись о <u><b>доходе</b></u> успешно внесена!")
        else:
            await message.reply("Не удалось определить сумму!")
    else:
        await message.reply("Не введена сумма!")

@dp.message_handler(commands = ("add"), commands_prefix = "/!")
async def start(message: types.Message):
    cmd_variants = (('/add'))

    value = message.text
    for i in cmd_variants:
        for j in i:
            value = value.replace(j, '').strip()

    date = "10.12.2022"

    BotDB.add_homework(message.from_user.id, date, value)

    await message.reply("✅ Запись <u><b>успешно</b></u> внесена!")

@dp.message_handler(commands = ("history", "h"), commands_prefix = "/!")
async def start(message: types.Message):
    cmd_variants = ('/history', '/h', '!history', '!h')
    within_als = {
        "day": ('today', 'day', 'сегодня', 'день'),
        "month": ('month', 'месяц'),
        "year": ('year', 'год'),
    }

    cmd = message.text
    for r in cmd_variants:
        cmd = cmd.replace(r, '').strip()

    within = 'day'
    if(len(cmd)):
        for k in within_als:
            for als in within_als[k]:
                if(als == cmd):
                    within = k

    records = BotDB.get_records(message.from_user.id, within)

    if(len(records)):
        answer = f"🕘 История операций за {within_als[within][-1]}\n\n"

        for r in records:
            answer += "<b>" + ("➖ Расход" if not r[2] else "➕ Доход") + "</b>"
            answer += f" - {r[3]}"
            answer += f" <i>({r[4]})</i>\n"

        await message.reply(answer)
    else:
        await message.reply("Записей не обнаружено!")