import random
total_count = 100
sample_count = 10
i = 1

while i <= 10:
    rs1 = random.sample(range(1, total_count), sample_count)
    print("Loop count: ", i,  ". Ramdom Sample: ", rs1)
    i = i  + 1
