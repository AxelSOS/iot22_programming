

def func_a():
    print("Hello from A")
    try:
        func_b()
    except ValueError:
        print("Oops when running B()")

def func_b():
    print("Hello from B")
    try:
        func_c()
    except IndexError:
        pass
        # hantera snyggt
    except ValueError:
        print("Oops when running C()")
        raise  # re-raise

def func_c():
    print("Hello from C")
    raise ValueError


func_a()