import pywhatki


def send_message_inst():
    mobile = input('Введите номер получателя: ')
    message = input('Текст сообщения: ')
    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message)


def send_message():
    mobile = input('Введите номер получателя: ')
    message = input('Текст сообщения: ')
    hour = int(input('Введите часы: '))
    minutes = int(input('Введите минуты: '))
    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message, time_hour=hour, time_min=minutes)

def main():
    send_message_inst()

if __name__ == '__main__':
    main()
