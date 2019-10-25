from dictionnary import ville

distancep = 0
vitesse = 0
tmp = 0
pauses = 0

            

def depart():
    Vdepart = input("Ville de depart : ") 
    Varrive = input("Ville d'arrive : ")
    return depart, arrive

def kilometre(depart, arrive):
    distance = ville[Vdepart][Varrive]
    totaldistance = distance 
    


def accelerer():
    global vitesse, tmp, distancep
    while vitesse < 90:
        vitesse += 10
        tmp += 1
        distancep -= 7.5

def freiner():
    global vitesse, tmp, distancep
    while vitesse != 0:
        vitesse -= 10
        tmp += 1
        distancep -= 7.5

def pause():
    global tmp
    if tmptrajet%120 == 0:
        freinage()
        pauses += 15
        acceleration()


def trajet(depart, arrive):
    kilometre()
    accelerer()
    while distancep > 7.5:
        tmp += 1
        distance -= 1.5
        pause()
    freinage()

tmp += pauses

print('totaldistance : ','tmp :')



