#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    str1 = ""
    for s in range(len(text)):
        str1 += text[s]
        if text[s] in ".?:":
            print(str1 + '\n')
            str1 = ""
