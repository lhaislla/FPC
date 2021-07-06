def merge_sort(data):
    """
	Função que determina se a lista está
	dividida em partes individuais
    """
    # Definimos o base case
    if len(data) < 2:
        return data

    middle = len(data)//2

    # Dividimos a lista em duas partes
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])

    # Unimos as duas partes ordenadas
    merged = merge(left, right)
    return merged

def merge(left, right):
    """
	Quando os lados esquerdo/direito estiverem vazios,
	Significa que é um item indiviual e está ordenado!
    """
    # Garantimos que os lados esquerdo/direito não estão vazios,
    # Indicando que é um item individual e já está ordenado
    if not len(left):
        return left

    if not len(right):
        return right

    result = []
    leftIndex = 0
    rightIndex = 0
    totalLen = len(left) + len(right)

    while (len(result) < totalLen):
        # Executamos as comparações necessários e unimos as duas partes
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1
        if leftIndex == len(left) or rightIndex == len(right):
            result.extend(left[leftIndex:] or right[rightIndex:])
            break
    return result

array = [6,3,13,9,7,1]
sorted_array = merge_sort(array)
print(sorted_array)