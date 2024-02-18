"""Test the crontab manager."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager, CommandError

from crontab_lib import CrontabManager, NonexistentCrontabFileError
from tests.mock_crontab_lib import mock_command_executor_method, mock_crontab_file, mock_cronjob_list


class TestCrontabManager(unittest.IsolatedAsyncioTestCase):
    """Test the crontab manager."""

    def setUp(self) -> None:
        """Set up the test."""
        self.crontab_manager = CrontabManager(CommandManager("augusto", "augusto"))

    async def test_get_cron_jobs(self) -> None:
        """Test correctly functioning of command manager when get cron jobs in crontab file."""
        with mock.patch(mock_command_executor_method, return_value=mock_crontab_file):
            self.assertEqual(await self.crontab_manager.get_cron_jobs(), mock_cronjob_list)

    async def test_user_has_not_crontab_file(self) -> None:
        """Test correctly functioning of command manager when user hasn't a crontab file."""
        with mock.patch(mock_command_executor_method, side_effect=CommandError(1, "crontab: no crontab for augusto")):
            with self.assertRaises(NonexistentCrontabFileError):
                await self.crontab_manager.get_cron_jobs()
