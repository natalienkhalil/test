# Arithmetic mean of a small example dataset

This is an explicitly labeled publishing integration test, not a scientific study. The numbers below are illustrative test data, not observations of people or the natural world.

## Data and method

The complete dataset in `data/values.csv` consists of the three values 2, 3, and 4. We calculate the arithmetic mean by summing all values and dividing by the number of values. The implementation is in `analysis.py`.

## Result

The arithmetic mean of this three-value example dataset is 3. The sum is 9 and the sample size is 3, so 9 / 3 = 3. This result applies only to the stated illustrative dataset.

## Reproducibility

Run `python3 analysis.py`. It reads the committed CSV and prints the sample size and arithmetic mean as JSON. The expected result is recorded in `result.json`.
