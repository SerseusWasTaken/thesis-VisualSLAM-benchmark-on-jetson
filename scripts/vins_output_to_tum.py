import sys

#this script transforms the output of VINS-FUSION into a by evo parsable TUM format
#after this, timestamps still have to be adjusted since ROS algorithms use current time as starting point instead of 0

file_to_parse = sys.argv[1]
output_name = sys.argv[2]

with open(file_to_parse, 'r') as input_file:
    lines = input_file.readlines()

with open(output_name, 'w') as output_file:
    for line in lines:
        line = line.replace(',', ' ')
        line = line[:-2] + '\n'
        split_text = line.split()
        timestamp = split_text[0]
        adjusted_number = timestamp[:10] + '.' + timestamp[-9:]
        number_to_replace = split_text[0]
        line = line.replace(number_to_replace, adjusted_number)
        output_file.write(line)
