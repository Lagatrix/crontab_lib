"""Test the crontab inserter."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from crontab_lib.managers.inserters import CrontabInserter
from tests.mock_crontab_lib import mock_command_executor_method, mock_cron_job


class TestCrontabInserter(unittest.IsolatedAsyncioTestCase):
    """Test the crontab inserter."""

    def setUp(self) -> None:
        """Set up the test."""
        self.crontab_inserter = CrontabInserter(CommandManager("augusto", "augusto"))

    async def test_insert_cron_job_in_existent_file(self) -> None:
        """Test correctly functioning of command manager when adding a cron job in the crontab file."""
        with mock.patch(mock_command_executor_method, return_value=[]):
            await self.crontab_inserter.add_cron_job(mock_cron_job)

    async def test_insert_cron_job_in_new_file(self) -> None:
        """Test correctly functioning of command manager when adding a cron job in new crontab fiel."""
        with mock.patch(mock_command_executor_method, return_value=[]):
            await self.crontab_inserter.add_cron_job_in_new_file(mock_cron_job)
