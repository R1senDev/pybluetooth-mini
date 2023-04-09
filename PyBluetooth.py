import os
import threading

class Device:
	def __init__(self, mac):
		self.address = mac.upper()

	def __str__(self):
		return self.address

	def pair(self, lock=True):
		if lock:
			os.system(f'bluetoothctl pair {self.address} > /dev/null')
		else:
			thr = threading.Thread(target=lambda: os.system(f'bluetoothctl pair {self.address} > /dev/null'), args=())
			thr.start()

	def remove(self, lock=True):
		if lock:
			os.system(f'bluetoothctl remove {self.address} > /dev/null')
		else:
			thr = threading.Thread(target=lambda: os.system(f'bluetoothctl remove {self.address} > /dev/null'), args=())
			thr.start()

	def connect(self, lock=True):
		if lock:
			os.system(f'bluetoothctl connect {self.address} > /dev/null')
		else:
			thr = threading.Thread(target=lambda: os.system(f'bluetoothctl connect {self.address} > /dev/null'), args=())
			thr.start()

	def disconnect(self, lock=True):
		if lock:
			os.system(f'bluetoothctl disconnect {self.address} > /dev/null')
		else:
			thr = threading.Thread(target=lambda: os.system(f'bluetoothctl disconnect {self.address} > /dev/null'), args=())
			thr.start()

class _Bluetooth:
	_enabled = None
	@property
	def enabled(self):
		return self._enabled

	def enable(self, lock=True):
		if lock:
			os.system('bluetoothctl power on > /dev/null')
			self._enabled = True
		else:
			thr = threading.Thread(target=_btsetenable(True), args=())
			thr.start()

	def disable(self, lock=True):
		if lock:
			os.system('bluetoothctl power off > /dev/null')
			self._enabled = False
		else:
			thr = threading.Thread(target=_btsetenable(False), args=())
			thr.start()

Bluetooth = _Bluetooth()

def _btsetenable(state):
	if type(state) != type(True): raise TypeError('new Bluetooth state must be boolean')
	if state:
		os.system('bluetoothctl power on > /dev/null')
	else:
		os.system('bluetoothctl power off > /dev/null')
	Bluetooth._enabled = state

