import random
from tkinter import *

class Game:
    def __init__(self) -> None:
        self.möglichkeiten = ["Schere", "Stein", "Papier"]
        self.choose = ""
        self.myChoose = ""
        self.winner = ""

        self.Gui = Tk()
        self.Gui.geometry("360x190")

        self.label3 = Label(master=self.Gui, text = self.winner)
        self.label3.place(x=20, y=120, height=50, width=320)

        self.schere = Button(master=self.Gui,text="Schere", command=self.comSchere)
        self.stein = Button(master=self.Gui,text="Stein",command=self.comStein)
        self.papier = Button(master=self.Gui,text="Papier",command=self.comPapier)

        self.schere.place(x=20,y=50,width=100,height=50)
        self.stein.place(x=130,y=50,width=100,height=50)
        self.papier.place(x=240,y=50,width=100,height=50)
    
    def run(self):
        self.Gui.mainloop()

    def chooseComputer(self):
        self.choose = self.möglichkeiten[random.randint(0,2)]

    def comSchere(self):
        print("schere")
        self.Winner("Schere")
    
    def comStein(self):
        print("stein")
        self.Winner("Stein")
    
    def comPapier(self):
        print("papier")
        self.Winner("Papier")

    def Winner(self, myChoose):
        self.chooseComputer()
        print(self.choose)
        print(myChoose)
        #Unentschieden
        if myChoose == "Schere" and self.choose == "Schere":
            self.winner = f"Unentschieden, Nochmal!: {myChoose} | {self.choose}"
        elif myChoose == "Stein" and self.choose == "Stein":
            self.winner = f"Unentschieden, Nochmal!: {myChoose} | {self.choose}"   
        elif myChoose == "Papier" and self.choose == "Papier":
            self.winner = f"Unentschieden, Nochmal!: {myChoose} | {self.choose}"

        #Gewonnen
        elif myChoose == "Schere" and self.choose == "Papier":
            self.winner = f"Du hast gewonnen, herzlichen Glühstrumpf!: {myChoose} | {self.choose}"
        elif myChoose == "Stein" and self.choose == "Schere":
            self.winner = f"Du hast gewonnen, herzlichen Glühstrumpf!: {myChoose} | {self.choose}"
        elif myChoose == "Papier" and self.choose == "Stein":
            self.winner = f"Du hast gewonnen, herzlichen Glühstrumpf!: {myChoose} | {self.choose}"

        #Verloren
        elif myChoose == "Schere" and self.choose == "Stein":
            self.winner = f"Du hast leider Verloren, viel Glück beim nächsten mal!: {myChoose} | {self.choose}"

        elif myChoose == "Stein" and self.choose == "Papier":
            self.winner = f"Du hast leider Verloren, viel Glück beim nächsten mal!: {myChoose} | {self.choose}"

        elif myChoose == "Papier" and self.choose == "Schere":
            self.winner = f"Du hast leider Verloren, viel Glück beim nächsten mal!: {myChoose} | {self.choose}"

        self.label3.configure(text=self.winner)



SchniSchnaSchnu = Game()
SchniSchnaSchnu.run()