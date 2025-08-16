# calculator.py  

def add(a, b):  
    return a + b  

def divide(a, b):  
    if b == 0:  
        raise ValueError("No se puede dividir entre cero")  
    return a / b  

def sqrt_approx(x, iterations=10):  
    guess = x / 2.0  
    for _ in range(iterations):  
        guess = 0.5 * (guess + x / guess)  
    return guess  

def exp_approx(x, terms=15):  
    result = 1.0  
    term = 1.0  
    for n in range(1, terms):  
        term *= x / n  
        result += term  
    return result  
