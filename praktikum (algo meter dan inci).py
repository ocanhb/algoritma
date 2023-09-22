# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 20:33:57 2023

@author: ocanh
"""
print ("hitung luas lapangan")
panjang = int(input("masukkan panjang lapangan"))
lebar = int(input("masukkan lebar lapangan"))
satuan = input("Pilih satuan (meter/inci): ")
if satuan == "meter":
    luas = panjang*lebar
    print(f"Luas lapangan dengan panjang {panjang} dan lebar {lebar} adalah {luas} meter")

elif satuan == "inci":
    luas = panjang*lebar
    print (f"Luas lapangan dengan panjang {panjang} dan lebar {lebar} adalah {luas} inci" )

else:
    print("Satuan yang dimasukkan tidak valid. Gunakan 'meter' atau 'inci'.")