fibonacci = int(input("Masukkan jumlah Fibonacci yang diinginkan: "))

angka1 = 0
angka2 = 1

print("Deret Fibonacci:")
while angka1 < fibonacci:
    print(angka1)
    angka_lanjut = angka1 + angka2
    angka1 = angka2
    angka2 = angka_lanjut