# -*- coding: utf-8 -*-
"""day6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19AQdA1AOqcoTahDZs4xLVmMFOVBukrhN
"""

a= open("/content/drive/MyDrive/https:  www.lin.txt",'r')

a= open("/content/drive/MyDrive/https:  www.lin.txt",'w')

a= open("/content/drive/MyDrive/https:  www.lin.txt",'a')

a= open("/content/drive/MyDrive/https:  www.lin.txt",'rb')

a = open("/content/drive/MyDrive/Colab Notebooks/Untitled","r")
content = a.read()
print(content)
a.close()

a = open("/content/drive/MyDrive/Colab Notebooks/Untitled","a")
content = a.write("apple")
print(content)
a.close()

a = open("/content/drive/MyDrive/Colab Notebooks/Untitled","w")
content = a.write("123")
print(content)
a.close()

a = open("/content/drive/MyDrive/Colab Notebooks/Untitled", "wb")
content = a.write("123".encode())
print(content)
a.close()

try:
  num =int(input("rnter the num:"))
  print(10/num)
except ZeroDivisionError:
  print("0 is not divisible")

try:
  num =int(input("rnter the num:"))
  print(10/num)
except ZeroDivisionError:
    print("0 is not divisible")
finally:
  print("error")

def reena(age):
  if age<18:
    raise ValueError("age must be 18")
  return True
try:
  reena(15)
except ValueError:
    print("error")