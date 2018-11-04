from mongoengine import Document,StringField,IntField

class River(Document):
    #binh thuong se phai init nhung da thuoc Document
    name = StringField()
    continent = StringField()
    length = IntField()