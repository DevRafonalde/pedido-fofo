import os
import tkinter as tk
import turtle
from tkinter import *
import random

root = tk.Tk()
root.title("Aceitas?")
root.geometry("600x600")
root.configure(background="#ffc8dd")


def chamar():
    window = turtle.Screen()
    window.bgcolor("#ffc8dd")
    window.title("Te amo meu amor!")

    pen = turtle.Turtle()
    pen.color("red")
    pen.fillcolor("red")
    pen.pensize(3)
    pen.speed(10)

    pen.begin_fill()
    pen.left(140)
    pen.forward(224)
    for _ in range(200):
        pen.right(1)
        pen.forward(2)
    pen.left(120)
    for _ in range(200):
        pen.right(1)
        pen.forward(2)
    pen.forward(224)
    pen.end_fill()

    pen.up()
    pen.goto(0, -70)
    pen.down()
    pen.color("black")
    pen.write("Eu te amo meu amor, pizzazinha aqui em casa mais tarde?", align="center", font=("Arial", 16, "bold"))
    pastaUsuario = os.getenv('USERPROFILE')
    os.system('start ' + pastaUsuario + "\\Downloads\\Pedido\\aceitou.url")
    pen.hideturtle()
    turtle.done()


def moveBotao1(e):
    if abs(e.x - botao1.winfo_x()) < 50 and abs(e.y - botao1.winfo_y()) < 40:
        x = random.randint(0, root.winfo_width() - botao1.winfo_width())
        y = random.randint(0, root.winfo_width() - botao1.winfo_width())
        botao1.place(x=x, y=y)


def aceito():
    root.destroy()
    chamar()


def negado():
    botao1.destroy()


margem = Canvas(root, width=500, bg="#ffc8dd", height=100, bd=0, highlightthickness=0, relief="ridge")
margem.pack()

textId = Label(root, bg="#ffc8dd", text="Quer namorar comigo?", fg="#590d22", font=("Montserrat", 24, "bold"))
textId.pack()

botao1 = tk.Button(root, text="Não", bg="#ffb3c1", command=negado, relief=RIDGE, bd=3, font=("Montserrat", 8, "bold"))
botao1.pack()
root.bind("<Motion>", moveBotao1)

botao2 = tk.Button(root, text="Sim", bg="#ffb3c1", command=aceito, relief=RIDGE, bd=3, font=("Montserrat", 14, "bold"))
botao2.pack()

root.mainloop()
