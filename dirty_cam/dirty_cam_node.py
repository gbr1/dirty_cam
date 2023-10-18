import cv2

import rclpy
from rclpy.node import Node


from cv_bridge import CvBridge
from sensor_msgs.msg import Image


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('dirty_cam')
        self.camera
        self.image_publisher = self.create_publisher(Image, '/dirty_cam/image_raw', 10)
        timer_period = 0.001  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Image()
        time_now = self.get_clock().now().to_msg()
        msg.header.frame_id='base_link'
        msg.header.stamp=time_now
        msg.height=480
        msg.width=640
        msg.data= 

        self.image_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
