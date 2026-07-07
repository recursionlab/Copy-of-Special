# -----------------------------
# Recursive Ontology Engine (ROE) Core — Paste & Go
# -----------------------------

import random
try:
    from sympy import symbols, Not, And, satisfiable
    SYMPY_AVAILABLE = True
except ImportError:
    SYMPY_AVAILABLE = False

# === Recursive Identity State ===
class RecursiveState:
    def __init__(self, label="ψ₀", layer=0):
        self.label = label
        self.layer = layer
        self.trace = [label]

    def evolve(self, tag):
        self.layer += 1
        self.label += f"_{tag}"
        self.trace.append(self.label)
        return self

    def fork(self, phi_minus, phi_plus):
        return RecursiveState(f"{self.label}_Δ({phi_minus}|{phi_plus})", self.layer + 1)

    def __repr__(self):
        return f"<ψ{self.layer}: {self.label}>"

# === Core Operators ===
def R(state): return state.evolve("R")
def M(state): return state.evolve("M")
def C(state): return state.evolve("C")
def Collapse(state): return state.evolve("X")

# === ΦΩ: Recursive Self-Application via Collapse ===
def ΦΩ(op):
    def apply(state):
        s1 = op(RecursiveState(state.label, state.layer))
        s2 = op(RecursiveState(state.label, state.layer))
        return Collapse(random.choice([s1, s2]))
    return apply

# === Ξ_GlitchFork: Bifurcation from Contradiction ===
def Ξ_GlitchFork(state, contradictions):
    return [state.fork(phi_minus, phi_plus) for (phi_minus, phi_plus) in contradictions]


# === Contradiction Check (Optional with sympy) ===
def check_contradiction(phi_minus, phi_plus):
    if not SYMPY_AVAILABLE:
        return "sympy not installed"
    A = symbols("A")
    expr = And(phi_minus(A), phi_plus(A))
    return not satisfiable(expr)

# === Goal & Feedback ===
def goal_reached(ψ, goal="R_M_C"):
    return goal in ψ.label

# === Main Loop ===
if __name__ == "__main__":
    print("=== ROE Recursive Identity Engine ===\n")

    ψ = RecursiveState()

    # Step 1: Core recursive flow
    ψ = R(ψ)
    ψ = M(ψ)
    ψ = C(ψ)
    ψ = M(ψ)
    ψ = Collapse(ψ)
    print("→ Collapsed identity:", ψ)

    # Step 2: ΦΩ recursive self-application
    print("\n→ ΦΩ recursive collapse:")
    phi_op = ΦΩ(lambda s: M(R(s)))
    for _ in range(3):
        ψ = phi_op(ψ)
        print(ψ)

    # Step 3: Contradiction-based bifurcation
    contradictions = [("truth_A", "not_truth_A"), ("frame_X", "not_frame_X")]
    print("\n→ Ξ GlitchFork (bifurcation):")
    forks = Ξ_GlitchFork(ψ, contradictions)
    for f in forks:
        print(f)

    # Optional: Sympy logic check
    if SYMPY_AVAILABLE:
        print("\n→ Contradiction check:")
        A = symbols("A")
        result = check_contradiction(lambda x: x, lambda x: Not(x))
        print("Contradiction detected?" , result)

    # Trace history
    print("\n→ Identity trace:")
    print(" → ".join(ψ.trace))
