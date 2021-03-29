def TowerOfHanoi(n, A, B, C):
    if n == 1:
        print(f"Move disk 1 from rod {A} to rod {B}")
        return
    TowerOfHanoi(n - 1, A, C, B)
    print(f"Move disk {n} from rod {A} to rod {B}")
    TowerOfHanoi(n - 1, C, B,A)
TowerOfHanoi(3, 'A', 'B', 'C')