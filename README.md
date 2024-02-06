# AIoT-Smart-EyeWear-for-Law-Enforcement
Background :

Body cameras have become an important tool for law enforcement agencies in recent years. These cameras are typically worn on the chest or shoulder of an officer and can capture video
and audio recordings of interactions with civilians. However, these devices only record videos and audio and sometimes they are blocked by the hand movement of the police officers. 
A randomized controlled trial conducted by the Rialto Police Department in California found that the use of body-worn cameras led to a 59% reduction in use-of-force incidents and an 
87.5% reduction in citizen complaints against officers. A study published in the Journal of Criminal Justice found that the use of body cameras was associated with a 25.2% reduction 
in the odds of a case being prosecuted in court. 

Solution :

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

Benefits :

•	The AIoT smart glasses can contribute to a reduction in the use of force and instances of corruption. By providing real-time monitoring and video recording capabilities, the smart 
glasses promote transparency, accountability, and responsible decision-making among law enforcement personnel. This can lead to improved public trust and confidence in the justice 
system.

•	The integration of a camera and microphone in the smart glasses allows for seamless and efficient evidence collection and suspect identification using face recognition by law 
enforcement officers. This technology enables them to capture crucial moments and events in real-time, improving the accuracy and reliability of collected evidence.

•	The AIoT smart glasses incorporate sensors and IoT technology to monitor the health and safety of police personnel during duty. The data collected by these sensors, such as heart 
rate, temperature, and motion, can be transmitted to a mobile application, enabling real-time monitoring and early detection of any potential health issues or safety risks.



<img width="524" alt="CAD design" src="https://github.com/OptiCops2023/AIoT-Smart-EyeWear-for-Law-Enforcement/assets/130657253/8fcc9e8e-f9e5-4ad7-9d51-f59895b5a4a5">
