import turtle
import random
import kartyak
import time

def uj_ablak():
    turtle.setup(width=0.9, height=0.8)
    turtle.setworldcoordinates(-910, -500, 910, 450)
    turtle.tracer(0)

def kard():
    turtle.width(3)
    turtle.color("black")
    turtle.down()
    turtle.forward(20)
    turtle.left(90)
    turtle.width(2)
    turtle.forward(10)
    turtle.backward(20)
    turtle.forward(10)
    turtle.right(90)
    turtle.width(4)
    turtle.forward(80)
    turtle.up()

def ij():
    turtle.width(1)
    turtle.down()
    turtle.forward(100)
    turtle.right(120)
    turtle.width(3)
    for i in range(120):
        turtle.forward(1)
        turtle.right(1)
    turtle.up()
    turtle.setheading(90)

def katapult():
    turtle.width(5)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.up()
    turtle.forward(2)
    turtle.right(90)
    turtle.down()
    turtle.forward(50)
    turtle.left(90)
    turtle.up()
    turtle.backward(2)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(3)
    turtle.right(90)
    turtle.forward(2)
    turtle.down()
    turtle.width(3)
    turtle.forward(80)
    turtle.left(145)
    turtle.forward(100)
    turtle.up()
    turtle.left(125)
    turtle.forward(55)
    turtle.left(90)
    turtle.forward(2)
    turtle.left(40)
    turtle.down()
    turtle.forward(60)
    turtle.begin_fill()
    turtle.left(40)
    turtle.forward(5)
    turtle.right(40)
    turtle.forward(10)
    turtle.right(60)
    turtle.forward(5)
    turtle.right(120)
    turtle.forward(20)
    turtle.end_fill()
    turtle.up()
    turtle.setheading(90)
    

def hatter():
    turtle.clear()
    turtle.reset()
    turtle.bgcolor("floral white")
    turtle.color("black")
    turtle.left(90)
    turtle.st()
    turtle.up()
    turtle.backward(450)
    turtle.down()
    turtle.right(90)
    turtle.begin_fill()
    turtle.fillcolor("sandy brown")
    turtle.forward(900)
    turtle.left(90)
    turtle.forward(900)
    turtle.left(90)
    turtle.forward(1800)
    turtle.left(90)
    turtle.forward(900)
    turtle.left(90)
    turtle.forward(900)
    turtle.end_fill()
    turtle.up()

    turtle.fillcolor("grey")
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(6)
    for i in range(8):
        turtle.right(90)
        turtle.down()
        turtle.begin_fill()
        turtle.forward(800)
        turtle.left(90)
        turtle.forward(109)
        turtle.left(90)
        turtle.forward(1600)
        turtle.left(90)
        turtle.forward(109)
        turtle.left(90)
        turtle.forward(800)
        turtle.end_fill()
        turtle.up()
        turtle.left(90)
        turtle.forward(111)

    turtle.color("black")
    turtle.setpos(-680, -105)
    kard()
    turtle.setpos(-680, 5)
    kard()
    turtle.setpos(-680, 115)
    ij()
    turtle.setpos(-680, -215)
    ij()
    turtle.setpos(-698, -323)
    katapult()
    turtle.setpos(-698, 230)
    katapult()

    turtle.update()

def kartyat_rajzol(kartya, small_screen):
    """Megrajzolja a kártyát az adatai alapján"""
    if kartya.hos:
        turtle.fillcolor("gold")
    else:
        turtle.fillcolor("moccasin")
    turtle.down()
    turtle.right(90)
    turtle.begin_fill()
    turtle.forward(45)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(45)
    turtle.left(90)
    turtle.end_fill()
    turtle.up()
    turtle.forward(30)
    turtle.color("black")
    if len(kartya.neve) > 12:
        neve = kartya.neve[:12]+"."
    else:
        neve = kartya.neve
    if small_screen:
        turtle.write(neve, align="center", font=("Arial", 6, "normal"))
    else:
        turtle.write(neve, align="center")
    turtle.forward(30)
    betumeret = 12 if small_screen else 22
    turtle.write(kartya.erosseg, align="center", font=("Impact", betumeret, "normal"))
    turtle.backward(50)
    turtle.write(kartya.tipus.upper(), align="center")
    turtle.backward(10)

def napot_rajzol():
    turtle.forward(30)
    turtle.right(90)
    turtle.down()
    turtle.fillcolor("black")
    turtle.begin_fill()
    for i in range(12):
        turtle.circle(20, 30)
        turtle.right(90)
        turtle.forward(20)
        turtle.backward(20)
        turtle.left(90)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.backward(30)

