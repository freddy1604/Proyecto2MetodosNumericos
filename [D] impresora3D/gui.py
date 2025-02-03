import tkinter as tk
from tkinter import messagebox
from processing import start_printing

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menú Principal")
        self.root.geometry("400x300")
        self.root.configure(bg="blue")

        title_label = tk.Label(self.root, text="Menú Principal", font=("Arial", 24, "bold"), bg="blue", fg="white")
        title_label.pack(pady=20)

        tk.Label(self.root, text="Resolución de impresión (mm):", bg="blue", fg="white").pack()
        self.resolution_entry = tk.Entry(self.root)
        self.resolution_entry.pack()
        self.resolution_entry.insert(0, "0.5")

        tk.Button(self.root, text="Iniciar", command=self.start_program, font=("Arial", 14), bg="white", fg="black", width=15).pack(pady=10)
        tk.Button(self.root, text="Salir", command=self.exit_program, font=("Arial", 14), bg="white", fg="black", width=15).pack(pady=10)

    def start_program(self):
        resolution = float(self.resolution_entry.get())
        start_printing(resolution)

    def exit_program(self):
        self.root.quit()

    def run(self):
        self.root.mainloop()
