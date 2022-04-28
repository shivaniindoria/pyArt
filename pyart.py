from os import system
system("pip install Art")
from art import tprint
print("Enter any number or word to see magic:")
text = input().replace(" ","") or "shivani"
print("\nlength not supported,below 10 is good\n" if len(text) >= 20 else "")
for i in range(20): tprint(text, "rnd-small")