from FrequencyTest import FrequencyTest
from RunTest import RunTest
from Matrix import Matrix
from Spectral import SpectralTest
from TemplateMatching import TemplateMatching
from Complexity import ComplexityTest
from Serial import Serial
from ApproximateEntropy import ApproximateEntropy
from CumulativeSum import CumulativeSums
from RandomExcursions import RandomExcursions


for f in range(1,2):
    FILE_NAME = "final_result_v"+ str(f) +".txt"  # Specify the file extension
    NUM_OF_DATA = 60000
    print('File',f,"'s test:")
    
    with open(FILE_NAME, 'r') as file:
        y = file.read()
    
    def data_process(data):
        data = data.split('\n')  # Split the string into lines
        binary_data = []
        for line in data:
            try:
                binary_data.append(float(line))
            except ValueError:
                pass  # Ignore lines that are not valid 
        return binary_data
    
    def dataProcessStr(data): #Making strings of the arrays for the tests
        binary_data_str = ""
        for i in data:
            if i == 0:
                binary_data_str += '0'
            if i == 1:
                binary_data_str += '1'
        return  binary_data_str
    
    binary_data1 = data_process(y)
    binary_data = dataProcessStr(binary_data1)
    
    print('The statistical test of the Binary Expansion of e')
    print(' 1.: Frequency Test:\t\t\t\t\t\t\t\t', FrequencyTest.monobit_test(binary_data[:1000000]))
    print(' 2.: Block Frequency Test:\t\t\t\t\t\t\t', FrequencyTest.block_frequency(binary_data[:1000000]))
    print(' 3.: Run Test:\t\t\t\t\t\t\t\t\t\t', RunTest.run_test(binary_data[:1000000]))
    print(' 4.: Run Test (Longest Run of Ones): \t\t\t\t', RunTest.longest_one_block_test(binary_data[:1000000]))
    print(' 5.: Binary Matrix Rank Test:\t\t\t\t\t\t', Matrix.binary_matrix_rank_text(binary_data[:1000000]))
    print(' 6.: Discrete Fourier Transform (Spectral) Test:\t', SpectralTest.spectral_test(binary_data[:1000000]))
    print(' 7.: Non-overlapping Template Matching Test:\t\t', TemplateMatching.non_overlapping_test(binary_data[:1000000]))
    print(' 8.: Overlappong Template Matching Test: \t\t\t', TemplateMatching.overlapping_patterns(binary_data[:1000000]))
    print(' 9.: Linear Complexity Test:\t\t\t\t\t\t', ComplexityTest.linear_complexity_test(binary_data[:1000000]))
    print('10.: Serial Test:\t\t\t\t\t\t\t\t\t', Serial.serial_test(binary_data[:1000000]))
    print('11.: Approximate Entropy Test:\t\t\t\t\t\t', ApproximateEntropy.approximate_entropy_test(binary_data[:1000000]))
    print('12.: Cumulative Sums (Forward):\t\t\t\t\t', CumulativeSums.cumulative_sums_test(binary_data[:1000000], 0))
    print('12.: Cumulative Sums (Backward):\t\t\t\t\t', CumulativeSums.cumulative_sums_test(binary_data[:1000000], 1))
    result = RandomExcursions.random_excursions_test(binary_data[:1000000])
    print('13.: Random Excursion Test:')
    print('\t\t STATE \t\t\t xObs \t\t\t\t P-Value \t\t\t Conclusion')
    
    for item in result:
        print('\t\t', repr(item[0]).rjust(4), '\t\t', item[2], '\t\t', repr(item[3]).ljust(14), '\t\t',
              (item[4] >= 0.01))
    
    result = RandomExcursions.variant_test(binary_data[:1000000])
    
    print('14.: Random Excursion Variant Test:\t\t\t\t\t\t')
    print('\t\t STATE \t\t COUNTS \t\t\t P-Value \t\t Conclusion')
    for item in result:
        print('\t\t', repr(item[0]).rjust(4), '\t\t', item[2], '\t\t', repr(item[3]).ljust(14), '\t\t',
              (item[4] >= 0.01))
    print('\n\n\n')