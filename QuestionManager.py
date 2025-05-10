import Import_data
from PIL import Image


# for i in Import_data.getquestions_yes_no():
#     print(i)

# for i in Import_data.getquestions_with_img():
#     print(i)
    # image_path = str(i["Картинка"])
    # img = Image.open(image_path)
    # img.show()
q=Import_data.get_five_questions(1)
p=str(q[2]["Картинка"])
im=Image.open(p)
im.show()
print(q)

