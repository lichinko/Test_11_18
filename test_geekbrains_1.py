from typing import Union, List, Dict, Tuple, Set
'''По скольку в python как таковых нет массивов(если не устанавливать дополнительных библиотек), я решил реализовать 
задание по отношению к спискам, кортежам, множествам и словарям.'''

def copy_array(array: Union[List, Dict, Tuple, Set]) -> Union[List, Dict, Tuple, Set]:
    '''Функция принимает список, кортеж, словарь или множество и рекурсивно обходит все их элементы создавая копии,
    при этом так же обрабатывая вложенные списки, кортежи, словари и множества.'''

    if isinstance(array, dict):
        new_dict = dict()
        for key, value in array.items():
            if type(value) in (list, dict, tuple, set):
                new_dict[key] = copy_array(value)
            else:
                new_dict[key] = value
        return new_dict

    new_array = []

    for elem in array:
        if type(elem) in (list, dict, tuple, set):
            new_array.append(copy_array(elem))
        else:
            new_array.append(elem)
    if isinstance(array, tuple):
        return tuple(new_array)
    elif isinstance(array, set):
        return set(new_array)
    return new_array


def main():
    '''тест содержащий в себе словарь с вложенными данными, включая другой словарь, множество, список и кортеж.'''
    my_dict = {1: 3, 3: 4, 5: {1: 4}, 7: (3, 4, 5), 9: ['sdf', 34, 'df'], 2: {3, 4, 6, 2, 67}}
    print(copy_array(my_dict))


if __name__ == "__main__":
    main()
