numa = 1
numb = 1

while numa <= 10:
    while numb <=10:
        mult = numa*numb
        print(f"{numa} x {numb} = {mult}")
        numb+=1
    numa+=1
    numb=1
    if numa != 11:
        print(f'-----------Tabuada do número {numa}--------------')
