from pathlib import Path
from datetime import datetime

def main():
    # Use absolute path to the mounted fileshare
    base_output_path = Path("/mnt/output")
    
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create paths with vm1 directory and timestamped filename
    output_bronze = base_output_path / f"bronze/vm3/vm3_{timestamp}.txt"
    output_silver = base_output_path / f"silver/vm3/vm3_{timestamp}.txt"
    output_gold = base_output_path / f"gold/vm3/vm3_{timestamp}.txt"
    
    output_files = [output_bronze, output_silver, output_gold]
    
    for output_file in output_files:
        # Create parent directories (including vm1 subdirectory)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Write the file with timestamp in content too
        with open(output_file, 'w') as f:
            f.write("Hello, World from vm3\n")
            f.write("Generated at: {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

if __name__ == "__main__":
    main()
