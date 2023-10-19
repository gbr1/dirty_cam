import cv2

import rclpy
from rclpy.node import Node


from cv_bridge import CvBridge
from sensor_msgs.msg import Image


class CameraPublisher(Node):
    def __init__(self):
        super().__init__('dirty_cam')
        #self.camera = cv2.VideoCapture(0)
        self.camera = cv2.VideoCapture('v4l2src device=/dev/video3 ! video/x-raw, framerate=30/1, width=640, height=480 ! appsink', cv2.CAP_GSTREAMER)
        self.cv_bridge = CvBridge()
        self.image_publisher = self.create_publisher(Image, '/dirty_cam/image_raw', 1)
        timer_period = 0.001
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        ret, capture = self.camera.read()
        self.image_publisher.publish(self.cv_bridge.cv2_to_imgmsg(capture,"bgr8"))


def main(args=None):
    rclpy.init(args=args)
    camera_publisher = CameraPublisher()
    rclpy.spin(camera_publisher)
    camera_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
