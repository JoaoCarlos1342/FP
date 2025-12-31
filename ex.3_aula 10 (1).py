
# Complete o programa!

"""import os
current_folder = os.path.dirname(os.path.abspath(__file__))
print("caminho do ficheiro novo", current_folder)

file_name = os.path.join(current_folder, "drawing.txt")
print("caminho do ficheiro novo", current_folder)"""

# a)
def loadFile(fname, lst):
    with open(fname, "r") as f:
        f.readline()
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 5:
                numero = int(parts[0])
                nome = parts[1]
                n1 = float(parts[2])
                n2 = float(parts[3])
                n3 = float(parts[4])
                lst.append((numero, nome, n1, n2, n3))

# b) Crie a função notaFinal aqui...
def notafinal(reg):
    média = (reg[2] + reg[3] + reg[4])/3
    return média

# c) Crie a função printPauta aqui...
def printPauta(lst):
    print("{:<7s}{:^50s}{:>5s}".format("Número", "Nome", "Nota"))

    for reg in lst:
        num = reg[0]
        nome = reg[1]
        nota = notafinal(reg)
        print("{:7d}{:^50s}{:<5.1f}".format(num, nome, nota))

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # ordenar a lista
    lst.sort()
    
    # mostrar a pauta
    if lst:
        printPauta(lst)
    else:
        print("A lista de alunos está vazia.")


# Call main function
if __name__ == "__main__":
    main()
