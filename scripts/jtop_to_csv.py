import csv
import sys

#script to transorm the output of jtop into CSV for import into excel

file_to_parse = sys.argv[1]

with open(file_to_parse, 'r') as file:
    lines = file.readlines()

    #strip any leading/trailing whitespaces and split the lines
    entries = [line.strip() for line in lines if line.strip()]
    formatted_data = []

    for i in range(0, len(entries), 4):
        time_elapsed = float(entries[i].split(": ")[1])
        gpu_load = entries[i + 1].split(": ")[1] 
        cpu_user_load = round(float(entries[i + 2].split(": ")[1]), 2)
        memory_used = int(entries[i + 3].split(": ")[1])

        formatted_data.append({
            "Time elapsed": time_elapsed,
            "GPU load": gpu_load,
            "CPU user load": cpu_user_load,
            "Memory used": memory_used
        })

with open('formatted_data.csv', 'w') as csvfile:
    fieldnames = ['Time elapsed', 'GPU load', 'CPU user load', 'Memory used']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for entry in formatted_data:
        writer.writerow(entry)
