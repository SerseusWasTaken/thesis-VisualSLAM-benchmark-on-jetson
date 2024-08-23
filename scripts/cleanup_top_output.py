import sys

#script to clean the output of top. at the moment it only filters processes with 0 % CPU load
#expects top output as argument

class TopProcess:
    def __init__(self, pid, user, pr, ni, virt, res, shr, s, cpu, mem, time, command):
        #descriptions are from top manual
        self.pid = pid
        self.user = user
        self.pr = str(pr) #priority
        self.ni = int(ni)
        self.virt = str(virt) #everything in-use and/or reserved (all quadrants) + swap
        self.res = res #anything occupying physical memory; needs complex string parsing since values such as 982.2m are possible
        self.shr = int(shr) #subset of RES (excludes 1, includes all 2 & 4, some 3)
        self.s = s #The status of the task which can be one of:
               #D = uninterruptible sleep
               #I = idle
               #R = running
               #S = sleeping
               #T = stopped by job control signal
               #t = stopped by debugger during trace
               #Z = zombie
        self.cpu = float(cpu)
        self.mem =float(mem) #simply RES divided by total physical memory
        self.time = time #total CPU time the task has used since it started
        self.command = command #command line to start the program

def is_int(str):
    try: 
        int(str) 
        return True
    except ValueError:
        return False

def line_to_TopProcess(line):
    return TopProcess(line[0],line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8],
     line[9], line[10], line[11])

def process_header(line, split, file):
    file.write(line)

def process_proc(line, split, file):
    proc = line_to_TopProcess(split)
    if proc.cpu > 0.0: #filter all entries with cpu load 0% 
        file.write(line)

file_path = sys.argv[1]
output_path='./cleaned_top_output.txt'
last_line_proc = False
with open(output_path, 'w') as output_file:
    with open(file_path, 'r') as file:
        for line in file:
            split = line.split()
            if (len(split) > 0): #check if line is not empty
                if is_int(split[0]): #process lines start with PID
                    process_proc(line, split, output_file)
                    if not last_line_proc:
                        last_line_proc = True
                else: #header lines start with a string
                    process_header(line, split, output_file)
            elif last_line_proc: #write \n when next top output tick follows
                output_file.write('\n')
                last_line_proc = False

            
            
        