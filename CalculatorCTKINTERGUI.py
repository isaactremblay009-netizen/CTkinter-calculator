import customtkinter as ctk

# Appearance and theme
ctk.set_appearance_mode("Dark")

# Create main window
app = ctk.CTk()
app.title("Isaac's basic arithmetic calculator")
app.geometry("565x525")


#display variable
display_text = ctk.StringVar(value="")

#Display box at top
display = ctk.CTkEntry(app,
                       textvariable=display_text,
                       width=520,
                       height=70,
                       font=("Arial", 32),
                       justify="right",
                       corner_radius=10)
display.pack(pady=(20, 10))  # Use pack so it's fixed at top

#button functions
def press(value):
    """Handles numbers and operators"""
    current = display_text.get()
    display_text.set(current + value)

def clear():
    """Clears the display"""
    display_text.set("")

def backspace():
    """Deletes the last character (safe)"""
    try:
        current = display_text.get()
        # If nothing to delete, just return (no error)
        if not current:
            return
        # Remove last character
        display_text.set(current[:-1])
    except Exception as e:
        # Failsafe
        display_text.set("Error")




def calculate():
    """Calculates the arithmetic calculator"""
    try:
        result = str(eval(display_text.get()))
        display_text.set(result)
    except Exception:
        display_text.set("Error....")


button_frame = ctk.CTkFrame(app, fg_color="transparent")
button_frame.pack(pady=10)

#Layout for the buttons
rows = [
    [("√", lambda: press("**0.5")), ("⌫", backspace), ("𝑥ˣ", lambda: press("**")), ("¹⁄𝑥", lambda: press("1/("))],
    [("7", lambda: press("7")), ("8", lambda: press("8")), ("9", lambda: press("9")), ("÷", lambda: press("÷"))],
    [("4", lambda: press("4")), ("5", lambda: press("5")), ("6", lambda: press("6")), ("+", lambda: press("+"))],
    [("1", lambda: press("1")), ("2", lambda: press("2")), ("3", lambda: press("3")), ("×", lambda: press("×"))],
    [("0", lambda: press("0")), (".", lambda: press(".")), ("=", calculate), ("-", lambda: press("-"))],
]
#Buttons to go on the grid layout above
for r, row in enumerate(rows):
    for c, (text, cmd) in enumerate(row):
        button = (ctk.CTkButton(button_frame, font= ("arial", 24), text=text, fg_color="#3B3B3B", width = 120, height=60, command=cmd))
        button.grid(row=r, column=c, padx=10, pady=10)
#Clear button
clear_button = ctk.CTkButton(app, text="C",font=("Arial", 24),
                             fg_color="#B33A3A",
                             width=520,
                             height=50,
                             command=clear)
# Main loop
app.mainloop()
