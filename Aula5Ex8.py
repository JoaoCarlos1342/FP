def evenThenOdd(string):
    even = string[::2]
    odd = string[1::2]
    all = even + odd

    return "".join(all)

def shortner(string):
    if len(string) == 0:
        return ""

    resultado = string[0]

    for char in string[1:]:
        if char != resultado[-1]:
            resultado += char
            
    return resultado

def generate_pattern(num):
    lista = []
    for numero in range(1, num + 1):
        for _ in range(numero):
            lista.append(numero)
            
    return lista



def main():
    string = input("Palavra: ")
    print(evenThenOdd(string))

    string = "Mississippi"
    print(f"Original: {string}")
    print(f"Resultado: {shortner(string)}")

    # Teste extra
    string2 = "AAABBBCCCA"
    print(f"Original: {string2} -> Resultado: {shortner(string2)}")

    num = int(input("Número: "))
    print(generate_pattern(num))

main()