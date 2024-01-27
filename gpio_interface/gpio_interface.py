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
            self.declare(str(i), False)

        #RPi.GPIO.setup(16, RPi.GPIO.OUT)
        #RPi.GPIO.setup(17, RPi.GPIO.OUT)
        #RPi.GPIO.setup(18, RPi.GPIO.OUT)
        #RPi.GPIO.setup(19, RPi.GPIO.OUT)
        #RPi.GPIO.setup(22, RPi.GPIO.OUT)
        #RPi.GPIO.setup(25, RPi.GPIO.OUT)

        self.log=self.get_logger()

        #self.declare_parameter('17', False)
        #self.declare_parameter('18', False)
        #self.declare_parameter('19', False)
        #self.declare_parameter('22', False)
        #self.declare_parameter('25', False)
        
        self.add_on_set_parameters_callback(self.function)

    def function(self, params):
        for param in params:
            if param.name == '16':

                RPi.GPIO.output(16, param.value)
                self.log.info(str(param.value))

            if param.name == '17':

                RPi.GPIO.output(17, param.value)
                self.log.info(str(param.value))

            if param.name == '18':

                RPi.GPIO.output(18, param.value)
                self.log.info(str(param.value))

            if param.name == '19':

                RPi.GPIO.output(19, param.value)
                self.log.info(str(param.value))

            if param.name == '22':

                RPi.GPIO.output(22, param.value)
                self.log.info(str(param.value))

            if param.name == '25':

                RPi.GPIO.output(25, param.value)
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