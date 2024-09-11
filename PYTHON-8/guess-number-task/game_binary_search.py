import numpy as np

def binary_search(target):
    """Performs binary search to guess the target number.
    
    Args: 
        target (int): The number to guess.
        
    Returns: 
        int: The number of attempts taken to guess the target. 
    """

    low, high = 1, 100  # Define the search range from 1 to 100
    attempts = 0  # Initialize the number of attempts
    while low <= high:
        attempts += 1
        mid = (low + high) // 2  # Calculate the midpoint

        # If the middle element is the target, return the number of attempts
        if mid == target:
            return attempts
        # If the middle element is less than the target, search the right half
        elif mid < target:
            low = mid + 1
        # If the middle element is greater than the target, search the left half
        else:
            high = mid - 1

    return attempts  # Return the number of attempts

def score_game(binary_search_func):
    """Evaluates the performance of the binary search algorithm. 
    
    Args: 
        binary_search_func (function): The binary search function. 
    
    Returns: None 
    """
    
    count_list = []  # List to track the number of attempts for each trial
    np.random.seed(51)  # Set seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000))  # Generate 1000 random numbers

    # Perform binary search for each number in the array
    for number in random_array:
        count_list.append(binary_search_func(number))

    # Print statistics of the search performance
    print(f'Average number of attempts: {int(np.mean(count_list))}')
    print(f'Maximum number of attempts: {max(count_list)}')
    print(f'Minimum number of attempts: {min(count_list)}')

if __name__ == "__main__":
    score_game(binary_search)