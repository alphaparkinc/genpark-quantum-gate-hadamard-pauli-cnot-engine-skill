from client import QuantumGateEngine

def run_example():
    print("=== GenPark Quantum Gate Engine Example ===")
    engine = QuantumGateEngine()
    print("Gate Execution:", engine.benchmark_quantum_gates())

if __name__ == "__main__":
    run_example()
