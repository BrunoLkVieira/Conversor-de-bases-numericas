from time import sleep


def binario_para_decimal(n):
    tamanho = len(n)

    base = 2
    c = 0
    coluna = tamanho - 1
    resultado = 0
    while c != tamanho:
        resultado += int(n[coluna]) * (base ** c)
        coluna += -1
        c += 1

    return resultado

def decimal_para_binario(n):

    n = int(n)
    base = 2
    c = 1

    resto = n % base
    quociente = n // base
    restos = [resto]

    while c != 0:

        resto = quociente % base
        restos.append(resto)
        quociente = quociente // base
        if quociente < base:
            if quociente != 0:
                restos.append(quociente)
            c = 0

    i = len(restos)
    resultado = ''
    for c in range(i):
        restos[c] = str(restos[c])

    for c in range(i):
        resultado += restos[i - 1]
        i += -1
    return resultado

def octal_para_decimal(n):
    tamanho = len(n)

    base = 8
    c = 0
    coluna = tamanho - 1
    resultado = 0
    while c != tamanho:
        resultado += int(n[coluna]) * (base ** c)
        coluna += -1
        c += 1

    return resultado

def decimal_para_octal(n):

    n = int(n)
    base = 8
    c = 1

    resto = n % base
    quociente = n // base
    restos = [resto]

    while c != 0:

        resto = quociente % base
        restos.append(resto)
        quociente = quociente // base
        if quociente < base:
            if quociente != 0:
                restos.append(quociente)
            c = 0

    i = len(restos)
    resultado = ''
    for c in range(i):
        restos[c] = str(restos[c])

    for c in range(i):
        resultado += restos[i - 1]
        i += -1
    return resultado
def hexadecimal_para_decimal(n):
    n= n.upper()
    tamanho = len(n)

    base = 16
    c = 0
    coluna = tamanho - 1
    resultado = 0
    letras = ["A", "B", "C", "D", "E", "F"]
    while c != tamanho:
        if n[coluna] in letras:
            if n[coluna] == "A":
                L = 10
            if n[coluna] == "B":
                L = 11
            if n[coluna] == "C":
                L = 12
            if n[coluna] == "D":
                L = 13
            if n[coluna] == "E":
                L = 14
            if n[coluna] == "F":
                L = 15
            resultado += L * (base ** c)
        else:
            resultado += int(n[coluna]) * (base ** c)
        coluna += -1
        c += 1

    return resultado

def decimal_para_hexadecimal(n):

    n = int(n)
    base = 16
    c = 1
    restos = []
    resto = n % base
    quociente = n // base
    if n < base:

        restos.append(n)
        c = 0
    else:

        restos = [resto]

    while c != 0:

        resto = quociente % base
        restos.append(resto)
        quociente = quociente // base
        if quociente < base:
            if quociente != 0:
                restos.append(quociente)
            c = 0

    i = len(restos)
    resultado = ''
    for c in range(i):
        if restos[c] >= 10:
            if restos[c] == 10:
                restos[c] = "A"
            if restos[c] == 11:
                restos[c] = "B"
            if restos[c] == 12:
                restos[c] = "C"
            if restos[c] == 13:
                restos[c] = "D"
            if restos[c] == 14:
                restos[c] = "E"
            if restos[c] == 15:
                restos[c] = "F"
        restos[c] = str(restos[c])

    for c in range(i):
        resultado += restos[i - 1]
        i += -1
    return resultado

def base30_para_decimal(n):
    tamanho = len(n)
    n=n.upper()
    base = 30
    c = 0
    coluna = tamanho - 1
    resultado = 0
    letras = ["A", "B", "C", "D", "E", "F", 'G', 'H', "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U"]
    while c != tamanho:
        if n[coluna] in letras:
            if n[coluna] == "A":
                L = 10
            if n[coluna] == "B":
                L = 11
            if n[coluna] == "C":
                L = 12
            if n[coluna] == "D":
                L = 13
            if n[coluna] == "E":
                L = 14
            if n[coluna] == "F":
                L = 15
            if n[coluna] == "G":
                L = 16
            if n[coluna] == "H":
                L = 17
            if n[coluna] == "I":
                L = 18
            if n[coluna] == "J":
                L = 19
            if n[coluna] == "K":
                L = 20
            if n[coluna] == "L":
                L = 21
            if n[coluna] == "M":
                L = 22
            if n[coluna] == "N":
                L = 23
            if n[coluna] == "O":
                L = 24
            if n[coluna] == "P":
                L = 25
            if n[coluna] == "Q":
                L = 26
            if n[coluna] == "R":
                L = 27
            if n[coluna] == "S":
                L = 28
            if n[coluna] == "T":
                L = 29
            if n[coluna] == "U":
                L = 30
            resultado += L * (base ** c)
        else:
            resultado += int(n[coluna]) * (base ** c)
        coluna += -1
        c += 1

    return resultado

