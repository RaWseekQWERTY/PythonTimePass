from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elaplsed = 0
    print(CLEAR)
    while time_elaplsed < seconds:
        time.sleep(1)
        time_elaplsed +=1
        
        time_left = seconds - time_elaplsed
        minutes_left =time_left // 60
        seconds_left = time_left % 60
        
        print(f"{CLEAR_AND_RETURN}The alarm will sound in:{minutes_left:02d}:{seconds_left:02d}")
    playsound(r"C:\Users\Hp\Downloads\PythonP\Easy\alarm.wav")

minutes = int(input("Enter minute:"))
seconds = int(input("Enter Second:"))
total = minutes*60+seconds
        
alarm(total)