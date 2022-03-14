{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "from IPython.display import display, clear_output\n",
    "\n",
    "#-----------------------------------\n",
    "def lead_lag(MV, Kp, Tlead, Tlag, Ts, PV, PVinit=0, method='EBD'):\n",
    "    \"\"\"\n",
    "    The function \"lead_lag\" needs to be included in a \"for or while loop\".\n",
    "    \n",
    "    :MV: input vector\n",
    "    :Kp: process gain\n",
    "    :Tlead: lead time constant [s]\n",
    "    :Tlag: lag time constant [s]\n",
    "    :Ts: sampling period [s]\n",
    "    :PV: output vector\n",
    "    :PVInit: (optional: default value is 0)\n",
    "    :method: discretisation method (optional: default value is 'EBD')\n",
    "        EBD: Euler Backward difference\n",
    "        EFD: Euler Forward difference\n",
    "        TRAP: Trapezoïdal method\n",
    "    \n",
    "    The function \"lead_lag\" appends a value to the output vector \"PV\".\n",
    "    The appended value is obtained from a recurrent equation that depends on the discretisation method.\n",
    "    \"\"\"    \n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
