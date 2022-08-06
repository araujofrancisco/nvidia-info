class nvidia_info:
    def __init__(self, client, entry_date, fan_speed, temperature, power_used, power_limit, memory_used):
        self.client = client
        self.entry_date = entry_date
        self.fan_speed = fan_speed
        self.temperature = temperature
        self.power_used = power_used
        self.power_limit = power_limit
        self.memory_used = memory_used

    def __repr__(self):
        return "nvidia_info('{}', '{}', {}, {}, {}, {}, {})".format(self.client, self.entry_date, self.fan_speed, 
                                                      self.temperature, self.power_used, self.power_limit,
                                                      self.memory_used)