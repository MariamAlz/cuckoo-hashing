# Cuckoo Hashing vs. Chaining

> **Course:** COSC 607 Algorithm Design Techniques · MSc, Khalifa University

Implementation of both Cuckoo hashing and the chaining approach in Python, with a script that compares their lookup times. Cuckoo hashing gives every key two possible slots, so a lookup checks at most two positions; chaining stores colliding keys in a list at a single slot.

## What it does

- **Universal hashing**: both tables use hash functions of the form `h(k) = ((a·k + b) mod p) mod m`, with `p` a random prime between 10,001 and 20,002 and random `a`, `b`.
- **Cuckoo hashing** (`cuckoo-hashing.py`)
  - Two hash functions; a key goes into its first free candidate slot.
  - If both slots are taken, the key evicts ("kicks") the occupant of its first slot, and the evicted key moves to its alternative slot, repeating as needed.
  - If evictions go on too long, the table draws new hash functions and reinserts every key (rehash).
  - `search` checks only the two candidate slots.
- **Chaining** (`chaining-hashing.py`): one hash function, each slot holds a list of keys; includes a printer for the table.
- **Comparison** (`comparison.py`)
  - Cuckoo table with dynamic resizing: a rehash is triggered after `m/10` consecutive kicks, and the table size doubles when the load factor is at least 0.5.
  - Builds both tables with the same 3,000 random keys (750–50,000) in a table of size 1,000, then times a lookup of the same key in each.
  - Repeats for 10 iterations and reports per-iteration and total search times and which method was faster.

## Project structure

| File | Contents |
| --- | --- |
| `cuckoo-hashing.py` | Cuckoo hash table; inserts 500 random keys into a table of size 1,000 with a verbose log of placements and kicks |
| `chaining-hashing.py` | Hash table with chaining; inserts 20 keys, prints the table and times one search |
| `comparison.py` | Resizing cuckoo table vs. chaining, lookup-time comparison over 10 iterations |
| `cuckoo-undergrad.pdf` | Reference lecture note on cuckoo hashing and chaining |

## Getting started

Requirements: Python 3 (standard library only).

```bash
python cuckoo-hashing.py     # cuckoo insertions with placement/kick log
python chaining-hashing.py   # chaining table demo
python comparison.py         # cuckoo vs. chaining search-time comparison
```

Keys are random, so output and timings differ between runs.

## Tech

Python 3 (standard library: `random`, `math`, `time`).

## Credits

`cuckoo-undergrad.pdf` is Rasmus Pagh's lecture note *Cuckoo Hashing for Undergraduates* (IT University of Copenhagen, 2006), included as reference material. The Python code is my own.
