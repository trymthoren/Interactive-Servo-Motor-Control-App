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

Here are the "types" of code you can use within the constraints of the current system:

### 1. Servo Control
The primary capability of your mini-IDE is controlling the virtual servo's angle. The `servo_turn` function is explicitly made available for execution:

```python
servo_turn(45)  # Rotates the servo to 45 degrees
servo_turn(180)  # Rotates the servo to 180 degrees
servo_turn(0)  # Rotates the servo back to 0 degrees
```

### 2. Python Standard Operations
Beyond controlling the servo, the mini-IDE can run any standard Python code that doesn't require additional context or access to external functions and variables not explicitly provided. This includes:

- Mathematical operations:
    ```python
    result = 10 * 5  # Multiplication
    print(result)
    ```
  
- Conditional statements:
    ```python
    angle = 90
    if angle > 45:
        servo_turn(angle)
    else:
        servo_turn(0)
    ```
  
- Loops:
    ```python
    for angle in range(0, 181, 45):
        servo_turn(angle)
        # Assume you add a way to pause between movements
    ```

### 3. Python Built-in Functions
You can use Python's built-in functions as long as they don't require access to the restricted context:

```python
print("Rotating servo")
servo_turn(90)
print("Rotation complete")
```

### Limitations and Security Concerns
The use of `exec` to run code entered into a mini-IDE presents significant security risks, particularly with unrestricted access to Python's capabilities. In your current implementation, the risks are somewhat mitigated by providing a very limited execution context (`allowed_funcs`), but it's essential to be aware of the security implications, especially if expanding the system's capabilities or making it accessible to others.

### Expanding Capabilities
If you want to expand the types of code users can execute in your mini-IDE, you'll need to:

1. **Define Additional Functions**: Create more functions in your Python script that perform different operations on the servo or provide new functionalities. 

2. **Expose Functions to the Execution Context**: Add these functions to the `allowed_funcs` dictionary passed to `exec`. This will make them available for use within the mini-IDE.

3. **Consider Security**: Carefully consider the implications of exposing more functionality, especially if it interacts with the file system, network, or other sensitive resources.

For a more interactive and educational experience, consider implementing error handling within the IDE's UI to provide feedback on syntax errors or exceptions raised by user-entered code.

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
