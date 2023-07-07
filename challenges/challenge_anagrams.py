def merge_sort(string):
    # Caso base: se a string tem tamanho 1, ela já está ordenada
    if len(string) <= 1:
        return string

    # Divide a string em duas partes
    middle = len(string) // 2
    left = merge_sort(string[:middle])
    right = merge_sort(string[middle:])

    # Combina as duas metades ordenadas
    return merge(left, right)


def merge(left, right):
    result = []
    index_left = 0
    index_right = 0

    # Combina as duas metades em ordem crescente
    while index_left < len(left) and index_right < len(right):
        if left[index_left] < right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

    # Adiciona os elementos restantes
    result.extend(left[index_left:])
    result.extend(right[index_right:])

    return result


def is_anagram(first_string, second_string):
    first_string_order = ''.join(merge_sort(first_string.lower()))
    second_string_order = ''.join(merge_sort(second_string.lower()))

    if not first_string_order and not second_string_order:
        return first_string_order, second_string_order, False
    result = first_string_order == second_string_order
    return first_string_order, second_string_order, result


print(is_anagram('amor', 'roma'))
