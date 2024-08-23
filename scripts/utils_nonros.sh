#!/bin/bash

output_path=output/path

(python3 -u track_jtop.py > ${output_path}/jtop_output.csv)&
jtop_pid=$!

((top -d 1 -b) > ${output_path}/top_output.txt)&
top_pid=$!

echo "Started top with pid $top_pid" 
echo "Started jtop with pid $jtop_pid" 
sleep 2


#RGBD
#VOOM
#((./rgbd_tum_with_ellipse ../Vocabulary/ORBvoc.txt ../Cameras/TUM3.yaml /home/jonas/Downloads/freiburg/rgbd_dataset_freiburg3_walking_xyz/ /home/jonas/Downloads/freiburg/rgbd_dataset_freiburg3_walking_xyz/association.txt ../Data/own_detections/detections_yolov8x_tum3_walking_xyz.json points fr3) > ${output_path}/slam_output.txt)&

#Crowd-SLAM
((./rgbd Vocabulary/ORBvoc.txt Examples/RGB-D/TUM2.yaml ~/Downloads/freiburg/rgbd_dataset_freiburg3_long_office_household/ ~/Downloads/freiburg/rgbd_dataset_freiburg3_long_office_household/association.txt) > ${output_path}/slam_output.txt)&

#MONO
#oa-slam
#((./oa-slam ../Vocabulary/ORBvoc.txt ../Cameras/TUM3.yaml /home/jonas/Downloads/freiburg/rgbd_dataset_freiburg3_walking_xyz/rgb.txt ../Data/own_detections/fr3_walking_xyz.json null points+objects result) > ${output_path}/slam_output.txt)&

#ORB-SLAM
#((./mono_tum ../../Vocabulary/ORBvoc.txt TUM2.yaml ~/Downloads/freiburg/rgbd_dataset_freiburg2_360_hemisphere) > ${output_path}/slam_output.txt)&
#((./mono_kitti ../../Vocabulary/ORBvoc.txt KITTI04-12.yaml ~/Downloads/kitti/data_odometry_gray/dataset/sequences/04/) > ${output_path}/slam_output.txt)&

#LIFT-SLAM
#((./SLAM/Examples/Monocular/mono_kitti_lift SLAM/Vocabulary/ORBvoc.txt SLAM/Examples/Monocular/KITTI00-02.yaml data/00/) > ${output_path}/slam_output.txt)&

slam_pid=$!
echo "SLAM pid is $slam_pid"
 
while ps -p $slam_pid > /dev/null; do
	sleep 1
done 
echo "Killing tracker..." 

sleep 2

kill $jtop_pid
kill $top_pid

echo "SLAM finished, tracker stopped" 
