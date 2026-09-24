number1 = int(input("Masukkan angka pertama: "))
number2 = int(input("Masukkan angka kedua: "))
number3 = int(input("Masukkan angka ketiga: "))

if number1 >= number2 and number1 >= number3:
    print("Angka terbesar adalah:", number1)
elif number2 >= number1 and number2 >= number3:
    print("Angka terbesar adalah:", number2)
else:
    print("Angka terbesar adalah:", number3)