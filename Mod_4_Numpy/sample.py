import numpy as np

data = [10 , 20 , 30 , 40 , 50]
count = [1 , 2 , 3 , 4 , 5]
print(np.mean(data))
print(np.average(data , weights=count))