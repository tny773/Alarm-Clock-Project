import os
import winsound
import time

def play_alarm_sound(alarm_sound):
    # Play alarm sound for 30 seconds
    winsound.PlaySound(alarm_sound, winsound.SND_FILENAME)
    time.sleep(30)

def set_alarm(alarm_time, alarm_sound):
    current_time = time.strftime("%H:%M:%S")
    print(f"Alarm is set for {alarm_time}.")
    while True:
        if current_time >= alarm_time:
            print("Time to wake up!")
            play_alarm_sound(alarm_sound)
            choice = input("Enter 's' to snooze or 'd' to dismiss: ")
            if choice.lower() == 's':
                snooze_alarm()
            elif choice.lower() == 'd':
                print("Alarm dismissed.")
                break
            else:
                print("Invalid choice.")
                continue
        else:
            current_time = time.strftime("%H:%M:%S")
            time.sleep(1)

def snooze_alarm():
    print("Alarm snoozed for 5 minutes.")
    time.sleep(300)  # Snooze alarm for 5 minutes

def select_alarm_sound():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    sounds_folder = os.path.join(desktop_path, "sounds")
    
    alarm_sounds = []
    if os.path.exists(sounds_folder):
        alarm_sounds += [os.path.join(sounds_folder, file) for file in os.listdir(sounds_folder) if file.endswith(".wav")]

    # Get system sounds
    system_sounds = ["SystemAsterisk", "SystemExclamation", "SystemHand", "SystemQuestion"]
    alarm_sounds += system_sounds
    
    print("Select an alarm sound:")
    for i, sound in enumerate(alarm_sounds, start=1):
        print(f"{i}. {sound}")
    choice = int(input("Enter the number of your choice: "))
    return alarm_sounds[choice - 1]

def main():
    print("Welcome to Simple Alarm Clock!")
    print("1. Set Alarm")
    print("2. Snooze Alarm")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        alarm_time = input("Enter the time for the alarm (HH:MM): ")
        alarm_sound = select_alarm_sound()
        set_alarm(alarm_time, alarm_sound)
    elif choice == "2":
        snooze_alarm()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
