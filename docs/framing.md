<!-- ROLE: background viewpoint. AUTHORED (source: TJO, conversation with Nico Giulini, 2026-08-24). Informs the theory; is NOT cited in the paper. -->

# Background framing (Giulini viewpoint)

TJO (2026-08-25), after a conversation with Nico Giulini that "cleared up a lot
of confusions about the asymptotic symmetry ↔ memory ↔ soft theorem" story:
the continuum literature is scattered and often sloppy. The disciplined
viewpoint to keep in the background of every theory artifact in this repo:

1. **Symplectic actions of symmetries.** A symmetry is asymptotic/physical iff
   it acts on the phase space with a well-defined (integrable) symplectic
   action; "large" vs "small" (gauge) is decided by whether the associated
   charge is nonzero/well-defined, not by fall-off slogans.
2. **Poisson–Lie algebras for charges.** The charges must close under the
   Poisson bracket (possibly with central/anomalous extensions — on the
   lattice, the projective class [ω] ∈ H²(G,U(1)) is exactly such an
   extension). Statements about "the asymptotic symmetry group" are statements
   about this charge algebra.
3. **Careful selection of function spaces.** Which transformations are allowed
   and which observables exist is fixed by the function spaces (decay/summability
   classes) chosen at infinity; theorems must state these choices explicitly.
   Lattice translation: the class of allowed g(x) profiles for truncated /
   modulated symmetry operations, and the norms in which soft limits and
   remainders R(k) are controlled.
4. **The potential is the fundamental object.** In the continuum the vector
   potential (not the field strength) carries the memory observable and the
   symplectic structure at the boundary. Lattice analogue to develop: the
   virtual/bond degrees of freedom (the V(g) insertions, the MPS gauge/tangent
   data X) are the "potential"; physical spin observables are the "field
   strength". Memory lives in the bond data.

Discipline this imposes here:
- Corner A must be phrased as: charge algebra + its action on the relevant
  state space (superselection sectors / vacuum manifold), with the H² class as
  the central extension — not as loose "symmetry at infinity" talk.
- Conjecture S's remainder R(k) requires an explicit norm and an explicit
  admissible class of states (function-space discipline).
- Corner B's memory observable should be identified with a bond/virtual
  quantity (collective coordinate ↔ boundary symplectic pair), and the
  A ⇒ C ⇒ B chain should ideally be exhibited as one symplectic/Ward statement.
