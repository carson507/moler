import os.path
from moler.config import load_config
from moler.device.device import DeviceFactory


def test_network_outage():
    load_config(config=os.path.abspath('config/my_devices.yml'))
    unix1 = DeviceFactory.get_device(name='MyMachine1')
    unix2 = DeviceFactory.get_device(name='MyMachine2')
    ping = unix1.get_cmd(cmd_name="ping", cmd_params={"destination": "localhost", "options": "-O"})
    ping.start(timeout=120)


if __name__ == '__main__':
    test_network_outage()
