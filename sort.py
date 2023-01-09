def bubble(arr: list, i_num: int, j_num: int) -> tuple(list, int, int):
    """
    This function is a modified version of the bubble sorting algorithm.
    After one switch in the inputted array is made, the function returns
    the new array and where the algorithm stopped.

    PRECONDITION: i_num must be greater than or equal to 0
    PRECONDITION: j_num must be greater than or equal to 0
    """
    n = len(arr)
    for i in range(i_num, n-1):
        for j in range(j_num, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                return arr, i, j+1
        j_num = 0


def selection(arr: list, i_num: int) -> tuple(list, int, int):
    """
    This function is a modified version of the bubble sorting algorithm.
    After one switch in the inputted array is made, the function returns
    the new array and where the algorithm stopped.

    PRECONDITION: i_num must be greater than or equal to 0
    """
    for i in range(i_num, len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr, i+1, min_idx


def insertion(arr: list, i_num: int) -> tuple(list, int, int):
    """
    This function is a modified version of the bubble insertion algorithm.
    After one switch in the inputted array is made, the function returns
    the new array and where the algorithm stopped.

    PRECONDITION: i_num must be greater than or equal to 0
    """
    for i in range(i_num+1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            arr[j] = key
            return arr, 0, j
