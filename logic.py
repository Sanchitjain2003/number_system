# Decimal to Binary Converter
def decimalToBinary (num):
    result = str()
    while num != 0:
        rem = num%2
        result += str(rem)
        num = num//2
    #print (result[::-1])
    return result[::-1]

hex_dict= {'0': '0', '1': '1', '2':'2', '3':'3', '4':'4', '5':'5','6':'6','7':'7','8':'8','9':'9','10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
hexR_dict= {'0':'0', '1': '1', '2':'2', '3':'3', '4':'4', '5':'5','6':'6','7':'7','8':'8','9':'9','A':'10', 'B':'11', 'C':'12', 'D':'13', 'E':'14', 'F':'15'}
def decimalToHex (num):
    result = str()
    while num != 0:
        rem = str(num%16)
        result += hex_dict.get(rem)
        num = num//16
    #print (result[::-1])
    return result[::-1]

def decimalToOcta (num):
    result = str()
    while num != 0:
        rem = num%8
        result += str(rem)
        num = num//8
    #print (result[::-1])
    return result[::-1]

def binaryToDecimal (num):
    result = 0
    num = num [::-1]
    for i in range (len(num)-1, -1, -1):
        val = int (num[i])
        result += val* (2**i)
    #print (result)
    return (int(result))

def hexToDecimal (num):
    result = 0
    num = num [::-1]
    for i in range (len(num)-1, -1, -1):
        temp = str (num[i])
        val = int(hexR_dict.get(temp))
        result += val* (16**i)
    #print (result)
    return (int(result))

def octalToDecimal (num):
    result = 0
    num = num [::-1]
    for i in range (len(num)-1, -1, -1):
        val = int (num[i])
        result += val* (8**i)
    #print (result)
    return (int(result))

num =  input ("Enter a number here: ")
state = input ("State type of number entered (int for integers, hex for hexadecimal and octal for octal values): ")
conversion = input ("Convert it into (int for integers, hex for hexadecimal and octal for octal values): ")
if state == 'int' and conversion == 'bin':
    num = int (num)
    num = decimalToBinary (num)
    print (num)
elif state == 'int' and conversion == 'hex':
    num = int (num)
    num = decimalToHex(num)
    print (num)
elif state == 'int' and conversion == 'octal':
    num = int (num)
    num = decimalToOcta(num)
    print (num)
if state == 'bin' and conversion == 'int':
    num = binaryToDecimal(num)
    print (num)
elif state == 'hex' and conversion == 'int':
    num = hexToDecimal(num)
    print (num)
elif state == 'octal' and conversion == 'int':
    num = octalToDecimal(num)
    print (num)
if state == 'octal' and conversion == 'bin':
    num = octalToDecimal(num)
    num = decimalToBinary(num)
    print (num)
if state == 'octal' and conversion == 'hex':
    num = octalToDecimal(num)
    num = decimalToHex(num)
    print (num)
if state == 'hex' and conversion =='bin':
    num = hexToDecimal(num)
    num = decimalToBinary(num)
    print (num)
if state == 'hex' and conversion == 'octal':
    num = hexToDecimal(num)
    num = decimalToOcta(num)
    print (num)
if state == 'bin' and conversion == 'octal':
    num = binaryToDecimal(num)
    num = decimalToOcta(num)
    print (num)
if state == 'bin' and conversion =='hex':
    num = binaryToDecimal(num)
    num = decimalToHex(num)
    print (num)
elif state == conversion:
    print (num)


