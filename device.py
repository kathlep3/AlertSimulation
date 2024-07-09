class Device:
    def __init__(self, device_id):
        self.device_id = device_id
        self.propagation_dict = {}
        self.check_cancellation = False

    def add_propagation(self, device_id, delay):
        self.propagation_dict[device_id] = delay
