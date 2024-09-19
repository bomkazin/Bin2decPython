# def converter():
#     print("I've got this")

#     #get input from the user or just use a number

#     binary = 11011101
#     print(binary)
#     list_binary = [int(x) for x in str(binary)]
#     print(list_binary)
#     list_binary.reverse()
#     print(list_binary)

#     # position = list_binary.index()
#     # print(position)

#     bin_length = len(str(binary))
#     print(bin_length)

#     for index, val in enumerate(list_binary):
#         print(index, val)

#         decimal = val * (2 ** index)
#         print(decimal)
#         sum1 = sum([decimal])
#     print(sum1)

# converter()

def converter():
    print("I've got this\n\n")

    while True:
        binary = input("Enter the binary number (max 8 characters): ")

        # Check if the length of the binary input is within the valid range
        if not (1 <= len(binary) <= 8):
            print("Error: The binary number must be between 1 and 8 characters long.")
        # Check if all characters in the binary input are either '0' or '1'
        elif not all(char in '01' for char in binary):
            print("Error: Only 0s and 1s are allowed.")
        else:
            # If both conditions are met, exit the loop
            break

    #Now we need to add and octal conversion after working on the client side


    # Convert the binary number to a list of digits
    list_binary = [int(x) for x in str(binary)]
    print(f"Binary list: {list_binary}")

    # Reverse the binary list to match positional powers of 2
    list_binary.reverse()
    print(f"Reversed binary list: {list_binary}\n")

    # Initialize sum for decimal conversion
    sum1 = 0

    # Loop through the binary list and calculate the decimal equivalent
    for index, val in enumerate(list_binary):
        decimal = val * (2 ** index)
        print(f"Binary digit: {val}, Position: {index}, Decimal value: {decimal}")
        sum1 += decimal

    print(f"\nDecimal equivalent: {sum1}")

converter()