from qulacs import QuantumState
from qulacs import QuantumCircuit
from qulacs import Observable
from qulacs.gate import X

n = 1
state = QuantumState(n)
state.set_zero_state()

index = 1
while True:
x_gate = X(index)
x_gate.update.quantum_state(state)

# observable setting
# observalable = Observable(n)
# observable.add_operator(1.0, "Z 2")
# value = observable.get_expectation_value(state)
# print(value)

# Assuming that this program takes of zero time to perform its n-th Pauli-X gate step,
# this program allows a countably infinite number of algorithmic steps.
# Thomson lamp is a hypothetical problem.
# But,how about the result of measurement?  
# Is measurement available? After the completion of infinite steps...


