# 1. Check if a string is a palindrome:

def is_palindrome(s):
    
    return s == s[::-1]

print(is_palindrome("radar"))  
print(is_palindrome("hello"))  


# 2. Find the factorial of a number recursively:

def factorial(n):
    
    if n == 0:
        return 1
   
    else:
        return n * factorial(n-1)


print(factorial(5))  


# 3. Generate the Fibonacci sequence up to a certain number of terms:

def fibonacci(n):
    
    fib_sequence = [0, 1]
   
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


print(fibonacci(10))  


# 4. Find the maximum and minimum numbers in a list:

def find_max_min(numbers):
   
    if not numbers:
        return None, None
    
    return max(numbers), min(numbers)

# Example usage:
number = [3, 1, 7, 4, 9, 2]
print(find_max_min(number))  


# 5. Reverse a list:

def reverse_list(lst):
   
    return lst[::-1]


original_list = [1, 2, 3, 4, 5]
print(reverse_list(original_list)) 


# 6. Check if a given number is prime:

def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        
        if n % i == 0:
            return False
   
    return True


print(is_prime(11)) 
print(is_prime(15)) 


# 7. Calculate the square root of a number using Newton's method:

def sqrt1(n):
   
    guess = n / 2
   
    while abs(guess**2 - n) > 1e-9:
     
        guess = (guess + n / guess) / 2
    return guess


print(sqrt1(9))

# 8. Remove duplicate elements from a list: 
def remove_dup(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

original_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_dup(original_list))  



# 9. Check if two strings are anagrams of each other:

def are_anagrams(s1, s2):
   
    return sorted(s1) == sorted(s2)


print(are_anagrams("listen", "silent"))  
print(are_anagrams("hello", "world"))   


# 10. Count the occurrences of each word in a string:

def count_word_occurrences(sentence):
  
    words = sentence.split()
   
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


input_sentence = "hello world hello"
print(count_word_occurrences(input_sentence))  


# 11. Find the largest and smallest elements in a list without using built-in functions:

def find_max_min(numbers):
    
    if not numbers:
        return None, None
    
    max_num = min_num = numbers[0]
   
    for num in numbers:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    return max_num, min_num


numbers_list = [3, 1, 7, 4, 9, 2]
print(find_max_min(numbers_list))  # Output: (9, 1)


# 12. Convert a decimal number to binary:

def decimal_to_binary(n):
   
    binary = ""
   
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

print(decimal_to_binary(10))  


# 13. Find the GCD (Greatest Common Divisor) of two numbers:

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(24, 36)) 

# 14. Calculate the factorial of a number iteratively:

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial_iterative(5)) 

# 15. Find the sum of digits of a positive integer:

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


print(sum_of_digits(12345))  


# 16. Merge two sorted lists into a single sorted list:

def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list


list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(merge_sorted_lists(list1, list2))  


# 17. Check if a given year is a leap year:

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


print(is_leap_year(2020))  
print(is_leap_year(2021))  


# 18. Generate a random password of a given length:

import random
import string

def random_password(length):
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char) for _ in range(length))
    return password

lent=int(input("enter the no of length"))
print(random_password(lent))  


# 19. Find the median of a list of numbers:

def find_median(nums):
    sorted_nums = sorted(nums)
    n = len(nums)
    if n % 2 == 0:
        return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    else:
        return sorted_nums[n//2]

nums = [1, 2, 3, 4, 5]
print(find_median(nums)) 



