# Exercise 5 - Swedish Robber Translator
# Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") should return the string "tothohisos isos fofunon".
def Swedish_robber_translator(string=str(input("enter the text to translate : "))):
    vowels = ['a', 'e', 'i', 'o', 'u']
    translated_text = ''
    for i in string:
        if i not in vowels and i != ' ':
            translated_text += i + 'o' + i
        else:
            translated_text += i
    return translated_text


print(Swedish_robber_translator())
