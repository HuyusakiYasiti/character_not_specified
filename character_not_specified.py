number = int()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

chosen = str()
flag = str()

while True:
    chosen = input("Please enter a letter. : ")
    if chosen in letters: 
        number = letters.index(chosen)
        letters.remove(chosen)
        letters.insert(number, " ")

    flag = input("Please enter a letter to countinue. :")
    flag = bool(flag)
　　　　　　　　if flag == True:
        continue

    break

letters = str(letters)
letters = letters.replace("\'", "")
letters = letters[1: -1]

print(letters)
