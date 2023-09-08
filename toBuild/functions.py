# importing basic data dictionaries that are used in this function
import keywords as k
# function to do arethmetic operation
def toOperate(value , value2 , value3):
    if(value2 == '+'):
        v=(value + value3)
        if(v>20):
            print('work is on progress')
        else:
            return  v
    elif(value2 == '-'):
        v=(value - value3)
        if(v>20 or v <0 ):
            print('work is on progress')
        else:
            return  v
    elif (value2 == '*'):
        v=(value * value3)
        if(v>20 or v<0):
            print('work is on progress')
        else:
            return  v
    elif(value2 == '/'):
        v=(value / value3)
        if((value / value3).float):
            print('work progress')

#giving values for arethemetics operation
#spilit functions is to spilit the string according o the spaces
input = "PUNCH ZARBE CHAAR" .split()
# token is used to store each value in the form of the list
token = []
# for loop is used to tokenize or make lexemes of each input given
for word in input:
    # checks if the input contain sth that belongs or is number
    if word in k.NUMBERS:
        token.append(['NUMBERS' , k.NUMBERS[word]])
    # checks if the input contain sth that belongs or is arethmetic
    elif word in k.ARETHMATIC:
        token.append(['OPERATOR' ,k.ARETHMATIC[word]])
# printing the token
print(token)
# in this loop we are calling a function to do appropriate operations on behalf of the input
for word in k.NUMBERS:
    if(toOperate(token[0][1] , token[1][1] ,token[2][1] ) == k.NUMBERS[word]):
        # at here we are just printing the value of the word or the k.numbers key value
        print(word)
