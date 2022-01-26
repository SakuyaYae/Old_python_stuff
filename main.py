#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sakuya with a simple menu to start up with.
Sakuya doesnt do anything, just presents a menu with some choices.
You should add functinoality to Sakuya.
"""

marvin_image = r'''
                                     ___,
                   d88888baa__________            ____aad88888b
                  d888P""~~~~~~~~~~~~~~-----___ad88888888888888
              __-""                           "Y888888888888888b
             /                                  ~~Y8888P"""aaaa88a
            ,,,aaaaaaaaa,,,...__                   ~Yaaa8888888888
        __ d88888888888888888888888b                 8888888888888
      _- ,d88888P""""""~~~~~"""Y8888baa,             Y"""88888888P
     /  /~~~~~~                    """Y88a...         888""""888P
    /  /      ,     |      |    |         |  `.       8888888aP
   |  |      |     | ||    |     |         |  `;      Y888888P       _
  |  |     /|     |  | \    \    |          | ' ;      88888P       | |
  |  |    / |     |   | |    |    |         |          8888P     ___| |___
 |  |    /  |    |    |  \    \    |         |         Y888     |___   ___|
|  |    |  |    /     |   |.   \_   \        |          Y8P         | |
| |    |  |  __|_      `. __\====__   \__----|          |"          | |
  |__-|__-\ ~~~|           ~ ~~~  ~~,.  | | |    |      |          | /
        .\ ~~~_____        _,aaaa._     | | |     |     |          |/
        | \ ,""88b        ""Y"P:888ba   | | |     |      |       _________
        |  |   8o8           d8d888P~~  | | |     |      |      |_______  |
        |  |   Y88b          888888     | |  |    |      |              | |
        |  |    888          888888     | |  |    |       |             | |
        |  |    888          Y88888     | |  |     |      |      _______| |
        |  |    Y8P         __8888Pa    | |  |     |      |     |_______  |
       |   |   ~~~         ~~""Y88P""   | |  |     |       |       _   _'-'
       |   |        /                  |  |   |    |       |      | | | |
       |   |        \                  |  |   |     |      |      | | | |
       |   |                           |  |   |     |       |     | | | |
       |    \         -                |  |    |    |       |     | | | |
       |    | \                        |  |    |     |      |    / /  | |_-,
       |    ||  \                 __ --|  |    |     |       |  <_/    \___/
       |    || |  \         __ --      |  |     |    |       |     _   _
      |     || |     \__ -,            |  |     |     |      |    | | | |
      |    | |  |         |            |  ||     |    |       |   | | | |
      |    | |  |         |           ||  ||      |    |      |   | | | |
      |    ||   |        ,|           ||  ||       \    |     |   | | | |
     |     ||   |       a8|           ||  | |       \   |      | / /  | |_-,
     |    | |   |     d88P|---8888"""| |  | |         \         <_/    \___/
    |     ||   |     """""""""""""888| |  || |
    |     ||   |    d8888888888888888| |  | |
    |     ||  |   d88888888888888888|
'''

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
while True:
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("konnichiwa, I'm Sakuya. I know What you want to do")
    print("1) Tell Sakuya your name.")
    print("2) Convert Celcius till Farenheit.")
    print("3) Word multiplying.")
    print("4) Sum and avrage.")
    print("5) More or less or same.")
    print("6) String manipulation.")
    print("7) Isogram check.")
    print("8) shuffle letters.")
    print("9) reversed words.")
    print("10) shortname.")
    print("11) word masking.")
    print("12) Informativ info.")
    print("Comands you can type: inv, inv add item, inv drop item, inv drop, citat.")
    print("q) Quit.")

    import marvin
    import inventory
    import quote
    import sakuya

    choice = input("--> ")

    if choice == "q":
        print("Bye, bye - Lets meet again sometime!")
        break

    elif choice == "1":
        marvin.choice1()

    elif choice == "2":
        marvin.choice2()

    elif choice == "3":
        marvin.choice3()

    elif choice == "4":
        marvin.choice4()

    elif choice == "5":
        marvin.choice5()

    elif choice == "6":
        marvin.choice6()

    elif choice == "7":
        marvin.choice7()

    elif choice == "8":
        marvin.choice8()

    elif choice == "9":
        marvin.choice9()

    elif choice == "10":
        marvin.choice10()

    elif choice == "11":
        marvin.choice11()

    elif choice == "12":
        sakuya.choice12()

    elif choice == "inv":
        inventory.invread()

    elif "inv add " in choice:
        item = choice.replace("inv add ", "")
        inventory.invadd(item)

    elif "inv drop " in choice:
        item = choice.replace("inv drop ", "")
        inventory.invdrop(item)

    elif choice == "inv drop":
        inventory.invdropall()

    elif choice == "citat":
        quote.quoteread()

    elif "hej" in choice:
        quote.hi()

    elif "lunch" in choice:
        quote.lunch()

    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")
