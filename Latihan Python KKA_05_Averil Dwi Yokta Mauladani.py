import math

print("Nama : Averil Dwi Yokta Mauladani \nAbsen : 05\nKelas : XI RPL 2\n")

print("Soal no 1")
integer = 1
float = 1.1
string = "Averil"
listt = [1,2,3]
print(type(integer))
print(type(float))
print(type(string))
print(type(listt))

print("\nSoal no 2")
listbelanja = ["beras", "minyak", "telur"]
listbelanja.extend(["gula", "kopi"])
print('Daftar Belanja')
for i in range(5):
    print(listbelanja[i])
    
print("\nSoal no 3")
belanjaan = {
    "beras" : 12000,
    "minyak" : 17000,
    "telur" : 24000,
    "gula" : 15000,
    "kopi" : 20000
}
total = sum(belanjaan.values())
print("Total belanja =",total)

print("\nSoal no 4")
radius = int(input("Jari-jari = "))
area = math.pi * radius * radius
circumference = 2*math.pi*radius

print("Luas =",area,"\nKeliling =",circumference)


