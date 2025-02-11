import os

folder_path = 'bin'

total_lines = 0

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                total_lines += len(lines)

print(f'Общее количество строк во всех файлах в папке "{folder_path}": {total_lines}')
