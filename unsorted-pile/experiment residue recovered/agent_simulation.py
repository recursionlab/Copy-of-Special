import networkx as nx
import random, numpy as np, pandas as pd, matplotlib.pyplot as plt
from fpdf import FPDF
import os

# CONFIG
N_AGENTS = 12
EDGE_PROB = 0.25
INIT_BUDGET = 1200
DEPTH_COST = 7
MAX_DEPTH = 15
RECOVER = 10
ROUNDS = 200
random.seed(42)

# Ricci proxy
def ricci_curvature(G):
    curv = {}
    for u, v in G.edges():
        deg_u, deg_v = G.degree[u], G.degree[v]
        curv[(u, v)] = 1.0 * (4 - (deg_u + deg_v))
    return curv

# Init
G = nx.erdos_renyi_graph(N_AGENTS, EDGE_PROB)
for n in G.nodes():
    G.nodes[n]['budget'] = INIT_BUDGET
    G.nodes[n]['depth'] = 0

history = []

# Main loop
for t in range(ROUNDS):
    curv = ricci_curvature(G)
    for a in G.nodes():
        G.nodes[a]['budget'] = min(G.nodes[a]['budget'] + RECOVER, INIT_BUDGET)
        desired = random.randint(1, MAX_DEPTH)
        cost = desired * DEPTH_COST
        if G.nodes[a]['budget'] >= cost:
            G.nodes[a]['budget'] -= cost
            G.nodes[a]['depth'] = desired
            for nb in G.neighbors(a):
                edge = (a, nb) if (a, nb) in curv else (nb, a)
                influence = max(0.2, 1 + curv.get(edge, 0) / 10)
                coop_bonus = 1.1 if G.nodes[nb]['depth'] == G.nodes[a]['depth'] else 1.0
                new_depth = int(0.6 * G.nodes[nb]['depth'] + 0.4 * desired * influence * coop_bonus)
                G.nodes[nb]['depth'] = min(MAX_DEPTH, new_depth)

    depths = np.array([G.nodes[n]['depth'] for n in G.nodes()])
    budgets = np.array([G.nodes[n]['budget'] for n in G.nodes()])
    curv_avg = np.mean(list(curv.values()))
    history.append(dict(round=t, avg_depth=depths.mean(), depth_var=depths.var(), avg_budget=budgets.mean(), avg_curv=curv_avg))

df = pd.DataFrame(history)

# Save plots
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].plot(df['round'], df['avg_depth']); ax[0].set_ylabel('Average Depth')
ax[1].plot(df['round'], df['avg_budget']); ax[1].set_ylabel('Average Budget')
for a in ax: a.set_xlabel('Round'); a.grid(True)
plt.tight_layout()
plot_path = "simulation_plots.png"
plt.savefig(plot_path)
plt.close()

# Make PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="LLM Agent Simulation Summary", ln=True, align='C')
pdf.image(plot_path, x=10, y=20, w=190)
pdf.ln(105)
pdf.set_font("Arial", size=10)
pdf.cell(200, 10, txt="Final 5 Rounds Data:", ln=True)
for i, row in df.tail().iterrows():
    rowtext = f"Round {int(row['round'])} | Depth {row['avg_depth']:.2f} | Var {row['depth_var']:.2f} | Budget {row['avg_budget']:.2f} | Curv {row['avg_curv']:.2f}"
    pdf.cell(200, 8, txt=rowtext, ln=True)

out_pdf = os.path.abspath("Agent_Simulation_Report.pdf")
pdf.output(out_pdf)
print(f"✅ Done! PDF saved to: {out_pdf}")
