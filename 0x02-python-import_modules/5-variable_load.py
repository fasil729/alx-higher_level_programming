#!/usr/bin/python3
if __name__ == "__main__":
    import variable_load_5
    try:
        print(variable_load_5.a)
    except AttributeError:
        print("there is no such variable")
