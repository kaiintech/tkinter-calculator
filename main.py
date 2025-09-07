import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.config(bg="#2c5364")
root.geometry("350x500")
root.resizable(False, False)

current_input = ""
just_evaluated = False  

def click(value):
    global current_input, just_evaluated

    if value.isdigit() or value == ".":
        if just_evaluated:
            current_input = ""
            just_evaluated = False
        current_input += value
        display.delete(0, tk.END)
        display.insert(0, current_input)
    elif value in ["+", "-", "/", "*"]:
        if current_input == "":
            return
        current_input += value
        display.delete(0, tk.END)
        display.insert(0, current_input)
        just_evaluated = False
    elif value == "=":
        try:
            result = eval(current_input)
            display.delete(0, tk.END)
            display.insert(0, str(result))
            current_input = str(result)
            just_evaluated = True
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
            current_input = ""
            just_evaluated = False
    elif value == "C":
        current_input = ""
        display.delete(0, tk.END)
        just_evaluated = False

    elif value == "DEL":
        current_input = current_input[:-1]
        display.delete(0, tk.END)
        display.insert(0, current_input)
        just_evaluated = False

display = tk.Entry(root, font=("Arial", 20), bd=8, relief="ridge",
                   bg="#111", fg="white", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("DEL", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("+", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    (".", 4, 0), ("0", 4, 1), ("=", 4, 2), ("x", 4, 3),
    ("C", 5, 0), ("/", 5, 1)
]

def create_button(text, row, col):
    action = "*" if text == "x" else text
    def handler():
        click(action)
    b = tk.Button(root, text=text, width=5, height=2,
                  font=("Arial", 16),
                  bg="black", fg="aqua",
                  activebackground="#999",
                  highlightbackground="aqua",
                  highlightthickness=2,
                  bd=0,
                  command=handler)
    b.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

for (text, row, col) in buttons:
    create_button(text, row, col)

root.mainloop()