import datetime

__all__ = []

labels = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
]


class RelativeDatetime(object):
    def __init__(self, value):
        self.value = value

    @property
    def ago(self):
        return datetime.datetime.utcnow() - self.value

    @property
    def in_future(self):
        return datetime.datetime.utcnow() + self.value


for idx, label in enumerate(labels):
    class DateQuery(object):
        value = idx

        @property
        def seconds(cls):
            return RelativeDatetime(datetime.timedelta(0, cls.value))
        second = seconds

        @property
        def minutes(cls):
            return RelativeDatetime(datetime.timedelta(0, cls.value * 60))
        minute = minutes

        @property
        def hours(cls):
            return RelativeDatetime(datetime.timedelta(0, cls.value * 60 * 60))
        hour = hours

        @property
        def days(cls):
            return RelativeDatetime(datetime.timedelta(0, cls.value * 24 * 60 * 60))
        day = days

    locals()[label] = DateQuery()
    __all__.append(label)

