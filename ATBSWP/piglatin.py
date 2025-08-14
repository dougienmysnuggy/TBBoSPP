#English to pig latin
message = input('Enter the English message to translate to Pig Latin: ')

VOWELS = ['a', 'e', 'i', 'o', 'u']

pig_latin_message = []

'''
iterate through each word until we find the first vowel
split the word at that point
pig latin message += 2nd part of the split + first part of the split + yay
'''
for word in message.split():
    #separate non characters from beginning
    prefix_non_characters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_characters += word[0] #adds non alpha to prefix list
        word = word[1:] #removes the first character
    
    # in case it's all non alpha
    if len(word) == 0:
        pig_latin_message.append(prefix_non_characters)
        continue
    
    #seperate non characters from end
    suffix_non_characters = ''
    while not word[-1].isalpha():
        suffix_non_characters += word[-1]
        word = word[:-1]
        
    # save the case
    was_uppercase = word.isupper()
    was_title_case = word.istitle()
    
    # convert it all to lowercase
    word = word.lower()
    
    # separate consanents at beginning of the work
    consanents = ''
    while len(word) > 0 and not word[0] in VOWELS:
        consanents += word[0]
        word = word[1:]
        
    # put it all together
    if consanents != '':
        word += consanents + 'yay'
    else:
        word += 'yay'
        
    # change case back
    if was_uppercase:
        word = word.upper()
    if was_title_case:
        word = word.title()
        
    # add with prefix and suffix non alphas          
    pig_latin_message.append(prefix_non_characters + word + suffix_non_characters)
    
#print it out
print(' '.join(pig_latin_message))
        
