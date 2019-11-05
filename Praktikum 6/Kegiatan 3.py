Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Fadhlih Hasan Setiawan'
>>> NIM = "L200194209"
>>> X = "1" + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # Because the "X" data had changed to integer data type.
>>> type(b)
<class 'int'>
>>> # Because the "Nama" data Has a "len" instruction.
>>> a / b
54.95454545454545
>>> # Because the result of 1209 divided by 22 is 54.95454545454545 (integer divided by integer the result is float)
>>> a // b
54
>>> # Because the meaning of "//" is division with rounding down. integer divided with rounding down by integer the result is integer.
>>> 10 * (a - 999)
2100
>>> # Because the value of "a" minus 999 is 210, after that it will multiplied by 10 and the result is 2100.
>>> b ** 2
484
>>> # Because the value of "b" squared 2 is 484.
>>> a % b
21
>>> # Because the remainder of division the value "a" and "b" is 21.
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> # Because data type of the value "c" is 12.5 ; 12.5 is a float data type.
>>> a / c
96.72
>>> # Because the result of the value of "a" divided by the value of "c" is 96.72  (integer divided by float the result is float)
>>> a // c
96.0
>>> # Because the meaning of "//" is division with rounding down.  integer divided with rounding down by float the result is float.
>>> a % c
9.0
>>> # Because the remainder of division the value "a" and "b" is 9.0
>>> c > b
False
>>> # Because the value of "c" less than the value of "b"
>>> type(c > b)
<class 'bool'>
>>> # Because the value "c" more than "b" is False. False is a bool data type
>>> a > b and b > c
True
>>> # Because the value "a" more than  "b" is True and the value "b" more than "c" is True. So the result is True   
>>> a > 1100 or b < 10
True
>>> # Because the value "a" more than 1100 is True or the value "b" less than 10 is False. So the result is True
