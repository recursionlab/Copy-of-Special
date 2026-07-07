---
title: "Hurewicz theorem"
source: "https://en.wikipedia.org/wiki/Hurewicz_theorem"
author:
  - "[[Wikipedia]]"
published: 2004-04-12
created: 2026-05-19
description:
tags:
  - "clippings"
---
In [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), the **Hurewicz theorem** is a basic result of [algebraic topology](https://en.wikipedia.org/wiki/Algebraic_topology "Algebraic topology"), connecting [homotopy theory](https://en.wikipedia.org/wiki/Homotopy_theory "Homotopy theory") with [homology theory](https://en.wikipedia.org/wiki/Homology_theory "Homology theory") via a map known as the **Hurewicz homomorphism**. The theorem is named after [Witold Hurewicz](https://en.wikipedia.org/wiki/Witold_Hurewicz "Witold Hurewicz"), and generalizes earlier results of [Henri Poincaré](https://en.wikipedia.org/wiki/Henri_Poincar%C3%A9 "Henri Poincaré").

## Statement of the theorems

The Hurewicz theorems are a key link between [homotopy groups](https://en.wikipedia.org/wiki/Homotopy_group "Homotopy group") and [homology groups](https://en.wikipedia.org/wiki/Homology_group "Homology group").

### Absolute version

For any [path-connected](https://en.wikipedia.org/wiki/Path_connected "Path connected") space *X* and strictly positive integer *n* there exists a [group homomorphism](https://en.wikipedia.org/wiki/Group_homomorphism "Group homomorphism")

${\displaystyle h_{*}\colon \pi _{n}(X)\to H_{n}(X),}$

called the **Hurewicz homomorphism**, from the *n* -th [homotopy group](https://en.wikipedia.org/wiki/Homotopy_group "Homotopy group") to the *n* -th [homology group](https://en.wikipedia.org/wiki/Homology_\(mathematics\) "Homology (mathematics)") (with integer coefficients). It is given in the following way: choose a canonical generator ${\displaystyle u_{n}\in H_{n}(S^{n})}$, then a homotopy class of maps ${\displaystyle f\in \pi _{n}(X)}$ is taken to ${\displaystyle f_{*}(u_{n})\in H_{n}(X)}$.

The Hurewicz theorem states cases in which the Hurewicz homomorphism is an [isomorphism](https://en.wikipedia.org/wiki/Group_isomorphism "Group isomorphism").

- For ${\displaystyle n\geq 2}$, if *X* is [${\displaystyle (n-1)}$ -connected](https://en.wikipedia.org/wiki/N-connected "N-connected") (that is: ${\displaystyle \pi _{i}(X)=0}$ for all ${\displaystyle i<n}$), then ${\displaystyle {\tilde {H_{i}}}(X)=0}$ for all ${\displaystyle i<n}$, and the Hurewicz map ${\displaystyle h_{*}\colon \pi _{n}(X)\to H_{n}(X)}$ is an isomorphism.[^1]<sup><span title="Page: 366, Thm.4.32">: 366, Thm.4.32</span> </sup> This implies, in particular, that the [homological connectivity](https://en.wikipedia.org/wiki/Homological_connectivity "Homological connectivity") equals the [homotopical connectivity](https://en.wikipedia.org/wiki/Homotopical_connectivity "Homotopical connectivity") when the latter is at least 1. In addition, the Hurewicz map ${\displaystyle h_{*}\colon \pi _{n+1}(X)\to H_{n+1}(X)}$ is an [epimorphism](https://en.wikipedia.org/wiki/Epimorphism "Epimorphism") in this case.[^1]<sup><span title="Page: 388, Ex.4.2.23">: 388, Ex.4.2.23</span></sup>
- For ${\displaystyle n=1}$, the Hurewicz homomorphism induces an [isomorphism](https://en.wikipedia.org/wiki/Group_isomorphism "Group isomorphism") ${\displaystyle {\tilde {h}}_{*}\colon \pi _{1}(X)/[\pi _{1}(X),\pi _{1}(X)]\to H_{1}(X)}$, between the [abelianization](https://en.wikipedia.org/wiki/Commutator_subgroup "Commutator subgroup") of the first homotopy group (the [fundamental group](https://en.wikipedia.org/wiki/Fundamental_group "Fundamental group")) and the first homology group.

### Relative version

For any [pair of spaces](https://en.wikipedia.org/wiki/Topological_pair "Topological pair") ${\displaystyle (X,A)}$ and integer ${\displaystyle k>1}$ there exists a homomorphism

${\displaystyle h_{*}\colon \pi _{k}(X,A)\to H_{k}(X,A)}$

from relative homotopy groups to relative homology groups. The Relative Hurewicz Theorem states that if both ${\displaystyle X}$ and ${\displaystyle A}$ are connected and the pair is ${\displaystyle (n-1)}$ -connected then ${\displaystyle H_{k}(X,A)=0}$ for ${\displaystyle k<n}$ and ${\displaystyle H_{n}(X,A)}$ is obtained from ${\displaystyle \pi _{n}(X,A)}$ by factoring out the action of ${\displaystyle \pi _{1}(A)}$. This is proved in, for example, [Whitehead (1978)](#CITEREFWhitehead1978) by induction, proving in turn the absolute version and the Homotopy Addition Lemma.

This relative Hurewicz theorem is reformulated by [Brown & Higgins (1981)](#CITEREFBrownHiggins1981) as a statement about the morphism

${\displaystyle \pi _{n}(X,A)\to \pi _{n}(X\cup CA),}$

where ${\displaystyle CA}$ denotes the [cone](https://en.wikipedia.org/wiki/Cone_\(topology\) "Cone (topology)") of ${\displaystyle A}$. This statement is a special case of a [homotopical excision theorem](https://en.wikipedia.org/wiki/Homotopical_excision_theorem "Homotopical excision theorem"), involving induced modules for ${\displaystyle n>2}$ ([crossed modules](https://en.wikipedia.org/wiki/Crossed_module "Crossed module") if ${\displaystyle n=2}$), which itself is deduced from a higher homotopy [van Kampen theorem](https://en.wikipedia.org/wiki/Van_Kampen_theorem "Van Kampen theorem") for relative homotopy groups, whose proof requires development of techniques of a cubical higher homotopy groupoid of a filtered space.

### Triadic version

For any triad of spaces ${\displaystyle (X;A,B)}$ (i.e., a space *X* and subspaces *A*, *B*) and integer ${\displaystyle k>2}$ there exists a homomorphism

${\displaystyle h_{*}\colon \pi _{k}(X;A,B)\to H_{k}(X;A,B)}$

from triad homotopy groups to triad homology groups. Note that

${\displaystyle H_{k}(X;A,B)\cong H_{k}(X\cup (C(A\cup B))).}$

The Triadic Hurewicz Theorem states that if *X*, *A*, *B*, and ${\displaystyle C=A\cap B}$ are connected, the pairs ${\displaystyle (A,C)}$ and ${\displaystyle (B,C)}$ are ${\displaystyle (p-1)}$ -connected and ${\displaystyle (q-1)}$ -connected, respectively, and the triad ${\displaystyle (X;A,B)}$ is ${\displaystyle (p+q-2)}$ -connected, then ${\displaystyle H_{k}(X;A,B)=0}$ for ${\displaystyle k<p+q-2}$ and ${\displaystyle H_{p+q-1}(X;A)}$ is obtained from ${\displaystyle \pi _{p+q-1}(X;A,B)}$ by factoring out the action of ${\displaystyle \pi _{1}(A\cap B)}$ and the generalised Whitehead products. The proof of this theorem uses a higher homotopy van Kampen type theorem for triadic homotopy groups, which requires a notion of the fundamental ${\displaystyle \operatorname {cat} ^{n}}$ -group of an *n* -cube of spaces.

### Simplicial set version

The Hurewicz theorem for topological spaces can also be stated for *n* -connected [simplicial sets](https://en.wikipedia.org/wiki/Simplicial_set "Simplicial set") satisfying the Kan condition.[^2]

### Rational Hurewicz theorem

**Rational Hurewicz theorem:[^3] [^4]** Let *X* be a simply connected topological space with ${\displaystyle \pi _{i}(X)\otimes \mathbb {Q} =0}$ for ${\displaystyle i\leq r}$. Then the Hurewicz map

${\displaystyle h\otimes \mathbb {Q} \colon \pi _{i}(X)\otimes \mathbb {Q} \longrightarrow H_{i}(X;\mathbb {Q} )}$

induces an isomorphism for ${\displaystyle 1\leq i\leq 2r}$ and a surjection for ${\displaystyle i=2r+1}$.

## Notes

## References

- Brown, Ronald (1989), "Triadic Van Kampen theorems and Hurewicz theorems", *Algebraic topology (Evanston, IL, 1988)*, Contemporary Mathematics, vol. 96, Providence, RI: American Mathematical Society, pp. 39–57, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1090/conm/096/1022673](https://doi.org/10.1090%2Fconm%2F096%2F1022673), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [9780821851029](https://en.wikipedia.org/wiki/Special:BookSources/9780821851029 "Special:BookSources/9780821851029"), [MR](https://en.wikipedia.org/wiki/MR_\(identifier\) "MR (identifier)") [1022673](https://mathscinet.ams.org/mathscinet-getitem?mr=1022673)
- Brown, Ronald; Higgins, P. J. (1981), "Colimit theorems for relative homotopy groups", *Journal of Pure and Applied Algebra*, **22**: 11–41, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/0022-4049(81)90080-3](https://doi.org/10.1016%2F0022-4049%2881%2990080-3), [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0022-4049](https://search.worldcat.org/issn/0022-4049)
- Brown, R.; Loday, J.-L. (1987), "Homotopical excision, and Hurewicz theorems, for n-cubes of spaces", *Proceedings of the London Mathematical Society*, Third Series, **54**: 176–192, [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX_\(identifier\) "CiteSeerX (identifier)") [10.1.1.168.1325](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.168.1325), [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1112/plms/s3-54.1.176](https://doi.org/10.1112%2Fplms%2Fs3-54.1.176), [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0024-6115](https://search.worldcat.org/issn/0024-6115)
- Brown, R.; Loday, J.-L. (1987), "Van Kampen theorems for diagrams of spaces", *[Topology](https://en.wikipedia.org/wiki/Topology_\(journal\) "Topology (journal)")*, **26** (3): 311–334, [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/0040-9383(87)90004-8](https://doi.org/10.1016%2F0040-9383%2887%2990004-8), [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0040-9383](https://search.worldcat.org/issn/0040-9383)
- Rotman, Joseph J. (1988), [*An Introduction to Algebraic Topology*](https://archive.org/details/introductiontoal0000rotm), [Graduate Texts in Mathematics](https://en.wikipedia.org/wiki/Graduate_Texts_in_Mathematics "Graduate Texts in Mathematics"), vol. 119, [Springer-Verlag](https://en.wikipedia.org/wiki/Springer-Verlag "Springer-Verlag") (published 1998-07-22), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-387-96678-6](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-96678-6 "Special:BookSources/978-0-387-96678-6")
- [Whitehead, George W.](https://en.wikipedia.org/wiki/George_W._Whitehead "George W. Whitehead") (1978), *Elements of Homotopy Theory*, [Graduate Texts in Mathematics](https://en.wikipedia.org/wiki/Graduate_Texts_in_Mathematics "Graduate Texts in Mathematics"), vol. 61, [Springer-Verlag](https://en.wikipedia.org/wiki/Springer-Verlag "Springer-Verlag"), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-387-90336-1](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-90336-1 "Special:BookSources/978-0-387-90336-1")

[^1]: [Hatcher, Allen](https://en.wikipedia.org/wiki/Allen_Hatcher "Allen Hatcher") (2001), *Algebraic Topology*, [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press "Cambridge University Press"), [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0-521-79160-1](https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-79160-1 "Special:BookSources/978-0-521-79160-1")

[^2]: Goerss, Paul G.; [Jardine, John Frederick](https://en.wikipedia.org/wiki/Rick_Jardine "Rick Jardine") (1999), *Simplicial Homotopy Theory*, Progress in Mathematics, vol. 174, Basel, Boston, Berlin: Birkhäuser, [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-3-7643-6064-1](https://en.wikipedia.org/wiki/Special:BookSources/978-3-7643-6064-1 "Special:BookSources/978-3-7643-6064-1"), III.3.6, 3.7

[^3]: Klaus, Stephan; [Kreck, Matthias](https://en.wikipedia.org/wiki/Matthias_Kreck "Matthias Kreck") (2004), "A quick proof of the rational Hurewicz theorem and a computation of the rational homotopy groups of spheres", *[Mathematical Proceedings of the Cambridge Philosophical Society](https://en.wikipedia.org/wiki/Mathematical_Proceedings_of_the_Cambridge_Philosophical_Society "Mathematical Proceedings of the Cambridge Philosophical Society")*, **136** (3): 617–623, [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode (identifier)"):[2004MPCPS.136..617K](https://ui.adsabs.harvard.edu/abs/2004MPCPS.136..617K), [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1017/s0305004103007114](https://doi.org/10.1017%2Fs0305004103007114), [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [119824771](https://api.semanticscholar.org/CorpusID:119824771)

[^4]: [Cartan, Henri](https://en.wikipedia.org/wiki/Henri_Cartan "Henri Cartan"); [Serre, Jean-Pierre](https://en.wikipedia.org/wiki/Jean-Pierre_Serre "Jean-Pierre Serre") (1952), "Espaces fibrés et groupes d'homotopie, II, Applications", *[Comptes rendus de l'Académie des Sciences](https://en.wikipedia.org/wiki/Comptes_rendus_de_l%27Acad%C3%A9mie_des_Sciences "Comptes rendus de l'Académie des Sciences")*, **2** (34): 393–395