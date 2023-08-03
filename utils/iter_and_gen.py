"""
Source: https://pymbook.readthedocs.io/en/latest/igd.html
"""
# Iterator is an object that implement __iter__ and __next__
from textwrap import wrap
from unittest import result


class Counter(object):
    def __init__(self, low, high) -> None:
        self.current = low
        self.high = high

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Utility driver
c = Counter(5,10)
for i in c:
    print(i, end=' ')


# Generator is an object that deal with yield and doesn't load the data
# into memory at once
def my_generator():
    print('Inside my generator')
    yield 'a'
    yield 'b'
    yield 'c'

# utility
my_generator()
for char in my_generator():
    print(char)

# function based generator of counter
def counter_generator(low, high):
    while low <= high:
        yield low
        low += 1

for i in counter_generator(5, 10):
    print(i, end=' ')


# object based generator of counter
class Counter:
    def __init__(self, low: int, high: int) -> None:
        self.low = low
        self.high = high

    def __iter__(self):
        counter = self.low
        while self.high>= counter:
            yield counter
            counter += 1

# generator expression
g = (x*x for x in range(1, 10)) # -> returns generator
next_element = next(g) # -> gives next element
g = sum(g)

# similar
g = sum([x*x for x in range(10)]) # takes much space


# Closures - they are nothing but function that are returned by another function

def add_number(num: int):
    def adder(number):
        'adder is a closure'
        return num + number
    return adder

a_10 = add_number(10)
a_10(21)
# 31
a_10(11)
# 42

# Decorators - it is a way to dynamically add some new behaviour to some object

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Before call')
        result= func(*args, **kwargs)
        print('After call')
        return result
    return wrapper

@my_decorator
def add(a,b):
    return a+b
