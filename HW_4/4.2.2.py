import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    'fruit': ['apple', 'banana', 'orange'] * 3,
    'weight': ['high', 'medium', 'low'] * 3,
    'price': np.random.randint(0, 15, size=9)
})

df2 = pd.DataFrame({
    'pazham': ['apple', 'orange', 'pine'] * 2,
    'kilo': ['high', 'low'] * 3,
    'price': np.random.randint(0, 15, size=6)
})

merged_df = pd.merge(
    df1,
    df2,
    left_on=['fruit', 'weight'],
    right_on=['pazham', 'kilo']
)

print("Объединенный DataFrame:")
print(merged_df)

df1 = pd.DataFrame({
    'fruit': ['apple', 'orange', 'banana'] * 3,
    'weight': ['high', 'medium', 'low'] * 3,
    'price': np.arange(9)
})

df2 = pd.DataFrame({
    'fruit': ['apple', 'orange', 'pine'] * 2,
    'weight': ['high', 'medium'] * 3,
    'price': np.arange(6)
})

df_diff = pd.concat([df1, df2, df2], ignore_index=True).drop_duplicates(keep=False)

print("\nРезультат удаления строк, присутствующих в df2:")
print(df_diff)
