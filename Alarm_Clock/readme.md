# Alarm Clock

An alarm clock is a clock with a function that can be activated to ring at a time set in advance, used to wake someone up.

-----

## Code Break:

```python
from datetime import datetime
from playsound import playsound
```

These lines import the necessary modules. `datetime` is used to work with dates and times, and `playsound` is used to play an alarm sound.

```python
alarm_time = input("Enter the time of alarm to be set: HH:MM:SS\n")
```

This line prompts the user to input the desired alarm time in the format "HH:MM:SS".

```python
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
```

These lines extract the hour, minute, seconds, and period (AM/PM) from the user's input.

```python
print("Setting up alarm..")
```

This line prints a message indicating that the alarm is being set up.

```python
while True:
```

This initiates an infinite loop to continuously check the current time and compare it with the specified alarm time.

```python
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
```

These lines retrieve the current hour, minute, seconds, and period from the current time.

```python
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minute == current_minute:
                if alarm_seconds == current_seconds:
                    print("Wake Up!")
                    playsound("audio.mp3")
                    break
```

This nested set of `if` statements checks if the current time matches the specified alarm time. If all conditions are met, it prints "Wake Up!", plays the specified audio file ("audio.mp3") using the `playsound` module, and breaks out of the loop, ending the script.

Note: The script will continue to run in an infinite loop until the specified alarm time is reached, and it might be resource-intensive. Additionally, it's essential to have the `playsound` module and an audio file named "audio.mp3" in the same directory as the script for the alarm sound to work.

-----