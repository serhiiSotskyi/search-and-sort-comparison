# Generate Arrays
def generate_ordered_array(size):
    return [i for i in range(size)]

def generate_reverse_ordered_array(size):
    return [i for i in range(size, 0, -1)]

def generate_unsorted_array(size):
    import random
    return [random.randint(1, size) for _ in range(size)]

# Sorting Algorithm 1 (Add swap counter)
def sorting_algorithm_1(array):
    swap_count = 0
    # Implement your logic here
    # Example: Bubble Sort
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap_count += 1
    return swap_count

# Sorting Algorithm 2 (Add swap counter)
def sorting_algorithm_2(array):
    swap_count = 0
    # Implement your logic here
    # Example: Selection Sort
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]
            swap_count += 1
    return swap_count

# Main Program for Sort
def main_sort():
    size = 100
    arrays = {
        "Ordered": generate_ordered_array(size),
        "Reverse Ordered": generate_reverse_ordered_array(size),
        "Unsorted": generate_unsorted_array(size),
    }

    for array_type, array in arrays.items():
        print(f"\nTesting {array_type} Array:")
        swaps_1 = sorting_algorithm_1(array.copy())
        print(f"Algorithm 1 Swaps: {swaps_1}")

        swaps_2 = sorting_algorithm_2(array.copy())
        print(f"Algorithm 2 Swaps: {swaps_2}")

        print(f"Best Algorithm for {array_type}: {'Algorithm 1' if swaps_1 < swaps_2 else 'Algorithm 2'}")

if __name__ == "__main__":
    main_sort()
