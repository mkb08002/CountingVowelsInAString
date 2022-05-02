def count_vowels(user_input):
    vowels = 0
    for letter in user_input:
        if letter == 'a':
            vowels += 1
        elif letter == 'e':
            vowels += 1
        elif letter == 'o':
            vowels += 1            
        elif letter == 'i':
            vowels += 1
        elif letter == 'u':
            vowels += 1
    return vowels

user_input = input('Enter a string: ').lower()

print('There are ' + str(count_vowels(user_input)) + ' vowels in the string ' + user_input)
