import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult
import RPi.GPIO

class Gpio_interface(Node):
    def __init__(self):
        super().__init__('gpio_interface')

        RPi.GPIO.setmode(RPi.GPIO.BCM)
        RPi.GPIO.setup(2, RPi.GPIO.OUT)

        self.log=self.get_logger()

        self.declare_parameter('gpio', False)
        self.add_on_set_parameters_callback(self.function)

    def function(self, params):
        for param in params:
            if param.name == 'gpio':

                RPi.GPIO.output(2, param.value)
                self.log.info(str(param.value))

        return SetParametersResult(successful=True)

        

def main():
    rclpy.init()
    gpio = Gpio_interface()
    rclpy.spin(gpio)

    gpio.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()