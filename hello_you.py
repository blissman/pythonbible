# Ask user for name

name = input("What is your name?: ")

# Ask user for age
age = input("What is your age?: ")

# Ask user for city
city = input("In what city do you live?: ")

# Ask user about what they enjoy
love = input("What's an activity you enjoy?: ")

# Create output text
string = "Your name is {}, you are {}-years old, living in {} and you love {}."
output = string.format(name, age, city, love)

# Print output to screen
print(output)
