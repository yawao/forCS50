def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce #hello = announce(hello)
def hello():
    print("Hello, world!")
hello()
