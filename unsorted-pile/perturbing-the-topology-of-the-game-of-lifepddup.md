---
stub: true
title: "Perturbing The Topology Of The Game Of Life.Pd Dup"
created: 2026-05-12
updated: 2026-05-12
type: concept
tags: [fixed_point, "ingested"]
sources: ["Perturbing the Topology of the Game of Life.pd_dup.md"]
psi_tier: fixed_point
---

# Perturbing The Topology Of The Game Of Life.Pd Dup

# Perturbing the Topology of the Game of Life.pd

Perturbing the Topology of the Game of Life
Increases its Robustness to Asynchrony
Nazim Fatès1 and Michel Morvan1,2
1 ENS Lyon - LIP UMR CNRS - ENS Lyon - UCB Lyon - INRIA 5668 46, allée d’Italie - 69 364 Lyon Cedex 07 - France.
2 Institut Universitaire de France {Nazim.Fates},{Michel.Morvan}@ens-lyon.fr
Abstract. An experimental analysis of the asynchronous version of the “Game of Life” is performed to estimate how topology perturbations modify its evolution. We focus on the study of a phase transition from an “inactive-sparse phase” to a “labyrinth phase” and produce experimental data to quantify these changes as a function of the density of the initial configuration, the value of the synchrony rate, and the topology missing-link rate. An interpretation of the experimental results is given using the hypothesis that initial “germs” colonize the whole lattice and the validity of this hypothesis is tested.
1 Introduction
Cellular automata were originally introduced by von Neumann in order to study the logical properties of self-reproducing machines. Following Ulam’s suggestions, the requirements he made for constructing such a machine was the discreteness of space using cells, discreteness of time using an external clock, the symmetry of the rules governing cells interaction, and the locality of these interactions; it resulted in the birth of the cellular automaton (CA) model. In order to make the self-reproduction not trivial he also required that the self-reproducing ma-chine should be computation-universal (e.g., [13]). The resulting CA used 29 elementary states for each cell and updates used 5 neighbors. Later on, Conway introduced a CA called “Game of Life” or simply Life which was also proved to be computation universal [2]. This CA is simpler than von Neumann’s in at least two ways: the local rule uses only two states and it can be summarized with by sub-rules (birth and death rules).
However, the question remained open to know what is the importance of perfect synchrony on a CA behavior. Indeed, since the first study on the effects of asynchronous update carried out by Ingerson and Buvel [6], many criticisms have been addressed to the use of the CA as models of natural phenomena. Some authors investigated, using various techniques, how synchrony variations changed CA qualitative behavior [6], [10], [3], [5], [14], [8]. All studies agree on the
fact that for some CA, there are situations in which small changes in the update method lead to qualitative changes of the evolution of the CA, thus showing the need for further studies of robustness to asynchronism. Similarly, some authors investigated the effect of perturbing the topology (i.e., the links between cells) in one dimension [11] by adding links, or in two dimensions with small-world construction algorithms [15], [9]. Here too, the studies showed that robustness to topology changes was a key factor in the CA theory and that some CA showed “phase transitions” when varying the intensity of the topology perturbation.
The aim of this work is to question, in the case of Life, the importance of the two hypotheses used in the classical CA paradigm: what happens when the CA is no longer perfectly synchronous and when the topology is perturbed? In Section 2, we present the model and describe the qualitative behavior induced by the introduction of asynchronism and/or topology perturbations. In Section 3.1, we observe that (i) Life is sensitive to asynchronism; (ii) robust to topology perturbations and (iii) that the robustness to asynchronism is increased when the topology characteristics become irregular. Section 3.2 is devoted to presenting a rigorous experimental validation and exploration of these phenomena for which a potential explanation based on the notion of “germ” development is discussed and studied in Section 4.
2 The Model
Classically, Life is run on a regular subset of Z2. For simulation purposes, the configurations are finite squares with N ×N cells and the neighborhood of each cell is constituted of the cell itself and the 8 nearest neighbors (Moore neighbor-hood). We use periodic boundary conditions meaning that all cell position indices are taken in Z/NZ. The type of boundary conditions does play an important role at least for small configurations as shown in [4].
Life belongs to the outer-totalistic (e.g., [12], [11]) class of CA: the local transition rule f is specified as a function of the present state q(c) and of the number S1(c) of cells with states 1 in the neighborhood. The Life transition function f(q, S1) can be written:
f(0, S1) = 1 if S1 = 3 ; f(0, S1) = 0 otherwise, (birth rule)
f(1, S1) = 1 if S1 = 2 or S1 = 3;f(1, S1) = 0 otherwise. (death rule)
In the sequel, we consider Life as an asynchronous cellular automaton (ACA) acting on a possibly perturbed topology.
There are several asynchronous dynamics: one may, for example update cells one by one in a fixed order from left to right and from bottom to top. This update method is called “line-by-line sweep” [14] and it has been shown that this type of dynamics introduce spurious behaviors due to the correlation between the spatial arrangement of the cells and the spatial ordering of the updates. These correlations can only be suppressed with a random updating of the cells. In this work, we choose to examine only one type of asynchronism which consists
in applying the local rule, for each cell independently, with probability α. The parameter α is called the “synchronicity” [5] or the synchrony rate; one can also view it as a parameter that would control the evolution of a probabilistic cellular automata (PCA) where the transition function results in applying Life rule with a probability α and the identity rule with probability 1− α.
We choose to perturb topology by definitely removing links between cells. Let G0 = (L, E0) be the oriented graph that represents cells interactions: (c, c′) ∈
E if and only if c′ belongs to neighborhood of c. The graph with perturbed topology G = (L, E) is obtained by examining each cell c ∈ L and, for each cell in the neighborhood of c and removing the link (c, c′) with a probability ǫ−; the parameter ǫ− is called missing-link rate. Note that, as the local function is expressed in an outer-totalistic mode, we can still apply it on neighborhoods of various sizes. The definition we use induces an implicit choice of behavior in the case where a link is missing : the use of S1 in the local rule definition implies that the cell will consider missing cells of the neighborhood as being in state 0. Other choices would have been possible; for example assuming this state to be 1 or the current value of the cell itself.
3 Observations and Measures
3.1 Qualitative Observations
Figure 1 shows that the behavior of Life depends on the synchrony rate α: a phase with labyrinthine shapes appears when α is lowered. Bersini and Detours studied this phenomenon and noticed that the asynchronous (sequential) updating of Life was significantly different from the (classical) synchronous version in that sense that a “labyrinth phase” (denoted by LP) appeared (see Fig. 1 below). For small lattice dimensions, they observed the convergence of this phase to a fixed point and concluded that asynchrony had a stabilizing effect on Life [3].
The phase transition was then measured with precision by Blok and Berg-ersen, who used the final density (i.e, the fraction of 1’s sites) as a means of quantifying the phase transition. They measured the value αc for which the phase transition was to be observed and found αc = 0.91 [5]. They showed that the type of phase transition is continuous (or a second-order transition): when α is decreased from α = 1.0 to α = αc, no change is observed in terms of the values of the average density. When we have α < αc the “labyrinth phase” gradually appears and the average density starts increasing in a continuous way. It is thus the derivative of the density that shows discontinuity rather than the function itself.
Figure 2 shows that the removal of links between cells does not qualitatively perturb the aspect of the final configurations attained. So, according to the observation of steady states, synchronous Life seems somehow robust to topology perturbations. However, we also noticed that the transients are much shorter in presence of topology errors: for N = 50×50, the order of magnitude of transients are T = 1000 for ǫ− = 0 and T = 100 for ǫ− = 0.1.
α = 1.0 α = 0.5 sequential updating
Fig. 1. Life configurations for N = 50 × 50, after T = 100 time steps, starting from a random configuration of density dini = 0.5. In the sequential updating, cells are randomly updated one after another.
ǫ− = 0 ǫ− = 0.05 ǫ− = 0.10
Fig. 2. Life configurations for synchronous evolution (α = 1.00) with N = 50 × 50, after T = 1000 time steps, starting from a random configuration of density dini = 0.5.
ǫ− = 0 ǫ− = 0.05 ǫ− = 0.10
Fig. 3. Life configurations for N = 50× 50, after T = 1000 time steps, starting from a random configuration of density dini = 0.5: (up) α = 0.90 (middle) α = 0.75 (bottom) α = 0.50. The figure in the upper-left corner shows that the system is still in a transient mode.
Figure 3 shows what happens when both asynchronism and topology pertur-bations are added. Rows of Fig. 3 display the behavior with a fixed synchrony rate α and columns display the behavior with a fixed missing-link rate ǫ−. We see that increasing topology errors from ǫ− = 0 to ǫ− = 0.05 makes the phase transition occur for a higher value of synchrony rate αc. With a further increase from ǫ− = 0.05 to ǫ− = 0.10, the phase transition cannot be observed any more, at least for the selected values of α.
This demonstrates that both parameters ǫ− and α control the phase tran-sition between the “inactive-sparse phase” [9] and the “labyrinth phase” (LP). The next section is devoted to quantitatively measure the interplay of these two control parameters.
3.2 Quantitative Approach
To detect the apparition of the labyrinth phase (LP), we need to look at the configurations by eye or to choose an appropriate macroscopic measure. Clearly, a configuration in LP contains much more 1’s than a configuration in the “inactive-sparse phase” ([9]). This leads us to quantify the change of behaviour using the measurement of the “steady-state density” (i.e. the average density after a transient time has elapsed). This method has been chosen by various authors (e.g. Blok and Bergersen [5]) and it has been applied to exhaustively study both the dynamics [7] and the robustness to asynchronism [8] of one dimensional elementary cellular automata.
We define the steady-state density ρ(dini, α) using the sampling algorithm defined in [8]: Starting from a random initial configuration constructed with a Bernoulli process of parameter dini, we let the ACA evolve with a synchrony rate α during a transient time Ttransient then we measure the value of the density during a sampling time Tsampling. The value of ρ is the average of the sampled densities.
The sampling operation results in the definition of a function ρ(dini, α) that can be represented in the form of a “sampling surface”. This surface contains part of the information on how the behaviour of a CA is affected by asynchronism. Figure 4 shows the experimental results obtained for N = 50 × 50, Ttransient = 1000 , Tsampling = 1000. The transient time Ttransient is chosen according to the observations made in [1] where equivalent transient times were found for greater lattice sizes.
Let us first look at what happens for dini ∈ [0.2, 0.8] (right column of Fig. 4). The invariance of the surface relatively to the dini-axis shows that the macro-scopic behavior of Life does not depend on the value of this parameter within this range. The upper right corner of Fig. 4 shows that for ǫ− = 0 (regular topology), the phase transition occurs for αc ∼ 0.90 as expected [5]. However, when ǫ− increases, experiments show that αc also decreases. This means that the settlement of LP becomes more difficult as links are removed; this can be inter-preted as an increase of the robustness to asynchrony. We can observe that for ǫ− = 0.10 , the surface is flat and horizontal, which means that the behavior is
Sampling Surface for Moore2D2  [50,1000,1000,0]
Avrg
0.02  0.04  0.06  0.08  0.1  0.12  0.14  0.16  0.18  0.2 Intit density
0.2  0.3
0.4  0.5
0.6  0.7
0.8  0.9
1
synchrony rate
0  0.05  0.1
0.15  0.2
0.25  0.3
0.35  0.4
0.45  0.5
Sampling Surface for Moore2D2  [50,1000,1000,0]
Avrg
0.2  0.3  0.4  0.5  0.6  0.7  0.8 Intit density
0.2  0.3
0.4  0.5
0.6  0.7
0.8  0.9
1
synchrony rate
0  0.05  0.1
0.15  0.2
0.25  0.3
0.35  0.4
0.45  0.5
Sampling Surface for Moore2D4  [50,1000,1000,0]
Avrg
0.02  0.04  0.06  0.08  0.1  0.12  0.14  0.16  0.18  0.2 Intit density
0.2  0.3
0.4  0.5
0.6  0.7
0.8  0.9
1
synchrony rate
0  0.05  0.1
0.15  0.2
0.25  0.3
0.35  0.4
0.45  0.5
Sampling Surface for Moore2D4  [50,1000,1000,0]
Avrg
0.2  0.3  0.4  0.5  0.6  0.7  0.8 Intit density
0.2  0.3
0.4  0.5
0.6  0.7
0.8  0.9
1
synchrony rate
0  0.05  0.1
0.15  0.2
0.25  0.3
0.35  0.4
0.45  0.5
Sampling Surface for Moore2D6  [50,1000,1000,0]
Avrg
0.02  0.04  0.06  0.08  0.1  0.12  0.14  0.16  0.18  0.2 Intit density
0.2  0.3
0.4  0.5
0.6  0.7
0.8  0.9
1
synchrony rate
0  0.05  0.1
0.15  0.2
0.25  0.3
0.35  0.4
0.45  0.5
Sampling Surface for Moore2D6  [50,1000,1000,0]
Avrg
0.2  0.3  0.4  0.5  0.6  0.7  0.8 Intit density
0.2  0.3
0.4  0.5
0.6  0.7
0.8  0.9
1
synchrony rate
0  0.05  0.1
0.15  0.2
0.25  0.3
0.35  0.4
0.45  0.5
Sampling Surface for Moore2D8  [50,1000,1000,0]
Avrg
0.02  0.04  0.06  0.08  0.1  0.12  0.14  0.16  0.18  0.2 Intit density
0.2  0.3
0.4  0.5
0.6  0.7
0.8  0.9
1
synchrony rate
0  0.05  0.1
0.15  0.2
0.25  0.3
0.35  0.4
0.45  0.5
Sampling Surface for Moore2D8  [50,1000,1000,0]
Avrg
0.2  0.3  0.4  0.5  0.6  0.7  0.8 Intit density
0.2  0.3
0.4  0.5
0.6  0.7
0.8  0.9
1
synchrony rate
0  0.05  0.1
0.15  0.2
0.25  0.3
0.35  0.4
0.45  0.5
Sampling Surface for Moore2D10  [50,1000,1000,0]
Avrg
0.02  0.04  0.06  0.08  0.1  0.12  0.14  0.16  0.18  0.2 Intit density
0.2  0.3
0.4  0.5
0.6  0.7
0.8  0.9
1
synchrony rate
0  0.05  0.1
0.15  0.2
0.25  0.3
0.35  0.4
0.45  0.5
Sampling Surface for Moore2D10  [50,1000,1000,0]
Avrg
0.2  0.3  0.4  0.5  0.6  0.7  0.8 Intit density
0.2  0.3
0.4  0.5
0.6  0.7
0.8  0.9
1
synchrony rate
0  0.05  0.1
0.15  0.2
0.25  0.3
0.35  0.4
0.45  0.5
Fig. 4. Sampling surfaces for ǫ− = [0 · · · 0.10], N = 50 × 50, Ttransient = 1000 , Tsampling = 1000. The left column has a different range for dini to focus on the be-havior for small initial densities.
not anymore perturbed by asynchronism (at least if we consider our observation function).
The left column of Fig. 4 shows the behavior of Life for dini ∈ [0, 0.2]. We observe two different abrupt change of behaviors. On the one hand, there is a value of dcini which separates the “inactive-sparse phase” and LP. On the other hand, the value of dcini increases as ǫ− increases. This means that LP becomes more difficult to reach when links are removed; which again can be interpreted as a gain of robustness.
Experiments were held for various lattice sizes and allowed to control that the sampling surface aspect was stable with N ; we however observed that when ǫ− and α are fixed, the value of dcini is a decreasing function of N .
All the previous phenomena may be the consequence of multiple intricate fac-tors. In the next section, we study the evolution of so called “micro-configurations” put in an empty array and propose a first hypothesis in the direction of under-standing these behaviors.
4 Micro-configurations Analysis
4.1 Experiments
The observation of the settlement of LP shows that it can develop from very localized parts of the lattice and then spreads across the lattice until it fills it totally. By analogy with a crystal formation, we call “germs” these particular configurations that have the possibility to give birth to an invasive LP. We inves-tigate the existence of germs by performing an exhaustive study of the potential evolution of micro-configurations, i.e. 3× 3 configurations that are placed in an empty array. There are 512 such configurations and we experimentally quantify, for each one, the probability that a it becomes a germ. Our goal is to infer the behavior of the whole structure from the evolution of these micro-configurations.
Setting the synchrony rate to α = 0.5, we used the following algorithm: For every micro-configuration i ∈ I, (a) we initialize the lattice N × N with i, and (b) we let the CA evolve until it reaches a fixed point or until it reaches LP. We repeat S = 1000 times operations (a) and (b) for the same initial micro-configuration but for a different update histories. We consider that the CA has reached LP if the density is greater of equal than a limit density d∞ = 0.1. Indeed, we observed that if the CA was able to multiply the number of 1’s from the micro-configuration to a constant ratio of the lattice, then it will almost surely continue to invade the whole lattice and, asymptotically, reach LP. We experimentally obtain the probability Pgerm[i] that a configuration i is a germ. Grouping micro-configurations by the number k of 1’s they contain, we obtain an array with 9 entries Pgerm(k), k ∈ [0, 9], displayed in Table 1.
Results show that for k < 3, Pgerm(k) = 0, which means that all such micro-configurations always tend to extinction. For n ≥ 3, the probability to reach LP increases as n increases.
Table 1. Probability Pgerm(k) for a micro-configuration to be a germ (in %) as a function of the number k of 1’s for different missing-link rates ǫ− (in %).
k 0 1 2 3 4 5 6 7 8 9
ǫ− = 0 0 0 0 1.28 4.34 7.88 14.52 21.76 29.92 40.90 ǫ− = 2 0 0 0 0.28 2.17 3.93 7.22 11.18 15.34 21.70 ǫ− = 4 0 0 0 0.19 0.72 1.24 2.40 3.96 5.52 8.00 ǫ− = 6 0 0 0 0.02 0.06 0.09 0.24 0.34 0.63 1.30
0
0.1
0.2
0.3
0.4
0.5

[... content truncated ...]

---

*Source: `Perturbing the Topology of the Game of Life.pd_dup.md` | Ingested: 2026-05-12 | Ψ-tier: fixed_point*
