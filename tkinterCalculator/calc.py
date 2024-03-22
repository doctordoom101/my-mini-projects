import tkinter as tk

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("350x450")
        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display the result
        result_entry = tk.Entry(self, textvariable=self.result_var, font=("Times New Roman", 20), bd=10, insertwidth=4, width=15, justify='right')
        result_entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, font=("Times New Roman", 20), padx=20, pady=20, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
        elif char == "C":
            self.result_var.set("0")
        else:
            current_text = self.result_var.get()
            if current_text == "0":
                self.result_var.set(char)
            else:
                self.result_var.set(current_text + char)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
