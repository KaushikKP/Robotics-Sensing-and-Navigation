#/usr/bin/env bash
sudo chmod 666 /dev/ttyUSB0
sudo chmod 666 /dev/ttyUSB1
export CLASSPATH=$PWD
#lcm-logger --auto-split-hours=0.5 -s ./data/lcm-log-%F-%T &
lcm-logger -s ./log/lcm-log-%F-%T &
lcm-spy & 

#./thruster_animatics_c5 /dev/ttyS11 THR_MAIN 32.5 &   #Thruster
#./fins_pololu /dev/ttyS10 &   #Fins
#./depth_paro /dev/ttyS1 &    #pressure sensor
#./umodem /dev/ttyS14 &
#./imu_xsens /dev/ttyUSB0
#./bmp /dev/ttyUSB0
./imudr.py /dev/ttyUSB0 &
#./gps_xsens /dev/ttyUSB1
#./bmp /dev/ttyUSB1
./utmconv.py /dev/ttyUSB1 &
#./dvl_rdi /dev/ttyS4   #DVL
#./state_estimator &
#./autopilot
kill %1 %2  # %3  %4 %5 %6 %7 %8 %9
