# Linux Process Manager

A simple application to manage Linux processes and services using a graphical user interface built with Tkinter.

## Features

- Display a list of active processes with their PID, CPU, and memory usage.
- Start, stop, enable, and disable system services.
- Display system statistics such as CPU and memory usage.

## Requirements

- Python 3.x
- `psutil` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/AlbertoTrujillo-ITB2425/linux-process-manager.git
    cd linux-process-manager
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python src/main.py
    ```

2. Use the graphical interface to manage processes and services.

## License

This project is licensed under the MIT License.
