# Write a function, persistence, that takes in a positive parameter num and returns
# its multiplicative persistence, which is the number of times you must multiply the
# digits in num until you reach a single digit.
# For example (Input --> Output):
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)

# from functools import reduce
# from operator import mul
#
# def persistence(n):
#     return 0 if n < 10 else persistence(reduce(mul, [int(i) for i in str(n)], 1)) + 1
#
#
# print(persistence(999))
# ----------------------------------------------------------------------------------------------------------------------
# Automatons, or Finite State Machines (FSM), are extremely useful to programmers when it comes to software design.
# You will be given a simplistic version of an FSM to code for a basic TCP session.
# The outcome of this exercise will be to return the correct state of the TCP FSM based on the array of events given.
# The input array of events will consist of one or more of the following strings:
#  APP_PASSIVE_OPEN, APP_ACTIVE_OPEN, APP_SEND, APP_CLOSE, APP_TIMEOUT, RCV_SYN, RCV_ACK, RCV_SYN_ACK, RCV_FIN, RCV_FIN_ACK
# The states are as follows and should be returned in all capital letters as shown:
# CLOSED, LISTEN, SYN_SENT, SYN_RCVD, ESTABLISHED, CLOSE_WAIT, LAST_ACK, FIN_WAIT_1, FIN_WAIT_2, CLOSING, TIME_WAIT
# The input will be an array of events. The initial state is CLOSED. Your job is to traverse the FSM
# as determined by the events, and return the proper final state as a string, all caps, as shown above.

# If an event is not applicable to the current state, your code will return "ERROR".

# Action of each event upon each state:
# (the format is INITIAL_STATE: EVENT -> NEW_STATE)
# CLOSED: APP_PASSIVE_OPEN -> LISTEN
# CLOSED: APP_ACTIVE_OPEN  -> SYN_SENT
# LISTEN: RCV_SYN          -> SYN_RCVD
# LISTEN: APP_SEND         -> SYN_SENT
# LISTEN: APP_CLOSE        -> CLOSED
# SYN_RCVD: APP_CLOSE      -> FIN_WAIT_1
# SYN_RCVD: RCV_ACK        -> ESTABLISHED
# SYN_SENT: RCV_SYN        -> SYN_RCVD
# SYN_SENT: RCV_SYN_ACK    -> ESTABLISHED
# SYN_SENT: APP_CLOSE      -> CLOSED
# ESTABLISHED: APP_CLOSE   -> FIN_WAIT_1
# ESTABLISHED: RCV_FIN     -> CLOSE_WAIT
# FIN_WAIT_1: RCV_FIN      -> CLOSING
# FIN_WAIT_1: RCV_FIN_ACK  -> TIME_WAIT
# FIN_WAIT_1: RCV_ACK      -> FIN_WAIT_2
# CLOSING: RCV_ACK         -> TIME_WAIT
# FIN_WAIT_2: RCV_FIN      -> TIME_WAIT
# TIME_WAIT: APP_TIMEOUT   -> CLOSED
# CLOSE_WAIT: APP_CLOSE    -> LAST_ACK
# LAST_ACK: RCV_ACK        -> CLOSED

# Examples
# ["APP_PASSIVE_OPEN", "APP_SEND", "RCV_SYN_ACK"] =>  "ESTABLISHED"
# ["APP_ACTIVE_OPEN"] =>  "SYN_SENT"
# ["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "APP_CLOSE", "RCV_FIN_ACK", "RCV_ACK"] =>  "ERROR"


