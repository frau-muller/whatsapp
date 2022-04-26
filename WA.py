import pywhatkit


def send_message_inst():
    mobile = input('Введите номер получателя: ')
    message = input('Текст сообщения: ')
    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message)


