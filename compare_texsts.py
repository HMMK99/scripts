text1 = '''
'''
text2 = '''
'''

text1 = text1.split('\n')
text2 = text2.split('\n')

min_len = len(text1)
min_text = text1
max_text = text2
if len(text2)<min_len:
    min_len=len(text2)
    min_text = text2
    max_text = text1

for line in range(min_len):
    if min_text[line] != max_text[line]:
        print(f'diff in line {line + 1}: {min_text[line]}')
    #char_count = 0
    # for char in min_text[line]:
    #     if char == max_text[char_count]:
    #         char_count = char_count+1
    #     else:
    #         print(char)
    #         print(max_text[char_count])
        #char_count = char_count+1
        

