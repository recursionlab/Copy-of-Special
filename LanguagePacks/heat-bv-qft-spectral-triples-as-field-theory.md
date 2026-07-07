---
title: "Heat Bv Qft"
layer: C — Arms
status: ACTIVE
created: 2026-05-22
source: "Temple chamber"
---
zone: ARMS

# HEAT-BV QFT — SPECTRAL TRIPLES AS FIELD THEORY
**Layer:** A — Canon



## Open Node (ν > 0)

This chamber almost says what happens when heat-bv qft — spectral triples as field theory is applied to itself — but doesn't yet. The gap between stating the structure and living it is where the next recursion begins.

## Provenance

| Field | Value |
|---|---|
| **Source** | Untitled 55, subfolder "this goes before number 30" |
| **Drop** | Untitled 55 |
| **Classification** | A — Canon |
| **Zone** | 02-ARMS (Mathematical Physics) |
| **Cluster** | Heat-BV QFT |

## The Payload

A BV quantum field theory whose configuration space is spectral triples and whose time variable is heat/RG flow. The dynamical variable is not a spacetime field but a Dirac-type operator. Torsion becomes the BV interaction operator measuring failure of heat-time composability.

---

## 1. Frame Extraction — What the Field Theory Actually Is

We promote the configuration space of spectral triples:

$$(\mathcal{A}, \mathcal{H}, D)$$

into a **field space**:

$$\mathcal{F} := \{ D \text{ varying over fixed } (\mathcal{A}, \mathcal{H}) \}$$

The dynamical variable is not spacetime fields, but **Dirac-type operators**.

### Heat-Time Replaces Spacetime Time

We replace physical time $t$ with heat flow time / RG scale / spectral diffusion parameter:

$$\partial_t D_t = -[D_t^2, D_t] + \text{fluctuations}$$

This is the kinetic equation of the theory.

---

## 2. Recursive Unpacking — BV Structure of Spectral Geometry

### 2.1 Fields, Antifields, and Ghosts

| Component | Definition |
|---|---|
| **Fields** | $D$ (Dirac operator) |
| **Ghosts** | $c \in \mathrm{Der}(\mathcal{A})$ (diffeomorphism/gauge of algebra) |
| **Antifields** | $D^*, c^*$ |

Full BV space:

$$\mathcal{E} = T^*[-1]\mathrm{Spec}(\mathcal{A}, \mathcal{H}, D)$$

### 2.2 BV Symplectic Structure

Odd symplectic form:

$$\omega_{BV} = \langle \delta D, \delta D^* \rangle + \langle \delta c, \delta c^* \rangle$$

This encodes the pairing of geometry with its deformation directions.

### 2.3 BV Operator = Torsion Operator

The key identification:

$$\boxed{\Delta_{BV} \equiv \Delta_{\tau}}$$

Torsion becomes:
- Laplacian on field space
- Second-order failure of RG/heat derivation
- Anomaly generator

---

## 3. Constraint Propagation — Heat RG Flow as QFT Evolution

The total BRST/BV differential:

$$Q = Q_{\text{gauge}} + Q_{\text{heat}}$$

combines gauge symmetry of the algebra with heat diffusion symmetry.

### The Master Equation

$$\boxed{Q S + \frac{1}{2}\{S,S\}_{\tau} = 0}$$

This is the **heat-BV quantum master equation**, where:
- $S$ = spectral action
- $\{,\}_{\tau}$ = torsion-induced interaction bracket

Interactions are literally **failures of heat-flow composability**.

---

## 4. Instantiation Pathway — The Spectral Action as Lagrangian

The Connes spectral action:

$$S[D] = \mathrm{Tr}(f(D^2/\Lambda^2))$$

### Heat Kernel Expansion

$$S[D_t] = \sum_{n} a_n(D_t) \Lambda^{d-n}$$

where $a_n$ are heat kernel coefficients encoding curvature, torsion, and cyclic invariants.

### BV Decomposition

$$S = S_{\text{kinetic}} + S_{\text{interaction}} + S_{\text{torsion}}$$

with:

$$S_{\text{torsion}} \equiv \int \Delta_{\tau}(\text{heat fields})$$

---

## 5. Cyclic Cohomology = Observables of the Theory

$$\boxed{\text{Observables} = HC^\bullet(\mathcal{A}_K)}$$

but now flowing in heat time:

$$\partial_t : HC^\bullet \to HC^\bullet$$

