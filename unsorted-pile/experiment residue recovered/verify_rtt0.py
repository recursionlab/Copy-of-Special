def f(x): return 1 - 0.5 * x  # Sample contraction map
def torsion(x, fx): return abs(fx - x)  # Torsion = difference between step and next

x = 0.0  # Initial seed
tau_star = 0.1  # Torsion threshold

for i in range(100):
    fx = f(x)
    tau = torsion(x, fx)
    print(f"Step {i}: x = {x}, f(x) = {fx}, τ = {tau}")
    if tau < tau_star:
        print("→ Stable fixpoint zone reached")
        break
    x = fx