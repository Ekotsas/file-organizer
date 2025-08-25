import os
import shutil

# Dictionary of file types and their extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".java", ".cpp", ".js", ".html", ".css"]
}

def organize_files(folder_path):
    # Go through every file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip if it's a folder
        if os.path.isdir(file_path):
            continue

        # Find which category this file belongs to
        moved = False
        for category, extensions in FILE_TYPES.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                category_folder = os.path.join(folder_path, category)
                os.makedirs(category_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"Moved {filename} → {category}/")
                moved = True
                break

        # If no category matched, put it in "Others"
        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved {filename} → Others/")

if __name__ == "__main__":
    path = input("Enter the folder path to organize: ")
    organize_files(path)
    print("✅ Files organized successfully!")