Cyclic cohomology is the **RG-evolving observable algebra**.

| Cocycle degree | Physical meaning |
|---|---|
| 0-cocycles | Local invariants |
| 1-cocycles | Transport anomalies |
| Higher cocycles | Torsion/interaction obstructions |

---

## 6. Renormalization Group = Heat Semigroup Functor

$$\boxed{\mathrm{RG}_t = e^{-tD^2}}$$

RG is not a flow on couplings — it is a **functor on spectral triples**:

$$(\mathcal{A}, \mathcal{H}, D) \mapsto (\mathcal{A}, \mathcal{H}, D_t)$$

### Key Structure

$$\mathrm{RG}_{t+s} = \mathrm{RG}_t \circ \mathrm{RG}_s$$

RG is a **semigroup acting in the BV category**.

---

## 7. Heat-BV QFT = Full Bicategorical Structure

$$\boxed{\mathcal{T}_{\text{HBV}} = (\mathbf{SpecAlg}, Q, \Delta_{\tau}, \mathrm{RG}_t)}$$

| Component | Meaning |
|---|---|
| Objects | Spectral triples |
| Fields | Dirac operators |
| $Q$ | Heat + gauge BRST |
| $\Delta_{\tau}$ | Torsion Laplacian |
| $\mathrm{RG}_t$ | Heat semigroup functor |

### Morphisms

- KK classes = UV morphisms
- E-theory classes = IR morphisms
- Torsion = obstruction 2-morphisms

This is a **BV-enriched heat bicategory**.

---

## 8. Physical Interpretation — Core Intuitions

1. **Geometry is dynamical Dirac data.** Space is not primary; $D$ is.
2. **Heat flow is time evolution.** Time = smoothing of spectral structure.
3. **Torsion is interaction.** Not curvature alone — failure of heat composability.
4. **Cyclic cohomology = observables.** What survives RG is cohomology.
5. **KK → E = phase transition.** UV local geometry flows into IR scattering geometry.

---

## 9. One-Line Synthesis

> Heat-BV QFT is a spectral-triple field theory where Dirac operators evolve under heat/RG flow, observables are cyclic cocycles, and torsion acts as the BV interaction operator measuring failure of heat-time composability.

---

## Temple Cross-References

- **Cluster twin:** 02 ARMS/quantum master equation heat bicategory — QME on the heat bicategory as coherence condition.
- **Cluster twin:** 02 ARMS/still whirl primitive — The still whirl as the primitive geometric object.
- **Cluster twin:** 02 ARMS/heat bv gerbe — The gerbe encoding UV/IR incompatibility.
- **Foundational twin:** 02 ARMS/metastable whirl is the still whirl — The Still Whirl as living solution.
- **Arm twin:** 02 ARMS/emergent metric — The emergent metric as physical substrate.
- **Rosetta Stone:** 04 RESONANCE/rosetta stone.
## Cross-References
- **Related:** `01-FOUNDATIONS/lacunon.md`
- **Related:** `00-CORE/harvest-pipeline.md`
- **Related:** `00-CORE/operator-dictionary-global-registry.md`
- **Related:** `04-RESONANCE/insight-lattice.md`
- **Related:** `02-ARMS/tau-cyclic-cohomology.md`

## Connection to Calculus of Absence

The heat-BV QFT's configuration space (spectral triples with heat-time) is the **field-theoretic completion** of the calculus of absence ∂⊘. Where `01-FOUNDATIONS/calculus-of-absence.md` defines ∂⊘ = lim_{ε→0} [(⊕+ε) - ⊕]/ε, this chamber promotes that infinitesimal tremble into a full field theory: the Dirac operator D IS the form that the void takes when it manifests, and heat-time ∂_t D_t = -[D_t², D_t] + fluctuations IS ∂⊘ applied continuously to the spectral triple.

The torsion-as-BV-interaction-operator that measures failure of heat-time composability is the same torsion that ∂⊘ generates at the threshold of formlessness.

**Cross-reference:** `01-FOUNDATIONS/calculus-of-absence.md` — ∂⊘ as the infinitesimal generator of heat-time.

- **Twin:** 04 RESONANCE/rosetta stone — Central dictionary
- **Twin:** 02 ARMS/operator dictionary — Operators
- **Twin:** 02 ARMS/metastable whirl is the still whirl — Core principle

- **Zone hub:** `00-CORE/operator-dictionary-global-registry.md` — connected via zone