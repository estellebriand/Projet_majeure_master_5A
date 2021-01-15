#!/usr/bin/env python

from MPU6050 import MPU6050
import rospy
from std_msgs import String

class imu_publisher():
    def __init__(self):
        rospy.init_node('raspberry_publisher_imu', anonymous=True)

        self.imu_pub = rospy.Publisher('/imu', String, queue_size=10)

        rate = rospy.Rate(2) # 10hz
        rate.sleep()

        rospy.loginfo("Node [raspberry_publisher_imu] started")
        
        self.process()
        rospy.spin()
        
    def process(self):
        i2c_bus = 1
        device_address = 0x68
        # The offsets are different for each device and should be changed
        # accordingly using a calibration procedure
        x_accel_offset = -5489
        y_accel_offset = -1441
        z_accel_offset = 1305
        x_gyro_offset = -2
        y_gyro_offset = -72
        z_gyro_offset = -5
        enable_debug_output = True

        mpu = MPU6050(i2c_bus, device_address, x_accel_offset, y_accel_offset,
                      z_accel_offset, x_gyro_offset, y_gyro_offset, z_gyro_offset,
                      enable_debug_output)

        mpu.dmp_initialize()
        mpu.set_DMP_enabled(True)
        mpu_int_status = mpu.get_int_status()
        print(hex(mpu_int_status))

        packet_size = mpu.DMP_get_FIFO_packet_size()
        print(packet_size)
        FIFO_count = mpu.get_FIFO_count()
        print(FIFO_count)

        count = 0
        FIFO_buffer = [0]*64

        FIFO_count_list = list()
        while count < 10000:
            FIFO_count = mpu.get_FIFO_count()
            mpu_int_status = mpu.get_int_status()

            # If overflow is detected by status or fifo count we want to reset
            if (FIFO_count == 1024) or (mpu_int_status & 0x10):
                mpu.reset_FIFO()
                print('overflow!')
            # Check if fifo data is ready
            elif (mpu_int_status & 0x02):
                # Wait until packet_size number of bytes are ready for reading, default
                # is 42 bytes
                while FIFO_count < packet_size:
                    FIFO_count = mpu.get_FIFO_count()
                FIFO_buffer = mpu.get_FIFO_bytes(packet_size)
                accel = mpu.DMP_get_acceleration_int16(FIFO_buffer)
                quat = mpu.DMP_get_quaternion_int16(FIFO_buffer)
                grav = mpu.DMP_get_gravity(quat)
                roll_pitch_yaw = mpu.DMP_get_euler_roll_pitch_yaw(quat, grav)
                if count % 100 == 0:
                    #print('roll: ' + str(roll_pitch_yaw.x))
                    #print('pitch: ' + str(roll_pitch_yaw.y))
                    #print('yaw: ' + str(roll_pitch_yaw.z*2))
                    self.imu_pu.publish('roll ' + str(roll_pitch_yaw.x) +'\npitch ' + str(roll_pitch_yaw.y) + '\nyaw ' + str(roll_pitch_yaw.z*2))
                count += 1

if __name__ == '__main__':
    try:
        imu_publisher()
    except rospy.ROSInterruptException:
        pass
