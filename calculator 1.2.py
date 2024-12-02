# making a functioning calculator application
from tkinter import Tk, Frame, Button, Label, RIDGE

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("615x695+410+110")
        self.root.config(bg="Lavender Blush2")

        self.mainframe = Frame(self.root, bd=18, width=600, height=700, relief=RIDGE, bg="PaleGreen4")
        self.mainframe.grid()
        self.widgetframe = Frame(self.mainframe, bd=18, width=590, height=660, relief=RIDGE, bg="Lavender Blush2")
        self.widgetframe.grid()

        self.lblDisplay = Label(self.widgetframe, width=30, height=2, bg="white", font=("arial", 20, "bold"), anchor="e")
        self.lblDisplay.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.input_button = ""

        # Row 1
        self.create_button("←", 1, 0, self.backspace)
        self.create_button("CE", 1, 1, self.clear_entry)
        self.create_button("C", 1, 2, self.clear_all)
        self.create_button("±", 1, 3, self.change_sign)

        # Row 2
        self.create_button("7", 2, 0, lambda: self.add_input("7"))
        self.create_button("8", 2, 1, lambda: self.add_input("8"))
        self.create_button("9", 2, 2, lambda: self.add_input("9"))
        self.create_button("+", 2, 3, lambda: self.add_input("+"))

        # Row 3
        self.create_button("4", 3, 0, lambda: self.add_input("4"))
        self.create_button("5", 3, 1, lambda: self.add_input("5"))
        self.create_button("6", 3, 2, lambda: self.add_input("6"))
        self.create_button("-", 3, 3, lambda: self.add_input("-"))

        # Row 4
        self.create_button("1", 4, 0, lambda: self.add_input("1"))
        self.create_button("2", 4, 1, lambda: self.add_input("2"))
        self.create_button("3", 4, 2, lambda: self.add_input("3"))
        self.create_button("*", 4, 3, lambda: self.add_input("*"))

        # Row 5
        self.create_button("0", 5, 0, lambda: self.add_input("0"))
        self.create_button(".", 5, 1, lambda: self.add_input("."))
        self.create_button("=", 5, 2, self.calculate_result)
        self.create_button("/", 5, 3, lambda: self.add_input("/"))

    def create_button(self, text, row, column, command):
        button_widget = Button(
            self.widgetframe,
            text=text,
            width=6,
            height=2,
            bd=4,
            bg="Lavender Blush2",
            font=("arial", 20, "bold"),
            command=command,
        )
        button_widget.grid(row=row, column=column, padx=5, pady=5)

    def add_input(self, value):
        self.input_button += value
        self.lblDisplay.config(text=self.input_button)

    def backspace(self):
        self.input_button = self.input_button[:-1]
        self.lblDisplay.config(text=self.input_button)

    def clear_entry(self):
        self.input_button = ""
        self.lblDisplay.config(text=self.input_button)

    def clear_all(self):
        self.clear_entry()

    def change_sign(self):
        if self.input_button:
            if self.input_button.startswith("-"):
                self.input_button = self.input_button[1:]
            else:
                self.input_button = "-" + self.input_button
        self.lblDisplay.config(text=self.input_button)

    def calculate_result(self):
        try:
            result = str(eval(self.input_button))
            self.lblDisplay.config(text=result)
            self.input_button = result
        except Exception as e:
            self.lblDisplay.config(text="Error")
            self.input_button = ""

root = Tk()
app = Calculator(root)
root.mainloop()

