#

# def hello():
#     print(’Hi’)
#     hello()
# hello()

def hello(count):
    if count == 0: return
    print("Hi")
    count -= 1
#     hello(count)

hello(3)

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(3))