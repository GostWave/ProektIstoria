import os.path
from sys import audit




def getquestions_yes_no():
    import pandas as pd
    file_path = "Data.csv"

    # Считывание базы вопросов

    df = pd.read_csv(file_path)
    df["Номер вопроса"] = df["Номер вопроса"].ffill()
    df["Тема"] = df["Тема"].ffill()

    limited_df = df.iloc[:20]

    #Заполнение вопросами с ответами да или нет

    questions_yesno = tuple(
        {"Тема": row["Тема"],"Номер вопроса": int(row["Номер вопроса"]), "Вопрос": row["Вопрос"], "Ответ": row["Ответ"]}
        for _, row in limited_df.iterrows()
        if pd.notna(row["Вопрос"]) and pd.notna(row["Ответ"])
    )
    return questions_yesno

def getquestions_with_img():
    import pandas as pd
    file_path = "Data.csv"
    df = pd.read_csv(file_path)
    df["Номер вопроса"] = df["Номер вопроса"].ffill()
    df["Тема"] = df["Тема"].ffill()
    limited_df = df.iloc[20:22]
    questions_with_img= tuple(
        {"Тема": row["Тема"],"Номер вопроса": int(row["Номер вопроса"]), "Вопрос": row["Вопрос"], "Картинка": row["Картинка"], "Ответ": row["Ответ"]}
        for _, row in limited_df.iterrows()
        if pd.notna(row["Вопрос"]) and pd.notna(row["Ответ"]) and os.path.exists(row["Картинка"])
    )
    return questions_with_img