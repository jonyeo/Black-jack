import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, ]



def banker(bankerTotal):
    bankerTotal += deck[0]
    deck.pop(0)
    global finalTotal
    finalTotal=bankerTotal
    #print("banker total " + str(bankerTotal))
    if bankerTotal < 16:
        banker(bankerTotal)
    else:
        finalTotal=bankerTotal

def drawing(wantDraw,playerTotal,bankerTotal):
    playerTotal += deck[0]
    deck.pop(0)
    print("This is your current total : " + str(playerTotal))
    print("Do you want to draw?(true/false) : ")
    wantDraw = input()
    if wantDraw=="true":
        drawing(wantDraw, playerTotal, bankerTotal)

    elif wantDraw == "false":
        noDraw(bankerTotal,playerTotal)

def noDraw( bankerTotal , playerTotal ):

    if bankerTotal > 21 and playerTotal<22:
        print("Banker had : " + str(bankerTotal) + " You had : " + str(playerTotal) + " You win")
    if bankerTotal < 22 and playerTotal > 21:
        print("Banker had : " + str(bankerTotal) + " You had : " + str(playerTotal) + " You lose")
    elif bankerTotal < 22 and playerTotal < 22:
        if bankerTotal > playerTotal:
            print("Banker had : " + str(bankerTotal) + " You had : " + str(playerTotal) + " You lose")
        elif bankerTotal < playerTotal:
            print("Banker had : " + str(bankerTotal) + " You had : " + str(playerTotal) + " You win")
        else:
            print("Banker had : " + str(bankerTotal) + " You had : " + str(playerTotal) + " Draw")
    main()

def game():
    global finalTotal
    finalTotal = 0
    global  playerTotal
    playerTotal = 0

    random.shuffle(deck)

    for y in range(2):
        playerTotal += deck[0]
        deck.pop(0)

    for y in range(2):
        finalTotal += deck[0]
        deck.pop(0)

    print(playerTotal)

    if finalTotal < 16:
        #print("banker total " + str(finalTotal))
        banker(finalTotal)

    wantDraw = input("Do you want to draw?(true/false) : ")

    if wantDraw == "true":
        drawing(wantDraw, playerTotal, finalTotal)

    elif wantDraw =="false":
        noDraw(finalTotal, playerTotal)

def main():
    print("Do you want to player?(yes/no)")
    reply = input()
    if reply == "yes":
        game()
    else:
        print("Thank you")

main()