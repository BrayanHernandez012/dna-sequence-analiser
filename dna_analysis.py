# This is the first bioinformatics script I have written.

seq = input("Enter a sequence ").upper().strip()
if seq == "":
    print("Please enter a valid sequence")

elif any(char not in "ACTG" for char in seq):
    print("Please enter a valid sequence")
else:
    print("=== BASIC ANALYSIS OF DNA SEQUENCES ===")
    print("Sequence:", seq)
    print("Length:", len(seq))
    print("A:", seq.count("A"), "T:", seq.count("T"), "G:", seq.count("G"), "C:", seq.count("C"))
    print("GC%:", round((seq.count("G") + seq.count("C")) / len(seq) * 100, 2))