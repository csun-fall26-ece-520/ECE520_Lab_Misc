import random
import sys
import pathlib

def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    random.seed(42)
    script_dir = pathlib.Path(__file__).resolve().parent
    out_path = script_dir.parent / "sim" / "input_data.txt"
    with open(out_path, "w") as f:
        for _ in range(n):
            a = random.randint(0, 0xFF)
            b = random.randint(0, 0xFF)
            f.write(f"{a:02x} {b:02x}\n")
    print(f"Wrote {n} pairs to {out_path}")

if __name__ == "__main__":
    main()
