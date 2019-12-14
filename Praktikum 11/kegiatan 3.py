from tkinter import *

my_app=Tk(className="Hitung Luas Bangun")

L1=Label(my_app, text="Bangun Prisma", font=('arial',30))
L1.grid(row=0, column=0)

L2=Label(my_app, text="Prisma (bahasa Inggris: prism) adalah bangun ruang tiga dimensi yang dibatasi oleh alas dan tutup identik berbentuk segi-n dan sisi-sisi tegak berbentuk persegi atau persegi panjang. \nPrisma segi-n memiliki n + 2 sisi, 3n rusuk dan 2n titik sudut. \nContohnya adalah atap rumah, tenda, bangku, lemari baju, kemasan snack, tempat tisu dan potongan kue.")
L2.grid(row=1, column=0)

L3=Label(my_app, text="Luas Alas :")
L3.grid(row=2, column=0)

num1 = StringVar()
E3=Entry(my_app,textvariable=num1)
E3.grid(row=2, column=1)

L4=Label(my_app, text="Keliling Alas :")
L4.grid(row=3, column=0)

num2 = StringVar()
E3=Entry(my_app,textvariable=num2)
E3.grid(row=3, column=1)

L5=Label(my_app, text="Tinggi :")
L5.grid(row=4, column=0)

num3 = StringVar()
E3=Entry(my_app,textvariable=num3)
E3.grid(row=4, column=1)
    
res = StringVar()
def wewe():
    hitung=2 * float(num1.get()) + float(num2.get()) * float(num3.get())
    res.set(hitung)
    if (hitung == int(hitung)):
        hitung = int(hitung)
    return hitung

B=Button(my_app, text="Hitung", command=wewe)
B.grid(row=6, column=0)

L6 = Label(my_app, text="Luas =")
L6.grid(row=7, column=0)

result = Entry(my_app,textvariable=res)
result.grid(row=7, column=1)

my_app.mainloop()
