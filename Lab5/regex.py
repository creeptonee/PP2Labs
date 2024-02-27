#ex1
import re

def match(string):
    pattern = 'ab*'
    if re.match(pattern, string):
        return True
    else:
        return False

word = input()
if match(word):
    print(True)
else:
    print(False)


#ex2
import re

def match(string):
    pattern = 'ab{2,3}'
    if re.match(pattern, string):
        return True
    else:
        return False

word = input()
if match(word):
    print(True)
else:
    print(False)


#ex3
import re

def sequence(string):
    pattern = '[a-z]+_[a-z]+'
    matches = re.findall(pattern, string)
    return matches

word = input()
result = sequence(word)
print(result)


#ex4
import re
def sequence(string):
    pattern = '[A-Z][a-z]+'
    matches = re.findall(pattern, string)
    return matches

word = input()
result = sequence(word)
print(result)

#ex5
import re

def match(string):
    pattern = 'a.*b$'
    if re.match(pattern, string):
        return True
    else:
        return False
word = input()
if match(word):
    print()
else:
    print()


#ex6
import re
word = input()
new_word = re.sub( "[ ,.]", ":" , v )
print(new_word)


#ex7
def snake_to_camel(snake):
    words = snake.split('_')
    camel = words[0] + ''.join(word.capitalize() for word in words[1:])
    
    return camel

snake_input = input()
camel_output = snake_to_camel(snake_input)
print(camel_output)


#ex8
import re
word = input()
new_word = re.findall('[A-Z][^A-Z]*', word)
print(new_word)


#ex9
import re
def insert_spaces(text):
    spaces = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
    return spaces

input_txt = input()
output_txt = insert_spaces(input_txt)
print(output_txt)


#ex10
def camel_to_snake(camel):
    snake = ''.join(['_' + c.lower() if c.isupper() else c for c in camel]).lstrip('_')
    return snake

camel_input = input()
snake_output = camel_to_snake(camel_input)
print(snake_output)

