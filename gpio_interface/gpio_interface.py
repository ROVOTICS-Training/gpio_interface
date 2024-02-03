import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult
import RPi.GPIO

class Gpio_interface(Node):
    def __init__(self):
        super().__init__('gpio_interface')

        RPi.GPIO.setmode(RPi.GPIO.BCM)

        self.gpio_pins = [16,17,18,19,22,25]

        for i in self.gpio_pins:
            RPi.GPIO.setup(i, RPi.GPIO.OUT)
            self.declare_parameter(str(i), False)

        self.log=self.get_logger()        
        self.add_on_set_parameters_callback(self.function)

    def function(self, params):
        for param in params:
            RPi.GPIO.output(int(param.name), param.value)
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