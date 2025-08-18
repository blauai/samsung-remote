# Samsung TV Remote

This project provides a web-based remote control for Samsung TVs, allowing you to control your TV from a web browser on the same network. It also includes a command-line interface for interactive control and a test script.

## Features

- **Web Interface**: A simple and intuitive web-based remote control with buttons for all major functions.
- **FastAPI Backend**: A lightweight and efficient backend powered by FastAPI.
- **`samsungctl` Integration**: Uses the `samsungctl` library to communicate with the TV.
- **Interactive CLI**: An interactive command-line remote control for terminal power users.
- **Easy to Set Up**: Just configure your TV's IP address and run the backend.

## Project Structure

- `home.html`: The HTML file for the web remote interface.
- `tv_remote.css`: The CSS file for styling the web remote.
- `tv_remote_backend.py`: The FastAPI backend that handles communication with the TV.
- `testRemote.py`: A script to test the connection and send commands to the TV.
- `interactive.py.txt`: A script for an interactive command-line remote control.
- `LICENSE`: The Apache 2.0 License file.
- `README.md`: This file.

## Prerequisites

- Python 3.7+
- A Samsung TV connected to the same network as the computer running the backend.
- The following Python libraries:
  - `fastapi`
  - `uvicorn`
  - `samsungctl`
  - `python-dotenv` (optional, for managing environment variables)

## Setup and Usage

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/samsung-remote.git
    cd samsung-remote
    ```

2.  **Install the required libraries:**

    ```bash
    pip install fastapi uvicorn samsungctl
    ```

3.  **Configure the TV's IP address:**

    Open the `tv_remote_backend.py` file and replace the placeholder IP address in the `config` dictionary with the actual IP address of your Samsung TV.

    ```python
    config = {
        "name": "Web Remote",
        "description": "TV Remote Control",
        "id": "webremote",
        "host": "YOUR_TV_IP_ADDRESS",  # <-- Replace with your TV's IP address
        "port": 8001,
        "method": "websocket",
        "timeout": 0
    }
    ```

4.  **Run the backend server:**

    ```bash
    uvicorn tv_remote_backend:app --host 0.0.0.0 --port 8000
    ```

5.  **Access the web remote:**

    Open your web browser and navigate to `http://localhost:8000/home`. You should see the web remote interface.

## Interactive Command-Line Remote

The `interactive.py.txt` script provides a command-line interface to control your TV.

1.  **Configure the TV's IP address:**

    If you haven't already, make sure the `host` in `testRemote.py` is set to your TV's IP address. The interactive script uses the configuration from this file.

2.  **Run the interactive script:**

    You can adapt the `testRemote.py` script to run the interactive mode.

## Testing

The `testRemote.py` script can be used to test the connection to your TV and send a series of commands.

1.  **Configure the TV's IP address:**

    Open `testRemote.py` and set the `host` in the `config` dictionary to your TV's IP address.

2.  **Run the test script:**

    ```bash
    python testRemote.py
    ```

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.