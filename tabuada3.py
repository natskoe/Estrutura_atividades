sair = False
while sair == False:
    numa = str(input("Digite um número: "))
    numa.lower()
    if numa == 'sair':
        sair = True
    else:
        num = int(numa)
        fatorial = 1
        multiplo = 2

        while multiplo <= num:
            fatorial = fatorial * multiplo
            multiplo = multiplo + 1
            print(fatorial)
        
        if num == 1:
            print(num)