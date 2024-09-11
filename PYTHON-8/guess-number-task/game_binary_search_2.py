import numpy as np

def binary_search(arr, key_value):
    """Performs binary search on a sorted array.

    Args:
        arr (list): A sorted array of numbers.
        key_value (int): The value to search for.

    Returns:
        int: The index of the found value, or -1 if not found.
    """

    low = 0  # Marks the left (first element) boundary of the subarray
    high = len(arr) - 1  # Marks the right (last element) boundary of the subarray

    # Continue searching as long as there are elements to examine
    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index

        # If the middle element is the target, return its index
        if arr[mid] == key_value:
            return mid

        # If the middle element is less than the target, search the right half
        elif arr[mid] < key_value:
            low = mid + 1  # Update the left boundary to the middle element + 1

        # If the middle element is greater than the target, search the left half
        else:
            high = mid - 1  # Update the right boundary to the middle element - 1

    # If the target was not found, return -1
    return -1

def score_game(binary_search_func):
    """Evaluates the performance of the binary search algorithm.

    Args:
        binary_search_func (function): The binary search function.

    Returns:
        int: The average number of attempts.
    """

    count_list = []
    np.random.seed(23)  # Sets the random seed for reproducibility
    random_array = np.arange(1, 101)  # Create a sorted array of numbers from 1 to 100
    random_array = np.random.permutation(random_array)  # Shuffle the elements randomly

    # Iterate over each element in the shuffled array
    for element in random_array:
        # Perform binary search and record the number of attempts
        count_list.append(binary_search_func(random_array, element) + 1)

    # Calculate the average number of attempts
    score = int(np.mean(count_list))
    print(f"Your algorithm guesses the number in an average of: {score} attempts")
    return score

if __name__ == "__main__":
    score_game(binary_search)