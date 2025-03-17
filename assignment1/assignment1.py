# Task 1: Hello
print("Task 1: Hello")
def say_hello():
  return "Hello!"
print(say_hello())

# Task 2: Greet with a Formatted String
print("Task 2: Greet with a Formatted String")
def create_greeting(name):
  greeting = f"Hi, {name}!"
  return greeting
print(create_greeting("Adryan"))

# 3. Task 3: Calculator // how do you expect me to know how to do this
print("Task 3: Calculator")
def calc(value1, value2, operation="multiply"):
    try:
        # operation block
        if operation == "multiply":
            return value1 * value2
        elif operation == "add":
            return value1 + value2
        elif operation == "subtract":
            return value1 - value2
        elif operation == "divide":
            return value1 / value2
        elif operation == "modulo":
            return value1 % value2
        elif operation == "int_divide":
            return value1 // value2
        elif operation == "power":
            return value1 ** value2
        else:
            return "error"
    except ZeroDivisionError:  # Exception block
        return "You can't divide by 0!"
    except TypeError:  # Exception block
        return "You can't multiply those values!"
    except Exception:  # Catch any other errors
        return "An error occurred"

result = calc(2, 3, "multiply")
print(f"Multiply result: {result}")
result = calc("dog", "dog", "multiply")
print(f"Multiply error result: {result}")
result = calc(2, 3, "add")
print(f"Addition result: {result}")
result = calc(2, 3, "subtract")
print(f"Substraction result: {result}")
result = calc(2, 3, "divide")
print(f"Division result: {result}")
result = calc(2, 0, "divide")
print(f"Division error result: {result}")
result = calc(2, 3, "modulo")
print(f"Modulo result: {result}")
result = calc(2, 3, "int_divide")
print(f"Integer division result: {result}")
result = calc(2, 3, "power")
print(f"Power result: {result}")

# Task 4: Data Type Conversion
print("Task 4: Data Type Conversion")
def data_type_conversion(value, data_type):
    if data_type == "float":
        try:
            return float(value)
        except ValueError:
            return f"You can't convert {value} into a {data_type}."
    elif data_type == "str":
        return str(value)
    elif data_type == "int":
        try:
            return int(value)
        except ValueError:
            return f"You can't convert {value} into a {data_type}."
    else:
        return None
print(data_type_conversion("dog", "float"))
print(data_type_conversion("dog", "str"))
print(data_type_conversion(3, "str"))
print(data_type_conversion("2.99", "int"))
print(data_type_conversion("dog", "int"))
print(data_type_conversion(10, "float"))

# Task 5: Grading System, Using *args
print("Task 5: Grading System, Using *args")
def grade_average(*args):
    try:
        if not args: #Handle case where no arguments are passed.
            return "No scores provided"
        average_score = sum(args) / len(args)

        if average_score >= 90:
            return "A"
        elif average_score >= 80:
            return "B"
        elif average_score >= 70:
            return "C"
        elif average_score >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."

print("First average: " + grade_average(80, 95, 100, 70, 85))
print("Second average: " + grade_average(50, 40, 30))
print("Third average: " + grade_average(90, 95, 99))
print("Fourth average: " + grade_average("test", 90)) #test for error handling
print("Fifth average: " + grade_average())

# Task 6: Use a For Loop with a Range
print("Task 6: Use a For Loop with a Range")
def repeat(string, count):
    repeated_string = ""
    for i in range(count):
        repeated_string += string
    return repeated_string
print(repeat("hi", 2))

# Task 7: Student Scores, Using **kwargs
print("Task 7: Student Scores, Using **kwargs")
def student_scores(query, **kwargs):
    if query == "best":
        highest_score = max(kwargs, key=kwargs.get)
        return highest_score
    elif query == "mean":
        mean_score = sum(kwargs.values()) / len(kwargs)
        return mean_score

print(student_scores("best", Joni=80, Steve=100, Shaan=50))
print(student_scores("mean", Joni=80, Steve=100, Shaan=50))

# Task 8: Titleize, with String and List Operations
print("Task 8: Titleize, with String and List Operations")
def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()

    capitalized_words = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) == 1 or word.lower () not in little_words:
            capitalized_words.append(word.capitalize())
        else:
            capitalized_words.append(word.lower())

    # words = string.split()
    # capitalized_words = [word.capitalize() for word in words]

    titleize_string = ' '.join(capitalized_words)
    return titleize_string

print(titleize("1844 economic and philosophic manuscripts"))

# Task 9: Hangman, with more String Operations
print("Task 9: Hangman, with more String Operations")
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

print(hangman("catdog", "og"))

# Task 10: Pig Latin, Another String Manipulation Exercise
print("Task 10: Pig Latin, Another String Manipulation Exercise")
def pig_latin(sentence):
    words = sentence.split() # split the sentence into words
    vowels = "aeiou"
    result = []

    for word in words:
        if word[0] in vowels: # if the word starts with a vowel
            result.append(word + "ay")
        elif word[:2] == "qu": 
            result.append(word[2:] + "quay")
        else:
            for i, letter in enumerate(word):
                if letter in vowels:
                    result.append(word[i:] + word[:i] + "ay")
    
    return " ".join(result)

sentence = "I barely understand pig latin as it is this is a horrible example for my nuerodivergent brain."
print(pig_latin(sentence))