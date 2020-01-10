# shape.py
# Author(s): Vivek Kumar
import numpy as np
from abc import ABC, abstractmethod

class Shape(ABC):
  """docstring for Shape"""
  @abstractmethod
  def __init__(self, shape_info:dict):
    self.name = shape_info["shape_type"]

  
  @abstractmethod
  def is_point_inside(self, point: np.ndarray)->bool:
    pass

  @abstractmethod
  def is_intersected_by_edge(self, point_1: np.ndarray , point_2: np.ndarray)->bool:
    pass

  @abstractmethod
  def sample_random_point(self)->np.ndarray:
    pass