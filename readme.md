# Hamming Distance Calculation

This Python script calculates the Hamming distance between two DNA sequences using different approaches: loop, set, and zip.

## Usage

1. **Loop Approach**
   - Function: `hamming_distance_loop(seq_1, seq_2)`
   - Description: Calculates Hamming distance by iterating through each position in the sequences.
   - Usage Example:
     ```python
     hamming_distance_loop("TTCGATCCATTG", "ATCAATCGATCG")
     ```

2. **Set Approach**
   - Function: `hamming_distance_set(seq_1, seq_2)`
   - Description: Calculates Hamming distance using sets to compare unique nucleotides.
   - Usage Example:
     ```python
     hamming_distance_set("TTCGATCCATTG", "ATCAATCGATCG")
     ```

3. **Zip Approach**
   - Function: `hamming_distance_zip(seq_1, seq_2)`
   - Description: Calculates Hamming distance using the `zip` function to compare nucleotides.
   - Usage Example:
     ```python
     hamming_distance_zip("TTCGATCCATTG", "ATCAATCGATCG")
     ```

## Output
The output of each function call will be the Hamming distance between the provided DNA sequences.