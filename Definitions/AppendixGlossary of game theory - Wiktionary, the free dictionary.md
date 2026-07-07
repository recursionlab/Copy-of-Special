---
title: "Appendix:Glossary of game theory - Wiktionary, the free dictionary"
source: "https://en.wiktionary.org/wiki/Appendix:Glossary_of_game_theory"
author:
published:
created: 2026-04-10
description:
tags:
  - "clippings"
---
This is a glossary of [game theory](https://en.wiktionary.org/wiki/game_theory "game theory") —the branch of mathematics in which [games](https://en.wiktionary.org/wiki/game "game") are studied: that is, models describing human behaviour.

**Contents:** [A](#A) [B](#B) [C](#C) [D](#D) [E](#E) [F](#F) [G](#G) [H](#H) [I](#I) [J](#J) [K](#K) [L](#L) [M](#M) [N](#N) [O](#O) [P](#P) [Q](#Q) [R](#R) [S](#S) [T](#T) [U](#U) [V](#V) [W](#W) [X](#X) [Y](#Y) [Z](#Z)

## Notational conventions

[real numbers](https://en.wiktionary.org/wiki/real_number "real number")

${\displaystyle \mathbb {R} }$.

The set of **players**

${\displaystyle \mathrm {N} }$.

strategy space

${\displaystyle \Sigma \ =\prod _{i\in \mathrm {N} }\Sigma \ ^{i}}$. Where:

player i's strategy space

${\displaystyle \Sigma \ ^{i}}$ is the space of all possible ways in which player **i** can play the game.

strategy for player **i**

${\displaystyle \sigma \ _{i}}$ is an element of ${\displaystyle \Sigma \ }$.

complements

${\displaystyle \sigma \ _{-i}}$ an element of ${\displaystyle \Sigma \ ^{-i}=\prod _{j\in \mathrm {N} ,j\neq i}\Sigma \ ^{j}}$, is a tuple of strategies for all players other than **i**.

outcome space

${\displaystyle \Gamma \ }$ is in most textbooks identical to -

payoffs

${\displaystyle \mathbb {R} ^{\mathrm {N} }}$, describing how much gain (money, pleasure, etc.) the players are allocated by the end of the game.

## A

acceptable game

A *game form* such that for every possible *preference profiles*, the game has *pure Nash equilibria*, all of which are *pareto efficient*.

allocation of goods

A function ${\displaystyle \nu \ :\Gamma \ \to \mathbb {R} ^{\mathrm {N} }}$. The allocation is a *cardinal* approach for determining the good (e.g. money) the players are granted under the different outcomes of the game.

## B

best reply

The best reply to a given complement ${\displaystyle \sigma \ _{-i}}$ is a strategy ${\displaystyle \tau \ _{i}}$ that maximizes player **i'** s payment. Formally, we want:  
${\displaystyle \forall \sigma \ _{i}\in \ \Sigma \ ^{i}\quad \quad \pi \ (\sigma \ _{i},\sigma \ _{-i})\leq \pi \ (\tau \ _{i},\sigma \ _{-i})}$.

## C

[coalition](https://en.wiktionary.org/wiki/coalition "coalition")

Any subset of the set of players: ${\displaystyle \mathrm {S} \subseteq \mathrm {N} }$.

[Condorcet winner](https://en.wiktionary.org/w/index.php?title=Condorcet_winner&action=edit&redlink=1 "Condorcet winner (page does not exist)")

An outcome such that all *non-dummy* players prefer it to all other outcomes, given a *preference* *ν* on the *outcome space*.

cooperative game

A game in which players are allowed form coalitions (and to enforce coalitionary discipline). A cooperative game is given by stating a *value* for every coalition:

${\displaystyle \nu \ :2^{\mathbb {P} (N)}\to \mathbb {R} }$

It is always assumed that the empty coalition gains nil. *Solution concepts* for cooperative games usually assume that the players are forming the *grand coalition* ${\displaystyle N}$, whose value ${\displaystyle \nu (N)}$ is then divided among the players to give an allocation.

[coordination game](https://en.wiktionary.org/w/index.php?title=coordination_game&action=edit&redlink=1 "coordination game (page does not exist)")

A normal form game in which players have the same sets of strategies and their payoffs are higher if they chose the same strategies than they are if they choose different strategies.

## D

dictator

A player is a *strong dictator* if he can guarantee any outcome regardless of the other players. ${\displaystyle m\in \mathbb {N} }$ is a *weak dictator* if he can guarantee any outcome, but his strategies for doing so might depend on the complement strategy vector. Naturally, every strong dictator is a weak dictator. Formally:  
*m* is a *Strong dictator* if:  
${\displaystyle \forall a\in \mathrm {A} ,\;\exists \sigma \ _{n}\in \Sigma \ ^{n}\;s.t.\;\forall \sigma \ _{-n}\in \Sigma \ ^{-n}:\;\Gamma \ (\sigma \ _{-n},\sigma \ _{n})=a}$  
*m* is a *Weak dictator* if:  
${\displaystyle \forall a\in \mathrm {A} ,\;\forall \sigma \ _{-n}\in \Sigma \ ^{-n}\;\exists \sigma \ _{n}\in \Sigma \ ^{n}\;s.t.\;\Gamma \ (\sigma \ _{-n},\sigma \ _{n})=a}$  

Another way to put it is:  
a *weak dictator* is ${\displaystyle \alpha }$ -effective for every possible outcome.  
A *strong dictator* is ${\displaystyle \beta }$ -effective for every possible outcome.  
See *Effectiveness*. Antonym: *dummy*.

dominated outcome

Given a *preference* *ν* on the *outcome space*, we say that an outcome *a* is dominated by outcome *b* (hence, *b* is the *dominant* strategy) if it is preferred by all players. If, in addition, some player strictly prefers *b* over *a*, then we say that *a* is *strictly dominated*. Formally:  
${\displaystyle \forall j\in \mathrm {N} \;\quad \nu \ _{j}(a)\leq \ \nu \ _{j}(b)}$ for domination, and  
${\displaystyle \exists i\in \mathrm {N} \;s.t.\;\nu \ _{i}(a)<\nu \ _{i}(b)}$ for strict domination.  
An outcome *a* is (strictly) *dominated* if it is (strictly) *dominated* by some other *outcome*.  
An outcome **a** is dominated for a *coalition* *S* if all players in *S* prefer some other outcome to *a*. See also *Condorcet winner*.

dominated strategy

A strategy is (strongly) dominated by strategy ${\displaystyle \tau \ _{i}}$ if for any complement strategies tuple ${\displaystyle \sigma \ _{-i}}$, player *i* benefits by playing ${\displaystyle \tau \ _{i}}$. Formally speaking:  
${\displaystyle \forall \sigma \ _{-i}\in \ \Sigma \ ^{-i}\quad \quad \pi \ (\sigma \ _{i},\sigma \ _{-i})\leq \pi \ (\tau \ _{i},\sigma \ _{-i})}$ and  
${\displaystyle \exists \sigma \ _{-i}\in \ \Sigma \ ^{-i}\quad s.t.\quad \pi \ (\sigma \ _{i},\sigma \ _{-i})<\pi \ (\tau \ _{i},\sigma \ _{-i})}$.  
A strategy *σ* is (strictly) *dominated* if it is (strictly) *dominated* by some other *strategy*.

dummy

A player **i** is a dummy if he has no effect on the outcome of the game. I.e. if the outcome of the game is insensitive to player **i'** s strategy. Antonyms: *say*, *veto*, *dictator*.

## E

[effectiveness](https://en.wiktionary.org/wiki/effectiveness "effectiveness")

A coalition (or a single player) *S* is *effective for* *a* if it can force *a* to be the outcome of the game. *S* is α-effective if the members of *S* have strategies s.t. no matter what the complement of *S* does, the outcome will be *a*.

*S* is β-effective if for any strategies of the complement of *S*, the members of *S* can answer with strategies that ensure outcome *a*.

[extensive form game](https://en.wiktionary.org/wiki/extensive_form_game "extensive form game")

A [tree](https://en.wiktionary.org/wiki/tree "tree"), where, at each [node](https://en.wiktionary.org/wiki/node "node") of the tree, a different player has the choice of choosing an [edge](https://en.wiktionary.org/wiki/graph_theory "graph theory").

## F

finite game

A game with finitely many players, each of which has a finite set of *strategies*.

## M

mixed strategy

For player *i*, a probability distribution *P* on ${\displaystyle \Sigma \ ^{i}}$. It is understood that player *i* chooses a strategy randomly according to *P*.

mixed Nash equilibrium

Same as *Pure Nash Equilibrium*, defined on the space of *mixed strategies*. Every finite game has *Mixed Nash Equilibria*.

## N

[Nash equilibrium](https://en.wiktionary.org/wiki/Nash_equilibrium "Nash equilibrium")

The set of choices of players' strategies for which no player can benefit by changing his or her strategy while the other players keep theirs unchanged.

[normal form game](https://en.wiktionary.org/wiki/normal_form_game "normal form game")

A function: ${\displaystyle \Sigma \ ^{i}\to \mathbb {R} ^{\mathrm {N} }}$, given the *tuple* of *strategies* chosen by the players, one is given an allocation of *payments* (given as real numbers).

A further generalization can be achieved by splitting the *game* into a composition of two functions: ${\displaystyle \Sigma \ ^{i}\to \Gamma \ }$ the *outcome function* of the game (some authors call this function "the game form"), and ${\displaystyle \nu \ :\Gamma \ \to \mathbb {R} ^{\mathrm {N} }}$ the allocation of *payoffs* (or *preferences*) to players, for each outcome of the game.

## O

[outcome function](https://en.wiktionary.org/w/index.php?title=outcome_function&action=edit&redlink=1 "outcome function (page does not exist)")

A function that assigns to each combination of chosen strategies an outcome from an outcome space. It appears in one of the formalizations of a normal form game; see normal form game.

[outcome space](https://en.wiktionary.org/w/index.php?title=outcome_space&action=edit&redlink=1 "outcome space (page does not exist)")

A set of all the possible outcomes of a game—outcomes to which a real-valued award is assigned for each player. Conventionally labeled as ${\displaystyle \ \Gamma }$. It appears in one of the formalizations of a normal form game; see normal form game.

## P

[Pareto efficiency](https://en.wiktionary.org/wiki/Pareto_efficiency "Pareto efficiency")

The property of being Pareto efficient.

[Pareto efficient](https://en.wiktionary.org/wiki/Pareto_efficient "Pareto efficient")

An *outcome* *a* of *game form* *π* is (strongly) *Pareto efficient* if it is *undominated* under all *preference profiles*.

[Pareto optimal](https://en.wiktionary.org/wiki/Pareto_optimal "Pareto optimal")

Of an allocation of goods to individual, such that it is Pareto efficient.

[Pareto optimal](https://en.wiktionary.org/wiki/Pareto_optimal "Pareto optimal")

Of a strategy of a player, such that there is no alternative strategy outperforming it agaist at least one opponent's strategy while not underperforming it against any opponent's strategy.

[Pareto optimality](https://en.wiktionary.org/wiki/Pareto_optimality "Pareto optimality")

The property of being Pareto optimal.

[payoff function](https://en.wiktionary.org/wiki/payoff_function "payoff function")

Informally, a mathematical function describing the real-valued award given to a single player at the outcome of a game. Formally, a function ${\displaystyle F:\Sigma \rightarrow \mathbb {R} }$, where ${\displaystyle \Sigma }$ is the strategy space. Accordingly, to completely specify a game, the payoff function has to be specified for each player in the player set *P* = {1, 2,..., *m* }.

[preference profile](https://en.wiktionary.org/w/index.php?title=preference_profile&action=edit&redlink=1 "preference profile (page does not exist)")

A real-valued function that specifies for each outcome of the game and each of N players to what degree he prefers the outcome; that is, ${\displaystyle \nu \ :\Gamma \ \to \mathbb {R} ^{\mathrm {N} }}$, where ${\displaystyle \Gamma }$ is the outcome space. See *allocation of goods*. This is the *ordinal* approach at describing the outcome of the game.

pure Nash equilibrium point

An element ${\displaystyle \sigma \ =\sigma \ _{i\in \mathrm {N} }}$ of the strategy space of a game is a *pure Nash equilibrium point* if no player **i** can benefit by deviating from his strategy ${\displaystyle \sigma \ _{i}}$, given that the other players are playing in ${\displaystyle \sigma \ }$. Formally:  
${\displaystyle \forall i\in \mathrm {N} \quad \forall \tau \ _{i}\in \ \Sigma \ ^{i}\quad \pi \ (\tau \ ,\sigma \ _{-i})\leq \pi \ (\sigma \ )}$.  
No equilibrium point is dominated.

## S

say

A player *i* has a *Say* if he is not a *Dummy*, i.e. if there is some tuple of complement strategies s.t. π (σ\_i) is not a constant function. Antonym: *dummy*.

simple game

A simplified form of a cooperative game, where the possible gain is assumed to be eiter '0' or '1'. A simple game is couple (*N*, *W*), where *W* is the list of "winning" *coalitions*, capable of gaining the loot ('1'), and *N* is the set of players.

## V

value

A *value* of a game is a rationally expected *outcome*. There are more than a few definitions of *value*, describing different meathods of obtaining a solution to the game.

veto

A veto denotes the ability (or right) of some player to prevent a specific alternative from being the outcome of the game. A player who has that ability is called *a veto player*. Antonym: *dummy*.

## W

weakly acceptable game

A game that has *pure Nash equilibria* some of which are *pareto efficient*.