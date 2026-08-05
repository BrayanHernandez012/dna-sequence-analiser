def transcribe(seq):
    print("\n=== TRANSCRIPTION OF DNA TO RNA ===")
    print(f"DNA: {seq}")
    seq = seq.replace("C", "_")
    seq = seq.replace("G", "C")
    seq = seq.replace("_", "G")
    seq = seq.replace("A", "U")
    seq = seq.replace("T", "A")
    print(f"\nRNA: {seq}")
                
dna = (input("Enter a DNA sequence: ").strip().upper())
while not dna or any(char not in "ATGC" for char in dna):
        dna = (input("Please enter a valid sequence: ").strip().upper())
transcribe(dna)