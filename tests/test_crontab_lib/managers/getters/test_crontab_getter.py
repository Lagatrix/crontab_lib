"""Test the crontab getter."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager, CommandError

from crontab_lib.managers.getters import CrontabGetter
from tests.mock_crontab_lib import mock_command_executor_method, mock_crontab_file, mock_entity_cron_job_list


class TestCrontabGetter(unittest.IsolatedAsyncioTestCase):
    """Test the crontab getter."""

    def setUp(self) -> None:
        """Set up the test."""
        self.crontab_getter = CrontabGetter(CommandManager("augusto", "augusto"))

    async def test_get_cron_jobs(self) -> None:
        """Test correctly functioning of command manager when get cron jobs in crontab file."""
        with mock.patch(mock_command_executor_method, return_value=mock_crontab_file):
            self.assertEqual(await self.crontab_getter.get_cron_jobs(), mock_entity_cron_job_list)

    async def test_user_has_crontab_file(self) -> None:
        """Test correctly functioning of command manager when check if user has a crontab file."""
        with mock.patch(mock_command_executor_method, return_value=mock_crontab_file):
            self.assertEqual(await self.crontab_getter.user_has_crontab_file(), True)

    async def test_user_has_not_crontab_file(self) -> None:
        """Test correctly functioning of command manager when check if user hasn't a crontab file."""
        with mock.patch(mock_command_executor_method, side_effect=CommandError(1, "crontab: no crontab for augusto")):
            self.assertEqual(await self.crontab_getter.user_has_crontab_file(), False)
