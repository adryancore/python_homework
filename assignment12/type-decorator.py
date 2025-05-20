# Step 2: Define the decorator that takes a type as an argument
def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)  # Attempt to convert return value
        return wrapper
    return decorator

# Step 3: Define return_int and decorate to convert to str
@type_converter(str)
def return_int():
    return 5

# Step 4: Define return_string and decorate to convert to int
@type_converter(int)
def return_string():
    return "not a number"

# Step 5: Mainline test code
if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__)  # Should print "str"

    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!")  # Expected result in Terminal