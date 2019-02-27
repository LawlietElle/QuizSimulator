from tkinter import *

a = []  # answers
q = []  # questions
options = [[]]
results = dict()


class Quiz:
    def __init__(self, master):
        self.opt_selected = IntVar()
        self.qn = 0
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        self.master = master

        # pulsantiera
        self.button = Button(master, text="Quick Exit", command=self.exit_btn)
        self.button.pack(side=BOTTOM)

        self.button = Button(master, text="Back", command=self.back_btn)
        self.button.pack(side=BOTTOM)

        self.button = Button(master, text="Next", command=self.next_btn)
        self.button.pack(side=BOTTOM)

    def create_q(self, master, qn):
        w = Label(master, text=q[qn])
        w.pack(side=TOP)
        return w

    def create_options(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="foo",
                              variable=self.opt_selected, value=b_val+1)
            b.append(btn)
            btn.pack(side=TOP, anchor="w")
            b_val = b_val + 1
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def check_q(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True
        return False

    def print_results(self):
        for i in range(len(q)):
            print("domanda ", i+1, "\n", q[i], "\nrisposta esatta:\n",
                  options[i][a[i]-1], "\nrisultato:", results[i], "\n\n\n")

    def back_btn(self):
        self.qn = self.qn - 1
        self.display_q(self.qn)
        results[self.qn] = "sbagliata"
        """
	se si torna indietro la risposta può essere modificata, quindi è settata a sbagliata ed eventualmente fosse selezionata l'opzione giusta
	il metodo di check la dà giusta
 	"""

    def next_btn(self):
        if self.check_q(self.qn):
            results[self.qn] = "corretta"
        else:
            results[self.qn] = "sbagliata"

        self.qn = self.qn + 1
        if self.qn >= len(q):
            self.print_results()
            self.master.destroy()
        else:
            self.display_q(self.qn)

    def exit_btn(self):
        for i in range(self.qn, len(q)):
            results[i] = "non data"

        self.print_results()
        self.master.destroy()
