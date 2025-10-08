import random
class Sportfrågor:
    def fråga1():
        print("Fråga : Vilket land har vunnit flest VM-guld i fotboll (herr)?")
        print("A) Brasilien")
        print("B) Tyskland")
        print("C) Italien\n")
        fotboll = input().lower()
        if fotboll =="a":
            print("rätt svar du får 1 poäng")
        else:
            print("du förtjanar inge poäng")
    def fråga2(): 
        print("Fråga : Hur många spelare finns på plan i ett basketlag samtidigt (per lag)?")
        print("A) 5")
        print("B) 6")
        print("C) 7\n")
        basket = input().lower()
        if basket =="a":
         print("WoW very amazing ett till poäng")
        else:
            print("HA sämst")
    def fråga3():
        print("Fråga : Vilken svensk tennisspelare vann Wimbledon fem år i rad under 1970-talet?")
        print("A) Stefan Edberg")
        print("B) Björn Borg")
        print("C) Mats Wilander\n")
        tennis = input()
        if tennis =="b":
            print("coolt ett till poäng")
        else:
            print("you are not him")
    def fråga4():        
        print("Fråga : Vilken sport kallas ibland 'den vita sporten'?")
        print("A) Tennis")
        print("B) Golf")
        print("C) Cricket\n")
        vit = input()
        if vit == "a":
            print("här är din belöning + 1 poäng")
        else:
            print("du får inge poäng")
    def fråga5():        
        print("Fråga : I vilken idrott kan man vinna Stanley Cup?")
        print("A) Ishockey")
        print("B) Fotboll")
        print("C) Baseball\n")
        hockey = input()
        if hockey =="a":
            print("i seeeee u dawg här ta ett till poäng +1")
        else:
            print("HAHAHA du får inge poäng")
    def fråga6():        
        print("Fråga : Vilket år arrangerade Sverige sommar-OS i Stockholm?")
        print("A) 1912")
        print("B) 1932")
        print("C) 1956\n")
        os = input()
        if os == "a":
            print("Global Elite? ett plus poäng")
        else:
            print("DEEEZZZ nuts inge poäng till dig") 
    def fråga7():
        print("Fråga : Hur lång är en maratonlöpning?")
        print("A) 32 km")
        print("B) 40 km")
        print("C) 42 km\n")
        maraton = input()
        if maraton == "c":
            print("Kevin utmanar dig att springa ett maraton så får du ett till poäng")
        else:
            print("som straff att du svara fel ska du springa 42km")
    def fråga8():        
        print("Fråga : Vilken svensk längdskidåkare kallas ofta 'Gunde'?")
        print("A) Gunde Svan")
        print("B) Thomas Wassberg")
        print("C) Sixten Jernberg\n")
        längdskidor = input()
        if längdskidor =="a":
            print("ett till poäng =)")
        else:
            print("=( inge poäng")
    def fråga9():        
        print("Fråga : Vilken sport utövar man i Wimbledon?")
        print("A) Rugby")
        print("B) Tennis")
        print("C) Cykling\n")
        sport = input()
        if sport =="b":
            print("ett till poäng")
        else:
            print(" no poäng till you")
    def fråga10():        
        print("Fråga : Vilket djur är symbol för den spanska sporten tjurfäktning?")
        print("A) Häst")
        print("B) Tjur")
        print("C) Hund\n")
        djur = input()
        if djur =="b":
            print("+1 poäng")
        else:
            print("inge poäng 0")

    alla_frågor = [fråga1, fråga2, fråga3, fråga4, fråga5, fråga6, fråga7, fråga8, fråga9, fråga10]
    while True:
        random.choice(alla_frågor)()


