import sys
import traceback
import numpy as np

class DataEmu(object):
    emu_dict = {}
    
    def normalization_data(self, data):
        min_value = min(self.emu_dict.values())
        max_value = max(self.emu_dict.values())
        return (self.emu_dict[data] + 0.1 - min_value) * 1.0 / min_value
    
    def run(self, data):
        data = data.strip()
        if data in self.emu_dict:
            return self.normalization_data(data)
        return 0.001