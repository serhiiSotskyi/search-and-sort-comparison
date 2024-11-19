# Generate Arrays
def generate_ordered_array(size):
    return [i for i in range(size)]

def generate_reverse_ordered_array(size):
    return [i for i in range(size, 0, -1)]

def generate_unsorted_array(size):
    import random
    return [random.randint(1, size) for _ in range(size)]

# Search Algorithm 1 (Add step counter)
def searching_algorithm_1(array, target):
    step_count = 0
    # Implement your logic here
    # Example: Linear Search
    for i in range(len(array)):
        step_count += 1
        if array[i] == target:
            break
    return step_count

# Search Algorithm 2 (Add step counter)
def searching_algorithm_2(array, target):
    step_count = 0
    # Implement your logic here
    # Example: Binary Search
    left, right = 0, len(array) - 1
    while left <= right:
        step_count += 1
        mid = (left + right) // 2
        if array[mid] == target:
            break
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return step_count

# Main Program for Search
def main_search():
    size = 100
    arrays = {
        "Ordered": generate_ordered_array(size),
        "Reverse Ordered": generate_reverse_ordered_array(size),
        "Unsorted": generate_unsorted_array(size),
    }

    target = size // 2  # Midpoint as target
    for array_type, array in arrays.items():
        print(f"\nTesting {array_type} Array:")
        steps_1 = searching_algorithm_1(array, target)
        print(f"Algorithm 1 Steps: {steps_1}")

        steps_2 = searching_algorithm_2(array, target)
        print(f"Algorithm 2 Steps: {steps_2}")

        print(f"Best Algorithm for {array_type}: {'Algorithm 1' if steps_1 < steps_2 else 'Algorithm 2'}")

if __name__ == "__main__":
    main_search()
