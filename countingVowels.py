def count_vowels(user_input):
    vowel_count = 0
    vowels = ["a", "e", "i", "o", “u”]
    for letter in user_input.lower():
        if letter in vowels:
            vowel_count +=1
    return vowel_count

user_input = input('Enter a string: ')

print('There are ' + str(count_vowels(user_input)) + ' vowels in the string ' + user_input)
