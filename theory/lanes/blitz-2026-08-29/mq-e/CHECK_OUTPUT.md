# `check_mq_e.py` recorded output

Command:

`python3 check_mq_e.py`

Output (exit `0`):

`PASS: 65 volume/charge pairs, 700 component vertices, 28936 local-tail checks`

Mutation command:

`python3 check_mq_e.py --red`

Output (exit `1`):

`RED-OK: shifted right-tail mutation was detected`

The mutation shifts the claimed right-tail wall pair by one bond.  It is
caught by the exhaustive component/edge comparison.  This is a finite-volume
falsifier, not the proof of the all-volume statement.
