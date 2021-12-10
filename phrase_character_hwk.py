"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""
#first method

def generate_phrase(characters, phrase):
    tc = set(characters)

    cd = dict()
    cd1 = dict()
    for i in tc:
        count = 0
        for j in characters:
            if i == j:
                count += 1
        cd[i] = count
        cd1[i] = 0

    tc1 = set(phrase)

    for i in tc1:
        count = 0
        for j in phrase:
            if i == j:
                count += 1
        cd1[i] = count
        if not i in cd.keys():
            cd[i] = 0

    for k,v in cd.items():
        if cd[k] < cd1[k]:
                return False
    return True

# print(generate_phrase("aabzz *zccd!", "abz c*d"))

#second method

def generate_phrase2(characters, phrase):
    for i in range(len(phrase)):
        try:
            characters.pop(characters.index(phrase[i]))
        except:
            return False
    return True

# print(generate_phrase2(list("abc!  *"), list("abc ! *")))

#third method

def generate_phrase3(characters, phrase):
    for i in range(len(phrase)):
        if phrase[i] in characters:
            characters.remove(phrase[i])
        else:
            return False
    return True

# print(generate_phrase3(list("abc!  *z"), list("abc *z")))


