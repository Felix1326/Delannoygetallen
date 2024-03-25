# Snel turtle tekenen
import turtle
import random
import math
import itertools
window = turtle.Screen()
pen = turtle.Turtle()
pen.speed("fastest")
pen.pensize(2)
pen.up()
window.tracer(0)
# VARIABELEN
penDikte = 1    # pendikte in pixels
lijnDikte = 3
aantalRoosters = None
zijde = 10      # aantal pixels in zijde vierkant
m = 5           # x-as van het Delannoy getal
n = 5           # y-as van het Delannoy getal
originx = -300 # x-coordinaat om te beginnen met tekenen
originy = 300  # y-coordinaat om te beginnen met tekenen
lijn1 = [45,45,45,45,45]      # maakt een list met stappen voor een lijn: 0 is horizontaal, 45 is diagonaal en 90 is verticaal
lijn2 = [0,45]
lijn3 = [0,90,0]
lijn4 = [45,0]
lijn5 = [90,0,0]
# FUNCTIES
pen.pensize(penDikte)
def vierkant(orx, ory):
    pen.up()
    pen.goto(orx, ory)
    pen.down()
    i = 0
    while i < 4:
        pen.forward(zijde)
        pen.left(90)
        i += 1
    pen.up()
    pen.goto(orx+1000,0)

def rooster(dimx, dimy, orx, ory):
    pen.up()
    pen.goto(orx, ory)
    #Teken eerste vierkant, als i < dimx teken nog een vierkant totdat de eerste
    # laag is getekent. Dan als j < dimy schuiven naar onder en opnieuw beginnen
    i = 0 #index voor x 
    j = 0 #index voor y
    while j < dimy:
        while i < dimx:
            vierkant(orx + i*zijde, ory + j*zijde)
            i += 1
        j += 1
        i = 0

def randomLijn(dimx, dimy, orx, ory, kleur): # moet hetzelfde zijn als het rooster
    pen.up()
    pen.goto(orx, ory)
    pen.pensize(lijnDikte)
    pen.color(kleur)
    # Neem een random aantal keren de operatie (1,1), dat ligt tussen de 0 en m (of n, afhankelijk
    # van welke het kleinste is). Bereken vervolgens de keren dat de andere operaties nodig zijn
    # (m-k, n-k) om de rechterbovenhoek te berijken.
    if dimx < dimy:
        diagonaal = random.randrange(dimx + 1)
        horizontaal = dimx - diagonaal
        verticaal = dimy - diagonaal
        xcoordinaat = 0
        ycoordinaat = 0
        while xcoordinaat != dimx and ycoordinaat != dimy:
            beweging = random.choice(["diagonaal", "verticaal", "horizontaal"])
            if beweging == "verticaal":
                pen.down()
                pen.left(90)
                pen.forward(zijde)
                pen.right(90)
                pen.up()
                ycoordinaat += 1
            elif beweging == "horizontaal":
                pen.down()
                pen.forward(zijde)
                pen.up()
                xcoordinaat += 1
            else:
                pen.down()
                pen.left(45)
                pen.forward(math.sqrt(2 * (zijde ** 2)))
                pen.right(45)
                pen.up()
                xcoordinaat += 1
                ycoordinaat += 1
        if xcoordinaat == dimx:
            while ycoordinaat != dimy:
                pen.down()
                pen.left(90)
                pen.forward(zijde)
                pen.right(90)
                pen.up()
                ycoordinaat += 1
        else:
            while xcoordinaat != dimx:
                pen.down()
                pen.forward(zijde)
                pen.up()
                xcoordinaat += 1
    else: # als n < m of n = m
        diagonaal = random.randrange(dimy + 1) # aantal mogelijke diagonale verschuivingen
        horizontaal = dimx - diagonaal # aantal mogelijke horizontale verschuivingen
        verticaal = dimy - diagonaal # aantal mogelijke verticale verschuivingen
        xcoordinaat = 0
        ycoordinaat = 0
        while xcoordinaat != dimx and ycoordinaat != dimy:
            beweging = random.choice(["diagonaal", "verticaal", "horizontaal"])
            if beweging == "verticaal":
                pen.down()
                pen.left(90)
                pen.forward(zijde)
                pen.right(90)
                pen.up()
                ycoordinaat += 1
            elif beweging == "horizontaal":
                pen.down()
                pen.forward(zijde)
                pen.up()
                xcoordinaat += 1
            else:
                pen.down()
                pen.left(45)
                pen.forward(math.sqrt(2 * (zijde ** 2)))
                pen.right(45)
                pen.up()
                xcoordinaat += 1
                ycoordinaat += 1
        if xcoordinaat == dimx:
            while ycoordinaat != dimy:
                pen.down()
                pen.left(90)
                pen.forward(zijde)
                pen.right(90)
                pen.up()
                ycoordinaat += 1
        else:
            while xcoordinaat != dimx:
                pen.down()
                pen.forward(zijde)
                pen.up()
                xcoordinaat += 1
    pen.color("black")
    pen.pensize(penDikte)
    pen.goto(500,500)

