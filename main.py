import tkinter as tk

def on_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")
root.resizable(False, False)


entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    
    for btn in row:
        if btn == "=":
            button = tk.Button(frame, text=btn, font=("Arial", 14),
                               command=calculate)
        else:
            button = tk.Button(frame, text=btn, font=("Arial", 14),
                               command=lambda b=btn: on_click(b))
        
        button.pack(side="left", expand=True, fill="both")

clear_btn = tk.Button(root, text="Clear", font=("Arial", 14), command=clear)
clear_btn.pack(fill="both", padx=10, pady=5)

root.mainloop()