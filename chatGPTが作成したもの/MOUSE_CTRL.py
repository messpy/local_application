import evdev
from evdev import ecodes

# キーボードのイベントを取得するデバイスを特定する
def find_keyboard():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if 'keyboard' in device.name.lower():
            return device
    return None

# キーイベントを監視する
def monitor_keyboard():
    keyboard = find_keyboard()
    if not keyboard:
        print("Keyboard not found.")
        return

    print(f"Found keyboard: {keyboard.name}")

    # イベントループ
    for event in keyboard.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            key_event = evdev.categorize(event)
            if key_event.keystate == 1:  # 1: Key down, 0: Key up, 2: Key hold
                print(f"Key {key_event.keycode} pressed")

# キーボードのイベントを監視する
monitor_keyboard()
