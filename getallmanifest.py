import os

# Define the root directory to search for __manifest__.py files
root_directory = '/Users/ramizmohamed/Desktop/odoo/'  # Replace with your root directory

# Output file to store the contents of all __manifest__.py files
output_file = 'all_manifests.py'

# Function to find and read all __manifest__.py files
def gather_manifest_files_contents(root_dir):
    manifest_contents = []
    for root, dirs, files in os.walk(root_dir):
        if '__manifest__.py' in files:
            file_path = os.path.join(root, '__manifest__.py')
            with open(file_path, 'r', encoding='utf-8') as file:
                manifest_content = file.read()
                manifest_contents.append((file_path, manifest_content))
    return manifest_contents

# Function to write all manifest contents to a single file
def write_to_output_file(manifest_contents, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for file_path, content in manifest_contents:
            file.write(f"# Content from: {file_path}\n")
            file.write(content)
            file.write("\n\n# End of file\n\n")

# Function to iterate through manifest contents for further processing
def process_manifests(manifest_contents):
    for file_path, content in manifest_contents:
        print(f"Processing file: {file_path}")
        # Add your custom processing logic here
        # Example: Check for certain keywords in the manifest content
        if 'name' in content:
            print(f"Found 'name' in {file_path}")

if __name__ == "__main__":
    # Gather all __manifest__.py file contents
    manifests = gather_manifest_files_contents(root_directory)
    
    # Write all manifest contents to a single output file
    write_to_output_file(manifests, output_file)
    
    # Process the gathered manifest contents
    process_manifests(manifests)
    
    print(f"\nTotal __manifest__.py files processed: {len(manifests)}")
    print(f"All contents have been written to: {output_file}")
