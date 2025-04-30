import os.path
from sys import audit




def getquestions_yes_no(topic):
    import pandas as pd
    file_path = "Data.csv"

    # Считывание базы вопросов

    df = pd.read_csv(file_path)
    df["Номер вопроса"] = df["Номер вопроса"].ffill()
    df["Тема"] = df["Тема"].ffill()

    # limited_df = df.iloc[]
    if topic==1:topic="Первая мировая война"
    if topic==2:topic="Вторая мировая война"

    #Заполнение вопросами с ответами да или нет

    questions_yesno = tuple(
        {"Тема": row["Тема"],"Номер вопроса": int(row["Номер вопроса"]), "Вопрос": row["Вопрос"], "Ответ": row["Ответ"]}
        for _, row in df.iterrows()
        if pd.notna(row["Вопрос"]) and pd.notna(row["Ответ"]) and (int(row["Номер вопроса"])==1 or int(row["Номер вопроса"])==2) and (str(row["Тема"])==topic)
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
        {"Тема": row["Тема"],"Номер вопроса": int(row["Номер вопроса"]), "Вопрос": row["Вопрос"], "Картинка": row["Картинка"], "Ответ": str(row["Ответ"]).split("/"), "Неверные ответы" : str(row["Неверные ответы"]).split(", ")}
        for _, row in limited_df.iterrows()
        if pd.notna(row["Вопрос"]) and pd.notna(row["Ответ"]) and  pd.notna(row["Неверные ответы"]) and os.path.exists(row["Картинка"]) and (int(row["Номер вопроса"])==3 or int(row["Номер вопроса"])==4)
    )
    return questions_with_img

# def getquestions_with_choice():
#     import pandas as pd
#     file_path = "Data.csv"
#     df = pd.read_csv(file_path)
#     df["Номер вопроса"] = df["Номер вопроса"].ffill()
#     df["Тема"] = df["Тема"].ffill()
#
#     # limited_df = df.iloc[]
#
#
#
#     questions_with_choice = tuple(
#         {"Тема": row["Тема"], "Номер вопроса": int(row["Номер вопроса"]), "Вопрос": row["Вопрос"],"Ответ": str(row["Ответ"]).split("/"), "Неверные ответы" : str(row["Неверные ответы"]).split(", ")}
#         for _, row in df.iterrows()
#         if pd.notna(row["Вопрос"]) and pd.notna(row["Ответ"]) and pd.notna(row["Неверные ответы"]) and (int(row["Номер вопроса"]) == 3 or int(row["Номер вопроса"]) == 4)
#     )
#     return questions_with_choice
def get_five_questions(type):
    question = getquestions_yes_no(type)
    print(question)