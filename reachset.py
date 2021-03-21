import numpy as np  
import polytope as pc 

A = np.array([[1, 1], 
              [0, 1]]) 
  
b = np.array([0, 1]) 
  
p = pc.Polytope(A, b) 
