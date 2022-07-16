def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce           # Here is how to use the decorator
def hello():
    print("Hello, world!")


hello()