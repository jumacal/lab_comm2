import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is a RF VCO and works as following: The first input receives both the carrier frequency and the sampling rate, the second block gives me my discretized carrier signal, receiving the parameter A which refers to the amplitude of the carrier and Q which refers to the phase, the block gives me a and which is my discretized carrier signal. 
    
    La primer entrada me recibe tanto la frecuencia de la portadora y la tasa de muestreo, el segundo bloque lo que me entrega es mi señal portadora discretizada, recibiendo el parametro A que hace referencia a la amplitud de la portadora y Q que se refiere a la fase, el bloque me entrega a y el cual es mi señal portadora discretizada"""

    def __init__(self, fc=128000, samp_rate=320000):  
        gr.sync_block.__init__(
            self,
            name='e_RF_VCO_ff',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.float32]
        )
        self.fc = fc
        self.samp_rate = samp_rate
        self.n_m=0

    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        N=len(A)
        n=np.linspace(self.n_m,self.n_m+N-1,N)
        self.n_m += N
        y[:]=A*np.cos(2*math.pi*self.fc*n/self.samp_rate+Q)
        return len(output_items[0])


