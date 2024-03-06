#Ahmed Abd elsamea Mosleh 20231010
#Mohamed Abd allah Galal  20231144
#Yasser Khaled Fath elbab 20231203



# function to check if input is binary or not
def checkbinary(binaryStr):
        # Check if the string is empty.
        if not binaryStr:
            return False
        # Check if all characters are either '0' or '1'.
        for char in binaryStr:
            if char not in ('0', '1'):
                return False

        return True



#function to convert an integer to its binary representation
def conv_int_to_bin(number):
    if number == 0:
        return '0b0'
    binary_digits = []
    while number > 0:
        binary_digits.append(str(number % 2))
        number //= 2
    binary_string = '0b' + ''.join(binary_digits[::-1])
    return binary_string



#Function to Calculates the 1st complement of a binary number.
def onesComp(binary_num):
    return "".join("0" if digit == "1" else "1" for digit in binary_num)



#Function to Calculates the 2nd complement of a binary number.
def twosComp(binary_num):
    ones_comp = onesComp(binary_num)
    if binary_num[0] == "0":
        return ones_comp
    else:
        return conv_int_to_bin(int(ones_comp, 2) + 1)[2:]



#Function to Adds two binary numbers.
def AddBin(num1, num2):
    sum = conv_int_to_bin(int(num1, 2) + int(num2, 2))[2:]
    return sum



#Function to Subtracts two binary numbers.
def SubBinary(num1, num2):
    result = conv_int_to_bin(int(num1, 2) - int(num2, 2))[2:]
    return result



#print of the first menu
while True:
    print("\nMenu 1")
    print("\n** Binary Calculator **")
    print("A) Insert new numbers")
    print("B) Exit")

    choice = input("Enter your choice: ").upper()



     # take first number from the user
    if choice == "A":
        num1 = input("Enter the first binary number: ")
        while not checkbinary(num1):
            print("Invalid binary number. Please enter a valid binary number.")
            num1 = input("Enter the first binary number: ")



# print of menu 2
        print("\nMenu 2")
        print("\n** Select Operation **")
        print("A) Compute one's complement")
        print("B) Compute two's complement")
        print("C) Addition")
        print("D) Subtraction")

        operation = input("Enter your choice: ").upper()




        """
            if the user choose A (program start to use onescomp function to calc 1st comp)
             or choose B(program start to use twoscomp function to calc 2nd comp)
         """
        if operation in ["A", "B"]:
            result = onesComp(num1) if operation == "A" else twosComp(num1)

            print("Result:", result)
            # trying choose A to Compute one's complement" input = 101 --> output = 010
            # trying choose B to Compute two's complement" input = 111 --> output = 001





        # if the user choose C (program start to use Addbin function to addition 2 bin numbers)
        # if the user choose D (program start to use Subbin function to subtraction 2 bin numbers)
        elif operation in ["C", "D"]:
            num2 = input("Enter the second binary number: ")
            while not checkbinary(num2):
                print("Invalid binary number. Please enter a valid binary number.")
                num2 = input("Enter the second binary number: ")

            result = AddBin(num1, num2) if operation == "C" else SubBinary(num1, num2)
            print("Result:", result)
            #trying choose c to addition 2 binary numbers if user insert num1=1010 and num2=1110 --> output=11000
            #trying choose D to subtract 2 binary numbers if user insert num1=1100 and num2=0111 -->output = 0101



        else:
            print("Invalid choice. Please try again.")



    # if user want to exit the program
    elif choice == "B":
        break


    # if user insert wrong input
    else:
        print("Invalid choice. Please try again.")