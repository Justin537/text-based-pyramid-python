text = input("Enter a word: ")

number = 0
cek = 0


for number in range(len(text)):
    number = number + 1
    if number <= len(text):
        while cek < number:
            print("\n")
            cek = cek + 1
            for i in range(cek):
                print("*" , end='')


    if number >= len(text):
        print("\n")
        print(text)
        cek = cek + 1

while number != 0:
    number = number - 1
    if number <= len(text):
        while cek > number:
            print("\n")
            cek = cek - 1
            for i in range(cek):
                print("*", end='')

def print_dynamic_pattern():
    # Ask the user for input
    word = input("Enter a word: ")
    length = len(word)  # Number of letters in the word

    # Top half of the pattern
    for i in range(1, length + 1):
        dashes = "-" * (length - i)
        stars = "*" * i
        print(f"{dashes}{stars}")

    # Print the user's input with a blank line before and after
    print(f"\n{word}\n")

    # Bottom half of the pattern
    for i in range(length, 0, -1):
        dashes = "-" * (length - i)
        stars = "*" * i
        print(f"{dashes}{stars}")


# Run the function
print_dynamic_pattern()