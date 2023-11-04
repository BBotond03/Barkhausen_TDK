from math import fabs as fabs
from scipy.fft import dct, idct

verbose = False # For debug purpose

for f in range(1, 10): # Names of our source files are indicated with a number
    FILE_NAME = str(f)  # Specify the file extension
    
    with open(FILE_NAME, 'r') as file:
        y = file.read()
    
    def data_process(data):
        data = data.split('\n')  # Split the string into lines
        processed_data = []
        for line in data:
            try:
                line = float(line)
                line = fabs(line) * pow(10, 17)
                processed_data.append(float(line))
            except ValueError:
                pass  # Ignore lines that are not valid 
        return processed_data
    
    
    def og_signal(raw, generator): # Subtracts the generator signal to get the "noise"
        result = []
        for i in range(len(raw)):
            result.append(raw[i]-generator[i])
        return result
    
    
    processed_data = data_process(y)
    y = dct(processed_data, norm='ortho')
    
    def bin_data(myArray,where):  # Generating a binary sequence from the noise
        output = []
        z= 0
        o= 1
        for i in myArray:
            if i > where:
                output.append(z)
            if i < where:
                output.append(o)
            else:
                pass
        return output
                
    
    yr = idct(y, norm='ortho')
    result= og_signal(processed_data, yr)
    
    result_sort = []
    for i in result:
        result_sort.append(i)
        
    result_sort.sort()
    mid = len(result_sort) // 2 
    median = (result_sort[mid] + result_sort[~mid]) / 2 
        
    
    final_data = bin_data(result, median)
    with open("final_result_v"+ str(f) +".txt", 'w') as file:
        for item in final_data:
            final_item = str(item)
            file.write("%s\n" % final_item)
    
    
    if verbose:
        num0 = 0 
        num1 = 0
        for i in final_data:
            if i == 0: 
                num0 += 1
            if i == 1:
                num1 += 1
        dif = fabs(num0 - num1)
        print('final_result_v' + str(f) + ':\n\tNumber of 0-s:', num0, '\n\tNumber of 1-s:', num1, '\n\tDifference between the number of 1-s and 0-s:', dif, '\n\n')
        # If the difference is greater than approximately 1% of the sequences's lenght, most tests should fail initially







