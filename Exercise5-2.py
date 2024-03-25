#2.sine and cosine series
import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sum_sine_series(x, n):
    s = 0
    for i in range(n):
        s += ((-1)**i) * (x**(2*i+1)) / factorial(2*i+1)
    return s

def sum_cosine_series(x, n):
    s = 0
    for i in range(n):
        s += ((-1)**i) * (x**(2*i)) / factorial(2*i)
    return s

angle_degrees = float(input("Enter the angle in degrees: "))
angle_radians = math.radians(angle_degrees)

n_terms = int(input("Enter the number of terms (N): "))

print(f"Sum of sine series: {sum_sine_series(angle_radians, n_terms)}")
print(f"Sum of cosine series: {sum_cosine_series(angle_radians, n_terms)}")