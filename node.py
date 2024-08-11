import rclpy
import rclpy.node
import cv2 
import zed
from sensor_msgs.msg import Image

class MinimalParam(rclpy.node.Node):
    def __init__(self):
        super().__init__('minimal_param_node')

        self.declare_parameter('FPS', 60)
        self.declare_parameter('RESOLUTION', 100)
        self.declare_parameter('exposure_time', 100)
        self.publisher_ = self.create_publisher(Image, 'topic', 10)
        self.timer = self.create_timer(1, self.timer_callback)
        image_zed = sl.Mat(zed.get_camera_information().camera_resolution.width, zed.get_camera_information().camera_resolution.height, sl.MAT_TYPE.U8_C4)
        # Retrieve data in a numpy array with get_data()
        image_ocv = image_zed.get_data()
        if zed.grab() == sl.ERROR_CODE.SUCCESS :
    # Retrieve the left image in sl.Mat
        zed.retrieve_image(image_zed, sl.VIEW.LEFT)
        # Use get_data() to get the numpy array
        image_ocv = image_zed.get_data()
        # Display the left image from the numpy array
        depth_zed = sl.Mat(zed.get_camera_information().camera_resolution.width, zed.get_camera_information().camera_resolution.height, sl.MAT_TYPE.F32_C1)
        self.publisher_.publish(
        if zed.grab() == sl.ERROR_CODE.SUCCESS :
            # Retrieve depth data (32-bit)
            zed.retrieve_measure(depth_zed, sl.MEASURE.DEPTH)
            # Load depth data into a numpy array
            depth_ocv = depth_zed.get_data()
            # Print the depth value at the center of the image
            print(depth_ocv[int(len(depth_ocv)/2)][int(len(depth_ocv[0])/2)])
            image_depth_zed = sl.Mat(zed.get_camera_information().camera_resolution.width, sl.get_camera_information().camera_resolution.height, sl.MAT_TYPE.U8_C4)

        if zed.grab() == sl.ERROR_CODE.SUCCESS :
            # Retrieve the normalized depth image
            zed.retrieve_image(image_depth_zed, sl.VIEW.DEPTH)
            # Use get_data() to get the numpy array
            image_depth_ocv = image_depth_zed.get_data()
            # Display the depth view from the numpy array
            cv2.imshow("Image", image_depth_ocv)
def main():
    rclpy.init()
    node = MinimalParam()
    rclpy.spin(node)

if __name__ == '__main__':
    main()