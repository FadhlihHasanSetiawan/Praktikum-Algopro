## Dibuat oleh Fadhlih L200194209
import random
angka = random.randint(0,1000)

Nama = 'Fadhlih Hasan Setiawan'
TanggalLahir = '6 Aprll 2001'
NamaSingkat = Nama[0] + '. ' + Nama[8] + '. ' + Nama[14:22]
Username = Nama[0] + TanggalLahir[0] + TanggalLahir[8:12]
Password = Nama[0:3] + str(angka)

print(Nama)
print(TanggalLahir)
print(NamaSingkat)
print(Username)
print(Password)
