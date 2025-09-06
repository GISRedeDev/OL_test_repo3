from pathlib import Path
from datetime import datetime

def main():
    # Use absolute path to the mounted fileshare
    base_output_path = Path("/mnt")
    base_reference_path = Path("/mnt/reference")  
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create paths with vm1 directory and timestamped filename
    output_bronze = base_output_path / f"bronze/vm3/vm3_{timestamp}.txt"
    output_silver = base_output_path / f"silver/vm3/vm3_{timestamp}.txt"
    output_gold = base_output_path / f"gold/vm3/vm3_{timestamp}.txt"
    staging_data = base_output_path / f"staging_data/vm3/vm3_{timestamp}.txt"
    
    output_files = [output_bronze, output_silver, output_gold, staging_data]
    
    for output_file in output_files:
        # Create parent directories (including vm1 subdirectory)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Write the file with timestamp in content too
        with open(output_file, 'w') as f:
            f.write("Hello, World from vm3 directly to blob\n")
            f.write("Generated at: {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            if base_reference_path.exists():
                for folder in base_reference_path.iterdir():
                    f.write(f"REF folder {folder.name} is here")
            f.write("Is there anything in reference?")

if __name__ == "__main__":
    main()
