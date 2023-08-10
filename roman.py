#This code converts the decimal numbers between 1 and 39 (correctly) in roman numbers

def dec2roman(dec: int) -> str:
    var = ''
    for i in range(dec):
        var += 'I'
        if var[-4:] == 'IIII':
            if 'V' in var:
              var = var[:-5] + 'IX'
            else:  
                var = var[:-3] + 'V'
        elif var[-3:] == 'IVI':
            var = var[:-3] +'V'
        elif var[-3:] == 'IXI':
            var = var[:-3] +'X'
    return var

if __name__ == '__main__':
    num = 50
    for i in range(1, num+1):
        print('The number '+ str(i) +' correspond to the roman number ' + dec2roman(i))

