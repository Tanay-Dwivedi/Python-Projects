# Shutdown Computer

The OS module in Python is used in various tasks that depend on the operating system.
It can also be used to shutdown your computer in just a few lines of code.
To shutdown your system using the Python programming language, you must have some knowledge of the OS module in Python.

-----

## Code Break:

```python
# Import the os module
import os
```

This line imports the `os` module.

```python
# Define a function to shut down the PC
def shutdown_PC():
    # Use os.system to execute the shutdown command
    os.system("shutdown /s /t 1")

# Call the shutdown_PC function
shutdown_PC()
```

The `shutdown_PC()` function uses the `os.system()` function to execute the "shutdown /s /t 1" command. This command tells the operating system to shut down the computer (`/s`) after a delay of 1 second (`/t 1`).

When you run this script, it will immediately initiate a shutdown sequence on a Windows PC. Keep in mind that the `/t` parameter sets the delay before shutdown, so you may adjust it based on your preference. In this case, it's set to 1 second (`/t 1`).

-----