from math import gcd
from fractions import Fraction 

numerator = eval(input("Enter a numerator. Value must be greater than 0>> "))
while numerator <= 0:
    print("Value must be greater than 0")
    numerator = eval(input("Please re-enter a numerator greater than 0>> "))

denominator = eval(input("Enter a denominator. Value must be greater than 0>> "))
while denominator <= 0:
    print("Value must be greater than 0")
    denominator = eval(input("Please re-enter a denominator greater than 0>> "))


gcd = gcd(numerator, denominator)
newNumerator = numerator//gcd
newDenominator = denominator//gcd

if numerator < denominator:
    print(f"{numerator}/{denominator} is a proper fraction")
    if gcd == 1:
        print("This proper fraction cannot be reduced any further")
    else:
        print(f"This fraction can be reduced to {Fraction(numerator, denominator)}")
else:
    print(f"{numerator}/{denominator} is an improper fraction")
    if gcd == 1:
        print("This improper fraction cannot be reduced any further.")
    else: 
        print(f"This improper fraction can be reduced to {Fraction(numerator, denominator)}")
    if denominator//gcd == 1 or denominator == 1 or (newNumerator)%(newDenominator) == 0:
        print(f"The whole number is {numerator//gcd}")
    else:
        print(f"The mixed number is {numerator//denominator} and {(newNumerator)%(newDenominator)}/{newDenominator}")
