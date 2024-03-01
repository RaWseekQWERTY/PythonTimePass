from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    try:
        while time_elapsed < seconds:
            time.sleep(1)
            time_elapsed += 1
            
            time_left = seconds - time_elapsed
            minutes_left = time_left // 60
            seconds_left = time_left % 60
            
            print(f"{CLEAR_AND_RETURN}The alarm will sound in:{minutes_left:02d}:{seconds_left:02d}")
    except KeyboardInterrupt:
        print("\nAlarm stopped.")
        return
    
    playsound(r"C:\Users\Hp\Downloads\PythonP\Easy\alarm.wav")

def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

minutes = get_input("Enter minutes: ")
seconds = get_input("Enter seconds: ")
total_seconds = minutes * 60 + seconds
        
alarm(total_seconds)
