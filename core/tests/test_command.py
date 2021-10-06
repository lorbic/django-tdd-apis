from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db setup to become available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            '''
            Mocking the behaviour of default database connection handler
            to be able to use in the test without real database.
            '''
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)  # do not sleep for 1 second during test
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            '''This code checks for 5 time failure to connect to db then returns true'''
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
