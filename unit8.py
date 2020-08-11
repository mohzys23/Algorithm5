#file = open('new.txt', 'r')
#try:
#   print(file.write('new.txt'))
#except:
#    print('Something went wrong')
import ast
from unit7LJ import invert_dict
file = open('new.txt', 'r')
make = file.read()
convert = ast.literal_eval(make)   #converts string item to dictioary
file.close()
print(convert)
invert = invert_dict(convert)    #inverted dictionary
print(invert)
Writeinvert = open('invert.txt', 'w')
Writeinvert.write(str(invert))    #writes the dictionary to invert.txt file
Writeinvert.close()
