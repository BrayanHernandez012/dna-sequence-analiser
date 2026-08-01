# This is the first bioinformatics script I have written.

def analyser(seq):
    a_count = seq.count("A")
    t_count = seq.count("T")
    g_count = seq.count("G")
    c_count = seq.count("C")

    length = len(seq)
    gc_percent = round(((g_count + c_count) / length) * 100, 2)

    print("\n=== BASIC ANALYSIS OF DNA SEQUENCES ===")
    print(f"Sequence: {seq}")
    print(f"Length: {length}")
    print(f"A: {a_count} | T: {t_count} | G: {g_count} | C: {c_count}")
    print(f"GC%: {gc_percent}%")

if __name__ == "__main__":
    seq = input("Enter a sequence: ").strip().upper()

    while not seq or any(char not in "ACTG" for char in seq):
        seq = input("Please enter a valid sequence: ").strip().upper()

analyser(seq)
