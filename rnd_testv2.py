import math

file_name = "final_result.txt"

def runsTest(l):
    runs = 1
    
    # Checking for start of new run 
    for i in range(1, len(l)):
        # no. of runs 
        if l[i] != l[i-1]:
            runs += 1

    runs_exp = (2 * len(l) - 1) / 3
    stan_dev = math.sqrt((16 * len(l) - 29) / 90)
    
    z = (runs - runs_exp) / stan_dev 

    return z

# Open the file with binary data (1s and 0s)
with open(file_name) as f:
    rnd_num = list(map(int, f.readlines()))

Z = abs(runsTest(rnd_num))

print('Z-statistic =', Z)
