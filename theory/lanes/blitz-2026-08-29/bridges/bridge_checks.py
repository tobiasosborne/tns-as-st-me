#!/usr/bin/env python3
"""Exact-arithmetic sanity checks for bridges.md; --red mutates SPT sign."""

from fractions import Fraction
import sys


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_spt(red: bool) -> None:
    for q in (Fraction(1, 3), Fraction(49, 100), Fraction(2, 3)):
        lam = 2 * q - 1
        for length in (1, 2, 5):
            lhs = -(1 - q) * sum(lam**n for n in range(length))
            rhs = -Fraction(1, 2) * (1 - lam**length)
            if red:
                rhs = -rhs
            require(lhs == rhs, f"SPT telescoping failed at q={q}, L={length}")


def check_ward_not_fredholm() -> None:
    source_dim = target_dim = 1
    fredholm_index = source_dim - target_dim
    ward_numerator = ward_denominator = Fraction(1)
    require(fredholm_index == 0, "doublet lowering-map index is not zero")
    require(ward_numerator / ward_denominator == Fraction(1), "Ward pairing is not one")
    require(fredholm_index != ward_numerator / ward_denominator,
            "analytic and Ward indices were spuriously identified")


def check_gauss_and_theta_offset() -> None:
    links = (-2, -1, 1, 0, 3)
    charges = tuple(links[n] - links[n - 1] for n in range(1, len(links)))
    require(sum(charges) == links[-1] - links[0], "Gauss telescoping failed")
    alpha = Fraction(1, 7)
    early, late = links[1] + alpha, links[-1] + alpha
    require(late - early == links[-1] - links[1], "theta offset did not cancel")


def check_fcs() -> None:
    law = {-2: Fraction(1, 4), 0: Fraction(1, 2), 3: Fraction(1, 4)}
    require(sum(law.values()) == 1, "TPM law is not normalized")
    chi_at_2pi = sum(law.values())  # exp(2*pi*i*n)=1 for integer n.
    first_moment = sum(nu * weight for nu, weight in law.items())
    require(chi_at_2pi == 1, "integer-support FCS is not periodic")
    require(first_moment == Fraction(1, 4), "FCS first moment mismatch")


def check_majorana_mod_two() -> None:
    pfaffian_start, pfaffian_end = 3, -2
    relative_parity = 1 if pfaffian_start * pfaffian_end > 0 else -1
    require(relative_parity == -1, "Pfaffian sign change was not detected")
    require(pfaffian_start > 0 > pfaffian_end, "path need not cross a zero")


def main() -> int:
    red = "--red" in sys.argv[1:]
    try:
        check_spt(red)
        check_ward_not_fredholm()
        check_gauss_and_theta_offset()
        check_fcs()
        check_majorana_mod_two()
    except AssertionError as exc:
        print(f"FAIL: {exc}")
        return 1
    print("PASS: SPT telescoping, Ward/Fredholm separation, Gauss offset, FCS, mod-two flow")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
