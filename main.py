import os
from qiskit import QuantumCircuit
from qiskit_ibm_provider import IBMProvider
from dotenv import load_dotenv

# Charger la clé API depuis .env
load_dotenv()
API_KEY = os.getenv("IBMQ_API_TOKEN")

if not API_KEY:
    raise ValueError("⚠️ Clé API IBM Quantum manquante. Ajoute-la dans un fichier .env")

# Se connecter à IBM Quantum
provider = IBMProvider(token=API_KEY)

# Choisir un backend quantique
backend = provider.get_backend("ibmq_qasm_simulator")

# Créer un circuit quantique simple
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Envoyer le circuit à IBM Quantum
job = backend.run(qc)
print(f">>> Job ID: {job.job_id()}")
