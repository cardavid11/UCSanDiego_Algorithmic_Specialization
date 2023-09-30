# For interview preparation, focusing on the following approaches would be most beneficial as they are commonly discussed and exhibit understanding of various algorithmic paradigms:
# Recursive Approach:
# Understanding the basic recursive approach is crucial as it forms the foundation. However, it's important to recognize its inefficiency and be able to optimize it.
# Dynamic Programming:
# Both Memoization and Tabulation are vital to grasp as they demonstrate your ability to optimize recursive algorithms and reduce time complexity. Dynamic Programming is a frequent topic in coding interviews and mastering it will be highly beneficial.
# Matrix Exponentiation (Optional):
# While it's less commonly asked, knowing matrix exponentiation can impress interviewers as it showcases a deeper understanding of algorithms. It's particularly useful when discussing problems related to the Fibonacci sequence or other recurrence relations.

# 1. Recursive Approach: O(2^n)
# Time Complexity: O(2^n) - due to the exponential growth of function calls.
# Space Complexity: O(n) - due to the maximum depth of the recursion tree (call stack).
# Discussion: This approach follows the mathematical definition directly but is highly inefficient due to repeated calculations.
# def fibonacci_number(n):
#     if n <= 1:
#         return n
    
#     return fibonacci_number(n - 1) + fibonacci_number(n - 2)

# Dynamic Programming (Memoization)
# Time Complexity: O(n) - as each Fibonacci number is computed once and stored in the memo table.
# Space Complexity: O(n) - due to the memo table and the maximum depth of the recursion tree (call stack).
# Discussion: Memoization optimizes the recursive approach by storing previously computed values to avoid redundant calculations.
memo = {}
def fibonacci_memoization(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
    return memo[n]

# Dynamic Programming (Tabulation)
# Time Complexity: O(n) - as the table is filled in a single pass.
# Discussion: Tabulation is a bottom-up approach that builds the table iteratively, often easier to understand and slightly more space-efficient compared to memoization.
# Space Complexity: O(n) - due to the table used to store the Fibonacci numbers.
# def fibonacci_tabulation(n):
#     fib_table = [0, 1] + [0] * (n - 1)
#     for i in range(2, n + 1):
#         fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
#     return fib_table[n]

# Matrix Exponentiation
# Time Complexity: O(log n) - due to the matrix exponentiation process.
# Space Complexity: O(1) - constant space regardless of the input size.
# Discussion: Matrix exponentiation is a fast method to compute the nth Fibonacci number but requires understanding of matrix operations.
# import numpy as np
# def fibonacci_matrix(n):
#     F = np.array([[1, 1], [1, 0]], dtype=object)
#     return np.linalg.matrix_power(F, n)[0, 1]

# Binet's Formula
# Time Complexity: O(1) - as it's a direct formula to compute the nth Fibonacci number.
# Space Complexity: O(1) - constant space regardless of the input size.
# Discussion: Binet's formula is theoretically the fastest but loses precision for large values of n due to floating-point arithmetic errors.
# import math
# def fibonacci_binet(n):
#     phi = (1 + math.sqrt(5)) / 2
#     psi = (1 - math.sqrt(5)) / 2
#     return int((math.pow(phi, n) - math.pow(psi, n)) / math.sqrt(5))

if __name__ == '__main__':
    input_n = int(input())
    # print(fibonacci_number(input_n))
    print(fibonacci_memoization(input_n))

###About dinamic programming###

# Dynamic Programming (DP) is a method for solving problems by breaking them down into smaller subproblems. The key principle behind DP is the notion of "overlapping subproblems," which means that the same subproblems are re-computed many times. By solving each subproblem only once and storing the results in a table to avoid redundant work, DP significantly reduces the computational time.

# Here are the fundamental components and steps involved in Dynamic Programming:

# Overlapping Subproblems:

# The problem can be broken down into subproblems which are reused several times throughout the computation.
# Optimal Substructure:

# The optimal solution to the problem can be constructed from the optimal solutions of its subproblems.
# Memoization:

# Memoization is a technique where you store the solutions to subproblems to avoid redundant work. This can be done using an array or a hash table where the results of subproblems are stored.
# Tabulation:

# Tabulation is the bottom-up approach to dynamic programming. Here, you solve the subproblems first, typically by filling up an n-dimensional table. Based on the results of the smaller subproblems, you solve bigger subproblems.
# Steps to Solve DP Problems:
# Identify the Subproblems:

# Break down the main problem into simpler, smaller subproblems.
# Write Down the Recurrence Relation:

# Determine how the solution to the main problem can be expressed in terms of solutions for smaller subproblems.
# Solve the Base Cases:

# Solve the smallest subproblems which are straightforward to solve and form the base for solving larger subproblems.
# Solve the Subproblems and Store Their Solutions:

# Either through Memoization (top-down approach) or Tabulation (bottom-up approach), solve the subproblems once and store their solutions for reuse.
# Use the Stored Solutions to Solve Original Problem:

# Utilize the solutions of subproblems to solve the original problem efficiently.