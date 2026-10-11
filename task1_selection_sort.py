def selection_sort(numbers, descending=False):
    """Sort a list using selection sort.

    descending=False: ascending order
    descending=True: descending order
    """
    numbers = numbers.copy()

    for i in range(len(numbers)):
        selected_index = i

        for j in range(i + 1, len(numbers)):
            if descending:
                if numbers[j] > numbers[selected_index]:
                    selected_index = j
            else:
                if numbers[j] < numbers[selected_index]:
                    selected_index = j

        numbers[i], numbers[selected_index] = numbers[selected_index], numbers[i]

    return numbers


if __name__ == "__main__":
    grades = [4, 2, 5, 3, 5, 4, 3]

    print("Исходный список:", grades)
    print("По возрастанию:", selection_sort(grades))
    print("По убыванию:", selection_sort(grades, descending=True))
