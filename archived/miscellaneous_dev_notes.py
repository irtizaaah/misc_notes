# FUNCTIONAL CONCEPTS
# Recursion
# Structural Pattern Matching
# Immutability 
# Pure Functions
# Higher Order Functions
# Function Composition
# Lazy Evaluation

# OOP CONCEPTS
# Single Responsbility 
# O
# L
# I
# D

# DESIGN PATTERN
# Factory Method Pattern
# Singleton Pattern
# Builder Pattern
# Prototype Pattern
# Adapter Pattern
# Decorator Pattern
# Facade Pattern
# Strategy Pattern
# Observer Pattern
# State Pattern

# # VIRTUAL ENVIRONMENT
# *VENV should sit beside source code*
# initialize: python -m venv env
# activate: source env/bin/activate 
# deactivate: deactivate
# saving dependencies: pip freeze > requirements.txt
# installing dependencies from file: pip install -r requirements.txt

# Iterables
class MyList1():
    def __init__(self, user_list: list[tuple]):
        self.user_list: list = user_list
    
    def __iter__(self):
        return iter(self.user_list)
        
class MyList2():
    def __init__(self, tuple_list: list):
        self.tuple_list: list = tuple_list
        self.curr: int = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        end: int = len(self.tuple_list)-1

        if self.curr > end:
            raise StopIteration
        else:
            self.curr += 1
            return self.tuple_list[self.curr-1][1]

li = MyList1([1,2,3,4,5,6,7,8,9,10])
for i in li:
    print(i)

li = MyList2([("one",1),("two",2),("three",3),("four",4)])
for i in li:
    print(i)

# Generators
def my_range(start, end):
    curr = start
    while curr <= end:
        yield curr
        curr += 1

for i in my_range(1,3):
    print(i)

# Dataclasses
# Dunder Methods
# Context Managers & try/except
from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    except Exception as e:
        raise Exception(f"ERROR: {e}") from e
    finally:
        f.close()

with open_file('sample.txt', 'w') as f:
    f.write("hello world")


# Logging
import logging
logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w", 
                    format="%(asctime)s - %(levelname)s - %(message)s")
logging.debug("debug")
logging.info("info")

logger = logging.getLogger("logger")
file_handler = logging.FileHandler("log1.log")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

logger.debug("debug")
logger.info("info")

# Unit Testing
import unittest

def add(a,b):
    return a + b

class Test(unittest.TestCase):
    def test_happy_case(self):
        res = add(1,2)
        self.assertEqual(res, 2)

    def test_edge_case(self):
        res = add(0,0)
        self.assertEqual(res, 0)

    def test_corner_case(self):
        res = add(1000000,1000000)
        self.assertEqual(res, 2000000)

if __name__ == "__main__":
    unittest.main()