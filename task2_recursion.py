def count_items(nums):
    """Count list items recursively without using len()."""
    if nums == []:
        return 0

    return 1 + count_items(nums[1:])


if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    print("Список:", numbers)
    print("Количество элементов:", count_items(numbers))
