from jtop import jtop
import time 

#based on https://rnext.it/jetson_stats/reference/jtop.html#jtop.jtop.loop_for_ever

start = time.time()

def read_stats(jetson):
    global start
    time_elapsed = str(round(time.time() - start, 2))
    gpu_load = str(jetson.gpu['ga10b']['status']['load'])
    memory = str(jetson.memory['RAM']['used'])
    cpu_load = str(round(jetson.cpu['total']['user'], 2)) #deprecated: cpu load is not used for evaluation 
    print(time_elapsed + "," + gpu_load + "," + memory + "," + cpu_load)

print("Time elapsed,GPU load,Memory used,CPU user load") #csv header
jetson = jtop()

jetson.attach(read_stats)
jetson.loop_for_ever()
