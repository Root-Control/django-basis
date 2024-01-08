from mongoengine import Document, StringField

class Article(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)

    meta = {'collection': 'articles'}