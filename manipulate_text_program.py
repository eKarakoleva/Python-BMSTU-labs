
text = []
file = open("testfile.txt", "r")
for line in file:
    text.append(line.replace('\n', ''))

def delete_word(word,arr_string):
    new_text = []
    word_len = len(word)
    line_num = -1
    n_line = 0
    i = ''
    ch = ''
    for line in arr_string:
        n_line = line.find(word)
        if n_line != -1:
            i = line.index(word)
            if len(line)-1 > i+(word_len-1):
                if line[i+(word_len)].isalpha():
                    if ch != 'y':
                        ch = input('Слово является частью другого слова.\nУверени что хотите удалить? Y/N')
                    if ch == 'y' or ch == 'Y':
                        line = line.replace(word, '')
                else:
                    line = line.replace(word,'')
        new_text.append(line)
        line_num += 1
    return new_text

def replace_word(word,new_word,text):
    new_text = []
    for line in text:
        line = line.replace(word,new_word)
        new_text.append(line)
    return new_text

def put_right(text):
    new_text = []
    max_l = -1
    for line in text:
        if max_l < len(line):
            max_l = len(line)
    for line in text:
        line = ' '.join(line.split())
        print(line.rjust(max_l, ' '))
        #new_text.append(line)
    #return new_text

def put_left(text):
    new_text = []
    max_l = -1
    for line in text:
        if max_l < len(line):
            max_l = len(line)
    for line in text:
        line = ' '.join(line.split())
        print(line.ljust(max_l, ' '))
        #new_text.append(line)
    #return new_text

def max_element(array):
    max_len_el = 0
    el_num = 0
    max_l = 0
    for element in array:
        if max_l < len(element):
            max_l = len(element)
            max_len_el = el_num
        el_num += 1
    return max_len_el

def min_element(array):
    min_len_el = 0
    el_num = 0
    min_l = -1
    for element in array:
        if min_l > len(element):
            min_l = len(element)
            min_len_el = el_num
        el_num += 1
    return min_len_el

def put_center(text):
    max_l = max_element(text)
    new_l = ''
    for i in range(len(text)):
        if len(text[i]) < len(text[max_l]):
            spaces = len(text[i].split())-1
            spaces_needed = len(text[max_l]) - len(text[i])
            if spaces != 0:
                put_spaces = spaces_needed/spaces
            else:
                put_spaces = spaces_needed
            for j in text[i].split():
                space = ' ' * int(put_spaces)
                new_l += j+space
            print(new_l)
            new_l=''
        else:
            print(text[i])

def extra_task(text):
    text = delete_word(",", text)
    max_len_line = max_element(text)
    min_len_word = min_element(text[max_len_line].split())
    max_line = text[max_len_line].split()
    return delete_word(max_line[min_len_word], text)

def print_text(text):
    for line in text:
        print(line)

options = {
    0: '[0] Удалить слово',
    1: '[1] Найти и замени слово',
    2: '[2] Выравнивание текта по правому краю',
    3: '[3] Выравнивание текта по левому краю',
    4: '[4] Выравнивание текта по ширине',
    5: '[5] Удалить самое короткое слово в самом длином по числу слов предложения'
}
print_text(text)
print()

ch = 'y';
while ch != "n" and ch != "N":
    for op in options:
        print(options[op])
    print()

    option = int(input('Выберите действие: '))
    if option == 0:
        word = input('Слово, которое хотите удалит: ')
        text = delete_word(word, text)
        print_text(text)
    elif option == 1:
        word = input('Слово, которое хотите заменить: ')
        new_word  = input('Новое слово: ')
        text = replace_word(word, new_word, text)
        print_text(text)
    elif option == 2:
        put_right(text)
    elif option == 3:
        put_left(text)
    elif option == 4:
        put_center(text)
    elif option == 5:
        text = extra_task(text)
        print_text(text)

    print()
    ch = input('Хотите продольжит? y/n')