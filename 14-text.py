import tkinter
canvas=tkinter.Canvas(width = 600, height = 400)
canvas.pack()

y=10
for i in range(10,30,2):
    canvas.create_text(300, y, text = 'ABCDEFGHIJ abcdefghij', font= ('Times New Roman',i))
    y+=i*2