# initial_dict = {
#     "CLOSED": {
#         "APP_PASSIVE_OPEN": "LISTEN",
#         "APP_ACTIVE_OPEN": "SYN_SENT",
#     },
#     "LISTEN": {
#         "RCV_SYN": "SYN_RCVD",
#         "APP_SEND": "SYN_SENT",
#         "APP_CLOSE": "CLOSED",
#     },
#     "SYN_RCVD": {
#         "APP_CLOSE": "FIN_WAIT_1",
#         "RCV_ACK": "ESTABLISHED",
#     },
#     "SYN_SENT": {
#         "RCV_SYN": "SYN_RCVD",
#         "RCV_SYN_ACK": "ESTABLISHED",
#         "APP_CLOSE": "CLOSED",
#     },
#     "ESTABLISHED": {
#         "APP_CLOSE": "FIN_WAIT_1",
#         "RCV_FIN": "CLOSE_WAIT",
#     },
#     "FIN_WAIT_1": {
#         "RCV_FIN": "CLOSING",
#         "RCV_FIN_ACK": "TIME_WAIT",
#         "RCV_ACK": "FIN_WAIT_2",
#     },
#     "CLOSING": {
#         "RCV_ACK": "TIME_WAIT",
#     },
#     "FIN_WAIT_2": {
#         "RCV_FIN": "TIME_WAIT",
#     },
#     "TIME_WAIT": {
#         "APP_TIMEOUT": "CLOSED",
#     },
#     "CLOSE_WAIT": {
#         "APP_CLOSE": "LAST_ACK",
#     },
#     "LAST_ACK": {
#         "RCV_ACK": "CLOSED",
#     }
# }
#
# def traverse_TCP_states(events):
#     state = "CLOSED"
#     try:
#         for i in events:
#             state = initial_dict[state][i]
#         return state
#     except KeyError:
#         return "ERROR"
#
# print(traverse_TCP_states(["RCV_SYN","RCV_ACK","APP_CLOSE"]))
# ---------------------------------------------------------
# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"
#
# def to_camel_case(text):
#     lst = text.replace("_", " ").replace("-", " ").split()
#     return lst[0] + "".join([i.capitalize() for i in lst[1:]])
#
# print(to_camel_case("the_stealth_warrior"))
# --------------------------------------------------------------------------------------------------
# As a part of this Kata, you need to create a function that when provided with a triplet,
# returns the index of the numerical element that lies between the other two elements.
# The input to the function will be an array of three distinct numbers (Haskell: a tuple).
# For example:
# gimme([2, 3, 1]) => 0
# 2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.
# Another example (just to make sure it is clear):
# gimme([5, 10, 14]) => 1
# 10 is the number that fits between 5 and 14 and the index of 10 in the input array is 1.

# def gimme(input_array):
#     return input_array.index(sorted(input_array)[1])
#
# print(gimme([2, 3, 1]))
# ----------------------------------------------------------
# Your task is to write a function which returns the sum of a sequence of integers.
# The sequence is defined by 3 non-negative values: begin, end, step.
# If begin value is greater than the end, your function should return 0.
# If end is not the result of an integer number of steps, then don't add it to the sum. See the 4th example below.
#
# Examples
# 2,2,2 --> 2
# 2,6,2 --> 12 (2 + 4 + 6)
# 1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
# 1,5,3  --> 5 (1 + 4)

# def sequence_sum(begin_number, end_number, step):
#     if begin_number > end_number:
#         return 0
#
#     lst = [i for i in range(begin_number, end_number + 1)]
#
#     summ = 0
#     for i in lst[0::step]:
#         summ += i
#
#     return summ
#
# print(sequence_sum(2, 2, 2)) #12
#------------------------------------------------------------------------
# Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?
#
# Examples:
# input:    output:
# 0    ->   0
# 2    ->   5
# 3    ->   5
# 12   ->   15
# 21   ->   25
# 30   ->   30
# -2   ->   0
# -5   ->   -5
# etc.
# Input may be any positive or negative integer (including 0).
# You can assume that all inputs are valid integers.

# def round_to_next5(n):
#     if -4 <= n <= 0:
#         return 0
#     elif 0 < n <= 5:
#         return 5
#     elif n % 5 == 0:
#         return n
#     else:
#         return (n // 5 + 1) * 5
#
# print(round_to_next5(12))

#---------------------------------------------------------------------
# Finish the solution so that it sorts the passed in array of numbers. If the function
# passes in an empty array or null/nil value then it should return an empty array.
#
# For example:
# solution([1,2,3,10,5]) # should return [1,2,3,5,10]
# solution(None) # should return []

# def solution(nums):
#     return [] if not nums else sorted(nums)
#
# print(solution(None))

#--------------------------------------------------------------------------
# Complete the function/method so that it returns the url with anything after the anchor (#) removed.
# Examples
#
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"

# def remove_url_anchor(url):
#     return url.partition("#")[0]
#
# print(remove_url_anchor("www.codewars.com/katas/"))
# -----------------------------------------------------------------------------------
# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
# Note: anagrams are case insensitive
# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
# Examples
#     "foefet" is an anagram of "toffee"
#     "Buckethead" is an anagram of "DeathCubeK"


# def is_anagram(test, original):
#     return sorted(list(test.lower())) == sorted(list(original.lower()))
#
# print(is_anagram("apple", "pale"))
# -------------------------------------------------------------------

