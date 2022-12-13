# -*- coding: utf-8 -*-

"""
KT1
Lue käyttäjältä kaksi lukua ja tulosta niistä suurempi. Käytä if-else -lausetta vertailussa.

"""

luku = 0
lukuKaksi = 0

luku = int(input("Anna luku yksi: "))
lukuKaksi = int(input("Anna luku kaksi: "))

if luku > lukuKaksi:
    print(luku)
elif lukuKaksi > luku:
    print(lukuKaksi)
else:
    print("Luvut ovat samanarvoisia")


