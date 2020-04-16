from qulacs import QuantumState
from qulacs import QuantumCircuit
from qulacs import Observable
from qulacs.gate import Z

n = 1
state = QuantumState(n)
state.set_zero_state()

index = 1
while True:
z_gate = Z(index)
z_gate.update.quantum_state(state)

# オブザーバブルの設定
# observalable = Observable(n)
# observable.add_operator(1.0, "Z 2")
# value = observable.get_expectation_value(state)
# print(value)


# assuming that this program takes of zero time to perform its n-th step,
# this program allows a countably infinite number of algorithmic steps.
# Thomson lamp is a hypothetical problem.


