# DNA Sequence Analyzer

## Video Demo

<URL HERE>

## Description

Program which simulates a DNA Sequence Analyzer.

This program is supposed to resemble a simplified bioinformatics tool for the analysis of DNA sequences, performing various biologically-relevant analysis.

It takes as input a DNA sequence (manually or from a FASTA file), validates it, calculates statistics, returns the reverse complement sequence, and performs transcription from DNA to RNA.

The program supports both standard nucleotides (A, C, G, T) and ambiguous nucleotides (N, R, Y).

Ambiguous nucleotides (N, R, Y) are accepted during validation, but they are currently excluded from GC content calculation.

## Workflow

(Note: in the final version most functions are implemented as methods of the DNASequence class)

* main()

  * input_method()
  * get_sequence()
  * get_sequence_from_file()
  * DNASequence class:

    * count_nucleotides()
    * gc_content()
    * transcription()
    * reverse_complement()
    * print_analysis()

## Features

* Input DNA sequence manually or from a FASTA file
* Sequence validation
* Nucleotide counting
* GC content calculation
* DNA > RNA transcription
* Reverse complement generation

## How It Works

The program asks the user to choose an input method:

* Manual input
* File input (FASTA format)

After validation, the program outputs:

* Sequence length
* Nucleotide counts
* GC content
* RNA sequence
* Reverse complement

## Project Structure

* project.py > main program
* test_project.py > unit tests (pytest)
* test.fasta > example of FASTA file containing sequence (use to test the "input_method()" function)
* README.md > project documentation

## Example_1

Input:

* ATGCGC

Output:

* Length: 6 bp
* GC Content: 66.67%
* RNA: AUGCGC
* Reverse Complement: GCGCAT

## Example_2

Input:

* ATGCGTACGTAGCTAGCTAGCTAGCTA

Output:

* Length: 27 bp
* GC Content: 48.15%
* RNA: AUGCGUACGUAGCUAGCUAGCUAGCUA
* Reverse Complement: TAGCTAGCTAGCTAGCTACGTACGCAT

## Example_3

Use the "test.fasta" file to test the input method from a file (format: FASTA). The file provides the DNA sequence for the "Keratin Homo sapiens" protein found on the web. You are welcome to test this file-input method with any other file of your choice, provided it is in FASTA format. Follow the instructions provided on the terminal by the program to select a file.fasta as the input method.

## Testing

This project uses pytest.

Run tests with:

* pytest test_project.py

## Future Improvements

* Translation from RNA to protein
* ORF detection

## Author

Created as final project for CS50’s "Introduction to Programming with Python" by Giulia Trentarossi (March 2026, Italy).

Linkedin profile: www.linkedin.com/in/giulia-trentarossi-8a67273a4
