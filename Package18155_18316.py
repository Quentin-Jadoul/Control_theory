import numpy as np

import matplotlib.pyplot as plt
from IPython.display import display, clear_output

#-----------------------------------

def LeadLag_RT(MV, Kp, Tlead, Tlag, Ts, PV, PVinit=0, method='EBD'):
    
    """
    The function "LeadLag_RT" needs to be included in a "for or while loop".
    
    :MV: input vector
    :Kp: process gain
    :Tlead: lead time constant [s]
    :Tlag: lag time constant [s]
    :Ts: sampling period [s]
    :PV: output vector
    :PVInit: (optional: default value is 0)
    :method: discretisation method (optional: default value is 'EBD')
        EBD: Euler Backward difference
        EFD: Euler Forward difference
        TRAP: Trapezoïdal method
    
    The function "LeadLag_RT" appends a value to the output vector "PV".
    The appended value is obtained from a recurrent equation that depends on the discretisation method.
    """    
    
    if (Tlag != 0):
        K = Ts/Tlag
        if len(PV) == 0:
            PV.append(PVinit)
        else: # MV[k+1] is MV[-1] and MV[k] is MV[-2]
            if method == 'EBD':
                PV.append((1/(1+K))*PV[-1] + (K*Kp/(1+K))*((1+Tlead/Ts)*MV[0]-Tlead/Ts*PV[-1]))
            elif method == 'EFD':
                PV.append((1-K)*PV[-1] + K*Kp*(Tlead/Ts*MV[0]+(1-Tlead/Ts)*MV[-1]))
            #elif method == 'TRAP':
                #PV.append((1/(2*T+Ts))*((2*T-Ts)*PV[-1] + Kp*Ts*(MV[-1] + MV[-2])))            
            else:
                #EBD par defaut
                PV.append((1/(1+K))*PV[-1] + (K*Kp/(1+K))*((1+Tlead/Ts)*MV[0]-Tlead/Ts*PV[-1]))
    else:
        PV.append(Kp*MV[-1])

#-----------------------------------

def PID_RT(SP, PV, Man, MVMan, MVFF, Kc, Ti, Td, alpha, Ts, MVin, MVMax, MV, MVP, MVI, MVD, E, ManFF=False, PVInit=0, method='EBD-EBD'):
    """
    :SP: SP (or Setpoint) vector
    :PV:
    :Man:
    :MVMan:
    :MVFF:

    :Kc:
    :Ti:
    :Td:
    :alpha:
    :Ts:

    :MVMin:
    :MVMax:

    :MV:
    :MVP:
    :MVI:
    :MVD:
    :E:

    :ManFF:
    :PVInit:

    :method:

    The function "PID_RT" appends new values to the vectors "MV", "MVP, "MVI", and "MVD".
    The appended values are based on the PID algorithm, the controller mode, and feedforward.
    Nate that saturation of "MV" within the limits [MVMin MVMax] is implemented with anti wind-up
    """
    print('hello')