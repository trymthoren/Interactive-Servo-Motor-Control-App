# Servo Simulator

This Python application utilizes the Kivy framework to simulate the movement of a servo motor. It offers a graphical user interface where users can adjust the angle of a virtual servo through a slider or by entering Python code directly into a mini-IDE. This project is an excellent starting point for those interested in learning about graphical user interface development in Python, animation with Kivy, and integrating Python code execution within an application.

## Features

- **Virtual Servo Movement**: Simulate the movement of a servo motor graphically.
- **Interactive Slider**: Control the servo's angle with a responsive slider.
- **Mini-IDE**: Execute Python code to control the servo, offering a hands-on experience with Python and Kivy.
- **Animation**: Smooth animation of servo movement to visually represent the angle adjustments.

## Requirements

- Python 3.6 or later
- Kivy

To install Kivy, run:

```sh
pip install kivy
```

## Usage

1. Clone the repository or download the source code.
2. Navigate to the directory containing the application.
3. Run the application with Python:

```sh
python ServoApp.py
```

4. Use the slider to adjust the servo's angle visually or use the mini-IDE to input commands for control.

## Mini-IDE Commands

Within the mini-IDE, you can use the following command to control the servo:

```python
servo_turn(angle)
```

- `angle`: An integer representing the servo's target angle (0 to 180 degrees).

## Expanding the Project

- **Custom Commands**: Add more functions to the allowed_funcs dictionary to expand the capabilities of the mini-IDE.
- **Servo Properties**: Enhance the servo model to include features like speed control or directional movement.
- **IoT Integration**: Extend the application to communicate with real hardware, using it as a control panel for an actual servo motor connected to a Raspberry Pi or Arduino.

## Security Note

This application uses Python's `exec` function to run user-supplied code, which can pose significant security risks. Ensure that you understand the implications and take necessary precautions if adapting this feature for broader use.

## Contribution

Contributions are welcome! Whether it's extending the functionality, improving the UI, or fixing bugs, feel free to fork the repository and submit a pull request.

## License

This project is open-source and available under the MIT License.
