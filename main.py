from random import *

# алгоритм игры
def guess_the_number(x, y):
    phrase_too_much = ['Ох, слишком много! Попробуй еще раз', 'Многовато будет!', 'Ого-го, это слишком много!',
                        'Много!', 'Бери ниже', 'Многовато!', 'Нужно меньшее число!']
    phrase_too_little = ['Ох, слишком мало! Попробуй еще раз', 'Маловато будет!', 'Эх, это слишком мало!',
                        'Мало!', 'Бери выше', 'Маловато!', 'Нужно большее число!']
    phrase_almost = ['Почти угадал!', 'Горячо, но не очень', 'Уже рядом', 'Ты близок', 'Ты уже рядом', 'Ну же, почти',
                      'Горячо!']
    phrases_guessed  = ['Поздравляю! Ты угадал моё число :)', 'Молодец! Ты угадал :)', 'Ура, ты угадал! :)']
    phrases_too_soon = ['Ого, так быстро!', 'Да ты волшебник! Ты угадал моё число', 'Скажи честно, ты подглядывал?',
                        'У тебя отличная интуиция!', 'Даже я бы не смог отгадать так быстро!']
    if x >  y:
        x, y = y, x
        hidden_num = randint(x, y)
        print(f'Я загадал число от {x} до {y}, попробуй угадать!')
    else:
        hidden_num = randint(x, y)
        print(f'Я загадал число от {x} до {y}, попробуй угадать!')
    count = 0
    while True:
        selected_num = int(input())
        count += 1
        if selected_num == hidden_num:
            if count == 1:
                print('Скажи честно, ты подглядывал?')
                if input('Хочешь сыграть еще раз? Введи "да" или "нет" ').lower() in ['да', 'lf']:
                    start()
                else:
                    print('Приходи ещё когда захочешь!')
                    break
            elif 1 <= count <= 5:
                print(choice(phrases_too_soon))
                if input('Хочешь сыграть еще раз? Введи "да" или "нет" ').lower() in ['да', 'lf']:
                    start()
                else:
                    print('Приходи ещё когда захочешь!')
                    break
            else:
                print(choice(phrases_guessed))
                if input('Хочешь сыграть еще раз? Введи "да" или "нет" ').lower() in ['да', 'lf']:
                    start()
                else:
                    print('Приходи ещё когда захочешь!')
                    break
        elif selected_num > hidden_num:
            if (hidden_num - selected_num) < 5:
                print(choice(phrase_too_much), choice(phrase_almost))
            else:
                print(choice(phrase_too_much))
        elif selected_num < hidden_num:
            if (hidden_num - selected_num) < 5:
                print(choice(phrase_too_little), choice(phrase_almost))
            else:
                print(choice(phrase_too_little))

# правила игры
def game_rules():
    print('Отлично! Давай ознакомлю тебя с правилами игры.')
    print('Я загадаю число, а ты будешь его отгадывать.')
    print('Диапазон чисел ты выберешь сам.')
    print('К примеру, если ты укажешь диапазон чисел от 0 до 100, я не смогу загадать число "101" :)')
    print('Я попрошу тебя ввести границы диапазона. Границы не должны совпадать! Так играть мы не сможем.')
    input('А теперь напиши что-нибудь, чтобы я был уверен, что ты понял правила игры :)')

# проверка на ошибки
def  is_valid_x(x):
    if x.isdigit() is False:
        print('Ты ввел не число :(')
        print('Что ж, ладно, введи новые числа.')
        start()
    else:
        return True
def is_valid_xy(x, y):
    if x == y:
        print('Так играть не получится! Числа одинаковые, попробуй по новой!')
        start()
    if y.isdigit() is False:
        print('Я запутался :( Это не число')
        print('Давай заново :)')
        start()
    else:
        return True

# начало игры
def start():
    x = input('Введите первую границу  диапозона: ')
    is_valid_x(x)
    y = input('Введите вторую границу  диапозона: ')
    if is_valid_xy(x, y) is True:
        x, y = int(x), int(y)
        print('Супер, начинаем игру!')
        guess_the_number(x, y)

# приглашение в игру
if input('Приветствую тебя в программе Виктора! Не желаешь сыграть в игру? Введи "да" или "нет" ').lower() in ['да', 'lf']:
    game_rules()
    start()
else:
    if input('Это не займёт много времени и сил. Если всё таки надумал, введи "да" :)').lower() in ['да', 'lf']:
        game_rules()
        start()
    else:
        print('Приходи, когда появится желание сыграть :)')