print("Welcome to binary converter")
g = input("Enter your username: ") 
if g == "aniket":
    print("Welcome")
else:
    exit()

while True:
    print("\nChoose an option:")
    print("1. Convert sentence to binary")
    print("2. Convert binary to sentence")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        sentence = input("Please enter a sentence to convert: ")
        for h in sentence:
            if h == "A":
                print("1000001")
            elif h == "B":
                print("1000010")
            elif h == "C":
                print("1000011")
            elif h == "D":
                print("1000100")
            elif h == "E":
                print("1000101")
            elif h == "F":
                print("1000110")    
            elif h == "G":
                print("1000111")
            elif h == "H":
                print("1001000")
            elif h == "I":
                print("1001001")
            elif h == "J":
                print("1001010")
            elif h == "K":
                print("1001011")
            elif h == "L":
                print("1001100")
            elif h == "M":
                print("1001101")
            elif h == "N":
                print("1001110")
            elif h == "O":
                print("1001111")
            elif h == "P":
                print("1010000")
            elif h == "Q":
                print("1010001")
            elif h == "R":
                print("1010010")
            elif h == "S":
                print("1010011")
            elif h == "T":
                print("1010100")
            elif h == "U":
                print("1010101")
            elif h == "V":
                print("1010110")
            elif h == "W":
                print("1010111")
            elif h == "X":
                print("1011000")
            elif h == "Y":
                print("1011001")
            elif h == "Z":
                print("1011010")
            elif h == "a":
                print("1100001")
            elif h == "b":
                print("1100010")
            elif h == "c":
                print("1100011")
            elif h == "d":
                print("1100100")
            elif h == "e":
                print("1100101")
            elif h == "f":
                print("1100110")
            elif h == "g":
                print("1100111")
            elif h == "h":
                print("1101000")
            elif h == "i":
                print("1101001")
            elif h == "j":
                print("1101010")
            elif h == "k":
                print("1101011")
            elif h == "l":
                print("1101100")
            elif h == "m":
                print("1101101")
            elif h == "n":
                print("1101110")
            elif h == "o":
                print("1101111")
            elif h == "p":
                print("1110000")
            elif h == "q":
                print("1110001")
            elif h == "r":
                print("1110010")
            elif h == "s":
                print("1110011")
            elif h == "t":
                print("1110100")
            elif h == "u":
                print("1110101")
            elif h == "v":
                print("1110110")
            elif h == "w":
                print("1110111")
            elif h == "x":
                print("1111000")
            elif h == "y":
                print("1111001")
            elif h == "z":
                print("1111010")
            elif h == " ":
                print("00100000")  
            else:
                print("Unknown character:")
                

    elif choice == '2':
       
        binary_input = input("Please enter a binary string to convert (separate each binary value with a space): ")
        binary_values = binary_input.split()
        converted_sentence = ""

        for binary in binary_values:
            try:
                character = chr(int(binary, 2))
                converted_sentence += character
            except ValueError:
                print(f"Binary value '{binary}' is not valid.")

        print("Converted sentence :", converted_sentence)

    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
