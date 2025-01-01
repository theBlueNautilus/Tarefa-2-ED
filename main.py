import time

def mede_tempo(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Lê a entrada e converte para inteiros (int) cada valor da lista de entrada
valores = [int(x) for x in input().strip().split()]

# Executa o SelectionSort e mede o tempo
tempo_sel = mede_tempo(selection_sort, valores)

# Executa o InsertionSort e mede o tempo
tempo_ins = mede_tempo(insertion_sort, valores)

# Imprime resultados
print("\nResultado SelectionSort:", valores)
print(f"Tempo SelectionSort: {tempo_sel:.6f} s\n")

print("\nResultado InsertionSort:", valores)
print(f"Tempo InsertionSort: {tempo_ins:.6f} s\n")

if tempo_sel < tempo_ins:
    print("SelectionSort foi mais rápido.")
elif tempo_sel > tempo_ins:
    print("InsertionSort foi mais rápido.")
else:
    print("Ambos demoraram o mesmo tempo.")
