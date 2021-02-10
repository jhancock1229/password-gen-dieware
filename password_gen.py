#!/usr/bin/env python3

import secrets


die = [1,2,3,4,5,6]
d = dict()
die_roll = secrets.choice(die)

# print(die_roll)
with open("dieware_list.txt") as f:
    for line in f:
        (key, val) = line.split()
        d[int(key)] = val

def generate_word_number():
    w = [0]*5
    return int("".join(map(str, [secrets.choice(die) for i in w])))

def generate_die_words(num_words=5):
    return [generate_word_number() for _ in range(num_words)]


actual_words = list()
for x in generate_die_words():
    actual_words.append(d[x])
# print(actual_words)

print(" ".join(actual_words))
# print(d)
# print(generate_word_number())
# print(generate_die_words())
# print(next(generate_die_words()))
# print(next(generate_die_words()))
# print(next(generate_die_words()))
# print(next(generate_die_words()))
# print(next(generate_die_words()))

# print(next(generate_die_words()))
# print(next(generate_die_words()))
# print(next(generate_die_words()))
# print(next(generate_die_words()))
# print(next(generate_die_words()))