def tekenLijn(stappen,orx,ory,kleur):
    pen.up()
    pen.goto(orx,ory)
    pen.pensize(lijnDikte)
    pen.color(kleur)
    for stap in stappen:
        if stap == 45:
            pen.down()
            pen.left(45)
            pen.forward(math.sqrt(2 * (zijde ** 2)))
            pen.right(45)
            pen.up()
        else:
            pen.down()
            pen.left(stap)
            pen.forward(zijde)
            pen.right(stap)
            pen.up()
    pen.color("black")
    pen.up()
    pen.goto(orx+1000, ory)

def Delannoy(m,n): # Berekening Delannoy getallen
    if m == 0 or n == 0:
        return 1
    else:
        delannoyG = Delannoy(m-1,n) + Delannoy(m-1,n-1) + Delannoy(m,n-1)
        return delannoyG    
def delers(getal): # bepaal delers, zet delers in list, neem de middelste 2 delen van de list, gebruik die als m en n
    i = 1
    delers = []
    while i < getal:
        if getal % i == 0:
            delers.append(i)
        i += 1
    delers.append(getal)
    return delers
# Nu gaan we het Delannoygetal berekenen, de delers ervan vinden, ordenen en de middelste twee delers nemen als dimensies voor waar we de roosters moet plaatsen
# Bijvoorbeeld: Delannoy(3,3) = 63 Bijgevolg tekenen we 7 rijen van 9 3x3 roosters
# Deze roosters staan telkens 10% van een zijde uiteen, en we gebruiken een variatie van de randomLijn() functie om elke lijn te tekenen
def tekenDelannoyRoosters(m,n,orx,ory):# Teken alle roosters bij een Delannoy getal
    if m == 0 or n == 0:
        return
    #print(Delannoy(m,n))
    aantalRoosters = Delannoy(m,n)
    #print(aantalRoosters)
    dimensies = math.ceil(math.sqrt(aantalRoosters)) # maakt de dimensies tot een simpel vierkant ipv bovenstaande uitleg
    i = 0
    #print(dimensies)
    j = 0
    originx = orx-dimensies*zijde/2
    originy = ory+dimensies*zijde/2
    roosterIndex = 0
    while j<dimensies:
        while i<dimensies:
            if roosterIndex < aantalRoosters:
            # Teken eerste rij de helft van de totale rijen naar boven en naar links 
                rooster(m,n,originx+i*zijde*m*5/4,originy-5/4*j*zijde*n)

                roosterIndex += 1 # Telt het aantal roosters
            i+=1
        j+=1
        i=0



def tekenDelannoyLijn(m,n,orx,ory, kleur):
    aantalDiag = 0 #We beginnen met alle oplossingen voor 0 diagonale lijnen, en bij elke stap tekenen we het pad, te beginnen bij een verticale stap
    lijnen = [] # Lijst van lijnen: eerst vullen dan loopen om elke lijn appart te tekenen
    # genereer alle mogelijke lijn lijsten, gebruik vervolgens de tekenlijn functie
    # we zetten telkens alle bewegingen in een lijst, waarna we ze printen
    while aantalDiag <= m and aantalDiag <= n:
        aantalHor = m - aantalDiag
        aantalVert = n - aantalDiag
        # vul een lijst met alle stappen
        # zet alle combinaties van die stappen in een lijst
        stappen = []
        diagonaalIndex = 0
        horizontaalIndex = 0
        verticaalIndex = 0
        while diagonaalIndex < aantalDiag:
            stappen.append(45)
            diagonaalIndex +=1
        while horizontaalIndex < aantalHor:
            stappen.append(0)
            horizontaalIndex += 1
        while verticaalIndex < aantalVert:
            stappen.append(90)
            verticaalIndex += 1
        # Nu hebben we alle stappen in een lijst
        # Met itertools gaan we nu alle combinaties van die elementen vinden
        combinaties = list(itertools.permutations(stappen))
        i = 0
        for combinatie in combinaties:
            if combinatie not in lijnen:
                lijnen.append(combinatie)
        
        aantalDiag += 1
    print(lijnen)
    print(len(lijnen))
    #teken nu alle lijnen op de posities
    #print(Delannoy(m,n))
    aantalLijnen = Delannoy(m,n)
    #print(aantalRoosters)
    dimensies = math.ceil(math.sqrt(aantalLijnen)) # maakt de dimensies tot een simpel vierkant ipv bovenstaande uitleg
    i = 0
    #print(dimensies)
    j = 0
    originx = orx-dimensies*zijde/2
    originy = ory+dimensies*zijde/2
    lijnIndex = 0
    while j<dimensies:
        while i<dimensies:
            if lijnIndex < aantalLijnen:
            # Teken eerste rij de helft van de totale rijen naar boven en naar links 
                tekenLijn(lijnen[lijnIndex],originx+i*zijde*m*5/4,originy-5/4*j*zijde*n, kleur)

                lijnIndex += 1 # Telt het aantal roosters
            i+=1
        j+=1
        i=0



#rooster(m,n,originx,originy)
#randomLijn(m,n,originx,originy,"red")
#print(Delannoy(4,4))
#print(delers(15))
tekenDelannoyRoosters(m,n,originx,originy)
tekenDelannoyLijn(m,n,originx,originy,"red")
window.update()
window.mainloop()
   
