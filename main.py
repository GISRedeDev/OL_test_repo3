from pathlib import Path

def main():
    output_bronze = Path(__file__).resolve().parent.parent.joinpath("mnt/output/bronze/vm3.txt")
    output_silver = Path(__file__).resolve().parent.parent.joinpath("mnt/output/silver/vm3.txt")
    output_gold = Path(__file__).resolve().parent.parent.joinpath("mnt/output/gold/vm3.txt")
    output_files = [output_bronze, output_silver, output_gold]
    for output_file in output_files:
        if not output_file.parent.exists():
            output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w') as f:
            f.write("Hello, World from vm3")


if __name__ == "__main__":
    main()