from django.db import models


class Language(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=50, unique=True, primary_key=True)
    complexity = models.PositiveSmallIntegerField(verbose_name="Сложность", default=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'languages'
        verbose_name = "язык"
        verbose_name_plural = "языки"


class Student(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    @full_name.setter
    def full_name(self, value):
        try:
            self.last_name, self.first_name = value.split(' ')
        except ValueError:
            print("Invalid full name")

    def __str__(self) -> str:
        return self.full_name


class Classroom(models.Model):
    rating = models.IntegerField(verbose_name="Рейтинг", default=0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student} изучает {self.language} [{self.rating}/10]'
