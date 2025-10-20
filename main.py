import os

def total_salary(path):
    total_sum = 0
    count = 0
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            if ',' in line:
                name, salary = line.strip().split(',')
                total_sum += float(salary)
                count += 1
    return (total_sum, total_sum / count if count > 0 else 0)


file_path = os.path.join(os.path.expanduser("~"), "Desktop", "salary_file.txt")

total, average = total_salary(file_path)
print(f"💰 Загальна: {total}")
print(f"📊 Середня: {average}")
