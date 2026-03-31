# DNA-Sequence Analyser, by Giulia Trentarossi for Harvard CS50, March 2026.


import re


class DNASequence:
    def __init__(self, sequence):
        # Sequence validation
        if not re.fullmatch(r"[ACGTNRY]+", sequence.upper()):
            raise ValueError("Invalid DNA sequence.")
        self.sequence = sequence

    # Count number of single nucleotides
    def count_nucleotides(self):
        nucleotides = {base: 0 for base in "ATCGNRY"}
        for letter in self.sequence:
            nucleotides[letter] += 1
        return nucleotides

    # Calculate GC-content in input sequence
    # N, R, Y = unknown nucleotides accepted but not yet counted in gc_content
    def gc_content(self):
        nucleotides = self.count_nucleotides()
        return ((nucleotides["G"] + nucleotides["C"]) / len(self.sequence)) * 100

    # Reverse-complement-sequence
    # Returns complementary and inverted sequence (template strand) of inputted sequence (coding strand)
    # R means A/G
    # Y means C/T
    # N means any base
    def reverse_complement(self):
        reverse_sequence = self.sequence[::-1]
        complement_map = {
            "A": "T",
            "T": "A",
            "C": "G",
            "G": "C",
            "N": "N",
            "R": "Y",
            "Y": "R"
        }
        complement = ""
        for base in reverse_sequence:
            complement += complement_map.get(base, "N")
        return complement

    # Transcription from DNA-Sequence to RNA-Sequence
    # Assumes input DNA is the coding strand (5'→3')
    def transcription(self):
        return self.sequence.replace("T", "U")

    # Print analysis results
    def print_analysis(self):
        print(f"Sequence: {self.sequence}")
        print(f"Length: {len(self.sequence)} bp")

        counts = self.count_nucleotides()
        for key, value in counts.items():
            print(f"{key}: {value}")

        print(f"GC Content: {self.gc_content():.2f}%")
        print(f"Matching RNA Sequence: {self.transcription()}")
        print(f"Reverse Complement: {self.reverse_complement()}")


def main():
    choice_method = input_method()
    if choice_method == "1":
        while True:
            sequence = get_sequence()
            try:
                dna = DNASequence(sequence)
                break
            except ValueError:
                print("Please, insert a valid sequence.")
    elif choice_method == "2":
        while True:
            sequence = get_sequence_from_file()
            try:
                dna = DNASequence(sequence)
                break
            except ValueError:
                print("Invalid sequence found in file.")
    dna.print_analysis()


# Choice of input method for dna sequence
def input_method():
    print("Choose input method for DNA sequence:\n1- Insert sequence manually\n2- Read sequence from file")
    while True:
        choice = input("Please, select 1 or 2: ")
        if choice in ["1", "2"]:
            return choice
        else:
            print("Invalid input.")


# Input DNA Sequence
def get_sequence():
    sequence = input("Insert sequence: ").upper().strip()
    sequence = re.sub(r"\s+", "", sequence)

    return sequence


# Input DNA Sequence from File
def get_sequence_from_file():
    while True:
        file_name = input("File name: ").strip()

        try:
            sequence = ""
            with open(file_name) as file:
                for line in file:
                    if line.startswith(">"):
                        continue
                    sequence += line.strip()
                if not sequence:
                    print("No valid sequence found in file.")
                    continue
                sequence = re.sub(r"\s+", "", sequence.upper())
                return sequence
        except FileNotFoundError:
            print("File not found. Please insert a valid file name.")


# Sequence validation through function not in class
# def is_valid(sequence):
    # return bool(re.fullmatch(r"[ACGTNRY]+", sequence))


if __name__ == "__main__":
    main()
