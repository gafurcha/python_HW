import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\User\Desktop\комп Настя\python\HW3_pandas.csv"

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Данные успешно загружены!")
        return data
    except FileNotFoundError:
        print("Ошибка: файл не найден. Проверьте путь к файлу.")
        exit()

def check_column(data, column):
    if column not in data.columns:
        raise ValueError(f"Столбец '{column}' не найден в файле!")
    print(f"\nСтолбец '{column}' успешно найден.")

def process_data(data, column):
    filtered_data = data[data[column] > 50]
    print(f"\nОтфильтрованные данные (где '{column}' > 50): {filtered_data.shape[0]} строк.")

    data[f"{column}_doubled"] = data[column] * 2
    print("\nДобавлен новый столбец с удвоенными значениями:")
    print(data.head())
    return data, filtered_data

def handle_missing_values(data):
    print("\nОбработка пропущенных данных...")
    if data.isnull().values.any():
        data.fillna(data.mean(numeric_only=True), inplace=True)
        print("Пропущенные значения заполнены средними значениями.")
    else:
        print("Пропущенные значения отсутствуют.")
    return data

def plot_graph(data, column):

    plt.figure(figsize=(10, 6))
    plt.scatter(data[column], data[f"{column}_doubled"], label=f'{column} vs Doubled')
    plt.title('График зависимости', fontsize=14)
    plt.xlabel(column, fontsize=12)
    plt.ylabel(f'{column}_doubled', fontsize=12)
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    data = load_data(file_path)

    print(f"\nИмена столбцов файла: {list(data.columns)}")
    print("\nПервые 5 строк данных:")
    print(data.head())

    required_column = 'Баллы'
    check_column(data, required_column)
    data, filtered_data = process_data(data, required_column)

    data = handle_missing_values(data)

    plot_graph(data, required_column)
