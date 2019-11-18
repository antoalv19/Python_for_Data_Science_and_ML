# what is 7 to the power of 4?

print(7 ** 4)

# Split this string: s = "Hi there Sam!" into a list.

s = "Hi there Sam!"
print(s.split())

"""** Given the variables:**

planet = "Earth"
diameter = 12742
** Use .format() to print the following string: **

The diameter of Earth is 12742 kilometers."""

planet = "Earth"
diameter = 12472

print("The diameter of {} is {} kilometers.".format(planet, str(diameter)))

# Given this nested list, use indexing to grab the word "hello"

lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]

print(lst[3][1][2][0])

# Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky.

d = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}

print(d["k1"][3]["tricky"][3]["target"][3])

# Create a function that grabs the email website domain from a string in the form: user@domain.com
# So for example, passing "user@domain.com" would return: domain.com


def domainGet(domain):

    a = list(domain.split("@"))
    print(a[1])


domainGet("user@domain.com")

# Create a basic function that returns True if the word 'dog' is contained in the input string.
# Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.


def is_there_dog(dog):
    a = dog.lower().find("dog")
    print(a > -1)


is_there_dog("Dog")

# Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases.


def how_many_dogs(dog):
    a = list(dog.lower().split())
    i = 0
    dog_counter = 0
    while i < len(a):
        if a[i] == "dog":
            dog_counter = dog_counter + 1
            i = i + 1
        else:
            i = i + 1
    print(dog_counter)


how_many_dogs("dog dog dog ,cane, dog, oooo")

# Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'.

seq = ['soup', 'dog', 'salad', 'cat', 'great']

filtered_seq = list(filter(lambda x: x[0] == "s", seq))

print(filtered_seq)

"""
You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible 
results: "No ticket", "Small ticket", or "Big Ticket". If your speed is 60 or less, the result is "No Ticket". If 
speed is between 61 and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big 
Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your 
birthday, your speed can be 5 higher in all cases.
"""


def caught_speeding(speed, is_birthday):
    if is_birthday:
        if speed <= 65:
            print("No Ticket")
        elif 66 <= speed <= 86:
            print("Small Ticket")
        else:
            print("Big Ticket")
    else:
        if speed < 60:
            print("No Ticket")
        elif 61 <= speed <= 81:
            print("Small Ticket")
        else:
            print("Big Ticket")


caught_speeding(61, False)

