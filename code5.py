import os
folder_name = "Youtube Videos"
os.makedirs(folder_name, exist_ok=True)
for i in range(1, 101):
    file_path = os.path.join(folder_name, f"Lesson{i}.YT")
    with open(file_path, "w") as file:
        file.write(f"This is file number {i}\n")
print("✅ 100 files created successfully!")




