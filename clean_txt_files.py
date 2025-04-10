import os

def remove_duplicate_lines_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    
    seen = set()
    unique_lines = []
    for line in lines:
        if line.strip() and line not in seen:
            unique_lines.append(line)
            seen.add(line)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(unique_lines)


folder_path = 'data/docs_raw'


for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        remove_duplicate_lines_from_file(file_path)

print("✅ All .txt files cleaned.")
