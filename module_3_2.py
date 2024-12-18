# Функция проверки одного адреса email на "правильность"
def email_testing(address):
    # Список из двух проверочных 'флагов', начальные значения False
    email_list = [False, False]
    # Проверка адреса на наличие '@', если есть, то флаг переключаем на True
    if "@" in address:
        email_list[0] = True
    # Делим строку address на список из подстрок по разделителю "."
    # Если адрес правильный, то последним элементом списка, автоматически становится
    # окончание доменной части адреса.
    list_a = address.split(".")
    # Также дополняем окончание доменной части ".", чтоб проверка на правильность
    # окончания адреса соответствовала п.2 Задачи
    list_a[-1] = "." + list_a[-1]
    # Проверка окончания email адреса на правильность (допустимость) доменного адреса.
    # При соответствии, флаг переключаем на True
    if list_a[-1] in [".ru", ".com", ".net"]:
        email_list[1] = True
    return email_list


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    list_r = email_testing(recipient)
    list_s = email_testing(sender)
    if False in list_r or False in list_s:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
