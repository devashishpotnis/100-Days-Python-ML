# ---- Built-in modules ----
from datetime import datetime
import os
import sys
import math
import random
from collections import Counter
import numpy as np

# ---- datetime ----
print("Current Date & Time:", datetime.now())

# ---- os ----
print("Current Working Directory:", os.getcwd())

# ---- sys ----
print("Python Version:", sys.version)

# ---- math ----
print("Square root of 25:", math.sqrt(25))

# ---- random ----
no = [1, 2, 3, 4, 5]
print("Random choice:", random.choice(no))

# ---- collections ----
data = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = Counter(data)
print("Item frequency:", count)

# ---- numpy ----
arr = np.array([10, 20, 30, 40])
print("NumPy Array:", arr)
print("Array Mean:", np.mean(arr))
