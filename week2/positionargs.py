#!/usr/bin/python3

# as alternative to writing arguments all in one line demo(name="Chad", age...etc)
#use keyword or positional arguments

# Keyword Arguments. One * for "any number of positional args, including 0"
# two ** means "any number of keyword args, including 0"

#this method hard prints each dictinary element
def demo(**stats):
    print(f"{stats['name']} statistics:")
    print(f" - Age: {stats['age']}")
    print(f" - Email: {stats['email']}")
    print(f" - Country: {stats['country']}")


# this method loops through the dictionary
def coolerpeep(**slappy):
    for key, value in slappy.items():
        print(f" - {key}- {value}")

chaddata = {
    "name":"Chad",
    "age":"37",
    "email":"122@aabc.com",
    "country":"united states"}

coolerpeep(**chaddata)
demo(**chaddata)

