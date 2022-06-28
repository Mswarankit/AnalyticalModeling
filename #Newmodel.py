#parameters
import numpy as np

L = 1000 # aquifer length, m
H = 10 # aquifer thickness, m
zb = -6 #aquifer bottom, m
k = 10 # hudraulic conductivity
n = 0.3 #porisity
T = k * H
h0 = 6
hL = 4

x = np.linespace(0, L, 100)
h = (hL - h0) * x/L + h0
Qx = - T * (hL - h0) / L * np.ones_like(x)
