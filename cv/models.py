from django.db import models
from django.urls import reverse


class Profil(models.Model):
    firstname = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='pictures', blank=True, null=True)
    profession = models.CharField(max_length=300, blank=True)
    age = models.IntegerField(default=0)
    email = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=200, blank=True)
    english_profil = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.firstname} {self.surname} -- english({self.english_profil})'


class Section(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Block(models.Model):
    title = models.CharField(max_length=200)
    section = models.ForeignKey(Section, related_name='section', null=True, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='pictures', blank=True, null=True)
    file = models.FileField(upload_to='files', blank=True, null=True)
    short_description = models.TextField(blank=True)
    paragraph1 = models.TextField(blank=True)
    paragraph2 = models.TextField(blank=True)
    paragraph3 = models.TextField(blank=True)

    def __str__(self):
        return f'{self.section.title} > {self.title}'


class PortfolioType(models.Model):
    name = models.CharField(max_length=200)
    pos_index = models.IntegerField(default=100)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(PortfolioType, related_name='section', null=True, on_delete=models.CASCADE)
    pos_index = models.IntegerField(default=100)
    picture1 = models.ImageField(upload_to='pictures', blank=True, null=True)
    picture2 = models.ImageField(upload_to='pictures', blank=True, null=True)
    picture3 = models.ImageField(upload_to='pictures', blank=True, null=True)
    file = models.FileField(upload_to='files', blank=True, null=True)
    short_description = models.TextField(blank=True)
    paragraph1 = models.TextField(blank=True)
    paragraph2 = models.TextField(blank=True)
    paragraph3 = models.TextField(blank=True)
    web_address = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return f'{self.type.name} > {self.name}'

    def get_absolute_url(self):
        return reverse("portfolio", kwargs={"id": self.id})


class VisitorMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    object = models.CharField(max_length=300)
    text = models.TextField()
    receiving_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-receiving_date']

    def __str__(self):
        formated_date = self.receiving_date.strftime("%B %d, %Y -- %H:%M")
        return f'Message from {self.name} | object --> {self.object[0:30]}... | {formated_date}'



