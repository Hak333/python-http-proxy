import threading, os

def vpn():
	os.system('python -m pproxy -l http://0.0.0.0:1087')
threading.Thread(target=vpn).start()
