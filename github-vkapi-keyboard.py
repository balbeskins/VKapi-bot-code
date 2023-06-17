import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

vk_session = vk_api.VkApi(token='your_token')
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)


keyboard = VkKeyboard(one_time=False)
keyboard.add_button('Button1', color=VkKeyboardColor.POSITIVE) # button1 - any text you want
keyboard.add_line()
keyboard.add_button('Button2', color=VkKeyboardColor.NEGATIVE) # button2 - any text you want

def sender(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': keyboard.get_keyboard()})

def listmessage():
    listm = ['your', 'text', 'here'] # any text you want
    printlist = '\n'.join(map(str, listm))

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        reseived = event.text
        id = event.user_id
        if reseived == "Your text 1:": # any text you want
            sender(id, listm) # listm - your previous list in def listmessage
        if reseived == "Your text 2:": # any text you want
            sender(id, "Your text 3") # any text you want
