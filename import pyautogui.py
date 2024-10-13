import pyautogui
import time


def get_mouse_position():
    try:
        while True:
            x, y = pyautogui.position()  # Get the current mouse coordinates
            print(f"Mouse Position: X={x} Y={y}")
            time.sleep(1)  # Update the position every 1 second
    except KeyboardInterrupt:
        print("\nStopped.")
        
# if __name__ == "__main__":
#     get_mouse_position()

key = {}


def init():
    with open('config.txt') as f:
        for line in f:
            if line != "\n":
                (k, val) = line.split("=", 1)
                key[k.strip()] = val.strip()

if __name__ == "__main__":
    init()


court = key.get("Court")
timing = key.get("Time")

base = (560,500)
x_coord,y_coord = (base[0] + (int(timing)-8)*40, base[1] + (int(court)-1)*40)  # Example X coordinate (replace with actual)
pyautogui.moveTo(x_coord,y_coord)