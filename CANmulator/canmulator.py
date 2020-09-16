"""
CANmulator main module.
"""
import time
import can
import json


def _can_bus_init(channel) -> object:
    """Init CAN socket
    """
    bus = can.interface.Bus(channel=channel, bustype='socketcan_native')
    return bus


def _parse_pcap(addr) -> dict:
    """Parse pcap file to dict.
    """
    with open(addr, 'r') as f:
        return(json.load(f))


def transmit(**kwargs) -> None:
    """Sends CAN messages to initialized port"""
    bus = _can_bus_init(kwargs['can'])

    in_dict = _parse_pcap(kwargs['pcap'])

    for frame in in_dict:
        can_id = frame['_source']['layers']['can']['can.id']
        can_data = frame['_source']['layers']['data']['data.data']
        can_xtd = frame['_source']['layers']['can']['can.flags.xtd']

        print(f"The id is: {can_id}\n"
              f"The data is: {can_data}\n"
              f"The extended frame is {bool(can_xtd)}\n")

        bus.send(can.Message(arbitration_id=int(can_id, 16),
                             data=[int(c, 16) for c in can_data.split(':')],
                             extended_id=int(can_xtd)))

        time.sleep(float(frame['_source']['layers']
                         ['frame']['frame.time_delta']))
