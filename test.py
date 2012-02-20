import datetime

from unittest import TestCase
from ago import *

class Tests(TestCase):
    def test_no_trash_in_scope(self):
        self.assert_('RelativeDatetime' not in globals())
        self.assert_('DateQuery' not in globals())

    def test_five_minutes_ago(self):
        self.assertEqual(
            five.minutes.ago.timetuple()[:6],
            (datetime.datetime.utcnow() - datetime.timedelta(0, 5 * 60)).timetuple()[:6]
        )

    def test_six_hours_ago(self):
        self.assertEqual(
            six.hours.ago.timetuple()[:6],
            (datetime.datetime.utcnow() - datetime.timedelta(0, 6 * 60 * 60)).timetuple()[:6]
        )

    def test_one_day_ago(self):
        self.assertEqual(
            one.day.ago.timetuple()[:6],
            (datetime.datetime.utcnow() - datetime.timedelta(0, 24 * 60 * 60)).timetuple()[:6]
        )

    def test_five_minutes_in_future(self):
        self.assertEqual(
            five.minutes.in_future.timetuple()[:6],
            (datetime.datetime.utcnow() + datetime.timedelta(0, 5 * 60)).timetuple()[:6]
        )

