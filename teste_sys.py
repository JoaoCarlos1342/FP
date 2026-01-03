import sys

def main():
    print("A lista completa é:", sys.argv)
    print("O nome do ficheiro é;", sys.argv[0])

    if len(sys.argv) > 1:
        print("O primeiro argumento é:", sys.argv[1])
    else:
        print("Não passaste nenhum argumento extra.")
main()
""" 
import sys

print("O programa iniciou!")  # Para termos a certeza que correu
print(sys.argv) """