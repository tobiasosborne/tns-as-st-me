# Anchored patch proposals

All anchors are strings or row labels; no line-number anchor is used.  The
corresponding full-file patched copies are `notation.patched.md`,
`CLAIMS.patched.md`, `ml2-completeness.patched.md`, and
`ml2_completeness_check.patched.py`.

## 1. `notation.md`

### Keep the D31 band-map spelling

No edit to the adjacent rows whose symbol cells are `` `Γ_K`, `Γ_{M,γ}` ``
and `` `Γ_M` ``.  The registered distinction is confirmed by
`ADJUDICATION.md` ⟨1⟩1 and `gamma_use_audit.py`.

### Correct the first-fix pointer for the free two-packet channel

Anchor: the row whose Symbol cell is
`` `ℋ_{0,12}`, `H_{0,12}`, `𝒟_{12}` ``.

Replace that entire row with:

```markdown
| `ℋ_{0,12}`, `H_{0,12}`, `𝒟_{12}` | labeled two-packet free magnon channel, sum Hamiltonian, and smooth product core | theory/ansatz-scattering-2m.md ⟨1⟩1 |
```

Do not add these symbols to D31: the shard introduces them; D31 does not.

### Widen overload 7

Within deliberate overload 7, anchor the exact string:

```text
`X = \cos q` is local to `ml2-completeness.md` ⟨1⟩3;
```

Replace it with:

```text
`X = \cos q` is local to `ml2-completeness.md` ⟨1⟩3--⟨1⟩4;
```

### Add the center-Fourier-transform row

Anchor after the row whose Symbol cell is
`` `\mathscr B_K^{D7}`, `\mathscr X_K`, `\mathscr E_K` `` and insert:

```markdown
| `{\cal U}_c` | unitary center Fourier transform from the ordered two-magnon chamber `ℓ²(ℤ×ℕ)` to `∫^⊕dK\,ℓ²(ℕ)`; the subscript distinguishes it from `U[f]` (D3) and `𝒰(g)` (D2) | theory/ml2-completeness.md (15) |
```

### Escape the malformed `J^z_0`, `S^±` row

Anchor: Symbol cell `` `J^z_0`, `S^±` ``.  Inside that row only, replace:

```text
`D_λ=Q_0|_{ker S^+}`
```

with:

```text
`D_λ=Q_0\|_{ker S^+}`
```

Change no other character in the row.

## 2. `claims/CLAIMS.md`

In each named row, perform only the displayed literal-pipe escaping.  Change
no other character.

- `S2-2body-S`: replace `` `|q_hard|>1` `` with
  `` `\|q_hard\|>1` ``.
- `ML4-Ward`: replace `` `D_λ=Q_0|_{ker S^+}` `` with
  `` `D_λ=Q_0\|_{ker S^+}` ``, and replace `` `|χ_π⟩` `` with
  `` `\|χ_π⟩` ``.
- `M-tk`: replace `` `T=|t|²` `` with `` `T=\|t\|²` ``.
- `M-INDEX-fin`: replace `|W|κ` inside the coset code span with
  `\|W\|κ`.
- `M-IDX-density`: replace `` `|φ_W(2π)-1|` `` with
  `` `\|φ_W(2π)-1\|` ``.

## 3. `theory/checks/ml2_completeness_check.py`

Anchor: function `def coincident_zero_audit(`, inside its
`for root_number in range(n_sites):` loop.

Immediately after:

```python
        momentum = (2 * root_number + 1) * np.pi / n_sites
```

insert:

```python
        k_1 = momentum
        k_2 = momentum
```

Then replace only the two `coordinate_wave` terms:

```python
                outgoing_amplitude * np.exp(1j * momentum * (x + y))
                + incoming_amplitude * np.exp(1j * momentum * (y + x))
```

with:

```python
                outgoing_amplitude * np.exp(1j * (k_1 * x + k_2 * y))
                + incoming_amplitude * np.exp(1j * (k_2 * x + k_1 * y))
```

This is n6's cosmetic specialization-visible spelling; the lane copy's
normal and optimized runs pass and match HEAD.

## 4. `theory/ml2-completeness.md`

### Mark n6 swept

Anchor the status paragraph beginning
`Status: **L6 loop CONVERGED — r2 critic PASS**` and replace its residue
sentences through `Neither sweep changed the mathematics of any step.` with
the corresponding block in `ml2-completeness.patched.md`.  This changes
`Only n6 remains open` to the dated statement that n6 was swept using the two
explicit plane-wave slots; no mathematical status changes.

### Record the deliberate L2 exception

Immediately after that status paragraph insert the paragraph beginning
`**L2 deliberate exception (2026-08-29).**` from
`ml2-completeness.patched.md`.  Ruling: retain the converged shard intact;
future ML2 work goes in a new shard.  The reason is anchor stability for the
single theorem, not an exemption for further growth.

## 5. No `definitions.md` patch

D31 remains byte-unchanged.  In particular, do not add
`ℋ_{0,12}`, `H_{0,12}`, or `𝒟_{12}` to its hypotheses; §1 corrects the
notation pointer to the actual introducing step instead.
