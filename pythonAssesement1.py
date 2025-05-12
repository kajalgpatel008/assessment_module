def reverse_string(s):
    return s[::-1]

def concatenate_string(s):
    S = input("Enter the string to concatenate: ")
    return s + S

def is_palindrome(s):
    return s == s[::-1]

def copy_string(s):
    return s[:]

def string_length(s):
    return len(s)

def character_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v = c = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v += 1
            else:
                c += 1
    return v, c

def count_spaces_digits(s):
    spaces = digits = 0
    for char in s:
        if char == ' ':
            spaces += 1
        elif char.isdigit():
            digits += 1
    return spaces, digits


while True:
        s = input("\nEnter a string: ")
        print("\nChoose an operation:")
        print("1. Reverse the string")
        print("2. Concate with another string")
        print("3. Check if palindrome")
        print("4. Copy the string")
        print("5. Find length of the string")
        print("6. Frequency of each character")
        print("7. Count vowels and consonants")
        print("8. Count blank spaces and digits")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            print("Reversed string:", reverse_string(s))
        elif choice == '2':
            print("Concatenated string:", concatenate_string(s))
        elif choice == '3':
            if is_palindrome(s):
                print("The string is a palindrome.")
            else:
                print("The string is not a palindrome.")
        elif choice == '4':
            print("Copied string:", copy_string(s))
        elif choice == '5':
            print("Length of the string:", string_length(s))
        elif choice == '6':
            freq = character_frequency(s)
            print("Character frequencies:")
            for char, count in freq.items():
                print(f"'{char}': {count}")
        elif choice == '7':
            v, c = count_vowels_consonants(s)
            print(f"Vowels: {v}, Consonants: {c}")
        elif choice == '8':
            spaces, digits = count_spaces_digits(s)
            print(f"Spaces: {spaces}, Digits: {digits}")
        else:
            print("Invalid choice. No operation performed.")

        cont = input("\nDo you want to continue? (yes/no): ").lower()
        if cont != 'yes':
            print("Goodbye!")
            break

