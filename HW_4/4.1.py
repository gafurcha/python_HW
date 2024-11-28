import pandas as pd

file_path = r'C:\Users\User\Desktop\комп Настя\python\sales.csv'

try:
    sales_data = pd.read_csv(file_path)
    print("Данные успешно загружены.")
except FileNotFoundError:
    print(f"Ошибка: файл '{file_path}' не найден.")
    exit()

sales_data = sales_data.dropna()

sales_data['Выручка'] = sales_data['Количество'] * sales_data['Цена']

total_revenue = sales_data['Выручка'].sum()
print(f"Общая выручка составляет: {total_revenue}")

phone_data = sales_data.query("Продукт == 'Телефон'")

print("\nДанные о продукте 'Телефон':")
print(phone_data)
