# 1. Time Complexity:
#    - Naive Solution: The time complexity is O(n^2) due to the nested loops, which requires comparing 
#      and computing the product for all pairs of elements in the sequence.
#    - Optimized Solution: The time complexity is O(n) as it only requires two single passes through 
#      the sequence to find the two largest numbers.

# 2. Space Complexity:
#    - Both solutions have a constant space complexity, O(1), as they only use a fixed amount of 
#      additional memory for storing indices and the maximum product.

# 3. Scalability:
#    - The naive solution's quadratic time complexity makes it less scalable for large input sizes as 
#      the running time increases dramatically with each additional element.
#    - The optimized solution's linear time complexity makes it much more scalable, as the running time 
#      increases linearly with the size of the input.

# 4. Readability and Simplicity:
#    - The naive solution is straightforward and easy to understand at a glance.
#    - The optimized solution, while still readable, requires a better understanding of the logic to 
#      identify the two largest numbers without examining all pairs.

# 5. Optimization Technique:
#    - The optimized solution employs a greedy approach to find the two largest numbers in a single or 
#      two passes, thus avoiding the need to check every pair. This is a common optimization technique 
#      that significantly reduces the time complexity.

### Naive Solution ###
# def max_pairwise_product(numbers):
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product,
#                 numbers[first] * numbers[second])
            
#     return max_product

### Optimized Solution ###
def max_pairwise_product(numbers):
    # It's assumed that the list 'numbers' contains at least two elements.
    max_index = 0  # Initializing to the first index
    # Finding the index of the maximum element
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[max_index]:
            max_index = i

    # If the maximum element is at the 0th index, initialize second_max_index to 1; otherwise, initialize to 0
    second_max_index = 1 if max_index == 0 else 0
    # Finding the index of the second maximum element
    for i in range(1, len(numbers)):
        if i != max_index and numbers[i] > numbers[second_max_index]:
            second_max_index = i

    return numbers[max_index] * numbers[second_max_index]

### Alternative Solution ###
# def max_pairwise_product(n, sequence):
#     # Assuming n > 1 and the sequence has at least two elements
#     max_index = -1
#     for i in range(n):
#         if max_index == -1 or sequence[i] > sequence[max_index]:
#             max_index = i

#     second_max_index = -1
#     for i in range(n):
#         if (i != max_index) and (second_max_index == -1 or sequence[i] > sequence[second_max_index]):
#             second_max_index = i

#     return sequence[max_index] * sequence[second_max_index]

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
