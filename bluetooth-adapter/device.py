import logging


log = logging.getLogger(__name__)


# TODO: maybe subclass this from a generic BluetoothDevice later on
class BleDevice(object):

    def __init__(self, backend, mac_address, name=None,
                 scan_response_rssi=None):
        log.debug("Creating BleDevice with MAC %s")
        self._backend = backend
        self._mac_address_string = mac_address
        self._mac_address_bytearray = bytearray(
            [int(b, 16) for b in self._mac_address_string.split(":")])
        self._name = name
        self._scan_response_rssi = scan_response_rssi
        log.debug("BleDevice created")

    def __repr__(self):
        return (
            "<{0}.{1} object at {2}: {3}, {4}>"
            .format(self.__class__.__module__, self.__class__.__name__,
                    hex(id(self)), self._mac_address_string, self._name)
        )

    # TODO: This could be done with a property decorator but personally I favor
    #       the getter method here.
    def get_mac_address(self):
        """Allow the programmer to view but not change MAC address."""
        log.debug("Getting mac_address %s", self._mac_address_string)
        return self._mac_address_string

    # TODO: This could be done with a property decorator but personally I favor
    #       the getter method here.
    def get_name(self):
        """Allow the programmer to view but not change name."""
        log.debug("Getting name %s", self._name)
        return self._name

    def get_rssi(self, from_connection=False):
        log.debug("Getting RSSI from %s",
                  'connection' if from_connection else 'scan response')
        rssi = None
        if from_connection:
            raise NotImplementedError()
        else:
            rssi = self._scan_response_rssi
        assert(rssi is not None)
        log.debug("RSSI is %d dBm", rssi)
        return rssi

    def connect(self):
        log.debug("Connecting")
        raise NotImplementedError()
        self._device_adapter.connect(self._mac_address_bytearray)
        log.debug("Connected")

    def encrypt(self):
        log.debug("Encrypting connection")
        raise NotImplementedError()
        self._device_adapter.encrypt()
        log.debug("Connection encrypted")

    def bond(self):
        log.debug("Forming bonded connection")
        raise NotImplementedError()
        self._device_adapter.bond()
        log.debug("Bonded connection formed")

    def char_read(self, characteristic):
        log.debug("Reading from characteristic {0}".format(characteristic))
        raise NotImplementedError()
        value_bytearray = self._backend.attribute_read(characteristic)
        log.debug("Read value {0}".format([hex(b) for b in value_bytearray]))
        return value_bytearray

    def char_write(self, characteristic, value_bytearray):
        log.debug("Writing value {0} to characteristic {1}"
                  .format(value_bytearray, characteristic))
        raise NotImplementedError()
        self._backend.attribute_write(characteristic, value_bytearray)
        log.debug("Done writing")

    def subscribe(self, characteristic, notifications=True, indications=False,
                  callback=None):
        log.debug("Subscribing to characteristic {0}".format(characteristic))
        raise NotImplementedError()
        self._device_adapter.subscribe(characteristic, notifications,
                                       indications, callback)
        log.debug("Done subscribing")
