import os.path
import random
from runpy import run_path
from sys import audit


def getquestions_yes_no(topic, questionNumber):
    import pandas as pd
    file_path = "Data3.csv"

    # Считывание базы вопросов

    df = pd.read_csv(file_path)
    df["Номер вопроса"] = df["Номер вопроса"].ffill()
    df["Тема"] = df["Тема"].ffill()

    # limited_df = df.iloc[]
    if topic == 1: topic = "Первая мировая война"
    if topic == 2: topic = "Вторая мировая война"

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
    file_path = "Data3.csv"
    df = pd.read_csv(file_path)
    df["Номер вопроса"] = df["Номер вопроса"].ffill()
    df["Тема"] = df["Тема"].ffill()
    if questionNumber ==3:
        limited_df = df.iloc[20:22]
    else:
        limited_df = df.iloc[30:31]

    if topic == 1: topic = "Первая мировая война"
    if topic == 2: topic = "Вторая мировая война"

    questions_with_img = tuple(
        {"Тема": row["Тема"], "Номер вопроса": int(row["Номер вопроса"]), "Вопрос": row["Вопрос"],
         "Картинка": row["Картинка"], "Ответ": str(row["Ответ"]).split("/"),
         "Неверные ответы": str(row["Неверные ответы"]).split(", ")}
        for _, row in limited_df.iterrows()
        if pd.notna(row["Вопрос"]) and pd.notna(row["Ответ"]) and pd.notna(row["Неверные ответы"])  and os.path.exists(
            row["Картинка"]) and int(row["Номер вопроса"]) == questionNumber and (str(row["Тема"]) == topic)
    )
    return questions_with_img


def getquestions_open(topic, questionNumber):
    import pandas as pd
    file_path = "Data3.csv"
    df = pd.read_csv(file_path)
    df["Номер вопроса"] = df["Номер вопроса"].ffill()
    df["Тема"] = df["Тема"].ffill()

    # limited_df = df.iloc[]

    if topic == 1: topic = "Первая мировая война"
    if topic == 2: topic = "Вторая мировая война"

    questions_open = tuple(
        {"Тема": row["Тема"], "Номер вопроса": int(row["Номер вопроса"]), "Вопрос": row["Вопрос"],
         "Ответ": str(row["Ответ"]).split("/")}
        for _, row in df.iterrows()
        if pd.notna(row["Вопрос"]) and pd.notna(row["Ответ"]) and int(row["Номер вопроса"]) == questionNumber and (
                str(row["Тема"]) == topic)
    )
    return questions_open


def get_five_questions(type):
    questions_1 = (random.choice(getquestions_yes_no(1, 1)),)
    questions_2 = (random.choice(getquestions_yes_no(1, 2)),)
    questions_3 = (random.choice(getquestions_with_img(1, 3)),)
    questions_4 = (random.choice(getquestions_with_img(1, 4)),)
    questions_5 = (random.choice(getquestions_open(1, 5)),)
    questions = questions_1 + questions_2 + questions_3 + questions_4 + questions_5
    return questions

