import os.path
import random
from runpy import run_path
from sys import audit


def getquestions_yes_no(topic, questionNumber):
    import pandas as pd
    file_path = "Data.csv"

    # Считывание базы вопросов

    df = pd.read_csv(file_path)
    df["Номер вопроса"] = df["Номер вопроса"].ffill()
    df["Тема"] = df["Тема"].ffill()

    # limited_df = df.iloc[]


    # Заполнение вопросами с ответами да или нет

    questions_yesno = tuple(
        {"Тема": row["Тема"], "Номер вопроса": int(row["Номер вопроса"]), "Вопрос": row["Вопрос"],
         "Ответ": row["Ответ"]}
        for _, row in df.iterrows()
        if pd.notna(row["Вопрос"]) and pd.notna(row["Ответ"]) and int(row["Номер вопроса"]) == questionNumber and (
                str(row["Тема"]) == topic)
    )
    return questions_yesno


def getquestions_with_img(topic, questionNumber):
    import pandas as pd
    file_path = "Data.csv"
    df = pd.read_csv(file_path)
    df["Номер вопроса"] = df["Номер вопроса"].ffill()
    df["Тема"] = df["Тема"].ffill()




    questions_with_img = tuple(
        {"Тема": row["Тема"], "Номер вопроса": int(row["Номер вопроса"]), "Вопрос": row["Вопрос"],
         "Картинка": row["Картинка"], "Ответ": str(row["Ответ"]).split("/"),
         "Неверные ответы": str(row["Неверные ответы"]).split(", ")}
        for _, row in df.iterrows()
        if pd.notna(row["Вопрос"]) and pd.notna(row["Ответ"]) and pd.notna(row["Неверные ответы"]) and
        int(row["Номер вопроса"]) == questionNumber and (str(row["Тема"]) == topic) and os.path.exists(row["Картинка"])
    )
    return questions_with_img


def getquestions_open(topic, questionNumber):
    import pandas as pd
    file_path = "Data.csv"
    df = pd.read_csv(file_path)
    df["Номер вопроса"] = df["Номер вопроса"].ffill()
    df["Тема"] = df["Тема"].ffill()

    # limited_df = df.iloc[]



    questions_open = tuple(
        {"Тема": row["Тема"], "Номер вопроса": int(row["Номер вопроса"]), "Вопрос": row["Вопрос"],
         "Ответ": str(row["Ответ"]).split("/")}
        for _, row in df.iterrows()
        if pd.notna(row["Вопрос"]) and pd.notna(row["Ответ"]) and int(row["Номер вопроса"]) == questionNumber and (
                str(row["Тема"]) == topic)
    )
    return questions_open


def get_five_questions(type):
    if type == 1: type = "Первая мировая война"
    if type == 2: type = "Вторая мировая война"
    questions_1 = (random.choice(getquestions_yes_no(type, 1)),)
    questions_2 = (random.choice(getquestions_yes_no(type, 2)),)
    questions_3 = (random.choice(getquestions_with_img(type, 3)),)
    questions_4 = (random.choice(getquestions_with_img(type, 4)),)
    questions_5 = (random.choice(getquestions_open(type, 5)),)
    questions = questions_1 + questions_2 + questions_3 + questions_4 + questions_5
    return questions

