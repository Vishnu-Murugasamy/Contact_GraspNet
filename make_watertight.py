import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

# Define the folder containing the .obj files
folder_path = "/home/rapa/repos/contact_graspnet/acronym/models"  # Replace with your folder path
output_folder = "/home/rapa/repos/contact_graspnet/acronym/output"  # Replace with your output folder path
error_log = os.path.join(folder_path, "error_log.txt")
max_workers = 10  # Adjust this number based on your CPU core count and workload

# List all .obj files in the folder
obj_files = [f for f in os.listdir(folder_path) if f.endswith('.obj')]

def process_file(obj_file):
    obj_path = os.path.join(folder_path, obj_file)
    temp_watertight_path = os.path.join(folder_path, obj_file[:-4]+"_temp.obj")
    output_path = os.path.join(output_folder, obj_file)
    
    try:
        # Step 1: Create a watertight mesh version using the updated manifold command
        manifold_command = f"./manifold {obj_path} {temp_watertight_path}"
        subprocess.run(manifold_command, shell=True, check=True)
        
        # Step 2: Simplify the watertight mesh
        simplify_command = f"./simplify -i {temp_watertight_path} -o {output_path} -m -r 0.5"
        subprocess.run(simplify_command, shell=True, check=True)
    
    except subprocess.CalledProcessError as e:
        with open(error_log, "a") as log:
            log.write(f"Failed to process {obj_file}: {str(e)}\n")
        print(f"Error processing {obj_file}. Logged in error_log.txt.")
    
    finally:
        # Optionally, delete the temporary watertight file after use
        if os.path.exists(temp_watertight_path):
            os.remove(temp_watertight_path)

def main():
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_file, obj_file) for obj_file in obj_files]
        
        for future in as_completed(futures):
            try:
                future.result()  # Will raise an exception if one occurred
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    print("Processing complete. Check error_log.txt for any errors.")

if __name__ == "__main__":
    main()
