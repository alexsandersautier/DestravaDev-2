from tkinter import *
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend import server
from tkinter.messagebox import showinfo, showerror

value = ""
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def calculate():
    global value 
    if size.get() != '' and heigth.get() != '':
        value = server.calculate(size.get(), heigth.get())
        showinfo("Info", "Calculo efetuado")
    else:
        showerror("Alerta", "Verifique os valores.. Precisa ser maior que 0")

def show_categories():
    message = ""
    categories = [
        {
            "description": "Muito abaixo do peso",
            "value": "Abaixo de 17"
        },
        {
            "description": "Abaixo do peso",
            "value": "Entre 17 e 18,5"
        },
        {
            "description": "Peso Normal",
            "value": "Entre 18,5 e 24,9"
        },
        {
            "description": "Acima do peso",
            "value": "Entre 25 e 29,9"
        },
        {
            "description": "Obesidade I",
            "value": "Entre 30 e 34,9"
        },
        {
            "description": "Obesidade II (severa)",
            "value": "Entre 35 e 39,9"
        },
        {
            "description": "Obesidade III (mórbida)",
            "value": "Acima de 40"
        },
    ]
    for i in categories:
        message += f"{i['description']} = {i['value']}\n"

    showinfo("Categorias", message)

def show_result():
    if value == '':
        showerror("Alerta", "Verifique os valores.. Precisa ser maior que 0")
        return 
    elif float(value) < 25:
        color = "GREEN"
    elif float(value) < 35:
        color = "#8B8000"
    else:
        color = "RED"

    label_info = Label(window, text=f"IMC = {value}", font=("Arial", 16), fg=color)
    label_info.grid(column=1, row=5)

window = Tk()
window.title("Calculadora IMC")
window.geometry("300x250")

text = Label(window, text="Peso(kg):")
text.grid(column=0, row=0)
size = Entry(window, width=20)
size.grid(column=1, row=0)

text = Label(window, text="Altura(m²):")
text.grid(column=0, row=1)
heigth = Entry(window, width=20)
heigth.grid(column=1, row=1)

btn_cal = Button(window, text="Calcular", command=calculate)
btn_cal.grid(column=0, row=2)

btn_result = Button(window, text="Resultado", command=show_result)
btn_result.grid(column=1, row=2)

btn_show_categories = Button(window, text="Categorias", command=show_categories)
btn_show_categories.grid(column=2, row=2)


center_window(window)
window.mainloop()