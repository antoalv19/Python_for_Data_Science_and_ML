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

