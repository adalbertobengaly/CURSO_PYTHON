"""  Este é um módulo de matriz """
print(f"Meu nome é {__name__}")
def matriz():
    M: int
    N: int

    M = int(input("Quantas linhas vai ter a matriz? "))
    N = int(input("Quantas colunas vai ter a matriz? "))

    mat: [[int]] = [[0 for _ in range(N)] for _ in range(M)]

    for i in range(0, M):
        for j in range(0, N):
            mat[i][j] = int(input(f"Elemento [{i},{j}]: "))
    print()
    print("MATRIZ DIGITADA:")

    for i in range(0, M):
        for j in range(0, N):
            print(f"{mat[i][j]} ", end="")
        print()

if __name__ == "__main__":
    matriz()