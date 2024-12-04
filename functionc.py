from random import randint, choice


# ---------------------------------

life = 100
mana = 100
gold = 0 
elixir = 0 

# ---------------------------------
                                                                            
def menu():
    while life >0:
        print ("wybierz opcje")
        print ("1-walka")
        print ("2-ulepszenia")
        print ("3-eksploracja")
        print ("4-koniec gry")
        wybor = input()
        if wybor == "1":
            walka()
        elif wybor == "2":
            ulepszenia()
        elif wybor == "3":
            eksploracja()
        elif wybor == "4":
            print("koniec gry")
            break
        else:
            print("wybierz poprawna opcje")

#-------------------------------

def zwykly_atak():
    return randint(3, 10)

def fire_ball():
    global mana
    if mana < 10:
        print("-"*40)
        print("Nie masz wystarczającej ilości many!")
        return 0
    mana -= 10
    return randint(13, 20)

def magic_punch():
    global mana
    if mana < 5:
        print("-"*40)
        print("Nie masz wystarczającej ilości many!")
        return 0
    mana -= 5
    return randint(10 ,15)

def dragon_fury():
    global gold 
    if gold < 5:
        print("-"*40)
        print("Nie masz wystarczającej ilości golda!")
        return 0
    gold -= 5
    return randint(20, 40)



def wybierz_atak():
    print('1 - Wykonaj Normalny Atak')
    print('2 - Fire ball!')
    print('3 - Magic punch')
    print("4 - Dragon fury")
    co = input()
    if co == '1':
        return zwykly_atak()
    elif co == '2':
        return fire_ball()
    elif co == '3':
        return magic_punch()
    elif co == "4":
        return dragon_fury()

    else:
        print("Nie wybrano akcji")
        return 0

def walka():
   
    global life,gold
    while life > 0:
        opponent = random_oponent()
        liczba_pokonanych_przeciwników = 0
        while opponent[1] > 0 and life > 0:
            print(f" walczy teraz z {opponent[0]}")
            print(f"Przeciwnik ma {opponent[1]} HP i zadaje Ci {opponent[2]} obrażeń")
       
            life -= opponent[2]
            if life <= 0:
                print("umarles")
                break


            print(f"Masz {life} HP i {mana} many")
            atak = wybierz_atak()
            opponent[1] -= atak
            print(f"Zadałeś {atak} obrażeń")


        if opponent[1] <= 0:
            print("="*30)
            print('Zabiłeś przeciwnika!!! dostajesz 10 gold')
            print("="*30)

            liczba_pokonanych_przeciwników += 1
            gold += 10
            print(f"=== masz {life} life,{mana} mamy,{gold} golda ===")

        if liczba_pokonanych_przeciwników==15:
            boss()
            break

# ---------------------------------
def random_oponent():
    opponents = [
        ["Mały Goblin", 15, 3, 0],
        ["Nimfa Wodna", 10, 3, 0]
    ]
    return choice(opponents)



# -------------------------------
def boss():
    global mana
    global life
    boss=["boss",90,10,0]
    while boss[1]>0 and life>0:
        print(f"Masz doczynienia z bossem:{boss[0]}")
        atak=wybierz_atak()
        boss[1]-=atak
        life -= boss[2]
        print(f"boss zadal ci {boss[2]} obrazen")
        if life <= 0:
            print(" === UMARLES === ")
            break
        print(f"zadales {atak} obrazen bossowi")
        print(f"=== masz {life} life,{mana} mamy,{gold} golda ===")
        if boss[1]<=0:
            print("pokonales bossa")
            print("zdobyles 30 life i 20 mana")
            life =+ 30
            mana =+ 20
            print("-"*30)
            print(f"=== masz {life} life,{mana} mamy,{gold} golda ===")
            print("-"*30)
            menu()

#-----------------------------
def ulepszenia():
    global gold,mana,elixir,life
    print("ULEPSZENIA")
    print("1   +20life za 10 gold")
    print("2   +15 mana za 12 gold")
    print("3   elixir za 15 gold")
    print("4   wyjdz z ulepszen")
    wybor = input()
    if wybor == "1" and gold>=10: 
        life += 20
        gold -= 10
        print("twoje zycie wzroslo o 20")
    elif wybor == "2" and gold>=12:
        mana += 15
        gold -= 12 
        print("twoja mana wzrosla o 15")
    elif wybor == "3" and  gold >=15:
        elixir += 1
        gold -= 15
        print("kupiles elixir")
    elif wybor == "4":
        print("wyjdz z ulepszen")
        return  
    else: 
        print("nie masz wystarczajaco golda lub wybrales zla opcje")





# ------------------------------

