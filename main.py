from pathlib import Path

def main():
    # Use absolute path to the mounted fileshare
    base_output_path = Path("/mnt/output")
    
    output_bronze = base_output_path / "bronze/vm3.txt"
    output_silver = base_output_path / "silver/vm3.txt" 
    output_gold = base_output_path / "gold/vm3.txt"
    
    output_files = [output_bronze, output_silver, output_gold]
    
    for output_file in output_files:
        if not output_file.parent.exists():
            output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w') as f:
            f.write("Hello, World from vm3")

if __name__ == "__main__":
    main()
