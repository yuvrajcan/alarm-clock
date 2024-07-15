import time
from datetime import datetime, timedelta
from playsound import playsound

def alarm_after_duration(duration_seconds):
    print(f"Alarm set for {duration_seconds} seconds from now.")
    time.sleep(duration_seconds)
    print("Time's up!")
    playsound('alarm_sound.mp3')  # Make sure the file path is correct

def alarm_at_time(alarm_time):
    current_time = datetime.now()
    time_diff = (alarm_time - current_time).total_seconds()

    if time_diff < 0:
        print("The specified time is in the past. Please set a future time.")
        return

    print(f"Alarm set for {alarm_time.strftime('%H:%M:%S')}.")
    time.sleep(time_diff)
    print("Time's up!")
    playsound('alarm_sound.mp3')  # Make sure the file path is correct

def main():
    print("Alarm Clock")
    print("1. Set alarm after X seconds/minutes")
    print("2. Set alarm at specific time")
    
    choice = input("Enter choice (1/2): ")

    try:
        if choice == '1':
            duration = int(input("Enter the duration in seconds: "))
            alarm_after_duration(duration)
        elif choice == '2':
            alarm_time_str = input("Enter the alarm time (HH:MM:SS): ")
            alarm_time = datetime.strptime(alarm_time_str, '%H:%M:%S').replace(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
            alarm_at_time(alarm_time)
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter numeric values for duration and valid time format for alarm time.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

'''strptime refers to parsing time which is used to read time in specific format.
Whereas strftime refers to formatting time, which we use to change the format of time to some new format. 
So, they are quite opposite of each other.'''