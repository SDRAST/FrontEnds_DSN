"""
Descriptions of DSN front ends without monitor and control functions
"""
import logging

from math import exp

from MonitorControl import ComplexSignal, ObservatoryError
from MonitorControl.FrontEnds import FrontEnd
from MonitorControl.FrontEnds.DSN.noise_parameters import T1, T2, a

module_logger = logging.getLogger(__name__)


class DSN_fe(FrontEnd):
  """
  Class for DSN front ends with no M&C functions
  """
  def __init__(self, name, inputs=None, output_names=None):
    """
    Create a DSN front end instance

    The name shall be a band (S, X, or Ka) followed by the station number.

    The input to output mapping and signal properties can be defined at the
    start because they never change.
    """
    mylogger = logging.getLogger(module_logger.name+".DSN_fe")
    self.name = name # needed by the next statement
    mylogger.debug(" initializing %s", self)
    mylogger.debug(" %s inputs: %s", name, inputs)
    FrontEnd.__init__(self, name, inputs=inputs, output_names=output_names)
    self.logger = mylogger
    self.name = name
    self.band = self.name[:-2] # This assumes a name like X14
    self.dss = int(self.name[-2:])
    self.get_frequencies()
    self.logger.debug(" assigning output port properties")
    for pol in self.outputs.keys():
      self.outputs[pol].source = self.inputs[self.name]
      self.outputs[pol].source.destinations.append(self.outputs[pol])
      self.outputs[pol].signal = ComplexSignal(self.outputs[pol].source.signal,
                                               pol=pol[-1],
                                               name=self.band+pol[-1])
      self.outputs[pol].signal['band'] = self.band
      self.outputs[pol].signal['frequency'] = self.data['frequency']
      self.outputs[pol].signal['bandwidth'] = self.data['bandwidth']
    self.logger.debug(" %s outputs: %s", self.name, self.outputs)
    self.logger.debug(" initialized  for %s",self)

  def get_frequencies(self):
    """
    The downlink bands allocated to Space Research (Space to Earth) are
                    S          X           K            Ka
    near Earth: 2200-2290  8450-8500  25500-27000
    deep space: 2290-2300  8400-8450               31800-32300
    Reference:http://deepspace.jpl.nasa.gov/dsndocs/810-005/201/201B.pdf

    The actual bandpasses are given below.
    """
    if self.band == 'S':
      self.data['frequency'] = 2250
      self.data["bandwidth"] = 100
    elif self.band == 'X':
      self.data['frequency'] = 8400
      self.data['bandwidth'] = 400
    elif self.band == 'K': # that is, DSN K-band
      self.data['frequency'] = 26250
      self.data['bandwidth'] = 750
    elif self.band == 'Ka':
      self.data['frequency'] = 32000
      self.data['bandwidth'] = 1000
    else:
      raise ObservatoryError(self.data["band"],"Is not a valid DSN band")
  
  def rx_noise_temp(self, pol="R", mode="X", elevation=90):
    """
    Noise temperature measured at the feed
    
    From Appendix A of 810-005 module 101
    
    @param pol : either 'R' (DSN standard) or 'L'
    @type  pol : int
    
    @param mode : either 'X' or 'SX' for dual (diplexer in)
    @type  mode : str
    
    @param elevation : angle in deg  from horizon to zenith
    @type  elevation : float
    """
    return T1[self.dss][self.band][pol][mode] + \
           T2[self.dss][self.band][pol][mode] * \
                              exp(-a[self.dss][self.band][pol][mode]*elevation)
 
  def Tsys_vacuum(self, pol="R", mode="X", elevation=90):
    """
    System temperature without an atmosphere
    
    This ignores attenuation through the atmosphere. Attenuation by the
    atmosphere is about 0.8% at S-band and between 0.8 and 1.3% at X-band.
    It also ignore ground pickup
    """
    return 2.725 + self.rx_noise_temp(pol, mode, elevation)

