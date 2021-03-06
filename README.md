


Update by me
------------------------
Use arduino code from : 
https://github.com/sparkfun/9DOF_Razor_IMU/releases/tag/V_3.0

it suits Razor 14001, if older version, please use 
https://github.com/sparkfun/9DOF_Razor_IMU/releases/tag/V_2.0

python-visual dowsn't work well in python 2.7.


If you want to run it, you should follow the following steps:
1) upload the firmware into arduino of Razor-imu-9dof, just use the code from sparkfun of 
	9DOF_Razor_IMU-V_3.0_/Firmware/_9DOF_Razor_M0_Firmware/_9DOF_Razor_M0_Firmware.ino
2) if you can not upload it in ubuntu, maybe it is the permission problem of /dev/ttyACM0,
   * check you permission with   
         ll /dev/ttyACM0
      then, follow the blog:
         http://blog.sina.com.cn/s/blog_73000beb0102uzbu.html
   * sign out your ubuntu and sign in again
3) download sudo apt-get install python-visual
4) revise the code, In its default configuration, ``razor_imu_9dof`` expects a yaml config file ``my_razor.yaml`` 


Camera
------------------------
download the qrcode from (you can change the size of the qrcode by edit the size in the link):
https://api.qrserver.com/v1/create-qr-code/?size=600x600&data=Example


Official ROS Documentation
--------------------------
A much more extensive and standard ROS-style version of this documentation can be found on the ROS wiki at:

http://wiki.ros.org/razor_imu_9dof


Install and Configure ROS Package
---------------------------------
1) Install dependencies:

	$ sudo apt-get install python-visual

2) Download code:

	$ cd ~/catkin_workspace/src
	$ git clone https://github.com/KristofRobot/razor_imu_9dof.git
	$ cd ..
	$ catkin_make


Install Arduino firmware
-------------------------
1) For SEN-14001 (9DoF Razor IMU M0), you will need to follow the same instructions as for the default firmware on https://learn.sparkfun.com/tutorials/9dof-razor-imu-m0-hookup-guide and use an updated version of SparkFun_MPU-9250-DMP_Arduino_Library from https://github.com/lebarsfa/SparkFun_MPU-9250-DMP_Arduino_Library (an updated version of the default firmware is also available on https://github.com/lebarsfa/9DOF_Razor_IMU).

2) Open ``src/Razor_AHRS/Razor_AHRS.ino`` in Arduino IDE. Note: this is a modified version
of Peter Bartz' original Arduino code (see https://github.com/ptrbrtz/razor-9dof-ahrs). 
Use this version - it emits linear acceleration and angular velocity data required by the ROS Imu message

3) Select your hardware here by uncommenting the right line in ``src/Razor_AHRS/Razor_AHRS.ino``, e.g.

<pre>
// HARDWARE OPTIONS
/*****************************************************************/
// Select your hardware here by uncommenting one line!
//#define HW__VERSION_CODE 10125 // SparkFun "9DOF Razor IMU" version "SEN-10125" (HMC5843 magnetometer)
//#define HW__VERSION_CODE 10736 // SparkFun "9DOF Razor IMU" version "SEN-10736" (HMC5883L magnetometer)
#define HW__VERSION_CODE 14001 // SparkFun "9DoF Razor IMU M0" version "SEN-14001"
//#define HW__VERSION_CODE 10183 // SparkFun "9DOF Sensor Stick" version "SEN-10183" (HMC5843 magnetometer)
//#define HW__VERSION_CODE 10321 // SparkFun "9DOF Sensor Stick" version "SEN-10321" (HMC5843 magnetometer)
//#define HW__VERSION_CODE 10724 // SparkFun "9DOF Sensor Stick" version "SEN-10724" (HMC5883L magnetometer)
</pre>

4) Upload Arduino sketch to the Sparkfun 9DOF Razor IMU board


Configure
---------
In its default configuration, ``razor_imu_9dof`` expects a yaml config file ``my_razor.yaml`` with:
* USB port to use
* Calibration parameters

An example``razor.yaml`` file is provided.
Copy that file to ``my_razor.yaml`` as follows:

    $ roscd razor_imu_9dof/config
    $ cp razor.yaml my_razor.yaml

Then, edit ``my_razor.yaml`` as needed

Launch
------
Publisher and 3D visualization:

	$ roslaunch razor_imu_9dof razor-pub-and-display.launch

Publisher only:

	$ roslaunch razor_imu_9dof razor-pub.launch

Publisher only with diagnostics:

	$ roslaunch razor_imu_9dof razor-pub-diags.launch

3D visualization only:

	$ roslaunch razor_imu_9dof razor-display.launch


Calibrate
---------
For best accuracy, follow the tutorial to calibrate the sensors:

http://wiki.ros.org/razor_imu_9dof

An updated version of Peter Bartz's magnetometer calibration scripts from https://github.com/ptrbrtz/razor-9dof-ahrs is provided in the ``magnetometer_calibration`` directory.

Update ``my_razor.yaml`` with the new calibration parameters.

Dynamic Reconfigure
-------------------
After having launched the publisher with one of the launch commands listed above, 
it is possible to dynamically reconfigure the yaw calibration.

1) Run:

    $ rosrun rqt_reconfigure rqt_reconfigure 
    
2) Select ``imu_node``. 

3) Change the slider to move the calibration +/- 10 degrees. 
If you are running the 3D visualization you'll see the display jump when the new calibration takes effect.

The intent of this feature is to let you tune the alignment of the AHRS to the direction of the robot driving direction, so that if you can determine that, for example, the AHRS reads 30 degrees when the robot is actually going at 35 degrees as shown by e.g. GPS, you can tune the calibration to make it read 35. It's the compass-equivalent of bore-sighting a camera.
