# functions
def pythagoras(a, b):
    c = (a**2 + b**2)**0.5
    return c

# usages
x = 3
y = 4
c = pythagoras(x, y)
print(pythagoras(3, 4))
print(pythagoras(5, 12))
print(pythagoras(8, 15))

def hello(name):
    if name == "Jack":
        print("Oh, f*ck of Jack!")
    else:
        print("Hello, " + name + "!")

# usage
hello("John")
hello("Jane")
hello("Jack")

def sum_of_list(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum

# usage
print(sum_of_list([1, 2, 3, 4, 5]))

def can_vote(age):
    if age >= 18:
        return True
    else:
        return False

# usage
print(can_vote(17))

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
# usage
print(is_even(5))

def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in sentence.lower():
            return False
    return True

# usage
print(is_pangram("The quick brown fox jumps over the lazy dog")) # True
print(is_pangram("The quick brown fox jumps over the lazy cat")) # False
