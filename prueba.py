import os
import tkinter as tk
from tkinter import filedialog, messagebox

def start_program():
    messagebox.showinfo("Inicio", "El programa ha comenzado.")
    # Aquí puedes llamar a la función de procesamiento si es necesario

def exit_program():
    root.quit()

# Crear interfaz gráfica
root = tk.Tk()
root.title("Menú Principal")
root.geometry("400x300")
root.configure(bg="blue")

title_label = tk.Label(root, text="Menú Principal", font=("Arial", 24, "bold"), bg="blue", fg="white")
title_label.pack(pady=20)

tk.Button(root, text="Iniciar", command=start_program, font=("Arial", 14), bg="white", fg="black", width=15).pack(pady=10)
tk.Button(root, text="Salir", command=exit_program, font=("Arial", 14), bg="white", fg="black", width=15).pack(pady=10)

root.mainloop()