def decimal_para_base30(n):

    n = int(n)
    base = 30
    c = 1
    restos = []
    resto = n % base
    quociente = n // base
    if n < base:

        restos.append(n)
        c = 0
    else:

        restos = [resto]

    while c != 0:

        resto = quociente % base
        restos.append(resto)
        quociente = quociente // base
        if quociente < base:
            if quociente != 0:
                restos.append(quociente)
            c = 0

    i = len(restos)
    resultado = ''
    for c in range(i):
        if restos[c] >= 10:
            if restos[c] == 10:
                restos[c] = "A"
            if restos[c] == 11:
                restos[c] = "B"
            if restos[c] == 12:
                restos[c] = "C"
            if restos[c] == 13:
                restos[c] = "D"
            if restos[c] == 14:
                restos[c] = "E"
            if restos[c] == 15:
                restos[c] = "F"
            if restos[c] == 16:
                restos[c] = "G"
            if restos[c] == 17:
                restos[c] = "H"
            if restos[c] == 18:
                restos[c] = "I"
            if restos[c] == 19:
                restos[c] = "J"
            if restos[c] == 20:
                restos[c] = "K"
            if restos[c] == 21:
                restos[c] = "L"
            if restos[c] == 22:
                restos[c] = "M"
            if restos[c] == 23:
                restos[c] = "N"
            if restos[c] == 24:
                restos[c] = "O"
            if restos[c] == 25:
                restos[c] = "P"
            if restos[c] == 26:
                restos[c] = "Q"
            if restos[c] == 27:
                restos[c] = "R"
            if restos[c] == 28:
                restos[c] = "S"
            if restos[c] == 29:
                restos[c] = "T"
            if restos[c] == 30:
                restos[c] = "U"

        restos[c] = str(restos[c])

    for c in range(i):
        resultado += restos[i - 1]
        i += -1

    return resultado



def binario_para_octal(n):
    resultado=decimal_para_octal(binario_para_decimal(n))
    return resultado
def binario_para_hexadecimal(n):
    resultado= decimal_para_hexadecimal(binario_para_decimal(n))
    return resultado
def binario_para_base30(n):
    resultado=decimal_para_base30(binario_para_decimal(n))
    return resultado
def octal_para_binario(n):
    resultado = decimal_para_binario(octal_para_decimal(n))
    return resultado

def octal_para_hexadecimal(n):
    resultado = decimal_para_hexadecimal(octal_para_decimal(n))
    return resultado
def octal_para_base30(n):
    resultado = decimal_para_base30(octal_para_decimal(n))
    return resultado
def hexadecimal_para_binario(n):
    resultado=decimal_para_binario(hexadecimal_para_decimal(n))
    return resultado

def hexadecimal_para_octal(n):
    resultado = decimal_para_octal(hexadecimal_para_decimal(n))
    return resultado
def hexadecimal_para_base30(n):
    resultado = decimal_para_base30(hexadecimal_para_decimal(n))
    return resultado
def base30_para_binario(n):
    resultado= decimal_para_binario(base30_para_decimal(n))
    return resultado
def base30_para_octal(n):
    resultado = decimal_para_octal(base30_para_decimal(n))
    return resultado
def base30_para_hexadecimal(n):
    resultado = decimal_para_hexadecimal(base30_para_decimal(n))
    return resultado

