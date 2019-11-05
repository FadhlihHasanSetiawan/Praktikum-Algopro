Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = "Fadhlih Hasan Setiawan"
>>> NIM = 209
>>> Tinggi = 1.73
>>> Berat = 44
>>> TahunLahir = 2001
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # Because the "Aku" is written in parentheses
>>> Aku[0]
2001
>>> # Because the first object in "Aku" data is "TahunLahir", The value of "TahunLahir" is 2001
>>> a = NIM % 4; Aku[a]
44
>>> # Because the remaining result of 209 divided by 4 is 1, so the result of Aku[1] is 44
>>> type(Aku[a])
<class 'int'>
>>> # Because the value of "Berat" is 44, 44 is an integer data type 
>>> Aku[a:4]
(44, 1.73, 209)
>>> # Because we show data in tuple from index 1 until index 3
>>> type(Aku[4])
<class 'str'>
>>> # Because the value of "Nama" is "Fadhlih Hasan Setiawan". "Fadhlih Hasan Setiawan" is a string data type
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> # Because data in tuple cannot be changed
>>> type(Data)
<class 'list'>
>>> # Because the value of Data is [TahunLahir, Berat, Tinggi, NIM, Nama]. [TahunLahir, Berat, Tinggi, NIM, Nama] is list data type 
>>> type(Data[4])
<class 'str'>
>>> # Because the value of "Nama" is "Fadhlih Hasan Setiawan". "Fadhlih Hasan Setiawan" is a string data type 
>>> Data[4][5]
'i'
>>> # Because the value of "Nama" is Fadhlih Hasan Setiawan.letters in index 5 of 'Fadhlih Hasan Setiawan' is 'i'
>>> Data[4][a:6]
'adhli'
>>> # Because the value of "Nama" is Fadhlih Hasan Setiawan. letters from index 1 until index 5 of 'Fadhlih Hasan Setiawan' is 'adhli'
>>> Data[0]= 'ok'; Data
['ok', 44, 1.73, 209, 'Fadhlih Hasan Setiawan']
>>> # Because in list, the value of "Data[0]" can be changed with 'ok'
>>> Data[-a]
'Fadhlih Hasan Setiawan'
>>> # Because the result of Data[-1] is 'Fadhlih Hasan Setiawan'
>>> range(a)
range(0, 1)
>>> # Because the result of range(1) is range(0, 1)
