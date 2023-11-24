import random
from datetime import date

class Uploader:
    def __init__(self, model_name):
        self.model = model_name

    def file_rename(self, file_name, number_digit):
        min_value = 10 ** (number_digit - 1)
        max_value = (10 ** number_digit) - 1
        name, extension = file_name.split('.')
        random_number = random.randint(min_value, max_value)
        formatted_date = date.today().strftime("%m-%Y")
        return extension, random_number, formatted_date


    def model_image_uploader(self, instance, file_name):
        file = self.file_rename(file_name, 10)
        return f'{self.model}/{file[2]}/{file[1]}_{instance.name}.{file[0]}'

