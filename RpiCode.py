import time
import board
import busio
from digitalio import DigitalInOut
import adafruit_max30102
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250
from pyrebase import pyrebase
import pybluez
import pyaudio
import wave
import picamera

config = {
    "apiKey": "AIzaSyAc4mIB3jgxScJYZTandxDvhemAEKbi_2Q",
    "authDomain": "i2hdemo.firebaseapp.com",
    "databaseURL": "https://i2hdemo-default-rtdb.firebaseio.com",
    "storageBucket": "gs://i2hdemo.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_max30102.MAX30102(i2c)
i2c_mpu = busio.I2C(board.SCL, board.SDA)
mpu = MPU9250(i2c_mpu, address=0x69)
bluetooth_mac = "XX:XX:XX:XX:XX:XX"
output_file = "output.wav"
record_audio(bluetooth_mac, output_file)
video_file = "evidence.h264"
recording_duration = 6*60*60  

def capture_video(output_file, duration):
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_recording(output_file)
        camera.wait_recording(duration)
        camera.stop_recording()
      
def record_audio(mac_address, output_file):
    socket = pybluez.BluetoothSocket(pybluez.RFCOMM)
    socket.connect((mac_address, 1))
    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=44100,
        input=True,
        input_device_index=socket.fileno(),
        frames_per_buffer=1024
    )
  
def read_sensor_data():
    max30102_data = sensor.read_sequential()
    accel = mpu.readAccelerometerMaster()
    gyro = mpu.readGyroscopeMaster()
    mag = mpu.readMagnetometerMaster()
    return {
        "max30102": max30102_data,
        "mpu9255": {
            "acceleration": accel,
            "gyroscope": gyro,
            "magnetometer": mag
        }
    }
def send_to_firebase(data):
    db.child("sensor_data").push(data)
  
while True:
    sensor_data = read_sensor_data()
    send_to_firebase(sensor_data)
    data = stream.read(1024)
    frames.append(data)
    capture_video(video_file, recording_duration)
    time.sleep(1)
