# Exercise 25 - Present Participle Form
# In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going.
# A simple set of heuristic rules can be given as follows:
#
# If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
# If the verb ends in ie, change ie to y and add ing
# For words consisting of consonant-vowel-consonant, double the final letter before adding ing
# By default just add ing
# Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form
# returns its present participle form. Test your function with words such as lie, see, move and hug.
# However, you must not expect such simple rules to work for all cases.
#
# Higher order functions and list comprehensions
def make_ing_form(input_verb=str(input("enter the verb "))):
    result_form = ''
    exceptions = ('be', 'see', 'flee', 'knee')
    word_to_detect = 'aeiou'
    if input_verb.endswith('ie'):
        result_form += input_verb.replace(input_verb[-2:], 'y') + 'ing'
    elif input_verb[-3] not in word_to_detect:
        if input_verb[-2] in word_to_detect:
            if input_verb[-1] not in word_to_detect:
                result_form += input_verb + input_verb[-1] + 'ing'
    elif input_verb.endswith('e'):
        if input_verb not in exceptions:
            result_form += input_verb.replace(input_verb[-1], 'ing')
    return result_form


print(make_ing_form())
