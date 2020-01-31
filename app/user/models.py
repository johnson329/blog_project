from app.extenstion import models


class User(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    nickname = models.Column(models.String(20))
    def save(self):
        models.session.add(self)
        models.session.commit()

