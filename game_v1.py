import numpy as np


def random_predict(number: int = 1) -> int:
    '''Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defauls to 1.

    Returns:
        int: Число попыток.
    '''

    minimum, maximum = 1, 100
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(minimum, maximum + 1) # предполагаем число исходя из усредненных границ
        if number > predict_number:
            minimum = predict_number + 1
        elif number < predict_number:
            maximum = predict_number - 1
        else:
            break
            
    return count


def score_game(random_predict) -> int:
    '''За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадыввания

    Returns:
        int: среднее количество попыток
    
    '''

    count_lst = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_arr = np.random.randint(1, 101, size = (1000)) # загадали список чисел

    for number in random_arr:
        count_lst.append(random_predict(number))

    score = int(np.mean(count_lst)) # находим среднее количество попыток

    print(f'Алгоритм угадывает число в среднем за {score} попыток')
    return score

#RUN
if __name__ == '__main__':
    score_game(random_predict)


