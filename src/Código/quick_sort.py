def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[len(array) / 2]
        esquerda = [i for i in array if i <= pivo]
        direita = [i for i in array if i > pivo]
        return quicksort(esquerda) + pivo + quicksort(direita)