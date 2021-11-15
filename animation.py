# file: animation.py

from manim import *

# Arduino
ARD_V5 = (-3.66, -2.71, 0)
ARD_GND_1 = (-3.55, -2.71, 0)
ARD_GND_2 = (-3.44, -2.71, 0)
ARD_PIN_6 = (-3.15, -0.28, 0)
ARD_PIN_7 = (-3.26, -0.28, 0)
ARD_PIN_9 = (-3.61, -0.28, 0)

# Sensor
SENSOR_VCC = (0.29, -2.52, 0)
SENSOR_TRIG = (0.41, -2.52, 0)
SENSOR_ECHO = (0.54, -2.52, 0)
SENSOR_GND = (0.66, -2.52, 0)

# Servo
SERVO_SIGNAL = (0.82, 0.38, 0)
SERVO_VCC = (0.93, 0.38, 0)
SERVO_GND = (1.04, 0.38, 0)

class CircuitDiagram(Scene):
    def construct(self):
        
        arduino = ImageMobject("C:/Users/PIYUSH/Downloads/arduino-publicdomain.png")
        sensor = ImageMobject("C:/Users/PIYUSH/Downloads/ultrasonic_sensor.png")
        servo = ImageMobject("C:/Users/PIYUSH/Downloads/servo.png")

        text1 = Text("Smart Dustbin Circuit Diagram")
        text2 = Text("Here Are The Wirings", font_size=72)

        text3 = Text("Smart Dustbin Circuit Diagram", font_size=24)
        text3.set_x(-4)
        text3.set_y(3)

        ard_text = Text("Arduino UNO", font_size=24)
        sensor_text = Text("Ultrasonic Sensor", font_size=24)
        servo_text = Text("Servo Motor", font_size=24)

        text4 = Text("Our Group Members", font_size=80)
        text4.set_y(2.5)

        gp_1 = Text("Vaibhav Kumar Mishra", font_size=28)
        gp_2 = Text("Harsh Narayan Jha", font_size=28)
        gp_3 = Text("Sakshi", font_size=28)
        gp_4 = Text("Rishabh Bhaskar", font_size=28)

        gp_1.set_y(1)
        gp_2.set_y(0)
        gp_3.set_y(-1)
        gp_4.set_y(-2)

        ard_text.set_x(-3.8)
        ard_text.set_y(0.2)

        sensor_text.set_x(3.4)
        sensor_text.set_y(-2)

        servo_text.set_x(2.5)
        servo_text.set_y(1.8)

        self.play(Create(text1))
        self.wait(2)
        self.play(FadeOut(text1))

        arduino.scale(0.2)
        arduino.set_x(-4)
        arduino.set_y(-1.5)

        sensor.scale(0.2)
        sensor.set_x(0.5)
        sensor.set_y(-2)

        servo.set_x(1)
        servo.set_y(1.5)

        #grid = NumberPlane()
        self.play(FadeIn(arduino), FadeIn(sensor), FadeIn(servo))

        self.play(FadeIn(ard_text))
        self.play(FadeIn(sensor_text))
        self.play(FadeIn(servo_text))

        self.wait(1)

        self.play(FadeOut(servo_text), FadeOut(sensor_text), FadeOut(ard_text))

        self.play(FadeIn(text3))

        self.wait(1)

        self.add(text2)
        self.wait(2.5)
        self.remove(text2)

        self.make_sensor_lines()
        self.make_servo_lines()
        self.draw_sensor_connections()
        self.draw_servo_connections()

        self.wait(4)
        self.clear()

        self.wait(1)
        self.play(Create(text4))
        self.wait(0.5)
        self.add(gp_1)
        self.wait(0.5)
        self.add(gp_2)
        self.wait(0.5)
        self.add(gp_3)
        self.wait(0.5)
        self.add(gp_4)

        self.wait(5)
        #self.play(Create(grid))

        thanks = Text("Thanks", font_size=90)
        self.play(FadeOut(text4), FadeOut(gp_1), FadeOut(gp_2), FadeOut(gp_3), FadeOut(gp_4))
        self.wait(0.5)

        self.play(Create(thanks))
        self.wait(3)

    def make_sensor_lines(self):
        # +5V to Sensor VCC
        self.line_5v_sensor_1 = Line(start=ARD_V5, end=(ARD_V5[0], -3.5, 0), color=PURE_RED)
        self.line_5v_sensor_2 = Line(start=self.line_5v_sensor_1.end, end=(SENSOR_VCC[0], -3.5, 0), color=PURE_RED)
        self.line_5v_sensor_3 = Line(start=self.line_5v_sensor_2.end, end=SENSOR_VCC, color=PURE_RED)

        # GND to Sensor GND
        self.line_gnd_sensor_1 = Line(start=ARD_GND_1, end=(ARD_GND_1[0], -3, 0), color=LIGHT_BROWN)
        self.line_gnd_sensor_2 = Line(start=self.line_gnd_sensor_1.end, end=(SENSOR_GND[0], -3, 0), color=LIGHT_BROWN)
        self.line_gnd_sensor_3 = Line(start=self.line_gnd_sensor_2.end, end=SENSOR_GND, color=LIGHT_BROWN)

        # PIN 6 to Sensor TRIG
        self.line_pin_6_sensor_trig_1 = Line(start=ARD_PIN_6, end=(ARD_PIN_6[0], 0.5, 0), color=GRAY)
        self.line_pin_6_sensor_trig_2 = Line(start=self.line_pin_6_sensor_trig_1.end, end=(-1, 0.5, 0), color=GRAY)
        self.line_pin_6_sensor_trig_3 = Line(start=self.line_pin_6_sensor_trig_2.end, end=(-1, -2.8, 0), color=GRAY)
        self.line_pin_6_sensor_trig_4 = Line(start=self.line_pin_6_sensor_trig_3.end, end=(SENSOR_TRIG[0], -2.8, 0), color=GRAY)
        self.line_pin_6_sensor_trig_5 = Line(start=self.line_pin_6_sensor_trig_4.end, end=SENSOR_TRIG, color=GRAY)

        # Pin 7 to Sensor ECHO
        self.line_pin_7_sensor_echo_1 = Line(start=ARD_PIN_7, end=(ARD_PIN_7[0], 0.25, 0), color=PURE_GREEN)
        self.line_pin_7_sensor_echo_2 = Line(start=self.line_pin_7_sensor_echo_1.end, end=(-1.5, 0.25, 0), color=PURE_GREEN)
        self.line_pin_7_sensor_echo_3 = Line(start=self.line_pin_7_sensor_echo_2.end, end=(-1.5, -2.9, 0), color=PURE_GREEN)
        self.line_pin_7_sensor_echo_4 = Line(start=self.line_pin_7_sensor_echo_3.end, end=(SENSOR_ECHO[0], -2.9, 0), color=PURE_GREEN)
        self.line_pin_7_sensor_echo_5 = Line(start=self.line_pin_7_sensor_echo_4.end, end=SENSOR_ECHO, color=PURE_GREEN)

        # Sensor Connections End

    def make_servo_lines(self):
        # +5V to Servo
        self.line_5v_servo_1 = Line(start=(SENSOR_VCC[0], -3.5, 0), end=(3, -3.5, 0), color=PURE_RED)
        self.line_5v_servo_2 = Line(start=self.line_5v_servo_1, end=(3, 0, 0), color=PURE_RED)
        self.line_5v_servo_3 = Line(start=self.line_5v_servo_2, end=(SERVO_VCC[0], 0, 0), color=PURE_RED)
        self.line_5v_servo_4 = Line(start=self.line_5v_servo_3, end=SERVO_VCC, color=PURE_RED)

        # GND to Servo
        self.line_gnd_servo_1 = Line(start=(SENSOR_GND[0], -3, 0), end=(2.5, -3, 0), color=LIGHT_BROWN)
        self.line_gnd_servo_2 = Line(start=self.line_gnd_servo_1, end=(2.5, -0.2, 0), color=LIGHT_BROWN)
        self.line_gnd_servo_3 = Line(start=self.line_gnd_servo_2, end=(SERVO_GND[0], -0.2, 0), color=LIGHT_BROWN)
        self.line_gnd_servo_4 = Line(start=self.line_gnd_servo_3, end=SERVO_GND, color=LIGHT_BROWN)

        # Pin 9 to Servo
        self.line_pin_9_servo_signal_1 = Line(start=ARD_PIN_9, end=(ARD_PIN_9[0], 1, 0), color=YELLOW_E)
        self.line_pin_9_servo_signal_2 = Line(start=self.line_pin_9_servo_signal_1, end=(-0.5, 1, 0), color=YELLOW_E)
        self.line_pin_9_servo_signal_3 = Line(start=self.line_pin_9_servo_signal_2, end=(-0.5, 0, 0), color=YELLOW_E)
        self.line_pin_9_servo_signal_4 = Line(start=self.line_pin_9_servo_signal_3, end=(SERVO_SIGNAL[0], 0, 0), color=YELLOW_E)
        self.line_pin_9_servo_signal_5 = Line(start=self.line_pin_9_servo_signal_4, end=SERVO_SIGNAL, color=YELLOW_E)

    def draw_sensor_connections(self):
        self.play(Create(self.line_5v_sensor_1))
        self.play(Create(self.line_5v_sensor_2))
        self.play(Create(self.line_5v_sensor_3))

        self.play(Create(self.line_gnd_sensor_1))
        self.play(Create(self.line_gnd_sensor_2))
        self.play(Create(self.line_gnd_sensor_3))

        self.play(Create(self.line_pin_6_sensor_trig_1))
        self.play(Create(self.line_pin_6_sensor_trig_2))
        self.play(Create(self.line_pin_6_sensor_trig_3))
        self.play(Create(self.line_pin_6_sensor_trig_4))
        self.play(Create(self.line_pin_6_sensor_trig_5))

        self.play(Create(self.line_pin_7_sensor_echo_1))
        self.play(Create(self.line_pin_7_sensor_echo_2))
        self.play(Create(self.line_pin_7_sensor_echo_3))
        self.play(Create(self.line_pin_7_sensor_echo_4))
        self.play(Create(self.line_pin_7_sensor_echo_5))

    def draw_servo_connections(self):
        self.play(Create(self.line_5v_servo_1))
        self.play(Create(self.line_5v_servo_2))
        self.play(Create(self.line_5v_servo_3))
        self.play(Create(self.line_5v_servo_4))

        self.play(Create(self.line_gnd_servo_1))
        self.play(Create(self.line_gnd_servo_2))
        self.play(Create(self.line_gnd_servo_3))
        self.play(Create(self.line_gnd_servo_4))

        self.play(Create(self.line_pin_9_servo_signal_1))
        self.play(Create(self.line_pin_9_servo_signal_2))
        self.play(Create(self.line_pin_9_servo_signal_3))
        self.play(Create(self.line_pin_9_servo_signal_4))
        self.play(Create(self.line_pin_9_servo_signal_5))