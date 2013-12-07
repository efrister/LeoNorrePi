# Simple print
print("Hello World")

# Print concatenated
i = 0
print("Value of i:", i)

# While Loop
a, b = 0, 1
while b < 10:
    print(b, end=",")
    a, b = b, a+b
print("\n")

# if
x = int(input("Enter any integer value: "))
if x < 0:
    x = 0
    print("Negatives changed to zero.")
elif x == 0:
    print("Exactly zero")
else:
    print("Greater than 0.")

# for
words = ["Cat", "Dog", "Mouse"]
for word in words:
    print(word, len(word))

# Slice (making an implicit copy)
print("\nAppending to the list: ")
for word in words[:]:
    if len(word) > 3:
        words.insert(0, word)

print(words)

# Range
print("\n Range:")
for i in range(2, 5):
    print(i)

# Functions
def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print()

fib(2000)
