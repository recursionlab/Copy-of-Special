import os, random, numpy as np, pandas as pd, matplotlib.pyplot as plt, networkx as nx
from fpdf import FPDF

# --- CONFIG --- #
N_AGENTS, EDGE_PROB, INIT_BUDGET, DEPTH_COST, MAX_DEPTH = 12, 0.25, 1200, 7, 15
RECOVER, ROUNDS = 10, 200
random.seed(42)

# --- Graph + Agent Setup --- #
G = nx.erdos_renyi_graph(N_AGENTS, EDGE_PROB)
for n in G.nodes():
    G.nodes[n].update(budget=INIT_BUDGET, depth=0, memory=[], role='unknown')

def ricci_curvature(G):
    return {(u,v): 1.0 * (4 - (G.degree[u] + G.degree[v])) for u,v in G.edges()}

def assign_roles(G):
    for n in G.nodes():
        mem = G.nodes[n]['memory'][-10:]
        if not mem: continue
        avg_depth = sum(mem)/len(mem)
        if avg_depth < 1: G.nodes[n]['role'] = 'stabilizer'
        elif np.var(mem) > 4: G.nodes[n]['role'] = 'explorer'
        else: G.nodes[n]['role'] = 'teacher'

history = []

# --- Main Simulation Loop --- #
for t in range(ROUNDS):
    curv = ricci_curvature(G)
    assign_roles(G)
    for a in G.nodes():
        G.nodes[a]['budget'] = min(INIT_BUDGET, G.nodes[a]['budget'] + RECOVER)
        memory = G.nodes[a]['memory'][-10:]
        avg = int(np.mean(memory)) if memory else 1
        fuzz = random.randint(-1, 3)
        desired = max(1, min(MAX_DEPTH, avg + fuzz))

        cost = desired * DEPTH_COST
        if G.nodes[a]['budget'] >= cost:
            G.nodes[a]['budget'] -= cost
            G.nodes[a]['depth'] = desired
            G.nodes[a]['memory'].append(desired)
            for nb in G.neighbors(a):
                edge = (a, nb) if (a, nb) in curv else (nb, a)
                influence = max(0.2, 1 + curv.get(edge, 0)/10)
                coop = 1.1 if G.nodes[nb]['depth'] == G.nodes[a]['depth'] else 1.0
                new = int(0.6 * G.nodes[nb]['depth'] + 0.4 * desired * influence * coop)
                G.nodes[nb]['depth'] = min(MAX_DEPTH, new)

    depths = [G.nodes[n]['depth'] for n in G.nodes()]
    budgets = [G.nodes[n]['budget'] for n in G.nodes()]
    curv_avg = np.mean(list(curv.values()))
    history.append(dict(round=t, avg_depth=np.mean(depths), depth_var=np.var(depths),
                        avg_budget=np.mean(budgets), avg_curv=curv_avg))

df = pd.DataFrame(history)

# --- PLOTS --- #
fig, ax = plt.subplots(1, 2, figsize=(12,4))
ax[0].plot(df['round'], df['avg_depth']);  ax[0].set_ylabel('Average Depth')
ax[1].plot(df['round'], df['avg_budget']); ax[1].set_ylabel('Average Budget')
for a in ax: a.set_xlabel('Round'); a.grid(True)
plt.tight_layout(); plt.savefig("agent_growth_plot.png"); plt.close()

# --- PDF Report --- #
pdf = FPDF(); pdf.add_page(); pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Agent Growth Simulation Report", ln=True, align='C')
pdf.image("agent_growth_plot.png", x=10, y=20, w=190); pdf.ln(105)

pdf.set_font("Arial", size=10)
roles = pd.Series([G.nodes[n]['role'] for n in G.nodes()]).value_counts()
pdf.cell(200, 10, txt="Roles in Final Round:", ln=True)
for role, count in roles.items():
    pdf.cell(200, 8, txt=f"{role.title()}: {count} agents", ln=True)

pdf.ln(5); pdf.cell(200, 10, txt="Final 5 Rounds:", ln=True)
for _, row in df.tail().iterrows():
    line = f"Round {int(row['round'])} | Depth {row['avg_depth']:.2f} | Var {row['depth_var']:.2f} | Budget {row['avg_budget']:.2f} | Curv {row['avg_curv']:.2f}"
    pdf.cell(200, 8, txt=line, ln=True)

outdir = os.path.expanduser("~/Desktop/Master Sheef")
os.makedirs(outdir, exist_ok=True)
pdf.output(os.path.join(outdir, "Agent_Growth_Report.pdf"))
print(f"✅ Done! Report saved to: {os.path.join(outdir, 'Agent_Growth_Report.pdf')}")
