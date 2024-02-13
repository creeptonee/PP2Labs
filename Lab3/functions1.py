#ex1 

def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams_amount = float(input())
result = grams_to_ounces(grams_amount)
print(result)


#ex2

def fahrenheit_to_celsius(temp):
    celsius = (5/9) * (temp - 32)
    return celsius

temperature = float(input())
result = fahrenheit_to_celsius(temperature)
print(result)

#ex3

def solve(numheads, numlegs):
    for chicken in range(0, numheads + 1):
        rabbit = numheads - chicken
        total_legs = chicken * 2 + rabbit * 4
        if total_legs == numlegs:
            return chicken, rabbit
    return "Wrong"

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print(result)

#ex4

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers

numbers = [int(x) for x in input().split()]
prime_numbers = filter_prime(numbers)
print(prime_numbers)

#ex5
from itertools import permutations

def print_permutations(input_string):
    perm = permutations(input_string)
    for p in perm:
        print(''.join(p))

user_input = input()
print_permutations(user_input)

#ex6
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
user_input = input()
reversed_sentence = reverse_words(user_input)
print(reversed_sentence)


#ex7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

#ex8
def spy_game(nums):
    zero_count = 0
    for num in nums:
        if num == 0:
            zero_count += 1
        elif num == 7:
            if zero_count >= 2:
                return True
            zero_count = 0
    return False

#ex9

def sphere_volume(radius):
    volume = (4/3) * 3.14 * radius**3
    return volume

radius = float(input())
volume = sphere_volume(radius)
print(volume)

#ex10
def unique_elements(input_list):
    unique = []
    
    for item in input_list:
        if item not in unique:
            unique.append(item)
    
    return unique

#ex11
def palindrome(word)
    reversed_word = word[::-1]

    if reversed_word == word:
        return "Palindrome!"
    
input_word = input()
palindrome(input_word)


#ex12
def histogram(numbers):
    for num in numbers:
        print('*' * num)


#ex13
import random

def guess_the_number():

    number = random.randint(1, 20)
    print("Well, KBTU, I am thinking of a number between 1 and 20.")
    num_guesses = 0
    while True:
        print("Take a guess.")
        guess = int(input())

        num_guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print("Good job, KBTU! You guessed my number in {num_guesses} guesses!")
            break

guess_the_number()

#ex14

