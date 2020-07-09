masterlist = {"alpha" :{"a" : 1, "b" : 2,"c" : 3,"d" : 4,"e" : 5,"f" : 6,"g" : 7,"h" : 8,
"i" : 9,"j" : 10,"k" : 11,"l" : 12,"m" : 13,"n" : 14,"o" : 15,"p" : 16,
"q" : 17,"r" : 18,"s" : 19,"t" : 20,"u" : 21,"v" : 22,"w" : 23,"x" : 24,
"y" : 25,"z" : 26, " ": 0},
"reverse" : {0: " ", 1 : "z", 2 : "y", 3 : "x", 4 : "w", 5 : "v", 6 : "u", 7 : "t",
8 : "s", 9 : "r", 10 : "q",11 : "p",12 : "o",13 : "n", 14 : "m", 15 : "l",
16 : "k", 17 : "j", 18 : "i", 19 : "h", 20 : "g", 21 : "f", 22 : "e",
23 : "d", 24 : "c", 25 : "b", 26 : "a"},
"beta" : {1 : 'n', 2 : 'o', 3 : 'p', 4 : 'q', 5 : 'r', 6 : 's', 7 : 't', 8 : 'u',
9 : 'v', 10 : 'w', 11 : 'x', 12 : "y", 13 : 'z', 14 : "a", 15 : 'b', 16 : "c",
17 : 'd', 18 : 'e', 19 : 'f', 20 : "g", 21 : 'h', 22 : "i", 23 : 'j', 24 : 'k',
25 : 'l', 26 : 'm', 0 : "@"},
"shift3" : {3: " ", 4 : "z", 5 : "y", 6 : "x", 7 : "w", 8 : "v", 9 : "u", 10 : "t",
11 : "s", 12 : "r", 13 : "q", 14 : "p", 15 : "o", 16 : "n", 17 : "m", 18 : "l",
19 : "k", 20 : "j", 21 : "i", 22 : "h", 23 : "g", 24 : "f", 25 : "e",
26 : "d", 0 : "c", 1 : "b", 2 : "a"}}

def encrypt_decrypt(choice = input("What do you want to do? (Encrypt/Decrypt): "), message = input("Message: "), cipher = input("Cipher(reverse, beta, shift3): ")):
    result = ""
    for x in message.lower():
        result += masterlist[cipher][masterlist["alpha"][x]]
    print("Original: " + message)
    print(choice + "ion: " + result)
    
encrypt_decrypt()