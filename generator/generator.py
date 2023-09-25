def is_prime(n):

    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

while True:
    try:
        mx = input("Maximum range: ")
        mx = int(mx)
        break
    except Exception:
        mx = input("Maximum range: ")

while True:
    try:
        mn = input("Minimum range: ")
        mn = int(mn)
        break
    except Exception:
        mn = input("Minimum range: ")

with open(f"determine prime within {mx}.py", 'w') as f:
    f.write("n=10\n")

f = open(f"determine prime within {mx}.py", 'a')

for num in range(mn, mx+1):
    if is_prime(num):
        f.write(f"if n == {num}:\n    print('{num} is a prime')\n")
    else:
        f.write(f"if n == {num}:\n    print('{num} is not a prime')\n")

f.close()