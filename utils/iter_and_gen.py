"""
Source: https://pymbook.readthedocs.io/en/latest/igd.html
"""
# Iterator is an object that implement __iter__ and __next__
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
