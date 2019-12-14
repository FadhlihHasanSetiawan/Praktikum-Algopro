from tkinter import Tk, Label, Button

my_app=Tk(className="Data Diri")

L0=Label(my_app, text="Data Diri", font=('arial',30))
L0.grid(row=0, column=0)

L1=Label(my_app, text="Nama")
L1.grid(row=1, column=0)

E1=Label(my_app, text="Fadhlih Hasan Setiawan")
E1.grid(row=1, column=1)

L2=Label(my_app, text="NIM")
L2.grid(row=2, column=0)

E2=Label(my_app, text="L200194209")
E2.grid(row=2, column=1)

L3=Label(my_app, text="Buku Favorit")
L3.grid(row=3, column=0)

E3=Label(my_app, text="Bob Sadino : Goblok Pangkal Kaya")
E3.grid(row=3, column=1)

L4=Label(my_app, text="Idola di kalangan sahabat")
L4.grid(row=4, column=0)

E4=Label(my_app, text="Diwantara Anugrah Putra")
E4.grid(row=4, column=1)

L5=Label(my_app, text="Motto")
L5.grid(row=5, column=0)

E5=Label(my_app, text="Percayalah.. Aku bisa.. Kamu bisa.. Kita bisa..")
E5.grid(row=5, column=1)

B=Button(my_app, text="Tutup", command=my_app.destroy)
B.grid(row=6, column=0)
