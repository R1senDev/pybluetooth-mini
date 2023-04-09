# pybluetooth-mini

PyBluetooth Mini is a lightweight Python library that will allow you to control the Bluetooth interface on Linux devices.

## Basic usage

Almost the entire library is enclosed in the `Device` class and the `Bluetooth` object.

To enable or disable Bluetooth, use this code:

``from PyBluetooth import Bluetooth, Device
Bluetooth.enable()
Bluetooth.disable()``

To control the connection to the device, use the `Device` class by passing the MAC address as an argument to the function:

``from PyBluetooth import Device
myDevice = Device('01:23:45:AB:CD:EF')``

## Methods of instances of the Device class

`myDevice.pair(lock=True)`

Starts the device binding procedure. A password entry field or confirmation window may appear on the screen.  
`lock` argument (optional, default — True): if True, the execution of your script is suspended until the pairing process is completed.

`myDevice.remove(lock=True)`

Removes the device from the list of paired devices.  
`lock` argument (optional, default — True): if True, the execution of your script is suspended until the pairing process is completed.

`myDevice.connect(lock=True)`

Connects the device.  
`lock` argument (optional, default — True): if True, the execution of your script is suspended until the pairing process is completed.

`myDevice.disconnect(lock=True)`

Disconnects the device.  
`lock` argument (optional, default — True): if True, the execution of your script is suspended until the pairing process is completed.

## Example

The script that connects the headphones to the computer and disconnects after half an hour:

``from PyBluetooth import Bluetooth, Device
import time
Bluetooth.enable()
headphones = Device('0C:AE:BD:D4:95:9F')
headphones.connect()
time.sleep(1800)
headphones.disconnect()
``