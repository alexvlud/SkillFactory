

def sort(array):            #функция сортировки вставками
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx-1] > x:
            array[idx] = array[idx-1]
            idx -= 1
        array[idx] = x
    return array


def binary_search_mod(array, element, left, right):     #функция поиска
    middle = (right + left) // 2  # находим середину
    if left > right:  # если левая граница превысила правую,
        return middle  # значит элемент отсутствует и возвращаем индекс элемента
                        # предшествующего введенному пользоватеоем

    if array[middle] == element:  # если элемент в середине,
        return middle-1  # возвращаем индекс элемента, который меньше введенного пользователем числа
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search_mod(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search_mod(array, element, middle + 1, right)


input_array = list(map(float, input("Введите последовательность чисел через пробел:").split(" ")))
element = float(input("Введите число: "))
sort(input_array)

print(input_array)  #вывод отсортированного массива

if element < input_array[0] or element > input_array[len(input_array)-1]:
    print(f"Введенное число {element} находится за пределами массива")
elif element == input_array[0]:
    print(f"Введенное число {element} - начальное значение массива")
else:
    print(f"Номер позиции искомого элемента начиная с 0: {binary_search_mod(input_array, element, 0, len(input_array)-1)}")