# Write a function that takes a single non-empty string of only lowercase and uppercase
# ascii letters (word) as its argument, and returns an ordered list containing
# the indices of all capital (uppercase) letters in the string.
# Example (Input --> Output)
#
# "CodEWaRs" --> [0,3,4,6]

# def capitals(word):
#     return [i for (i, c) in enumerate(word) if c.isupper()]
#
# print(capitals('PSOBpmOcx')) # [0, 1, 2, 3, 6]

# -------------------------------------------------------------------------------------------

# You will be given an array and a limit value. You must check that all values in the array
# are below or equal to the limit value. If they are, return true. Else, return false.#
# You can assume all values in the array are numbers.

# def small_enough(array, limit):
#     return len(array) == len([i for i in array if i <= limit])
#
# print(small_enough([78, 117, 110, 99, 104, 117, 107, 115], 100))

# ------------------------------------------------------------------------------------------------
# The two oldest ages function/method needs to be completed. It should take an array of numbers as
# its argument and return the two highest numbers within the array. The returned value should be
# an array in the format [second oldest age,  oldest age].
#
# The order of the numbers passed in could be any order. The array will always include at least
# 2 items. If there are two or more oldest age, then return both of them in array format.

# def two_oldest_ages(ages):
#     return sorted(ages)[-2::]
#
# print(two_oldest_ages([1, 5, 87, 45, 8, 8])) # [45, 87]
# --------------------------------------------------------------------------------

# Create a function that returns the name of the winner in a fight between two fighters.
# Each fighter takes turns attacking the other and whoever kills the other first is victorious.
# Death is defined as having health <= 0.
# Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.
# Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0.
# You can mutate the Fighter objects.
# Your function also receives a third argument, a string, with the name of the fighter that attacks first.

# class Fighter(object):
#     def __init__(self, name, health, damage_per_attack):
#         self.name = name
#         self.health = health
#         self.damage_per_attack = damage_per_attack
#
#     def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
#
#     __repr__ = __str__
#
#
# def declare_winner(fighter1, fighter2, first_attacker):#
#     if first_attacker == fighter1.name:
#         while fighter1.health > 0 or fighter2.health > 0:
#             fighter2.health -= fighter1.damage_per_attack
#             if fighter2.health <= 0:
#                 return fighter1.name
#             fighter1.health -= fighter2.damage_per_attack
#             if fighter1.health <= 0:
#                 return fighter2.name
#
#     if first_attacker == fighter2.name:
#         while fighter1.health > 0 or fighter2.health > 0:
#             fighter1.health -= fighter2.damage_per_attack
#             if fighter1.health <= 0:
#                 return fighter2.name
#             fighter2.health -= fighter1.damage_per_attack
#             if fighter2.health <= 0:
#                 return fighter1.name
#
#
# print(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"))

# ----------------------------------------------------------------------------------------------

# Given a string str, reverse it and omit all non-alphabetic characters.
# Example
# For str = "krishan", the output should be "nahsirk".
# For str = "ultr53o?n", the output should be "nortlu".
#
# def reverse_letter(st):
#     return "".join([i for i in list(st) if i.isalpha()])[::-1]
#
# print(reverse_letter("ultr53o?n"))  #"nortlu"
#---------------------------------------------------------------------------------------------------------------

# The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"].
# The second one contains a student's submitted answers.#
# The two arrays are not empty and are the same length. Return the score for this array of answers,
# giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer,
# represented as an empty string (in C the space character is used).
# If the score < 0, return 0.
#
#     Correct answer    |     Student's answer    |   Result
# --------------------- | ----------------------- | -----------
# ["a", "a", "b", "b"]      ["a", "c", "b", "d"]  →     6
# ["a", "a", "c", "b"]      ["a", "a", "b", ""]   →     7
# ["a", "a", "b", "c"]      ["a", "a", "b", "c"]  →     16
# ["b", "c", "b", "a"]      ["", "a", "a", "c"]   →     0

# def check_exam(arr1, arr2):
#     res = 0
#
#     for i, j in enumerate(arr1):
#         if arr1[i] == arr2[i]:
#             res += 4
#         elif arr1[i] == "" or arr2[i] == "":
#             res += 0
#         else:
#             res -= 1
#
#     return res if res > 0 else 0
#
#
# print(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""])) #7
# -------------------------------------------------------------------------------------------------
#
# Write a function named sumDigits which takes a number as input and
# returns the sum of the absolute value of each of the number's decimal digits.

# def sum_digits(number):
#     return sum([int(i) for i in str(abs(number))])
#
#
# print(sum_digits(-32))# 5








































