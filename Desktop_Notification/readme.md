# Desktop Notification

The desktop notification app will constantly notify us of the different to-do and actions to take throughout the day.
A desktop notification app to get a reminder to rest after every hour.

-----

## Installation

```
pip install plyer
```
Firstly import the `plyer` library through the terminal that will help in the program.

-----

## Code Break:

```python
import time
from plyer import notification
```

Imports the necessary modules, including `time` for time-related operations and `plyer` for notifications.

```python
while True:
    notification.notify(
        title="ALERT!!!", message="Take a break! It has been an hour!", timeout=10
    )
    time.sleep(3600)
```

Creates an infinite loop (`while True`) that repeats the following steps:

- `notification.notify(...)`: Sends a notification with the title "ALERT!!!" and the message "Take a break! It has been an hour!". The `timeout` parameter specifies how long the notification will be displayed (in seconds).

- `time.sleep(3600)`: Pauses the execution of the script for 3600 seconds (1 hour) before repeating the loop.

This script will keep running indefinitely, sending a notification every hour to remind the user to take a break.

-----