def menu():
    while True:

        print("\n", 10*"=", "Menu de Conversões", 10*"=")
        print("1. Binário -> Octal ")
        print("2. Binário -> Decimal")
        print("3. Binário -> Hexadecimal")
        print("4. Binário -> Base 30")
        print("5. Octal -> Binario")
        print("6. Octal -> Decimal")
        print("7. Octal -> Hexadecimal")
        print("8. Octal -> Base 30")
        print("9. Decimal -> Binario")
        print("10. Decimal -> Octal")
        print("11. Decimal -> Hexadecimal")
        print("12. Decimal -> Base 30")
        print("13. Hexadecimal -> Binario")
        print("14. Hexadecimal -> Octal")
        print("15. Hexadecimal -> Decimal")
        print("16. Hexadecimal -> Base 30")
        print("17. Base 30 -> Binario")
        print("18. Base 30 -> Octal")
        print("19. Base 30 -> Decimal")
        print("20. Base 30 -> Hexadecimal")
        print("0. Fechar")
        print(41 * "=")
        opcao = input("Escolha a conversão a ser utilizada : ")
        opcao = int(opcao)


        if opcao > 0 and opcao <= 20:
            numero = input(str("digite o Numero:"))

            if opcao == 1:
                resultado = binario_para_octal(numero)
                base_i = "Binario"
                base_f = "Octal"
            elif opcao == 2:
                resultado =binario_para_decimal(numero)
                base_i = "Binario"
                base_f = "Decimal"
            elif opcao == 3:
                resultado =binario_para_hexadecimal(numero)
                base_i = "Binario"
                base_f = "Hexadecimal"
            elif opcao == 4:
                resultado =binario_para_base30(numero)
                base_i = "Binario"
                base_f = "Base 30"
            elif opcao == 5:
                resultado =octal_para_binario(numero)
                base_i = "Octal"
                base_f = "Binario"
            elif opcao == 6:
                resultado =octal_para_decimal(numero)
                base_i = "Octal"
                base_f = "Decimal"
            elif opcao == 7:
                resultado =octal_para_hexadecimal(numero)
                base_i = "Octal"
                base_f = "Hexadecimal"
            elif opcao == 8:
                resultado =octal_para_base30(numero)
                base_i = "Octal"
                base_f = "Base 30"
            elif opcao == 9:
                resultado =decimal_para_binario(numero)
                base_i = "Decimal"
                base_f = "Binario"
            elif opcao == 10:
                resultado =decimal_para_octal(numero)
                base_i = "Decimal"
                base_f = "Octal"
            elif opcao == 11:
                resultado =decimal_para_hexadecimal(numero)
                base_i = "Decimal"
                base_f = "Hexadecimal"
            elif opcao == 12:
                resultado =decimal_para_base30(numero)
                base_i = "Decimal"
                base_f = "Base 30"
            elif opcao == 13:
                resultado =hexadecimal_para_binario(numero)
                base_i = "Hexadecimal"
                base_f = "Binario"
            elif opcao == 14:
                resultado =hexadecimal_para_octal(numero)
                base_i = "Hexadecimal"
                base_f = "Octal"
            elif opcao == 15:
                resultado =hexadecimal_para_decimal(numero)
                base_i = "Hexadecimal"
                base_f = "Decimal"
            elif opcao == 16:
                resultado =hexadecimal_para_base30(numero)
                base_i = "Hexadecimal"
                base_f = "Base 30"
            elif opcao == 17:
                resultado =base30_para_binario(numero)
                base_i = "Base 30"
                base_f = "Binario"
            elif opcao == 18:
                resultado =base30_para_octal(numero)
                base_i = "Base 30"
                base_f = "Octal"
            elif opcao == 19:
                resultado =base30_para_decimal(numero)
                base_i = "Base 30"
                base_f = "Decimal"
            elif opcao == 20:
                resultado =base30_para_hexadecimal(numero)
                base_i = "Base 30"
                base_f = "Hexadecimal"

            print(f"\n\033[32m{base_i}: {numero} ---> {base_f}: {resultado}\033[m")

        else:

            if opcao == 0:
                print("\n\033[34mFechando o programa.\033[m")
                print("\033[34mObrigado por usar!\033[m")
                break
            else:
                print("\033[31m Opção inválida. Tente novamente.\033[m")

        sleep(5)


if __name__ == "__main__":
    print("Trabalho de Bruno De Alencar Vieira")
    menu()

