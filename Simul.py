from tkinter import *
import Quiz


def Leggi_File():
    messaggio = False
    if nome_file.get():
        try:
            f.append(open(str(nome_file.get()), "r"))
            # risposte. Leggo dalla prima riga del file e inserisco COME INTERI nella lista "a"
            Quiz.a = list(map(int, f[0].readline().split(",")))

            j = 0
            for line in f[0]:
                if line is not "\n":
                    Quiz.q.append(line)
                    for i in range(4):
                        Quiz.options[j].append(
                            f[0].readline().replace("\n", ""))  #rimuovo \n finale di ogni riga delle opzioni
                    j += 1
                    Quiz.options.append([])

            f[0].close()
            Quiz.options.remove([])
            window.destroy()
        except FileNotFoundError:
            ris = "File non trovato"
            messaggio = True
    else:
        ris = "non hai inserito nessun file"
        messaggio = True
    if messaggio:
        widget = Text()
        widget.insert(END, ris)
        widget.grid(row=4, column=0)


"""schermata di ingresso: introduzione nome del file"""
window = Tk()
window.title("Simulatore_Quiz_by_Elle")
window.geometry("1000x500")
window.grid_columnconfigure(0, weight=1)

welcome = Label(window, text="Nome file delle domande: ")
welcome.grid(row=1, column=0, sticky="N")

nome_file = Entry()
nome_file.grid(row=2, column=0, sticky="N")

apri_button = Button(text="Inizia Simulazione", command=Leggi_File)
apri_button.grid(row=3, column=0, sticky="W")

f = []  # Can't find a better way to modify a variable by reference

if __name__ == '__main__':
    window.mainloop()



"""schermata delle domande"""
window = Tk()
window.title("Simulatore_Quiz_by_Elle")
window.geometry("1000x500")


app = Quiz.Quiz(window)

if __name__ == "__main__":
    window.mainloop()
