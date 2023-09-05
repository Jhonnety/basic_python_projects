import tkinter as tk

def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacion = operaciones.get()

        if operacion == "Suma":
            resultado.set(num1 + num2)
        elif operacion == "Resta":
            resultado.set(num1 - num2)
        elif operacion == "Multiplicación":
            resultado.set(num1 * num2)
        elif operacion == "Exponente":
            resultado.set(num1 ** num2)
        elif operacion == "División":
            if num2 != 0:
                resultado.set(num1 / num2)
            else:
                resultado.set("Error: División por cero")
        elif operacion == "División Entera":
            if num2 != 0:
                resultado.set(num1 // num2)
            else:
                resultado.set("Error: División por cero")
        elif operacion == "Modulo":
            resultado.set(num1 % num2)
    except ValueError:
        resultado.set("Error: Entradas inválidas")
"""         lbl_resultado.config(font=("Arial", 24, "bold")) """

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.config(padx=20, pady=20)
ventana.title("Calculadora mini")
ventana.config(background="#C7EACA")

num1 = tk.StringVar()
num2 = tk.StringVar()
resultado = tk.StringVar()

lbl_num1 = tk.Label(ventana, text="Calculadora mini!",foreground="#204F6F" ,font=("Arial", 16, "bold"), background="#C7EACA")
lbl_num1.grid(column=0, row=0, pady=20)

lbl_num1 = tk.Label(ventana, text="Número 1:",foreground="#204F6F", background="#C7EACA", font=("Arial", 12, "bold"))
lbl_num1.grid(column=0, row=1)
entry_num1 = tk.Entry(ventana, textvariable=num1)
entry_num1.grid(column=0, row=2)

lbl_num2 = tk.Label(ventana, text="Número 2:",foreground="#204F6F", background="#C7EACA", font=("Arial", 12, "bold"))
lbl_num2.grid(column=0, row=3)
entry_num2 = tk.Entry(ventana, textvariable=num2)
entry_num2.grid(column=0, row=4)

operaciones = tk.StringVar()
operaciones.set("Suma")
menu_operaciones = tk.OptionMenu(ventana ,operaciones, "Suma", "Resta", "Multiplicación", "Exponente", "División", "División Entera", "Modulo")
menu_operaciones.grid(column=0, row=5, padx=10, pady=10)
menu_operaciones.config(background="#339798", foreground="white",  font=("Arial", 10, "bold"))

btn_calcular = tk.Button(ventana, text="Calcular", command=calcular)
btn_calcular.grid(column=0, row=6)
btn_calcular.config(background="#339798", foreground="white",  font=("Arial", 10, "bold"))

lbl_resultado = tk.Label(ventana, textvariable=resultado, foreground="#204F6F", background="#C7EACA", font=("Arial", 12, "bold"))
lbl_resultado.grid(column=0, row=7, pady=20)

ventana.mainloop()
