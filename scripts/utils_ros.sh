#!/bin/bash

#expects a rosbag file as argument and runs the tracking software while rosbag file plays

if [ $# -eq 0 ]; then
	echo "No rosbag file provided. Aborting"
	exit 1
fi

output_path=output/path


rosbag_file=$1


((top -d 1 -b) > ${output_path}/top_output.txt)&
top_pid=$!

(python3 -u track_jtop.py > ${output_path}/jtop_output.txt)&
jtop_pid=$!

echo "Started top with pid $top_pid" 
echo "Started jtop with pid $jtop_pid" 
sleep 2


(rosbag play $rosbag_file > /dev/null)&
rosbag_pid=$!

echo "Rosbag pid is $rosbag_pid"
 
while ps -p $rosbag_pid > /dev/null; do
	sleep 1
done 
echo "Killing tracker and waiting for 30 seconds..." 

sleep 30 #give some time for buffered frames 

kill $jtop_pid
kill $top_pid

echo "Rosbag playback finished, tracker stopped" 
