import samsungctl
import time

config = {
    "name": "Web Remote Test",
    "description": "TV Remote Control Test",
    "id": "webremote_test",
    "host": "192.168.0.135",  # Replace with your TV's IP address
    "port": 8001,
    "method": "websocket",
    "timeout": 0
}

command_list = [
# 'KEY_POWER',
    'KEY_VOLUP',
    'KEY_VOLDOWN',
    'KEY_MUTE',
    'KEY_CHUP',
    'KEY_CHDOWN',
    'KEY_1',
    'KEY_2',
    'KEY_3',
    'KEY_POWER',
]

def test_remote():
    print("Connecting to TV...")
    try:
        with samsungctl.Remote(config) as remote:
            print("Connected!")
            for cmd in command_list:
                print(f"Sending command: {cmd}")
                remote.control(cmd)
                time.sleep(1)  # Wait a bit between commands
            print("All commands sent.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_remote()
