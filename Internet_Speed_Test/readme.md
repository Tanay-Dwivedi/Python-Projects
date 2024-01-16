# Internet Speed Test

When checking the speed of the Internet connection, the results are displayed as download speed and upload speed.
**Download speed refers to the speed at which your internet connection downloads data from the internet and upload speed refers to the speed at which your internet connection uploads data to the internet.**
So, calculating the download speed and the upload speed of an Internet connection sums up the Internet speed test.

-----

## Installation

```
pip install speedtest-cli
```
Firstly import the `speedtest-cli` library through the terminal that will help in the program.

-----

## Code Break:

```python
# Import the speedtest module
import speedtest
```

This line imports the `speedtest` module.

```python
# Create a Speedtest object
wifi = speedtest.Speedtest()
```

The `speedtest.Speedtest()` creates a Speedtest object, which you can use to measure the internet speed.

```python
# Print the download speed
print("Wifi Download Speed is ", wifi.download())
```

The `wifi.download()` method is used to measure and print the download speed of your internet connection.

```python
# Print the upload speed
print("Wifi Upload Speed is ", wifi.upload())
```

The `wifi.upload()` method is used to measure and print the upload speed of your internet connection.

When you run this script, it will output the download and upload speeds of your internet connection. Keep in mind that the results may vary based on network conditions.

-----