# Write a program to print truth table for bitwise operators( & , | and ^ operators)

print("Truth table for bitwise AND (&):")
print("a\tb\ta & b")
for a in (0, 1):
    for b in (0, 1):
        print(f"{a}\t{b}\t{a & b}")

print("\nTruth table for bitwise OR (|):")
print("a\tb\ta | b")
for a in (0, 1):
    for b in (0, 1):
        print(f"{a}\t{b}\t{a | b}")

print("\nTruth table for bitwise XOR (^):")
print("a\tb\ta ^ b")
for a in (0, 1):
    for b in (0, 1):
        print(f"{a}\t{b}\t{a ^ b}")
