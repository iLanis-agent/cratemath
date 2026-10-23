# Crate Math

Packing crate, weight, cost and time arithmetic. The 5000 items at 48 items a crate make 105 crates, the last crate covering 8 items.

## Named constants

None. Every number is the owner's own entry.

## What it computes

- **The crates truth** - the items (1 to 1000000) divided by the items a crate (1 to 10000), rounded up, with what the last crate covers.
- **The weight truth** - the crates (1 to 100000) times the kilograms a crate (1 to 1000), split into trips at the kilograms a trip (1 to 100000), with what the last trip carries.
- **The cost truth** - the crates times the crate price ($0.01 to $999.99) to the cent, and spread over the items, half rounded up.
- **The time truth** - the items divided by the items a minute (1 to 1000), rounded up, in minutes and in hours and minutes.

## Boundary

Arithmetic only. Counting applied as written. It has not seen any stock, crate or van and does not know whether the items will really fit, the floor will hold the weight or a price will hold, and it gives no verdict that a crate is worth its price or a van is right for the job. Every number is the owner's own entry.

## Files

- `index.html` - landing page with the boundary and starting examples.
- `app.html` - the calculator; every box recomputes on each keystroke.
- `engine.js` - the four truths, shared by the page and the tests.
- `oracle.py` - an independent Python re-implementation; writes `expected.json`.
- `test.js` - runs the engine against `expected.json` (99 cases, 20 error cases).

## Tests

```
python3 oracle.py
node test.js
```
