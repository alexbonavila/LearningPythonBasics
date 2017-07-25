#!/usr/bin/env python3

# This for loop make a sentence
words = ["Hello, ", "how ", "are ", "you", "?"]

sentence = ""

for val in words:
    sentence = sentence + val

print(sentence)


# This wile loop sum 1+2+3+4+5+6+7...100
n = 100
operation = 0
i = 1

while i <= n:
    operation = operation + i
    i = i+1

print(operation)
