import pandas as pd

df = pd.read_csv(
    "Corona_NLP_train.csv",
    encoding="latin1"          # або encoding="cp1252"
    # encoding_errors="ignore" # якщо раптом ще буде лаятись
)

# взяти 30% випадкових рядків
df_small = df.sample(frac=0.1, random_state=42)

df_small.to_csv("Corona_NLP_train_small.csv", index=False)
