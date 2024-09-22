# Counting letters

word = input("Enter a word")

for i in word:
    convert = ord(i)
    uppercase = i.upper()
    lowercase = i.lower()
    convert1 = ord(uppercase)
    convert2 = ord(lowercase)
    print(f"Nuicode of '{i}' is {convert}, uppecase: {convert1}, lowercase: {convert2}")

# Counting words

name = "A picture says more than a thousand words, a matematical formula says more than a thousand pictures."

words = name.split()
sums = 0
for x in words:
    sums = sums + 1

print(f"The number of the word is {sums}")

# palindrome

in_data = input("Enter some words")

words = in_data.lower().split()

for x in words:
    divid = int(len(x)/2)
    revers = x[::-1]
    
    if x[:divid] == revers[:divid]:
        print(f"The word {x} is palindrom ")

# Vowels

sentencis = "Pure mathematics is, in its way, the poetry of logical ideas"
words = sentencis.split()
vowels = ["e", "i", "u", "o", "a"]
sums = 0
for i in range(len(words)):
    for x in words[i]:
        if x == "a" or x == "A":
            sums = sums + 1
        elif x == "i" or x == "I":
            sums = sums + 1
        elif x == "u" or x == "U":
            sums = sums + 1
        elif x == "e" or x == "E":
            sums = sums + 1
        elif x == "o" or x == "O":
            sums = sums + 1

print(sums)


# Encryption

