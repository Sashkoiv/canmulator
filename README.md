# CANmulator
A simple tool to send a bunch of CAN frames from Wireshark dump.

## Setting up CAN interface on Linux machine
1. Install utils for `CAN` communication
    ```
    sudo apt-get install net-tools
    sudo apt-get install can-utils
    ```

1. Configure `CAN0`
    ```sh
    sudo ip link set can0 type can bitrate 500000
    sudo ifconfig can0 up
    ```

    Configure `CAN1` by your need
    ```sh
    sudo ip link set can1 type can bitrate 500000
    sudo ifconfig can1 up
    ```