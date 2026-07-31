# This is the first bioinformatics script I have written.
def analyser():
     global seq
     print("=== BASIC ANALYSIS OF DNA SEQUENCES ===")
     print("Sequence:", seq)
     print("Length:", len(seq))
     print("A:", seq.count("A"), "T:", seq.count("T"), "G:", seq.count("G"), "C:", seq.count("C"))
     print("GC%:", round((seq.count("G") + seq.count("C")) / len(seq) * 100, 2))

seq = input("Enter a sequence: ").strip().upper()
if seq == "" or any(char not in "ACTG" for char in seq):
    while seq == "" or any(char not in "ACTG" for char in seq):
        seq = input("Please enter a valid sequence: ").strip().upper()
        if seq != "" and not any(char not in "ACTG" for char in seq):
            analyser()
else:   
     analyser()
