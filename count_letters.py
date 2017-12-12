'''
Count letters in a text
'''

text = input('Enter text: ')   
dic = {}

i = 97
while i < 123:
    dic[chr(i)] = 0
    i+=1

if len(text) <= 300:
    for letter in text:
        if ord(letter) > 96 and ord(letter) < 123:
            if letter in dic.keys():
                new = dic[letter] + 1
                dic.update({letter:new})

    sorted_keys = sorted(dic.keys())
    for key in sorted_keys:
        print('Буква "%s" = %s'%(key,dic[key]))
else:
    print("Text must be less than 300 symbols!")
    
