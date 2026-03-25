text = input("Enter string: ").strip().lower()

a = 0
b = 0
c = 0
d = 0
others = {}

for char in text:
    if char == 'a':
        a += 1
    elif char == 'b':
        b += 1
    elif char == 'c':
        c += 1
    elif char == 'd':
        d += 1
    elif char.isalpha():
        others[char] = others.get(char, 0) + 1

if a > 0: print(f"a: {a}")
if b > 0: print(f"b: {b}")
if c > 0: print(f"c: {c}")
if d > 0: print(f"d: {d}")

for letter, count in sorted(others.items()):
    print(f"{letter}: {count}")

total = a + b + c + d + sum(others.values())
print(f"Total: {total}")