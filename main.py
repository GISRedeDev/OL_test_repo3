from pathlib import Path
from datetime import datetime
import os
import geopandas as gpd
import rasterio

def main():
    # Use absolute path to the mounted fileshare
    #batch_mounts_dir = os.environ.get('AZ_BATCH_NODE_MOUNTS_DIR')
    batch_mounts_dir = "/mnt"
    base_output_path = Path(batch_mounts_dir)
    base_reference_path = base_output_path.joinpath("reference")  
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create paths with vm1 directory and timestamped filename
    output_bronze = base_output_path / f"bronze/vm3/vm3_{timestamp}.txt"
    output_silver = base_output_path / f"silver/vm3/vm3_{timestamp}.txt"
    output_gold = base_output_path / f"gold/vm3/vm3_{timestamp}.txt"
    staging_data = base_output_path / f"staging-data/vm3/vm3_{timestamp}.txt"
    
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
            try:
                f.write("Geopandas version: {}\n".format(gpd.__version__))
            except Exception as e:
                f.write("Error getting Geopandas version: {}\n".format(e))
            try:
                f.write("Rasterio version: {}\n".format(rasterio.__version__))
            except Exception as e:
                f.write("Error getting Rasterio version: {}\n".format(e))

if __name__ == "__main__":
    main()
