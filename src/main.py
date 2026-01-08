import os
import shutil
from datetime import datetime

# Configuration: Define your categories and associated extensions
DIRECTORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Archives": [".zip", ".tar", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    "Audio": [".mp3", ".wav", ".m4a"],
    "Video": [".mp4", ".mkv", ".mov"]
}

def organize_folder(target_path):
    """
    Scans the target path and moves files into categorized folders.
    """
    # 1. Validation: Check if the directory exists
    if not os.path.isdir(target_path):
        print(f"[ERROR] Path not found: {target_path}")
        return

    # 2. Get list of all items in the directory
    try:
        items = os.listdir(target_path)
    except Exception as e:
        print(f"[ERROR] Could not list files: {e}")
        return

    if not items:
        print(f"The directory '{target_path}' is empty.")
        return

    # 3. Loop through each item
    for item in items:
        item_path = os.path.join(target_path, item)

        # Skip if it's a directory (we don't want to move existing folders)
        if os.path.isdir(item_path):
            continue

        # 4. Extract extension and categorize
        _, extension = os.path.splitext(item)
        extension = extension.lower()

        destination_folder = "Others" # Default if no match found
        for category, extensions in DIRECTORIES.items():
            if extension in extensions:
                destination_folder = category
                break

        # 5. Create the destination sub-folder path
        final_dir = os.path.join(target_path, destination_folder)
        
        if not os.path.exists(final_dir):
            os.makedirs(final_dir)

        # 6. Perform the move operation
        try:
            # Using shutil.move to relocate the file
            shutil.move(item_path, os.path.join(final_dir, item))
            print(f"[SUCCESS] Moved: {item} -> {destination_folder}/")
        except Exception as e:
            print(f"[ERROR] Failed to move {item}: {e}")

if __name__ == "__main__":
    # DYNAMIC PATHING:
    # __file__ is 'src/main.py'
    # os.path.dirname(__file__) gets the 'src' folder
    # Second dirname gets the 'file-organizer-tool' root folder
    script_location = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_location)
    
    # Target the 'data' folder inside your project
    data_folder = os.path.join(project_root, "data")

    print("="*40)
    print(f"STARTING ORGANIZATION: {datetime.now().strftime('%H:%M:%S')}")
    print(f"TARGET: {data_folder}")
    print("="*40)

    organize_folder(data_folder)
    
    print("="*40)
    print("ORGANIZATION COMPLETE")