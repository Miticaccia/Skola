import tkinter as tk
import random

def zobrazenie_textu():
    farba = random.randint(0,7)
    x = random.randint(100, 500)
    y = random.randint(100, 500)
    canvas.delete("maturitka") 
    canvas.create_text(x, y, text="Maturita 2024", fill='#'+str(farba)+str(farba)+str(farba), font=("Arial", 30, "bold"), tag="maturitka")
    root.after(1000, odstranenie_textu)
    
def odstranenie_textu():
    canvas.delete("maturitka")
    if running:
        zobrazenie_textu()  

def stlacena_klavesa(event):
    global running
    running = False
    root.destroy()

root = tk.Tk()
root.geometry("600x600")
root.title("Maturita 2024")


canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

running = True
root.bind("<Key>", stlacena_klavesa)

zobrazenie_textu()
root.mainloop()
