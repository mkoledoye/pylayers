import matplotlib.pyplot as plt
from pylayers.antprop.antenna import *
A = Antenna('defant.trx')
fig,ax = A.polar(fGHz=[2,3,4],phd=0)
fig,ax = A.polar(fGHz=[2,3,4],thd=90)
