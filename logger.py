import os
import sys
import json
import locale

from loguru import logger


log_messages = {
    'en': { # English
        'screen': 'Taking a screenshot of the phone screen...',
        'game.lvl': 'Determining the game level...',
        'solve.game': 'Solved the puzzle...',
        'need.swipes': 'For solving the puzzle needed <g>{}</g> swipes, starting...',
        'grid.error': "<r>Invalid grid</r> or <y>game didn't start</y>.",
        'sended': '<g>Sent</g>: {}',
        'screen.size': "Determining the phone screen size...",
        'screen.size.err': "<r>Your screen size was not found!</r> maybe you dont download ADB? https://developer.android.com/tools/releases/platform-tools",
        'coords.adj.do': "Adjusting coordinates <g>{}</g> to the screen size...",
        'map': 'Detected game grid:',
        'cant.find.path': "<r>Could not find the path in {} seconds... terminating</r>",
        'bfs.error': "<r>BFS terminated but could not find a path</r>",
        'stats': "<g>Time spent</g>: screen (<g>{:06.2f}</g>) | init (<g>{:06.2f}</g>) | solve (<g>{:06.2f}</g>) | run (<g>{:06.2f}</g>)",
        'exit': "Press Enter for close program...",
        'connect.device': "Are you sure you have connected the phone via USB and set it up properly? Connect the phone, configure it as described in README.txt and try again.",
        "screenshot.error": "<r>Screenshot not found, have you turned off the phone?</r>"
    },
    'ru': { # русский
        'screen': 'Делаем скриншот экрана телефона...',
        'game.lvl': 'Определяем уровень игры...',
        'solve.game': 'Решили головоломку...',
        'need.swipes': 'Для решения головоломки нужно <g>{}</g> свайпов, начинаем...',
        'grid.error': "<r>Некорректная определена сетка уровня</r> или <y>игра не запущена</y>.",
        'sended': '<g>Отправлено</g>: {}',
        'screen.size': "Узнаю размер экрана телефона...",
        'screen.size.err': "<r>Размеры вашего экрана не найден!</r>\nВы точно скачали ADB файлы? https://developer.android.com/tools/releases/platform-tools\nСкачайте их и положите файлы adb.exe, AdbWinApi.dll, AdbWinUsbApi.dll в папку с программой.",
        'coords.adj.do': "Преобразую координаты <g>{}</g> под размер экрана...",
        'map': 'Карта уровня:',
        'cant.find.path': "<r>Не удалось найти решение уровня за {} сек, завершаем.</r>",
        'bfs.error': "<r>Алгоритм BFS завершен и путь не найден :(</r>",
        'stats': "<g>Затраченное время</g>: скриншот (<g>{:06.2f}</g>) | детект-уровня (<g>{:06.2f}</g>) | решение (<g>{:06.2f}</g>) | выполнение (<g>{:06.2f}</g>)",
        'exit': "Нажмите Enter для выхода...",
        'connect.device': "Вы точно подключили телефон по USB и настроили его? Подключите телефон, настройте его как написано в README.txt и попробуйте снова.",
        "screenshot.error": "<r>Скриншот экрана не сделан, вы отключили телефон?</r>"
    }
}


def get_language():
    lang = locale.getlocale()[0][:2].lower()
    
    if lang not in log_messages:
        lang = 'en'
    
    if not os.path.exists('lang.json'):
        with open('lang.json', 'w') as file:
            json.dump({'language': lang}, file)
    
    return lang


LANG = get_language()


def get_msg(key, lang='en'):
    return log_messages.get(lang, {}).get(key, '')


logger.remove()
logger.add(sink=sys.stdout, format="<cyan>{time:DD-MM-YYYY HH:mm:ss.SS}</cyan>"
                                " | <level>{level: <5}</level>"
                                " | <white><b>{message}</b></white>")
logger = logger.opt(colors=True)
