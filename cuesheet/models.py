from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Route(models.Model):
    name = models.TextField(max_length=64, unique=True, db_index=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Route(id=%s, name='%s')" % (str(self.id), self.name)


class Cue(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    cue = models.TextField(max_length=64)
    mileage = models.IntegerField()

    def __str__(self):
        return "%s at %d" % (self.cue, self.mileage)

    def __repr__(self):
        return "Cue(id=%s, cue='%s',mileage=%d, route='%s')" % (str(self.id), self.cue, self.mileage, self.route)

