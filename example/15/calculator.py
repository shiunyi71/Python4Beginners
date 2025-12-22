# filepath: calculator.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    add_result = add(5, 3)
    multiply_result = multiply(4, 2)
    print(f"Addition Result: {add_result}")
    print(f"Multiplication Result: {multiply_result}")