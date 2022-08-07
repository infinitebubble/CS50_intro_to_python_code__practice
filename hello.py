# ask User for their name and printing it
# Removing whitespaces from the string adn Capitalizing name
name = input("What's your name? ").strip().title()  # input will take a string only

# printing the name
print(f"hello, {name}")
print("hello,", name)
print("Hello," + name)

first, last = name.split(" ")

# docs.python.com
# parameters

# + , - , *, / , % , **
# interactive coding :