## How it works

This project implements the following combinational logic function:

F = (A AND B) OR (NOT C)

The circuit has three inputs A, B, and C, and produces one output F.

Internally:
- Inputs A and B are ANDed together
- Input C is inverted
- The two results are ORed together to generate F

The output F is logic 1 when:
- both A and B are 1, or
- C is 0


## How to test

The design can be verified using the truth table below.

| A | B | C | F |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

Each input combination should be held stable for sufficient clock cycles
(e.g., 25 clock cycles) before checking the output F.



## External hardware

None.
