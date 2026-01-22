name = "Febrian satya rabbani"
print(name)
age = 17
print(age)
x = 9
y = 3
print(type(x/y))

for i in range(5):
    print("hello")

for i in range(10):
    print(i)

print(type(5 < 9))
print(type(50 > 100))
print(type(True))
print(type(False))

# catatan logika, and dan or 
print(True and True)
print(True and False)
print(True or True)
print(True or False)

# True and False
# True or True
# True or False
# perbanddingan atau comparison selalu bernilai boolean 

ac_on = 35
print(ac_on > 30)

presence = 1
print(presence > False)

temp = 24
unit = "°C"
print(str(temp) + unit)

count = 100
while count < 10:
    print("sells ticket")
    count = count - 1

word = ["run", "food"]
word[0] = "f"
print(word)

brands = ["Honda", "Toyota", "BMW", "Mercedes"]
print(brands[1 : 3])
print(brands[-3 : -1])

c = ['a', 'b', 'c', 'd']
print(c[1])
print(c[-1])
print(c[-3 : -1])


products = ['milk', 'apple', 'noodle']
print('bread' in products) #the output is false
kata = "bolo"
print("o" in kata)
for i in products:
    print(i)
print()

nama = ['bryan', 'ryan', 'loki','john']
for i in nama:
    print("Selamat datang " + i)

merek = ["avanza", "honda", "bmw"]
warna = ["merah", "biru", "hitam"]

for mobil in merek:
    for color in warna:
        print(mobil, color)
print()

colors  = ['red', 'blue']
vehicles = ['car', 'bike']
for vehicle in vehicles:
    for color in colors:
        print(color, vehicle)
print()

days = ['Monday', 'Tuesday', 'Wednesday']
tasks = ['Gym', 'Homework', 'Pool']
for day in days:
    print(day + ':')
    for task in tasks:
        print(task)
print()

for i in range(1,3):
    for j in range(2,4):
        print(i,j)
print()

moves = ["step out", "nigga", "fozy"]

for move in moves:
    for i in range(3):
        print(move)
print()

nilai_ujian = [50, 66, 69, 76, 77, 89, 90]
for score in nilai_ujian:
    if score >= 70:
        print(score)
print()

# countries = ['Canada', 'US', 'INA', 'IND']
# counter = 0
# for i in countries:
#     if i == 'US':
#         counter+=1

message = "kamu dapat notif terbaru"
count = 0
for i in message:
    if i == 'a':
        count += 1
print(count) 
#ngintungin berapa banyak huruf itu keluar dalam satu kalimat
print()

angka_ajah = [7, 5, 9, 6, 2]
total = 0
for i in angka_ajah:
    total+=i
print("total: ", total)
print()

# sold = 20
# while sold >= 0:
#     for i in range(sold):
#         print(i, "ticket terjual: ")
#     sold -= 1

# hari = ["sabtu", "jumat", "minggu", "senin"]
# hari= input(str("Mencari hari apa: "))
# for i in hari:
#     print("Mencari...")
#     if i == "sabtu":
#         print("Ini hari ", i)
#         break
#     elif i == "minggu":
#         print("ini hari minggu", i)
#         break
#     elif i == "senin":
#         print("ini hari senin" , i)
#         break
#     elif i == "jumat":
#         print("ini hari jumat" , i)
#         break
prices = [30, 10, 30, 23, 15, 4, 11]
total = 0
# for price in prices:
#     if price > 90:
#         break
#     print(price)
# print()

for price in prices:
    total+=price
    print(total)
    if total > 100:
        print("Limit")
        break
print()

p = 1
while p < 10:
    print(p)
    if p ==5:
        print("Stop")
        break
    p+=1
print()
# while True:
#     text =  input()
#     print(text)
#     if text == 'Stop':
#         break
# print()

umur_manusia = [10, 20, 30, 40, 50, 60, 70]
for po in umur_manusia:
    if po < 30:
        continue
    print(po)
print()

binatang = ["kucing", "anjing", "jerapah", "singa"]
for hewan in binatang:
    if hewan[0] == 'a':
        continue
    print(hewan)
