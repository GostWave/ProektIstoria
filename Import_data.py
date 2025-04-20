from sys import audit




def getquestions():
    import pandas as pd
    file_path = "Data2.csv"

    # Считывание базы вопросов

    df = pd.read_csv(file_path)
    limited_df = df.iloc[:20]

    #Заполнение вопросами с ответами да или нет

    questions_yesno = tuple(
        {"Вопрос": row["Вопрос"], "Ответ": row["Ответ"]}
        for _, row in limited_df.iterrows()
        if pd.notna(row["Вопрос"]) and pd.notna(row["Ответ"])
    )
    return questions_yesno
