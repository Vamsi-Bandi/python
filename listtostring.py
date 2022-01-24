spam = ['apples','bananas','tofu','cats']
empty = []

def function(spam):
    if spam == []:
        print('Empty list passed')
    for index, item in enumerate(spam):
        if index == (len(spam)-1):
            print('and ' + item)
        else:
            print(item + ', ', end='')

function(spam)
