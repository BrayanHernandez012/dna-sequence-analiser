table = str.maketrans("ATGC", "UACG")
def transcribe(seq):
    print("\n=== DNA TO RNA TRANSCRIPTION ===")
    print(f"DNA sequence: {seq}")
    seq = seq.translate(table)
    print(f"\nRNA sequence: {seq}")
                
dna = (input("Enter a DNA sequence: ").strip().upper())
while not dna or any(char not in "ATGC" for char in dna):
        dna = (input("Please enter a valid DNA sequence: ").strip().upper())

transcribe(dna)