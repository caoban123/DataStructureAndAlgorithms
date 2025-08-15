def TowersOfHaNoi(n, a, b, c):
    if n == 1:
        print(f"Chuyển đĩa từ tháp {a} sang tháp {c}")
    else:
        TowersOfHaNoi(n - 1, a, c, b)
        print(f"Chuyển đĩa từ tháp {a} sang tháp {c}")
        TowersOfHaNoi(n - 1, b, a, c)
TowersOfHaNoi(3, 'A', 'B', 'C')