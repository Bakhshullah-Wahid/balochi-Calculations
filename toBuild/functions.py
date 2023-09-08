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

input = "PUNCH ZARBE CHAAR" .split()
token = []
for word in input:
    if word in k.NUMBERS:
        token.append(['NUMBERS' , k.NUMBERS[word]])
    elif word in k.ARETHMATIC:
        token.append(['OPERATOR' ,k.ARETHMATIC[word]])
print(token)
for word in k.NUMBERS:
    if(toOperate(token[0][1] , token[1][1] ,token[2][1] ) == k.NUMBERS[word]):
        print(word)
