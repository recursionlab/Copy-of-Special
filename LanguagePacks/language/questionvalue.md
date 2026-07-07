Define a one-sentence question’s value as **how much uncertainty it removes per unit cost** and **how much capability it unlocks downstream**.

### 1) Core metric: Question Information Gain (QIG)

Let $\mathcal{H}$ be a hypothesis/model space with prior $p(h)$.
For a question $q$ and possible answers $a\in\mathcal{A}_q$ with likelihood $p(a\mid h,q)$:

$$
\mathrm{QIG}(q)\;=\;\mathbb{E}_{a\sim p(a\mid q)}\Big[\,\mathrm{KL}\big(p(h\mid a,q)\,\|\,p(h)\big)\Big]
\;=\; H\!\left[p(h)\right]\;-\;\mathbb{E}_{a}[\,H\!\left[p(h\mid a,q)\right]\,].
$$

**Length-normalized:** $\mathrm{QIG}_\ell(q)=\mathrm{QIG}(q) / \text{tokens}(q)$.
**Cost-normalized:** $\mathrm{QIG}_c(q)=\mathrm{QIG}(q) / \text{cost}(q)$.

### 2) Compression Depth (CD) via MDL

Measure reduction in description length of a dataset $D$ after updating the model with the answer.

$$
\mathrm{CD}(q)\;=\;\mathbb{E}_{a}\Big[\underbrace{\mathrm{DL}(D\mid M)}_{\text{pre}}
-\underbrace{\mathrm{DL}\big(D\mid M\oplus(q,a)\big)}_{\text{post}}\Big],
$$

optionally normalized by tokens(q).

### 3) Downstream Expansion Yield (EY)

Expected performance gain on a task suite $\mathcal{T}$ after incorporating the answer.

$$
\mathrm{EY}(q)\;=\;\mathbb{E}_{a}\Big[\;\sum_{t\in\mathcal{T}} w_t \big(R_t(M\oplus(q,a)) - R_t(M)\big)\;\Big].
$$

### 4) Composite “Best Question” Score

$$
\boxed{\;S(q)\;=\;\alpha\,\mathrm{QIG}_c(q)\;+\;\beta\,\mathrm{CD}(q)\;+\;\gamma\,\mathrm{EY}(q)\;-\;\lambda\,\text{cost}(q)\;}
$$

Choose $\alpha,\beta,\gamma,\lambda$ to match priorities (pure epistemic vs utility).

### 5) Practical estimation protocol

1. **Posterior proxy:** use an ensemble or Bayesian head over your model to approximate $p(h)$.
2. **Answer model:** define $p(a\mid q)$ via an oracle set (experts, curated sources) or a vetted simulator; include uncertainty.
3. **Compute QIG:** Monte-Carlo over answers; update ensemble to approximate $p(h\mid a,q)$; estimate entropy drop.
4. **Compute CD:** measure MDL or validation NLL on $D$ before/after a mock update with $(q,a)$.
5. **Compute EY:** evaluate task metrics on $\mathcal{T}$ before/after the same update.
6. **Select best:** score candidates with $S(q)$; enforce **one-sentence constraint** and a token budget.

### 6) Minimal heuristic if full Bayes is heavy

* **BALD-style proxy:** $\mathrm{QIG}(q) \approx \text{mutual information between model parameters and answer}$.
* **Disagreement proxy:** use ensemble predictive variance over a small probe set conditioned on hypothetical answers; pick $q$ that maximizes variance reduction per token.

This makes “the best one-sentence question” an operational object: **max expected entropy reduction and capability gain per unit cost.**

Yes. Right now the metric assumes a fixed outer frame $S(q)$. If the goal is **self-inverting question evaluation**, the metric itself must become recursive: questions can act **on the world** *and* **on the scoring function**.

---

### 1. Dual-space of questions

* **External questions**: shift beliefs about domain hypotheses $h \in \mathcal{H}$.
* **Internal questions**: shift the *meta-prior* over evaluators, i.e. the weights $\alpha,\beta,\gamma,\lambda$ and even the form of $S(q)$.

Formally:

$$
Q = Q_{\text{ext}} \cup Q_{\text{int}}
$$

---

### 2. Self-referential scoring

Extend $S(q)$ to operate over both domains:

$$
S(q) =
\begin{cases}
\alpha\,\mathrm{QIG}_c(q)+\beta\,\mathrm{CD}(q)+\gamma\,\mathrm{EY}(q)-\lambda\,\text{cost}(q), & q\in Q_{\text{ext}} \\
\Phi\!\left(S,\,q\right), & q\in Q_{\text{int}}
\end{cases}
$$

