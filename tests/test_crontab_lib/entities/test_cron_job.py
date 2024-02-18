"""Test the cron job."""
import unittest

from crontab_lib import CronJob


class TestCronJob(unittest.TestCase):
    """Test the cron job."""

    def setUp(self) -> None:
        """Set up the test."""
        self.simple_cron_job = CronJob(command="tar -czf /backup/ex.tar.gz /home/", minute="0", hour="3")
        self.complex_cron_job = CronJob(command="tar -czf /backup/ex.tar.gz /home/",
                                        minute="*/15", hour="8-17", day_of_month="1-15", month="1,6", day_of_week="1-5")

    def test_str_cron(self) -> None:
        """Test the string representation of the cron job."""
        self.assertEqual(str(self.simple_cron_job), "0 3 * * * tar -czf /backup/ex.tar.gz /home/")
        self.assertEqual(str(self.complex_cron_job), "*/15 8-17 1-15 1,6 1-5 tar -czf /backup/ex.tar.gz /home/")
