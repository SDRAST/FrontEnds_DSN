"""
Descriptions of DSN front ends without monitor and control functions
"""
import logging

from MonitorControl import ComplexSignal, ObservatoryError
from MonitorControl.FrontEnds import FrontEnd

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
    self.band = self.name[:-2]
    self.get_frequencies()
    self.logger.debug(" assigning output port properties")
    for pol in self.outputs.keys():
      self.outputs[pol].source = self.inputs[self.name]
      self.outputs[pol].source.destinations.append(self.outputs[pol])
      self.outputs[pol].signal = ComplexSignal(self.outputs[pol].source.signal,
                                               pol=pol[-1], name=self.band)
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
    elif self.band == 'K':
      self.data['frequency'] = 26250
      self.data['bandwidth'] = 750
    elif self.band == 'Ka':
      self.data['frequency'] = 32000
      self.data['bandwidth'] = 1000
    else:
      raise ObservatoryError(self.data["band"],"Is not a valid DSN band")