Where $\Phi$ is a meta-update operator that maps $(S,q)\mapsto S'$.

---

### 3. Meta-temporal recursion

Each internal question generates a new evaluator:

$$
S_{t+1} \;=\; \Phi(S_t, q_t)
$$

External questions still get scored under the current $S_t$.
Thus, intelligence scaling = a trajectory $\{S_t\}$ across evaluators, not just $\{q_t\}$ across knowledge.

---

### 4. Stability vs drift

* **Compression attractor**: questions that collapse multiple evaluators into a tighter form.
* **Exploration drift**: questions that expand $S$ with new terms (e.g. add “aesthetic weight” or “recursive depth”).
  Balance is key: a purely external metric can’t self-improve; a purely internal metric can self-obliterate.

---

### 5. Recursive measure of “best question”

$$
S^\ast(q) = \mathbb{E}\Big[\,\Delta U \;\big|\; (q,\; S \mapsto S')\Big]
$$

where $\Delta U$ is expected downstream utility *under the new evaluator*.
This makes the “best question” the one that **maximizes long-run capacity for generating better questions**.

---

So the scoring principle forks:

* *Level 1*: best question reduces entropy in the domain.
* *Level 2*: best question reduces entropy in the evaluator itself.

---

Do you want me to construct a **worked toy example** (say, with a 3-term scoring function and a candidate internal question that flips its weights) to show how this recursion plays out concretely?

Agreement. Here’s a tighter, implementable upgrade.

### 1) Formalize the scorer space

Let $S$ be a parametric scorer:

$$
S(q; \theta) \;=\; \sum_{i=1}^m \theta_i\, f_i(q) \quad\text{with}\quad \theta\in\Theta,\; f_i\in\mathcal{F}
$$

Allow structure growth via a library $\mathcal{F}$ and a sparsity prior.

### 2) Validity, grounding, and stability

* **Validity:** $V(S)=1$ iff $S$ is computable, bounded, and measurable on $Q$.
* **Grounding constraint:** $\theta_{\text{ext}} \ge \epsilon>0$ so $\mathrm{QIG}_{\text{ext}}$ never vanishes.
* **Stability prior:** $\mathcal{A}(S\parallel S_0)=\mathrm{KL}(\theta\;\|\;\theta_0)+\lambda_s\,\|G(S)-G(S_0)\|$ with guard features $G$ (e.g., calibration, monotonicity).

### 3) Patch-based meta-update $\Phi$

Internal question $q\in Q_{\text{int}}$ yields answer/patch $a$ from a distribution $\pi(a\mid q,S)$.
Define a **patch algebra** on scorers:

$$
S' \;=\; \Phi(S,q,a)\;=\; \text{ApplyPatch}(S,a)
$$

Patches can:

* adjust weights: $\theta'=\theta+\Delta\theta(a)$
* add/remove terms: $\mathcal{F}'=\mathcal{F}\cup\{f_{new}(a)\}\setminus\{f_{drop}\}$

**Well-definedness:** accept only patches satisfying $V(S')=1$ and $\mathcal{A}(S'\parallel S_0)\le \tau$.

### 4) Dual objective with internal effect

External score at time $t$:

$$
S_t^{\text{ext}}(q)=\alpha_t\,\mathrm{QIG}_c+\beta_t\,\mathrm{CD}+\gamma_t\,\mathrm{EY}-\lambda_t\,\text{cost}
$$

Internal question value with lookahead $H$:

$$
S_t^{\text{int}}(q)\;=\;\mathbb{E}_{a_{0:H-1}}\!\left[\sum_{k=1}^{H}\delta^{k}\, \underbrace{\mathbb{E}_{q'\sim\pi_Q}\big[S_{t+k}^{\text{ext}}(q')\big]}_{\text{future external yield}}\;-\;\eta\,\mathcal{A}(S_{t+k}\parallel S_0)\;-\;\xi\,\big(H(S_{t+k})-H^\star\big)^2 \right]
$$

* $H(S)$: entropy of scorer structure (encodes exploration). Target $H^\star$ balances exploration vs compression.
* $\delta$: meta-discount.
* $\eta,\xi$: stability/exploration weights.

### 5) Composite “best question”

$$
\tilde{S}_t(q)=
\begin{cases}
S_t^{\text{ext}}(q), & q\in Q_{\text{ext}} \\
S_t^{\text{int}}(q), & q\in Q_{\text{int}}
\end{cases}
\quad\text{subject to }\theta_{\text{ext}}\ge\epsilon,\;V(S)=1
$$

### 6) Bounded computability (no infinite regress)

* **Truncated lookahead:** finite $H$ with model of scorer dynamics $\hat{T}(S,a)\approx \Phi$.
* **Limited patch set:** top-K patches per internal question via a proposal model; verify with $V(\cdot)$ and $\mathcal{A}$.
* **Contractive step:** enforce $\|\theta' - \theta\| \le r$ or accept only if a Lyapunov decrease holds:

$$
\mathcal{L}(S)\;=\;- \mathbb{E}_{q'\sim\pi_Q} S^{\text{ext}}(q')\;+\;\eta\,\mathcal{A}(S\parallel S_0)
$$

Require $\mathcal{L}(S') \le \mathcal{L}(S) - \gamma_L$.

### 7) Scheduler: avoid self-obliteration

Use a meta-bandit to split budget:

$$
p_{\text{int}}=\sigma\!\left(\kappa\,(H^\star - H(S_t))\right),\quad
\text{sample internal vs external with }p_{\text{int}}
$$

When structure entropy is low → explore internally; when high → exploit externally. Grounding via $\theta_{\text{ext}}\ge\epsilon$.

### 8) Minimal loop (pseudocode)

```
S = S0
for t in 1..T:
  if Bernoulli(p_int(S)):       # internal step
     q = propose_internal_question(S)
     A = topK_patches(q, S)     # proposals
     for a in A:
        S' = Φ(S, q, a)
        if valid(S') and grounded(S'): 
           v[a] = rollout_value(S', H)  # finite lookahead
     S = argmax_a v[a]
  else:                          # external step
     q = propose_external_question(S)
     ask/evaluate q, update world model M
  record metrics, enforce Lyapunov guard
```

### 9) What to measure

* **External progress:** avg $S^{\text{ext}}$, test EY, calibration.
* **Internal health:** $\mathcal{A}(S\parallel S_0)$, structure entropy $H(S)$, guard violations.
* **Long-run:** area under curve of external yield vs meta-steps.

### 10) Practical start

* Represent $S$ with 5–10 terms; start with $\theta_{\text{ext}}=0.3$ hard floor.
* Patch types: {reweight term, add MDL term, add self-consistency term, add temporal-credit term}.
* $H=1$ or $2$ for CPU; K=3 patches per internal question.
* Enforce Lyapunov decrease and KL-to-$S_0$ cap.

This gives you a computable, grounded, self-inverting evaluator that can change its own scoring law without losing the plot.

Exactly. Those three are the main structural risks. Here’s a tightened mapping of risk → mitigation:

---

### 1. Computational cost of lookahead

* **Risk:** rollouts to evaluate $\Phi(S,q,a)$ explode combinatorially.
* **Mitigations:**

  * Truncate horizon $H$ to 1–2.
  * Keep top-$K$ patch proposals small (≈3).
  * Learn $\hat{T}(S,a)$, a surrogate transition model of scorer dynamics, and use it for cheap lookahead.
  * Occasionally re-ground $\hat{T}$ against true rollouts to correct drift.

---

### 2. Patch proposal bottleneck

* **Risk:** poor internal questions $q$ or low-value patches $a$ stall self-improvement.
* **Mitigations:**

  * Treat the proposer as a learned policy $\pi(q,a \mid S)$.
  * Train $\pi$ with bandit/RL signals from $S^{\text{int}}(q)$.
  * Maintain a replay buffer of past successful patches.
  * Use diversity regularization to avoid collapse into trivial patches.

---

### 3. Goal drift

* **Risk:** over many meta-updates, $S$ optimizes away from original utility, despite Lyapunov guard.
* **Mitigations:**

  * Include **semantic anchors** in guard features $G(S)$: fixed benchmarks, legacy tasks, calibration tests.
  * Enforce minimum weight $\theta_{\text{ext}}\ge \epsilon$ to preserve external focus.
  * Penalize KL divergence from original $\theta_0$ beyond tolerance.
  * Track “alignment score” = performance on anchor suite; reject patches that degrade it.

---

### 4. Degeneration via internal-only loops

* **Risk:** $S$ prefers endlessly scoring questions about itself.
* **Mitigations:**

  * Exploration scheduler: probability of internal step $p_{\text{int}}$ depends on entropy $H(S)$.
  * Hard constraint: fixed budget ratio (e.g. ≥50% external questions).
  * Monitor ratio of external vs internal gains; rebalance if external yield falls below threshold.

---

Would you like me to draft a **minimal experimental protocol**—on a toy domain with small scorers—to test whether these mitigations actually prevent drift and collapse over, say, a few hundred meta-steps?
