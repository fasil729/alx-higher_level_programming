#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
        except Exception:
            result += (a / b) ** i
        else:
            result = a + b
            break
    return result
