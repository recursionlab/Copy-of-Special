# Pentagon of 5 Bracketings (K₄ Associahedron)

## Vertices: 5 Complete Bracketings of 4 Elements

| Vertex | Bracketing | Tree Structure |
|--------|------------|----------------|
| V₁ | `(((a b) c) d)` | Left-combed (fully left-associated) |
| V₂ | `((a (b c)) d)` | Left-associated with right-branch at depth 2 |
| V₃ | `(a ((b c) d))` | Right-associated with left-branch at depth 2 |
| V₄ | `(a (b (c d)))` | Right-combed (fully right-associated) |
| V₅ | `((a b) (c d))` | Balanced / medial |

## Edges: 5 Associator Maps (forming a 5-cycle)

The standard Mac Lane pentagon edges (adjacent bracketings differ by ONE associator move):

```
E₁: V₁ → V₂   (((a b) c) d)  ──α₁──►  ((a (b c)) d)
   Associator on left triple:  (ab)c → a(bc)

E₂: V₂ → V₃   ((a (b c)) d)  ──α₂──►  (a ((b c) d))
   Reassociation of outer:  (a X) d → a (X d)  where X = (b c)

E₃: V₃ → V₄   (a ((b c) d))  ──α₃──►  (a (b (c d)))
   Associator on right triple:  (bc)d → b(cd)

E₄: V₄ → V₅   (a (b (c d)))  ──α₄──►  ((a b) (c d))
   Reassociation of outer:  a (b Y) → (a b) Y  where Y = (c d)

E₅: V₅ → V₁   ((a b) (c d))  ──α₅──►  (((a b) c) d)
   Reassociation of outer:  (a b) (c d) → ((a b) c) d
```

## The Pentagon Coherence Condition

The pentagon diagram commutes iff the following identity holds:
```
α₁ ∘ α₂ ∘ α₃ ∘ α₄ ∘ α₅ = id
```

In an A∞-algebra, this is the Stasheff relation for m₄ (the 4-ary operation) expressed in terms of m₂ (binary product) and m₃ (associator/homotopy).

## Classification Task

For each edge Eᵢ, classify the associator αᵢ by its invertibility properties:

| Logic Type | Forward (α) | Backward (α⁻¹) | Explosion? |
|------------|-------------|----------------|------------|
| Classical / Associative | ✓ | ✓ | No |
| Intuitionistic | ✓ | ✗ | No |
| Co-intuitionistic | ✗ | ✓ | No |
| Paraconsistent | ✓ | ✓ | No (both hold without collapse) |
| Paracomplete | ✗ | ✗ | N/A (gap) |

**5 edges vs 4 logics mismatch** → must resolve:
- Option A: 5th edge is Classical (two-sided inverse)
- Option B: 5th vertex is basepoint/neutral
- Option C: Need 5th logic category