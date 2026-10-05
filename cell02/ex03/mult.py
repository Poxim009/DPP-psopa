print("Enter the first number:")
f = int(input())
print("Enter the second number:")
s = int(input())

r = f*s
print(f"{f} x {s} = {r}")

if r>0:
    print("The result is positive.")
elif r<0:
    print("The result is negative.")

else:
    print("The result is positive and negative.")