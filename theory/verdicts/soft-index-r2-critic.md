FAIL(R2-O1) — 0 FATAL / 1 MAJOR / 0 MINOR / 0 NOTE

# Soft-index r2 hostile critic

## OBJECTIONS

### R2-O1 — MAJOR — `--red-register-trap` is an always-failing wrapper, not a live public red path

**Exact quoted target.**  The shard's checker table says:

> `--red-register-trap`; default green also runs the standing certificate's `--red`, `--red-register`, and `--red-chi` and requires each subprocess to exit 1

and `theory/checks/soft_index_r2_check.py` implements:

> `require(result.returncode == 1, ...)`
>
> `if red:`
>
> `    fail("SIDXR2-C1 RED detected: cross-register substitution is nonzero")`

**Recomputation.**  The underlying standing mutation is genuine: direct
`ml4_ward_n2_check.py --red-register` exits 1 and prints
`||naive-hw-reading - REFUTED display||=0.00e+00`, with cross-register error
`1.431e-01` at `n=2`.  The r2 public wrapper nevertheless has the following
truth table:

- child exits 1 because the real mutation is detected: `require` passes, then
  the unconditional `fail` exits 1;
- child exits 0 because the mutation survives undetected: `require` itself
  fails and exits 1.

Thus `soft_index_r2_check.py --red-register-trap` exits 1 under both outcomes.
Its observed exit code cannot certify that the registered mutation fired, and
its captured output suppresses the required `0.00e+00` coincidence.  This
violates the binding requirement that each public red mode exit 1 *via* a real
registered mutation.  It does not attack any Ward identity or S-IDX-fin's
proof, so the severity is MAJOR rather than FATAL.

I recomputed the advertised headline surfaces rather than accepting the green
checker as evidence:

1. **S-IDX-fin.**  On the full positive-weight sector,
   `A=D^†D=S^+S^-` has irrep eigenvalues
   `(j+m)(j-m+1) >= 2m > 0`, hence
   `P=D A^{-1}D^†`.  For highest-weight `psi`,
   `D^†J^-_0 psi=S^+J^-_0 psi=2J^z_0 psi`; therefore
   `PJ^-_0 psi=2D A^{-1}J^z_0 psi`, with `A` acting on the whole source
   sector.  In the different restricted register,
   `D_hw^†D_hw=2m I` but
   `D_hw^†J^-_0 psi=2 Pi_hw J^z_0 psi`, which gives
   `P_hwJ^-_0 psi=Q_0 Pi_hw J^z_0 psi/m`.  No intermediate line substitutes
   the scalar restricted Gram operator into the full-sector formula.  For a
   nonzero-momentum one-magnon state, momentum conservation gives
   `J^+_0|h>=0`, so `Pi_hw J^z_0|h>=J^z_0|h>`; the continuity equation gives
   `J^z_0|h>=iv_S(h)|h>`, and the norm `||Q_0|h>||^2=2(NS-1)` cancels the
   weight to leave the residue `2iv_S(h)`.  This proves every statement in
   the proposed finite row.
2. **Adler anchor.**  The exact-one computation is used only for
   `Phi_0=Q_0 psi_g`.  Since `[H,Q_0]=0` and `omega_S(0)=0`, its interacting
   and free coordinate rows coincide term by term.  The shard explicitly
   excludes the running `Q[f_epsilon]psi_g` family and quotes the `S>=1`
   counterexample to the dead (B6); no later value step consumes a stronger
   anchor.
3. **Conditional soft algebra and gap inventory.**  Under (PROTO-LSZ),

   `(ik)[a_leg(-i sgn/v_h)][2iv_h ell_h]
    =2i a_leg sgn ell_h k`.

   Packet integration replaces `k` by `bar k_*`; the compact hard window
   supplies the uniform `O(epsilon^2)` remainder, and the three other
   components are explicitly assumed `O(epsilon^2),O(epsilon^2),o(epsilon)`.
   D30 supplies no coefficient.  (PROTO-LSZ) expressly carries exhaustive
   decomposition, boundary decay, class nonemptiness, kernel existence, and
   the D24 normalisation; actual D29 limit-point existence and D30 on a model
   are separately listed as open.  (MATCH-S) is the displayed first-jet
   protocol/on-shell identification and therefore is the instance of the
   otherwise-unproved jet bridge used here; it is not silently imported from
   D24-VAL.  The order is outer `N,T,W,sigma` limit first and
   `epsilon -> 0` last, with no interchange asserted.
4. **Value chain and conventions.**  On the fixed compact
   `I subset (0,pi)`, S2-2body-S gives uniformly
   `S_phys(k,h)-1=i sgn(v_h-v_s)k/S+O(k^2)` in D7's physical branch.
   Integrating against the same D29 row measure gives
   `i sgn(v_h-v_s)bar k_*/S+O(epsilon^2)`.  Combining only then with
   (MATCH-S) yields the protocol phase law.  Comparison with the structural
   coefficient at the primitive unit-charge value `ell_h=1` gives
   `2 a_leg(S)=1/S`, hence `a_leg(S)=1/(2S)=1/Z_rho`.  The shard neither
   changes the D8 half-zone convention nor promotes a composite-charge law.
5. **`a_leg` riders.**  The text calls `a_leg(rho)` OPEN before matching,
   cites D24-VAL only for its conditional value, cites AMP as CONJECTURE,
   never derives the value from a leg normalisation, and keeps the
   charge-created/asymptotic-leg conversion at `sqrt(Z_rho)` in the LSZ limit
   and `sqrt(Z_rho-2/N)` at finite volume.  All four binding riders are met.
