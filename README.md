# AIoT-Smart-EyeWear-for-Law-Enforcement
The proposed solution is a pair of AIoT smart glasses whose lens are made of clear polycarbonate of 2mm thickness which is customized to be scratch proof. The body of the device is 3D 
printed using Acrylonitrile Butadiene Styrene (ABS) which has high impact resistance and light weight compared to other materials in market. The temple of the smart glasses measure 82mm 
in length, 42mm in width and 26mm in height. The device is provided with an elastic strap connected to the temples which is to be worn around the head. An SBC (Raspberry pi Zero 2W) is 
used as processor with 32GB SD card as storage. The device is powered by Li-ion battery of 3.7v 3700mAh which is stepped up to 5V using a boost converter. NEO-M8M GPS module is used for 
location monitoring, MAX30102 heart rate and pulse oximeter sensor for health monitoring, 5MP raspberry pi spy camera module for deploying face recognition and video recording for 
evidence collection, MPU9255 Gyroscope accelerometer magnetometer sensor for activity monitoring, INA219 current and voltage sensor module for battery level monitoring, speaker and 
microphone are placed on the glasses for the user to communicate with the smart glasses. All the sensors communicate with raspberry pi using I2C communication protocol. The superior 
officer responsible for each subsector is provided with an android application to monitor each police personnel’s location and health. The device gets online with the help of user’s 
internet and each user mobile MAC and smart glasses MAC address are cross referenced and uploaded to cloud. The superior officer can assign the location of each police personnel 
through the application and are received by the user through smart glasses and SMS. The video recording of the glasses gets initiated when, there is a spike in heart rate of police, 
sudden noise or when the police personnel runs or falls down which is detected by the gyroscope and accelerometer sensor. The total weight of the prototype is calculated to be 233 grams. The load current of the glasses is 1.2 amps and the battery life of the prototype is calculated to be approximately 2.22 hours.

<img width="524" alt="CAD design" src="https://github.com/OptiCops2023/AIoT-Smart-EyeWear-for-Law-Enforcement/assets/130657253/8fcc9e8e-f9e5-4ad7-9d51-f59895b5a4a5">