def szornyet_rajzol():
    turtle.fillcolor("firebrick")
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.down()
    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(10)
    turtle.left(60)
    turtle.forward(10)
    turtle.right(60)
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(50)
    turtle.circle(30, 180)
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(10)
    turtle.right(60)
    turtle.forward(10)
    turtle.left(60)
    turtle.forward(10)
    turtle.right(120)
    turtle.right(180)
    turtle.end_fill()
    turtle.up()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(10)
    turtle.fillcolor("white")
    turtle.down()
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.up()
    turtle.backward(20)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.up()
    turtle.forward(10)
    turtle.left(90)
    turtle.backward(50)
    turtle.backward(20)

def cimert_rajzol():
    turtle.color("navy")
    turtle.forward(20)
    turtle.width(8)
    turtle.down()
    for i in range(7):
        turtle.forward(10)
        turtle.width(8-i)
    turtle.backward(70)
    turtle.width(5)
    turtle.right(45)
    turtle.forward(30)
    turtle.width(4)
    turtle.circle(-10, 180)
    turtle.up()
    turtle.circle(-10, 180)
    turtle.width(5)
    turtle.backward(30)
    turtle.left(90)
    turtle.down()
    turtle.forward(30)
    turtle.width(4)
    turtle.circle(10, 180)
    turtle.up()
    turtle.circle(10, 180)
    turtle.backward(30)
    turtle.right(45)
    turtle.backward(20)
    turtle.color("black")
    turtle.width(2)

def nyil():
    turtle.down()
    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(10)
    turtle.left(60)
    turtle.forward(10)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(120)
    turtle.forward(10)
    turtle.left(60)
    turtle.end_fill()
    turtle.forward(80)
    turtle.begin_fill()
    turtle.right(120)
    turtle.forward(10)
    turtle.left(150)
    turtle.forward(20)
    turtle.left(120)
    turtle.forward(20)
    turtle.left(150)
    turtle.forward(10)
    turtle.end_fill()
    turtle.left(80)
    turtle.up()
    turtle.backward(60)

def nyilat_rajzol():
    turtle.fillcolor("dark gray")
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(30)
    turtle.right(135)
    nyil()
    turtle.left(135)
    turtle.backward(30)
    turtle.right(90)
    turtle.seth(90)
    turtle.backward(15)

def hajot_rajzol():
    turtle.fillcolor("purple")
    turtle.forward(20)
    turtle.right(90)
    turtle.begin_fill()
    turtle.down()
    turtle.forward(30)
    turtle.left(60)
    turtle.forward(15)
    turtle.left(120)
    turtle.forward(70)
    turtle.left(120)
    turtle.forward(15)
    turtle.left(60)
    turtle.forward(30)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(10)
    turtle.width(4)
    turtle.down()
    turtle.forward(60)
    turtle.backward(40)
    turtle.width(2)
    turtle.right(90)
    turtle.begin_fill()
    turtle.forward(30)
    turtle.left(150)
    turtle.circle(-20, 120)
    turtle.left(150)
    turtle.forward(60)
    turtle.left(30)
    turtle.circle(20, 120)
    turtle.left(30)
    turtle.forward(30)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.backward(70)

def mit_rajzol(frakcio):
    """Kártyahátlapra és játékos frakció ikonnak"""
    if frakcio == kartyak.Frakcio(1).name:
        napot_rajzol()
    elif frakcio == kartyak.Frakcio(4).name:
        szornyet_rajzol()
    elif frakcio == kartyak.Frakcio(2).name:
        cimert_rajzol()
    elif frakcio == kartyak.Frakcio(3).name:
        nyilat_rajzol()
    elif frakcio == kartyak.Frakcio(5).name:
        hajot_rajzol()

def hatlap_rajzol(frakcio):
    if frakcio != kartyak.Frakcio(3).name:
        turtle.fillcolor("dim gray")
    else:
        turtle.fillcolor("forest green")
    turtle.down()
    turtle.right(90)
    turtle.begin_fill()
    turtle.forward(45)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(45)
    turtle.left(90)
    turtle.end_fill()
    turtle.up()
    mit_rajzol(frakcio)

def jatekallas_update(small_screen, jpont, p1nyk, aip, p2nyk):
    """Bal oldalon köröként firssíti az állást"""
    betumeret = 12 if small_screen else 18
            
    turtle.setpos(-810, -420)
    turtle.write("Ponsztám: {}".format(jpont),
                 align="center", font=("Impact", betumeret, "normal"))
    turtle.setpos(-810, -380)
    turtle.write("Nyert körök: {}".format(p1nyk),
                 align="center", font=("Impact", betumeret, "normal"))
    
    turtle.setpos(-810, 350)
    turtle.write("Ponsztám: {}".format(aip),
                 align="center", font=("Impact", betumeret, "normal"))
    turtle.setpos(-810, 400)
    turtle.write("Nyert körök: {}".format(p2nyk),
                 align="center", font=("Impact", betumeret, "normal"))

