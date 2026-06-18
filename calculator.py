import tkinter
import math

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)
column_count = len(button_values[0])

color_black = "#000000"
color_grey = "#A3A3A3"
color_dark_grey = "#777777"
color_white = "#F4F4F4"

#window setup
window = tkinter.Tk()
window.title("Calculator")
window.resizable(False,False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text = "0", font = ("Segoe UI Light", 45), background = color_dark_grey, foreground = color_white,
                      anchor = "e", width = column_count)

label.grid(row =0, column = 0, columnspan = column_count, sticky = "we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text = value, font = ("Segoe UI Light", 25), width = column_count , height = 1,
                                command = lambda Value = value: button_clicked(Value))
        
        if value in top_symbols:
            button.config(foreground = color_black, background = color_dark_grey)
        elif value in right_symbols:
            button.config(foreground = color_white, background = color_black)  
        else:
            button.config(foreground = color_black, background = color_grey)    

        button.grid(row = row + 1, column = column)

frame.pack()

# A+B, A-B, A*B, A/B
A = "0"
operator = None
B = None

def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
    return f"{num:.6f}".rstrip("0").rstrip(".")    

def button_clicked(Value):
    global right_symbols, label, top_symbols, A, B, operator

    if Value in right_symbols:
        if Value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                            label["text"] = remove_zero_decimal(numA + numB)

                elif operator == "-":
                            label["text"] = remove_zero_decimal(numA - numB)

                elif operator == "×":
                            label["text"] = remove_zero_decimal(numA * numB)

                elif operator == "÷":
                            label["text"] = remove_zero_decimal(numA / numB)

                clear_all()            
        
        elif Value in "+-×÷":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0" 
            operator = Value 

    elif Value in top_symbols:
        if Value == "AC":
            clear_all()
            label["text"] = "0"

        elif Value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        elif Value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

    else:
        if Value == ".":
            if Value not in label["text"]:
                label["text"] += Value

        elif Value in "0123456789":
            if label["text"] == "0":
                label["text"] = Value   #replace 0

            else:
                label["text"] += Value  #append digit   

        elif Value in "√":
              number = float(label["text"])

              if number >= 0:
                result = math.sqrt(number)
                label["text"] = f"{result:.1f}".rstrip("0").rstrip(".")
              else:
                label["text"] = "Error"
        
#center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


window.mainloop()