def walka_eksploracja():
    print("1- ice_shard")
    print("2- thunder_strik")
    print("3-poison_dart")
    print("4- wind_slash_")
    print("5-earth_quake")
    wybor = input()
    if wybor == "1":
        return ice_shard()
    elif wybor == "2":
        return thunder_strike()
    elif wybor == "3":
        return poison_dart()
    elif wybor == "4":
        return wind_slash_()
    elif wybor == "5":
        return earth_quake() 
    else:
        print("nie wybrano akcji")
        return 0
     
def ice_shard():                                                         
    global mana
    if mana <8:
        print("nie masz wystarczajacej ilosci many")
        return 0
    mana -= 8 
    obrazenia = randint(10,15)
    return obrazenia

def earth_quake():
    global mana
    if mana <3:
        print("nie masz wystarczajacej ilosci many")
        return 0 
    mana -= 3
    obrazenia = randint(15,30)
    return obrazenia

def thunder_strike():
    global gold
    if gold <5:
        print("nie masz wystarczajacej ilosci golda")
        return 0
    gold -= 5
    obrazenia = randint(15,20)
    return obrazenia

def poison_dart():
    global elixir
    if elixir <1:
        print("nie masz elixirow")
        return 0 
    elixir -= 1 
    obrazenia = randint(20,25)
    return obrazenia 

def wind_slash_():
    global mana
    if mana <20:
        print("nie masz wystarczajacej ilosci many")
        return 0 
    mana -= 20
    obrazenia = randint(25,30)
    return obrazenia

def eksploracja():
    global life,mana,gold,elixir
    pokoje = 10
    zwiedzanie = True
    print("przed toba jest 10 pokoji w kazdym moze cie czekac cos innego")
    while pokoje >0 and zwiedzanie:
        print(f"pozostalo {pokoje} pokoji do eksploracji")
        wydarzenie = choice(["skarb","elixir","przeciwnik","pulapka","npc","nic"])
        if wydarzenie == "skarb":
            print("-"*20)
            znalezione_gold_=randint(10,30)
            gold += znalezione_gold_
            print(f"=== znalazles {znalezione_gold_} zlota === ")
        elif wydarzenie == "elixir":
            print("-"*20)
            elixir_typ = choice(["zycia","many","elixir"])
            if elixir_typ == "zycia":
                hp = randint(10,20)
                life += hp
                print(f" === znalazles elixir zycia, dostajesz {hp} zycia === ")
            elif elixir_typ == "many":
                dodana_mana = randint(10,20)
                mana += dodana_mana
                print(f" === znalazles elixir many, dostajesz {dodana_mana} many === ")
            elif elixir_typ == "elixir":
                elixir += 1 
                print(f" === dostales 1 elixir === ")
        elif wydarzenie == "przeciwnik":
            print("-"*20)
            print("musisz stoczyc walke")
            print("-"*20)
            przeciwnik = ["zombie",30,5,0]
            print(f" === spotkales przeciwnika {przeciwnik[0]} === ")
            while przeciwnik [1] >0 and life >0:
                print(f"przeciwnik ma {przeciwnik[1]} zycia, zadaje ci {przeciwnik[2]} obrazen")
                life -= przeciwnik[2]
                if life <= 0:
                    print("UMARLES")
                    zwiedzanie = False
                    break
                atak = walka_eksploracja()
                przeciwnik[1] -= atak
                print(f"zdales {atak} obrazen przeciwnikowi")
            if przeciwnik[1]<=0:
                print(f" === pokonales przeciwnika, dostajesz 5 golda === ")
                gold += 5 
        elif wydarzenie == "pulapka":
            print("-"*20)
            obrazenia =randint (5,15)
            life -= obrazenia
            print(f"wpadles w pulapke, tracisz {obrazenia} zycia")
            if life <= 0:
                    print("UMARLES")
                    zwiedzanie = False
                    break
        elif wydarzenie == "npc":
            print("-"*20)
            print(f" === spotykazsz tajemnicza osobe === ")
            npc_typ = choice (["pomoc","handel"])
            if npc_typ == "pomoc":
                print("dostales pomoc, odzyskujesz 20 zycia i 20 many")
                life += 20
                mana += 20
            elif npc_typ == "handel":
                print("dostajesz oferte aby kupic elixir za 20 golda")
                if gold >= 20:
                    wybor = input("czy chcesz kupic elixir?(1-tak/2-nie)")
                    if wybor == "1": 
                        gold -= 20
                        elixir += 1
                        print("kupiles elixir")
                    if wybor == "2":
                        print("odrzucasz oferte")
                    else:
                       print("nieprawidlowy wybor") 
                else:
                    print("nie masz wystarczajaca golda aby kupic elixir")
        else:
            print("nic tutaj sie nie znajduje, pokoj jest pusty")
        pokoje -= 1
        if pokoje >0:
            kontynuacje = input("czy chcesz eksplorowac dalej? (1-tak/2-nie) ")
            if kontynuacje != "1":
                print("koniec eksploracji")
                print(f"masz {life} zycia, {mana} many, {gold} golda, {elixir} elixirow")
                zwiedzanie = False
    
