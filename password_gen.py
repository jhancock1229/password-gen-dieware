#!/usr/bin/env python3


# Needs to be put into a class
# Needs a module to import dictionary values of the dieware list directly 
#   rather than creating the dict here.
# Clean up the horrible syntax of the functions.
#  Write some meaningful comments lol
# put an argparser in here

import secrets


die = [1,2,3,4,5,6]
d = dict()
die_roll = secrets.choice(die)

def generate_dictionary(txt_file):
    with open(txt_file) as f:
        for line in f:
            (key, val) = line.split()
            d[int(key)] = val

def generate_word_number():
    w = [0]*5
    return int("".join(map(str, [secrets.choice(die) for i in w])))

def generate_die_words(num_words=5):
    return [generate_word_number() for _ in range(num_words)]

def generate_password():
    return [d[x] for x in generate_die_words()]

def main():
    generate_dictionary("dieware_list.txt")
    return generate_password()

if __name__ == "__main__":
    x = main()
    print(x)
    # generate_password()

    # for x in generate_die_words():
    #     print(d[x])

