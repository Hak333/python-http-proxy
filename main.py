import threading, os

PORT = "your-port"

def vpn():
	if PORT == "your-port":
		print("Please change port in main.py")
		exit()
	else:
		os.system(f'python -m pproxy -l http://0.0.0.0:{PORT}')
		
threading.Thread(target=vpn).start()
