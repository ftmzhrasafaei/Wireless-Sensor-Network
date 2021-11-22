"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import cmath

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """ Calculate BER """

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='My BER',   # will show up in GRC
            in_sig=[np.int8],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.limit = []

    def work(self, input_items, output_items):
        """ Calculate BER"""
        in1 = input_items[0]
        out = output_items[0]
        e = 0
        for i in range(len(in1)):
            if abs(in1[i]) != 0  :
                e = 1 + e
        self.limit.append((e , len(in1)))
        l = 0
        error = 0
        for item in self.limit:
            error = item[0] + error
            l = item[1] + l
        error  = float(error) / float(l)
        for i in range(len(out)):
            out[i] = error

        #print(self.limit , error , l)
        return len(output_items[0])
