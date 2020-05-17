import RPi.GPIO as GPIO  
import time  
import sys

IN1 = 24    # pin11  
IN2 = 29  
IN3 = 31  
IN4 = 33  

def setStep(w1, w2, w3, w4):  
	GPIO.output(IN1, w1)  
	GPIO.output(IN2, w2)  
	GPIO.output(IN3, w3)  
	GPIO.output(IN4, w4)  

def stop():  
	setStep(0, 0, 0, 0)  

def forward(delay, steps):    
	for i in range(0, steps):  
		setStep(1, 0, 0, 0)  
		time.sleep(delay)  
		setStep(0, 1, 0, 0)  
		time.sleep(delay)  
		setStep(0, 0, 1, 0)  
		time.sleep(delay)  
		setStep(0, 0, 0, 1)  
		time.sleep(delay)  

def backward(delay, steps):    
	for i in range(0, steps):  
		setStep(0, 0, 0, 1)  
		time.sleep(delay)  
		setStep(0, 0, 1, 0)  
		time.sleep(delay)  
		setStep(0, 1, 0, 0)  
		time.sleep(delay)  
		setStep(1, 0, 0, 0)  
		time.sleep(delay)  

def setup():  
	GPIO.setwarnings(False)  
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location  
	GPIO.setup(IN1, GPIO.OUT)      # Set pin's mode is output  
	GPIO.setup(IN2, GPIO.OUT)  
	GPIO.setup(IN3, GPIO.OUT)  
	GPIO.setup(IN4, GPIO.OUT)  


def open():
		backward(0.003, 512)  # 512 steps --- 360 angle  
        print "open"
def close(): 
		forward(0.005, 512)  
        print "close"
 

def destroy():  
	GPIO.cleanup()             # Release resource  
status = sys.argv[2]
if __name__ == '__main__':     # Program start from here  
	setup()  
	try:  
		if status == "open":
            open()
        elif status == "close":
            close()
        else:
            print "Error"
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.  
		destroy()