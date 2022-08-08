from typing import List

def multyplying_arrays(array_1: List[int], array_2: List[int]) -> List[int]:
    '''Функция принимает два списка(массива), элементы которых являются коэффициентами полиномов.
     Функция возвращает новый список, элементы которого являются результатом перемножения полиномов,
     коэффициенты которых были приняты в эту функцию.'''
    sum_indexes = []

    for ratio_1, value_1 in enumerate(array_1):
        for ratio_2, value_2 in enumerate(array_2):
            new_ratio = ratio_1 + ratio_2
            if new_ratio < len(sum_indexes):
                sum_indexes[new_ratio] += value_1 * value_2
            else:
                sum_indexes.append(value_1 * value_2)
    return sum_indexes

def main():
    '''проверяем работу функции на примере нескольких полиномов.'''
    array_1 = [-1, 1]
    array_2 = [2, 1]
    array_3 = [-2, 2, -2, 2]
    array_4 = [-3, 3, -3]
    array_5 = [1, 2, 3, 4, 5]
    # тест 1
    print('Тест 1')
    print(multyplying_arrays(array_1, array_2))
    # тест 2
    print('\nТест 2')
    print(multyplying_arrays(array_3, array_4))
    # тест 3
    print('\nТест 3')
    print(multyplying_arrays(array_1, array_5))


if __name__ == "__main__":
    main()
