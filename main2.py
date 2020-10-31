import vk_api  #random,vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
vk_session = vk_api.VkApi(token='42bdd7df0907749dc697117dd14d3e17568f58871dd2bffb0cc244268e7697cf2724251afb227ce6fa1ab')
from vk_api.bot_longpoll import VkBotLongPoll  #VkBotEventType
longpoll = VkBotLongPoll(vk_session, '199882350')
vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType
Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Востановления Пароля ', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button('Регистрация', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button('Тех.Поддержка', color=VkKeyboardColor.PRIMARY)



for event in Lslongpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        vars0 = ['Начать', 'начать', 'start']
        if event.text in vars0:
            if event.from_user:
                Lsvk.messages.send(
                    user_id=event.user_id,
                    message='Здравствуйте чем я могу вам помочь',
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard()
                )
        vars1 = ['Востановления Пароля']
        if event.text in vars1:
            if event.from_user:
                Lsvk.messages.send(
                    user_id=event.user_id,
                    message='✅На сайте есть кнопка восстановления пароля',
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard()
                    )
                Lsvk.messages.send(
                    user_id=event.user_id,
                    message='✅Куда указываете свою личную эл.почту, которую указывали при регистрации.',
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard()
                )
                Lsvk.messages.send(
                    user_id=event.user_id,
                    message='✅Далее на этот email придет ссылка для сброса пароля и после перехода к нему можете ввести новый пароль. ',
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard()
                )
                Lsvk.messages.send(
                    user_id=event.user_id,
                    message='✅Если вы не помните логин и email, который указывали при регистрации, то надо аналогично регистрации заполнить свои данные и нажать на "Проверить" после если вы уже зарегистрированы, то покажет, ваш логин и email',
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard()
                )
        vars2 = ['Регистрация']
        if event.text in vars2:
            if event.from_user:
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='✅Для регистрации указываете ФИО, дату рождения и паспортные данные',

                    )
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='✅После этого нажимаете на "Проверить"',

                )
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='✅На следующей странице выбираете нужный логин и указываете пароль (они будут использоваться для входа в личный кабинет) и указываете телефон и email (Email используется для активации аккаунта и восстановления пароля) ',

                )
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='✅Далее на указанный email придет ссылка для активации аккаунта и после этого можете зайти на свой личный кабинет. ',

                )
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='Или посмотрите видеоролик                         📺: https://www.youtube.com/watch?v=nhMT3TcCyGQ',

                )
        vars3 = ['Тех.Поддержка']
        if event.text in vars3:
            if event.from_user:
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='✉️Пресс-служба press-service@s-vfu.ru',

                )
                Lsvk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='📞Телефон: +7 (4112) 49-65-40',

                )
