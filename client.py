import math
from typing import List, Dict, Any

class QuantumGateEngine:
    @staticmethod
    def apply_hadamard(state: List[complex], target: int) -> List[complex]:
        inv_sqrt2 = 1.0 / math.sqrt(2.0)
        new_s = list(state)
        bit = 1 << target
        for i in range(len(state)):
            if (i & bit) == 0:
                j = i | bit
                v0, v1 = state[i], state[j]
                new_s[i] = (v0 + v1) * inv_sqrt2
                new_s[j] = (v0 - v1) * inv_sqrt2
        return new_s

    @staticmethod
    def apply_cnot(state: List[complex], ctrl: int, targ: int) -> List[complex]:
        new_s = list(state)
        c_mask = 1 << ctrl
        t_mask = 1 << targ
        for i in range(len(state)):
            if (i & c_mask) != 0 and (i & t_mask) == 0:
                j = i | t_mask
                new_s[i], new_s[j] = state[j], state[i]
        return new_s

    def benchmark_quantum_gates(self) -> Dict[str, Any]:
        init = [complex(1.0, 0.0), complex(0.0, 0.0), complex(0.0, 0.0), complex(0.0, 0.0)]
        h_s = self.apply_hadamard(init, 0)
        cnot_s = self.apply_cnot(h_s, 0, 1)
        probs = [round(abs(c)**2, 4) for c in cnot_s]
        return {"bell_state_probs": probs, "gate_status": "ENTANGLED_SUCCESS"}
