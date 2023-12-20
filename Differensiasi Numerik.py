
def numerical_derivative(f, x, orde=1, h=1e-5):
    if orde == 1:
        return (f(x + h) - f(x - h)) / (2 * h)
    elif orde == 2:
        return (f(x + h) - 2 * f(x) + f(x - h)) / (h**2)
    elif orde == 3:
        return (-f(x + 2 * h) + 2 * f(x + h) - 2 * f(x - h) + f(x - 2 * h)) / (2 * h**3)
    elif orde == 4:
        return (f(x + 2 * h) - 4 * f(x + h) + 6 * f(x) - 4 * f(x - h) + f(x - 2 * h)) / (h**4)
    else:
        raise ValueError("Order must be between 1 and 4")

# Input dari pengguna
x_value = float(input("Masukkan nilai x: "))
h_value = float(input("Masukkan nilai h: "))

# Contoh fungsi
def f(x):
    return x**2  # Anda bisa menggantinya dengan fungsi lain

# Penghitungan turunan numerik
for orde in range(1, 5):
    result = numerical_derivative(f, x_value, orde=orde, h=h_value)
    print(f"Turunan orde {orde} di x = {x_value}: {result}")
