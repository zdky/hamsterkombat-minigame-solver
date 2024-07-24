<p align="center">
    <img width="100%" src="https://github.com/zdky/hamsterkombat-minigame-solver/blob/main/res/banner.png">
</p>

<p align="center">
    <a href="https://www.python.org/downloads/">
        <img src="https://img.shields.io/badge/python-3.11%2B-blue.svg?style=flat-square&logo=python&logoColor=white&color=blue" alt="python 3.11">
    </a>
    <a href="https://github.com/zdky/hamsterkombat-minigame-solver/issues">
        <img src="https://img.shields.io/github/issues/zdky/hamsterkombat-minigame-solver?style=flat-square" alt="open issues">
    </a>
    <a href="https://github.com/zdky/hamsterkombat-minigame-solver/issues?q=is%3Aissue+is%3Aclosed">
        <img src="https://img.shields.io/github/issues-closed/zdky/hamsterkombat-minigame-solver?style=flat-square" alt="closed issues">
    </a>
    <a href="https://t.me/Zhidky" target="_blank">
        <img src="https://img.shields.io/badge/Telegram-Join-Blue.svg?style=flat-square&logo=telegram&logoColor=white&color=blue" alt="Telegram">
    </a>
    <a href="https://www.donationalerts.com/r/zhidky" target="_blank">
        <img src="https://img.shields.io/badge/DonationAlerts-Thanks-blue.svg?style=flat-square&logo=paypal&logoColor=fff" alt="Support me">
    </a>
    <br>
</p>

> <b><a href="https://github.com/zdky/hamsterkombat-minigame-solver/blob/main/README_EN.md">English Documentation</a></b> 🇬🇧

## Функции ⚙️

* Делает скриншот на телефоне и отправляет на ПК
* Анализирует уровень алгоритмом «поиск в ширину» для решения
* Отправляет команды свайпа на телефон через adb (Android Debug Bridge)

## Запуск 🚀

<details>
<summary>Нажми на меня, чтобы открыть гайд на Windows (для новичков)</summary>

- **Шаг 0.** Установи Python и VSCode:

> Python: https://www.python.org/downloads <br>
> VSCode: https://code.visualstudio.com/download

- **Шаг 1.** Сохрани мой проект:

```bash
git clone https://github.com/zdky/hamsterkombat-minigame-solver.git
```
> или нажми на кнопку выше [Code] ➜ [Download ZIP]

- **Шаг 2.** Открой папку проекта и введи в адресной строке проводника:
```bash
cmd
```

- **Шаг 3.** Создай виртуальную среду для python. В открывшейся консоли введи:

```bash
python -m venv .
```

- **Шаг 4.** Правый клик в папке проекта и «Открыть с помощью Code»

- **Шаг 5.** Выбери свою виртуальную среду. В VSCode нажми «Ctrl+Shift+P» и введи:
```
python select interpreter
```
«Enter» и нажми на свою вирт.среду: «Python 3...('hamsterkombat-minigame-solver': venv)...»

- **Шаг 6.** Открой терминал. В VSCode меню: «Terminal» ➜ «New Terminal» или Ctrl+Shift+`

- **Шаг 7.** Установи библиотеки, введи в терминале VSCode:

```bash
pip install -r requirements.txt
```

- **Шаг 8.** Теперь настрой свой телефон:<br>1) Зайди в «Настройки» ➜ «О телефоне»<br>2) Листни вниз и найди «Номер сборки»<br>3) Нажми на «Номер сборки» семь раз<br>4) Если ты видишь сообщение «Вы теперь разработчик» — отлично!<br>5) Зайди в «Настройки» ➜ «Системы» или «Расширенные настройки» ➜ «Для разработчиков»<br>6) Найди «Отладка по USB» и включи её<br>7) Найди «Отладка по USB (Настройки безопасности)» и включи её*<br>*(*если требует авторизации в MIUI или другом сервисе, сделай это!*)
  
- **Шаг 9.** Присоедини телефон по USB к ПК

- **Шаг 10.** Открой в VSCode «Explorer» (Ctrl+Shift+E) и нажми на «main.py»

- **Шаг 11.** Запусти программу первый раз для теста. Нажми на ▷ в вверхнем правом углу

- **Шаг 12.** Открой мини-игру в HamsterKombat и начни её, сразу же запусти эту программу снова.

- **Шаг 99.** Наслаждаться и подписаться на [мой телеграм канал](https://t.me/Zhidky)

</details>

> *Ты новичок и не получилось запустить? [Напиши мне об этом!](https://github.com/zdky/hamsterkombat-minigame-solver/issues/)*


### Поддержать ☕

[![Sponsor zdky](https://img.shields.io/badge/Sponsor-zdky-%23158c41?style=for-the-badge&logo=paypal&logoColor=fff)](https://www.donationalerts.com/r/zhidky)


### Репорт багов 🕵

Если вы нашли что-то, что работает не так, как должно, или хотите предложить новую функцию, то создайте тикет на GitHub.
Для ошибок, пожалуйста, опишите шаги, необходимые для воспроизведения, и включите соответствующую информацию, например, информацию о системе и результаты логов программы.

[![Raise an Issue](https://img.shields.io/badge/Raise_an_Issue-GitHub-%23060606?style=for-the-badge&logo=github&logoColor=fff)](https://github.com/zdky/hamsterkombat-minigame-solver/issues/)


### Contributing 👨‍💻

Вклад любого рода очень приветствуется и будет высоко оценен.
Кодекс поведения: [Contributor Convent](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).<br>
Чтобы начать работу, создайте форк репозитория, внесите свои изменения, добавьте, зафиксируйте и выложите код, а затем вернитесь сюда, чтобы открыть pull request. Если вы новичок в GitHub или открытом коде, [вот гайд](https://www.freecodecamp.org/news/how-to-make-your-first-pull-request-on-github-3#let-s-make-our-first-pull-request-) или [git документация](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) поможет вам начать, но не стесняйтесь обращаться ко мне, если вам нужна поддержка.

[![Submit a PR](https://img.shields.io/badge/Submit_a_PR-GitHub-%23060606?style=for-the-badge&logo=github&logoColor=fff)](https://github.com/zdky/hamsterkombat-minigame-solver/compare)


### Благодарность ❤️

> Отдельное спасибо [AshishBora](https://github.com/AshishBora) за «[Unblock Me Solver](https://github.com/AshishBora/unblock-me-solver)» без его проекта, я бы не создал этот.


### Лицензия

> _**[zdky/hamsterkombat-minigame-solver](https://github.com/zdky/hamsterkombat-minigame-solver)** is licensed under [MIT](https://github.com/zdky/hamsterkombat-minigame-solver/blob/main/LICENSE) © [zdky](https://t.me/Zhidky) 2024._<br>
> <sup align="right">For information, see <a href="https://tldrlegal.com/license/mit-license">TLDR Legal > MIT</a></sup>
