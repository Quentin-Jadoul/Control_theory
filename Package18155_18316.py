from pickle import NONE
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

    K = Ts/Tlag
    if len(PV) == 0:
        PV.append(PVinit)
        
    else: # MV[k+1] is MV[-1] and MV[k] is MV[-2]
        if method == 'EBD':
            
            PV.append((1/(1+K))*PV[-1] + (K*Kp/(1+K))*((1+(Tlead/Ts))*MV[-1]-(Tlead/Ts)*MV[-2]))
        elif method == 'EFD':
            PV.append((1-K)*PV[-1] + K*Kp*(Tlead/Ts*MV[0]+(1-Tlead/Ts)*MV[-1]))
        #elif method == 'TRAP':
            #PV.append((1/(2*T+Ts))*((2*T-Ts)*PV[-1] + Kp*Ts*(MV[-1] + MV[-2])))            
        else:
            #EBD par defaut
            PV.append((1/(1+K))*PV[-1] + (K*Kp/(1+K))*((1+Tlead/Ts)*MV[0]-Tlead/Ts*PV[-1]))
def PID_RT(SP,PV,Man, MVMan, MVFF,Kc,Ti,Td,alpha,Ts, MVMin, MVMax,MV,MVP,MVI,MVD,E, ManFF=False, PVInit=0, method='EBD-EBD'):
    """
    The function "PID_RT" needs to be included in a "for or while loop".
    :SP: SP (or SetPoint) vector
    :PV: PV (or Process Value) vector
    :Man: Man(or Manual controller mode) vector  [True or False]
    :MVMan: MVMan(or Manual value for MV) vector
    :MVFF: MVFF (or feedforward) vector
    :Kp: process gain
    :Ti: integral time constant [s]
    :Td: derivative time constant [s]
    :alpha: Tfd=alpha*Td where Tfd is the derivative filter time constant [s]
    :Ts: sampling period [s]

    :MVMin: minimum value for MV (used for saturation and anti wind-up)
    :MVMax: maximum value for MV (used for saturation and anti wind-up)

    :MV: MV (or Manipulated Value) vector
    :MVP: MVP (or Proportional part of MV) vector 
    :MVI: MVI (or integral part of MV) vector
    :MVD: MVD (or derivative part of MV) vector
    :E: E (or control error) vector

    :ManFF:Activated FF in manual mode (optional: default boolean value is False)
    :PVInit: Initial value of PV (optional: default value is 0): used if PID_RT is ran first in the squence and no value of PV is available yet.

    :method: discretisation method (optional: default value is 'EBD')
        EBD-EDB: EBD for integral action and EBD for derivative action
        EBD-TRAP: EBD for integral action and TRAP for derivative action
        TRAP-EBD: TRAP for integral action and EBD for derivative action
        TRAP-TRAP: TRAP for integral action and TRAP for derivative action
    
    The function "PID_RT" appends new values to the vectors "MV", "MVP", "MVI", and "MVD" .
    The appended values are based on the PID algorithm, the controller mode, and feedforward.
    Note that saturation of "MV" within the limits [MVMin MVMax] is implemented with anti wind-up. 
    """ 

    if Man == True:
        MV=10
    elif Man == False:
        if method == 'EBD-EBD':
            
                
            MVP.append(Kc*E[-1])
            MVI.append(MVI[-2]+(Kc*Ts/Ti)*E[-1])
            #Tfd =alpha*Td
            MVD.append(((alpha*Td/alpha*Td+Ts)*MV[-2])+((Kc*Td/alpha*Td+Ts)*(E[-1]-E[-2])))
            MV.append(MVP+MVI+MVD)
    else:
        pass
            #elif method == 'EFD':
                #NONE
                #PV.append((1-K)*PV[-1] + K*Kp*(Tlead/Ts*MV[0]+(1-Tlead/Ts)*MV[-1]))
            #elif method == 'TRAP':
                #PV.append((1/(2*T+Ts))*((2*T-Ts)*PV[-1] + Kp*Ts*(MV[-1] + MV[-2])))            
    return 0
    
