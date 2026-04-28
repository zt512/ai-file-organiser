import os
import shutil

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"]
}

# Keyword-based classification (adds "AI-style" logic)
KEYWORDS = {
    "cv": "Documents",
    "invoice": "Documents",
    "report": "Documents"
}

def get_category(file_name):
    lower_name = file_name.lower()

    # Keyword-based classification first
    for keyword, category in KEYWORDS.items():
        if keyword in lower_name:
            return category

    # Then check file extensions
    _, ext = os.path.splitext(lower_name)
    
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    
    return "Others"

def organise_folder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # Only process files, not folders
        if os.path.isfile(file_path):
            category = get_category(file)
            category_path = os.path.join(folder_path, category)

            # Create category folder if it doesn't exist
            if not os.path.exists(category_path):
                os.makedirs(category_path)

            destination = os.path.join(category_path, file)

            # Handle duplicate file names
            count = 1
            while os.path.exists(destination):
                name, ext = os.path.splitext(file)
                new_name = f"{name}_{count}{ext}"
                destination = os.path.join(category_path, new_name)
                count += 1

            shutil.move(file_path, destination)

            print(f"Moved {file} -> {category}")

if __name__ == "__main__":
    folder = input("Enter folder path: ")
    organise_folder(folder)