6. **Damaged sites.**  The correction table maps exactly the eight DAMAGED
   lane-A sites `C-1,C-2,C-5,C-6,C-11,C-12,C-14,C-15` and the seven DAMAGED
   lane-B sites `E-1,E-2,E-5,E-7,E-15,E-17,E-19`.  It also separately repairs
   the two D-SUB sites `E-11,E-12`.  Each replacement is one of the two valid
   registered Ward formulas; no old (18) branch survives.
7. **Remaining checker results.**  Green exited 0 under `python3 -O`.  Each of
   the eight exposed r2 red flags exited 1:
   `--red-register-trap`, `--red-ward-residue`, `--red-adler-anchor`,
   `--red-s2-value`, `--red-lsz-factor`, `--red-tgt-value`,
   `--red-leg-power`, and `--red-limit-order`.  I also ran the standing ML4
   mutations directly: `--red`, `--red-register`, and `--red-chi` each exited
   1.  In particular the register run printed
   `||naive-hw-reading - REFUTED display||=0.00e+00` at `n=1,2,3`, while the
   cross-register error was `1.431e-01` at `n=2`.  Apart from R2-O1, the
   mutations respectively remove a real Ward/LSZ factor, substitute a
   nonzero-mode state for the Adler state, change the S2 coefficient, demand
   false TGT value invariance, replace a square-root leg conversion by a full
   power, or admit the forbidden fixed-`N` soft sample.  The checker section's
   negative evidential limits are accurate: no gate certifies protocol limits,
   (PROTO-LSZ), (MATCH-S), class membership, or the open constant.
8. **Falsifier.**  The frozen probe reran green: P1 gave `1.9929` versus `2`
   at `S=1/2` and `1.0217` versus `1` at `S=1`; P2(a) passed.  These are
   consistent with every finite and on-shell statement in the shard.  The
   shard labels P2(b) VOID and consumes no claim from its identical-expression
   gate.

## PROMOTABLE NOW

### `S-IDX-fin-r2` — certify as **PROVED** after the mechanical R2-O1 checker repair

Verbatim statement cell:

> In a finite SU(2) ring positive-weight sector, with `D=Q_0` on the full sector and `A=D^\dagger D` there, `PJ^-_0\psi=2DA^{-1}J^z_0\psi` for highest-weight `\psi`; in the separately restricted register `P_{hw}J^-_0\psi=Q_0\Pi_{hw}J^z_0\psi/m_\lambda`.  For a primitive spin-`S` one-magnon leg the residue is `2iv_S(h)`.  The pure `Q_0`-created row ratio is exactly one, with no claim about the running D29 family.

Certified status cell: `PROVED`.

The proof is complete, finite-dimensional, integrability-free, and R2-O1 does
not attack it.  Its status does not depend on D29, D30, (PROTO-LSZ),
(MATCH-S), D24-VAL, AMP, or any limiting construction.  The orchestrator can
promote it once the mandatory checker control flow is repaired and rerun.

### Rows certified only at **SKETCH**

`S-IDX-spec-struct-r2`, verbatim statement cell:

> Under D29, D30, and the separately displayed uninstantiated hypothesis (PROTO-LSZ), every actual ordered limit point obeys `\mathcal A_*=2i\mathfrak a_{\rm leg}(\rho)\operatorname{sgn}(v_h-v_s)\ell_h\bar k_*+o(\epsilon)` and has an Adler zero.  The D24(d)3b constant is OPEN; no `1/\rho` value is claimed.

`S-IDX-spec-r2`, verbatim statement cell:

> Add the D24-VAL membership antecedent and (MATCH-S), identifying the fixed-time D29 readout with the on-shell multiplier through `o(\epsilon)`.  For the primitive fully polarised spin-`S` band every actual limit point then has phase slope `\operatorname{sgn}(v_h-v_s)/S`; comparison supplies the conditional matched value `\mathfrak a_{\rm leg}(S)=1/(2S)=1/Z_\rho` (the existing D24-VAL row supplies `S=1/2,1,3/2,2`; other half-integer spins are a new SKETCH extension using S2-2body-S).  No D29 instance, unconditionally exhibited class member, composite-charge factor, or bridge-free AMP conclusion is claimed.

`S-IDX-HR-value-r2`, verbatim statement cell:

> Under D31 on D6, the fixed-packet constructed Haag--Ruelle channel of AC-EX-2M has multiplier `S_{phys}` and its scale-tied packet average has slope `\operatorname{sgn}(v_h-v_s)/S` by S2-2body-S.  This is an on-shell value instance, explicitly not a D29 protocol instance.

These three status cells remain `SKETCH`.  The first two have no proved D29
instance; the third is deliberately kept separate from the protocol headline
and is no basis for upgrading either spectral row.

## REPAIR ORDER

1. In `register_trap_gate(red=True)`, execute the real standing
   `--red-register` mutation, forward its output (including the checked
   `0.00e+00` trap coincidence), and propagate its return code.  The public red
   path must exit 1 exactly when that mutation is detected and must exit 0 if
   it survives.  Do not retain an unconditional `fail` or a `require` whose
   failure also maps the survivor case to exit 1.
2. Rerun green under `python3 -O`, every exposed r2 red flag, and the three
   standing ML4 red flags.  Mechanically verify the corrected truth table by
   temporarily substituting a child result of 0: the public register red path
   must then report `RED SURVIVED UNDETECTED` and exit 0.
3. Make no proof, D29/D30, value-chain, Adler, damaged-site, or frozen-probe
   change.  After step 2, promote only `S-IDX-fin-r2` to PROVED and retain the
   other three proposed rows at SKETCH.
