from project import DNASequence
import pytest


# Needs to be refined if ambiguous nucleotides are included or not
def test_gc_content():
    dna = DNASequence("GCGC")
    assert dna.gc_content() == 100.0

    dna = DNASequence("ATAT")
    assert dna.gc_content() == 0.0


def test_reverse_complement():
    dna = DNASequence("ATGC")
    assert dna.reverse_complement() == "GCAT"


def test_transcription():
    dna = DNASequence("ATGC")
    assert dna.transcription() == "AUGC"


def test_count_nucleotides():
    dna = DNASequence("AATCG")
    counts = dna.count_nucleotides()

    assert counts["A"] == 2
    assert counts["T"] == 1
    assert counts["C"] == 1
    assert counts["G"] == 1


def test_invalid_sequence():
    with pytest.raises(ValueError):
        DNASequence("XZ1")