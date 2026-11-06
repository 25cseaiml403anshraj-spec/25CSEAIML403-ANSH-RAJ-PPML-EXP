import numpy as np

a = np.array([10, 20, 30, 40, 50])

np.save("myarray.npy", a)

print("Array saved successfully.")

b = np.load("myarray.npy")

print("Loaded array:")
print(b)