#!/usr/bin/python3
def remove_char_at(str, n):
    i = 1
    for index in str:
        i = i + 1
    if n >= 0:
        j = str[0:n] + str[n + 1:i]
    else:
        j = str
    return j