def update(p1, p1_asztal, p2, p2_asztal, jatekos_pont, ai_pont, small_screen):
    """Körönként firssítjük a játék asztalára letett kártyákat"""
    turtle.clear()
    turtle.reset()
    hatter()
    turtle.width(2)
    
    cc = 0
    rc = 0
    s = 0
    for i in range(len(p1.pakli)): #kezünkben lévő lapok
        turtle.setpos(-663 + i*100, -440)
        kartyat_rajzol(p1.pakli[i], small_screen)
        turtle.backward(40)
        betumeret = 10 if small_screen else 14
        turtle.write(i + 1, align="center", font=("Arial", betumeret, "normal"))
    for i in range(len(p2.pakli)): #ellenfél kezében lévő lapok
        turtle.setpos(-663 + i*100, 340)
        hatlap_rajzol(p2.frakcio)
        
    for i in range(len(p1_asztal)): #általunk letett kártyák
        if len(p1_asztal[i].tipus) <= 2:
            if p1_asztal[i].tipus == "cc":
                turtle.setpos(-600 + cc*100, -108)
                cc += 1
            elif p1_asztal[i].tipus == "rc":
                turtle.setpos(-600 + rc*100, -220)
                rc += 1
            else:
                turtle.setpos(-600 + s*100, -330)
                s += 1            
        else:
            turtle.setpos(-790, -200)
        kartyat_rajzol(p1_asztal[i], small_screen)
        
    turtle.update()
    cc = 0
    rc = 0
    s = 0
    for i in range(len(p2_asztal)): #ellenfél által letett kártyák
        if len(p2_asztal[i].tipus) <= 2:
            if p2_asztal[i].tipus == "cc":
                turtle.setpos(-600 + cc*100, 5)
                cc += 1
            elif p2_asztal[i].tipus == "rc":
                turtle.setpos(-600 + rc*100, 115)
                rc += 1
            else:
                turtle.setpos(-600 + s*100, 226)
                s += 1
        else:
            turtle.setpos(-790, 100)
        if i == len(p2_asztal)-1:
            turtle.color("red")
        kartyat_rajzol(p2_asztal[i], small_screen)

    turtle.color("black")

    turtle.setpos(-810, -350)
    mit_rajzol(p1.frakcio) #frakciónk ikonja

    turtle.setpos(-810, 250)
    mit_rajzol(p2.frakcio)

    jatekallas_update(small_screen, jatekos_pont, p1.nyert_korok,
                      ai_pont, p2.nyert_korok)

def bevitel(valasztek, passzolt_e):
    """Körönként beolvassuk a játékos lépését"""
    szoveg = "Válassz kártyát: (1-{})\nPassz: -1\nKonzolra kártyák információi: 0".format(len(valasztek))
    if passzolt_e:
        szoveg += "\n(Ellenfeled már passzolt!)"
    v = int(turtle.numinput("Kártya sorszáma", szoveg, minval = -1, maxval = len(valasztek)))
    return v
    
def nyertes(szoveg):
    """Kiírja a nyertes nevét a képernőyre, majd bezárja az ablakot"""
    turtle.color("black")
    turtle.setpos(0, 0)
    turtle.write(szoveg, align="center", font=("Impact", 30, "bold"))
    time.sleep(3)
    turtle.bye()

def ki_kezd(frakcio):
    """Scoia'tael passzív miatt itt döntjük el, ki kezd"""
    if frakcio == kartyak.Frakcio(3).name:
        jatekos_kor = int(turtle.numinput("Scoia'tael passzív", "Szeretnél te kezdeni? (Igen: 0, Nem: 1)", minval = 0, maxval = 1))
        return jatekos_kor
    else:
        return random.randint(0, 1) #páros esetén játékos kezd

def jatekos_nev():
    """Beolvassuk a játékos nevét"""
    nev = turtle.textinput("Név", "Add meg a neved:")
    return nev

def frakcio_valasztas(fejlec):
    """Kiválasztjuk a frakciókat"""
    szoveg = "Válassz egy frakciót:\n"
    for i in range(0, 5):
        szoveg += "{}: {}".format(i + 1, kartyak.Frakcio(i+1).name)
        szoveg += "\n"
    szoveg += "6: Random"
    valasz = int(turtle.numinput(fejlec, szoveg, minval = 1, maxval = 6))
    if valasz == 6:
        return kartyak.Frakcio(random.randint(1, 5)).name
    return kartyak.Frakcio(valasz).name

