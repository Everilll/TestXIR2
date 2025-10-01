import time

number = int(input("\nInput number to check the number is Even or Odd: "))

def genapganjil(number):
    if number % 2 == 0:
        return "The number is Even"
    else:
        return "The number is Odd"
    
time.sleep(0.5)
print(genapganjil(number))

time.sleep(1)

angka = int(input("\nInput number to check if it is Positive/Negative/Zero: "))

def positivenegative(angka):
    if angka > 0:
        return "The number is Positive"
    if angka < 0:
        return "The number is Negative"
    if angka == 0:
        return "The number is Zero"
    else:
        return "Error"
    
time.sleep(0.5)
print(positivenegative(angka))

time.sleep(1)

str1 = input("\nString 1: ")
str2 = input("String 2: ")

def anagrams(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
    
time.sleep(0.5)
print(anagrams(str1, str2))

time.sleep(1)

numero = int(input("\nFactorial of: "))

def factorial(numero):
    result = 1
    for i in range(1, numero+1):
        result *= i
    return result
    
time.sleep(0.5)
print(factorial(numero))

time.sleep(1)

text = input("\nInput text to check if it is Palindrome or not: ")

def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False
    
time.sleep(0.5)
print(palindrome(text))

time.sleep(1)

num = int(input("\nInput number to check if it is Armstrong or not: "))

def armstrong(num):
    digits = str(num)
    mdigits = len(digits)
    total = 0
    
    for i in digits:
        total += int(i) ** mdigits
    
    if total == num:
        return True
    else:
        return False

time.sleep(0.5)
print(armstrong(num))

time.sleep(1)

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.saldo = 0

    def deposit(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            return f"Deposited {jumlah}. New balance: {self.saldo}"
        else:
            return "Invalid deposit amount"

    def tarik(self, jumlah):
        if jumlah > 0 and jumlah <= self.saldo:
            self.saldo -= jumlah
            return f"Withdrew {jumlah}. New balance: {self.saldo}"
        else:
            return "Invalid withdrawal amount or insufficient funds"

akun = BankAccount("NamaSaya")
print(akun.deposit(1000))
print(akun.tarik(500))
print(akun.tarik(600))

time.sleep(1)

class Student:
    def __init__(self, nama):
        self.nama = nama
        self.nilai = []

    def add_grade(self, angka):
        self.nilai.append(angka)
        return f"Grade {angka} added."

    def get_average(self):
        if len(self.nilai) == 0:
            return "No grades available."
        rata = sum(self.nilai) / len(self.nilai)
        return f"Average grade: {rata}"
    
murid = Student("Alice")
print(murid.add_grade(90))
print(murid.add_grade(80))
print(murid.add_grade(70))
print(murid.get_average())