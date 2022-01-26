#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The code of the choices Sakuya presents you whit
"""
import random

def choice1():
    """
    Tell Sakuya your name.
    """
    name = input("What is your name? ")
    print("\nSakuya says:\n")
    print("Hello %s - your a pro!" % name)
    print("What can I do you for?!")

def choice2():
    """
    Convert Celcius till Farenheit
    """
    tempratur_c = float(input("Tell me the tempratur in degrees C. "))
    tempratur_f = (((tempratur_c * 9) / 5) + 32)
    print("The temerture in F is ", tempratur_f, "degrees.")

def choice3():
    """
    Word multiplying
    """
    word = input("Type a word that Ill type asmany times as you want. ")
    times = int(input("type how many times I'll whrit your word. "))
    for num in range(times):
        num = word + num
        print(word)

def choice4():
    """
    Sum and avrage
    """
    sum1 = 0
    while True:
        numbers = int(input("Type the numbers you want to know the sum or avrage of or 0 to exit. "))
        if numbers == 0:
            break
        else:
            sum1 = numbers + sum1
            print("the sum is", sum1)
            avrage = sum1 / 2
            print("the avrage is", avrage)

def choice5():
    """
    More or less or same
    """
    small1 = 9999999
    while True:
        content = input("type q to quit or a number: ")
        if content == "q":
            break
        else:
            number = int(content)
            if number < small1:
                print("the number:", number, "is smaller than:", small1)
            elif number > small1:
                print("the number:", number, "is larger than:", small1)
            else:
                print("the number:", number, "is the same as:", small1)
        small1 = number

def choice6():
    """
    String manipulation
    """
    wordstring = input("type the word that you want me to manipulate: ")
    stringword = ""
    for index, letter in enumerate(wordstring):
        stringword += letter * (index + 1) + "-"
    print(stringword)

def choice7():
    """
    Isogram check
    """
    isogram1 = input("type the word that you want me to check if its a isogram: ")
    for letter in isogram1:
        if isogram1.count(letter) > 1:
            print("not a Isogram")
            break

    print("It is a Isogram if this is the only text sying Isogram whit a capital I")

def choice8():
    """
    shuffle letters
    """
    word = input("Type a word to shuffle: ")
    newword = ""
    countdown = len(word)
    while countdown > 0:
        index = random.randint(0, len(word) - 1)
        newword += word[index]
        word = word[:index] + word[index + 1:]
        countdown -= 1
    print(newword)

def choice9():
    """
    order of letters
    """
    word9 = input("Type the first word to check the letters in: ")
    drow9 = input("Type the second word to check the letters in: ")
    if sorted(word9.lower()) == sorted(drow9.lower()):
        print("The words are the reversed of etchother")

    else:
        print("The words are not the reversed of etchother")

def choice10():
    """
    shortname
    """
    useword = input("Type a word or name were the uppercases will create a shortname: ")
    shortname = ""
    for letter in useword:
        if letter.isupper():
            shortname += letter
    print(shortname)

def choice11():
    """
    Masking of string
    """
    unmaskedword = input("Type a word that will be masked exept for the last four letters: ")
    lenth = len(unmaskedword)
    masked = lenth - 4
    lastfour = unmaskedword[masked:]
    completstring = "*" * masked + lastfour
    print(completstring)
