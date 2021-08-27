import random
a = input("Hello! Welcome to Probability Simulation! What would you like to start off with? Please enter your game of choice with the following keywords: Dice, Number Gen, Cards, Marbles, and Coins.")
if a.lower() == "dice":
    b = input("You can now choose from Normal Mode or Guess Mode. n for Normal Mode, g for Guess Mode.")
    if b.lower() == "n":


        x = random.randint(1, 6)

        print("The amount of dots shown on your dice is " + str(x))
        c = input("Would you like to continue? y for yes, n for no.")
        if c.lower() == "y":

            y = input("Exactly how many times would you like to repeat?")
            d = 0

            while d < int(y):

                f = random.randint(1, 6)
                d = d + 1
                print("The amount of dots shown on your dice is " + str(f))

    if b.lower() == "g":

        e = input("What number do you guess? Please choose a number between 1 and 6.")
        if str(6) < e < str(1):
            print("Invalid Number.")
        if e <= str(6) and e >= str(1):
            x = random.randint(1, 6)


        if e != x:
            print("The amount of dots shown on your dice is " + str(x) + "." + "You lose!")
        if e == x:
            print("The amount of dots shown on your dice is " + str(x) + "." + "You win!")

        c = input("Would you like to continue? y for yes, n for no.")
elif a.lower() == "number gen":
    g = input("Please enter the parameter (minimum) of the number gen.")

    h = input("Please enter the parameter (maximum) for the number gen.")

    i = input("Please enter the amount of numbers you wish to generate.")

    j = 0
    while j < int(i):
        k = random.randint(int(g), int(h))
        j = j + 1
        print("Here are your numbers:")
        print(str(k))
elif a.lower() == "cards":
    myList = ["spades", "clubs", "hearts", "diamonds"]
    l = input("Would you like the Jack, Queen, and King to be 11,12, and 13 respectively? If yes, Jacks, Queens, and Kings will be represented as 11,12, and 13. If no, Jacks, Queens, and Kings will all be represented as 10.")
    if l.lower() == "yes":
        m = random.randint(1, 13)

        n = random.choice(myList)

        if m == 1:
            print("Your card is: " + "an Ace" + " of " + str(n) + ".")
        elif m > 1 and m <= 10:
            print("Your card is: " + "a " + str(m) + " of " + str(n) + ".")
        elif m == 11:
            print("Your card is: " + "a Jack" + " of " + str(n) + ".")
        elif m == 12:
            print("Your card is: " + "a Queen" + " of " + str(n) + ".")
        elif m == 13:
            print("Your card is: " + "a King" + " of " + str(n) + ".")
    if l.lower() == "no":

        o = random.randint(1, 9)

        myList2 = ["spades", "clubs", "hearts", "diamonds"]

        p = random.choice(myList2)

        if o == 1:
            print("Your card is: " + "an Ace" + " of " + str(p) + ".")
        elif o > 1 and o < 10:
            print("Your card is: " + "a " + str(o) + " of " + str(p) + ".")
        elif o == 10:
            myList3 = ["10", "Jack", "Queen", "King"]

            q = random.choice(myList3)

            print("Your card is: " + "a " + str(q) + " of " + str(n) + ".")
if a.lower() == "marbles":
    r = input("You are allowed three marbles. Please name the color of your first marble.")
    s = input("Please name the color of your second marble.")
    t = input("Please name the color of your third marble.")
    myList4 = [ str(r), str(s),str(t)]
    u = random.choice(myList4)
    print("The color of the marble chosen is " + str(u) + ".")
    v = input("Would you like to try again?")
    if v.lower() == "yes":
        w = input("Do you want to change your marble colors?")
        if w.lower() == "yes":
            a1 = input("You are allowed three marbles. Please name the color of your first marble.")
            b1 = input("Please name the color of your second marble.")
            c1 = input("Please name the color of your third marble.")
            f1 = input("How many times do you want to repeat this?")
            h1 = 0

            while int(h1) < int(f1):
                myList5 = [str(a1), str(b1), str(c1)]
                i1 = random.choice(myList5)
                print("The color of the marble chosen is " + str(i1) + ".")
                h1 = h1 + 1

        elif w.lower() == "no":
            d1 = input("How many times to you want to repeat this?")

            e1 = 0

            while int(e1) < int(d1):

                myList5 = [str(r), str(s), str(t)]
                g1 = random.choice(myList5)
                print("The color of the marble chosen is " + str(g1) + ".")
                e1 = e1 + 1
if a.lower() == "coins":
    j1 = input("How many times do you wish to flip a coin?")

    k1 = 0

    while k1 < int(j1):

        myList6 = ["Heads", "Tails"]

        l1 = random.choice(myList6)
        k1 = k1 + 1
        print("You flipped : " + str(l1) + ".")

























