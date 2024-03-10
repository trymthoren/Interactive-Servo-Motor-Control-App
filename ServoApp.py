from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color, Line
from kivy.animation import Animation
from kivy.properties import NumericProperty
from math import sin, cos


class ServoDisplay(BoxLayout):
    angle = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(0.7, 0.7, 0.7, 1)  # Gray color for background
            self.rect = Rectangle(pos=self.pos, size=self.size)

        with self.canvas:
            Color(0.2, 0.2, 0.2)  # Darker color for servo
            self.servo_body = Rectangle(size=(150, 50))
            Color(1, 0, 0, 1)  # Red for the servo arm
            self.servo_arm = Line(points=[self.center_x, self.center_y,
                                          self.center_x, self.center_y + 50], width=2)

        self.bind(pos=self.update_rect, size=self.update_rect)
        self.bind(angle=self.update_arm)  # Update arm when angle changes

    def animate_to_angle(self, angle):
        anim = Animation(angle=angle, duration=1)
        anim.start(self)

    def calculate_arm_points(self):
        length = 60*2
        rad_angle = (self.angle - 90) * (3.14159 / 180)
        end_x = self.center_x + length * cos(rad_angle)
        end_y = self.center_y + length * sin(rad_angle)
        return [self.center_x, self.center_y, end_x, end_y]

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.servo_body.pos = (self.center_x - 75, self.center_y - 25)
        self.servo_arm.points = self.calculate_arm_points()

    def update_arm(self, *args):
        self.servo_arm.points = self.calculate_arm_points()

    def set_angle(self, angle):
        self.angle = angle  # Directly set the angle when using the slider

    def animate_angle(self, angle):
        self.animate_to_angle(angle)  # Animate the angle when using the code


class ServoApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.servo_display = ServoDisplay(size_hint=(1, 0.6))
        layout.add_widget(self.servo_display)

        self.slider = Slider(min=0, max=180, value=0, size_hint=(1, 0.1))
        self.slider.bind(value=self.on_angle_change)
        layout.add_widget(self.slider)

        self.label = Label(text='Angle: 0°', size_hint=(1, 0.1))
        layout.add_widget(self.label)

        code_box = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        self.code_input = TextInput(hint_text='Enter Python code...')
        code_box.add_widget(self.code_input)
        self.run_button = Button(text="Run")
        self.run_button.bind(on_press=self.run_code)
        code_box.add_widget(self.run_button)
        layout.add_widget(code_box)

        return layout

    def on_angle_change(self, instance, angle):
        self.label.text = f"Angle: {angle:.2f}°"
        self.servo_display.set_angle(angle)

    def run_code(self, instance):
        user_code = self.code_input.text

        def servo_turn(angle):
            self.servo_display.animate_angle(angle)
            self.label.text = f"Angle: {angle:.2f}°"  # Update the label

        # Only allow certain commands
        allowed_funcs = {'servo_turn': servo_turn}

        try:
            exec(user_code, {}, allowed_funcs)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    ServoApp().run()
