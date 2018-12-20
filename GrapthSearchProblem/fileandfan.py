import numpy as np
from utilyti import *

protein = 'HHPP'
protein = list(protein)
CurrentState = State(protein)
CurrentState.getState()
CurrentState.makeMove('D')
CurrentState.getState()
CurrentState.makeMove('U')
CurrentState.getState()
CurrentState.makeMove('R')
CurrentState.getState()
CurrentState.makeMove('U')
CurrentState.getState()
