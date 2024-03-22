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


