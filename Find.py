'''words = ['hello','world','my','name','is','Anna']
char = 'o'
for item in words:
    if char in item:
        print item'''
def character(word_list, char):
    new_list = []
    for i in range(0, len(word_list)):
        if word_list[i].find(char) != -1:
            new_list.append(word_list[i])
    print new_list
words = ['hello','world','my','name','is','Anna']
character(words, 'o')