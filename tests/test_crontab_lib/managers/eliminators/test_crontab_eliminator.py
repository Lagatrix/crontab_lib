"""Test the crontab modifier."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from crontab_lib.managers.eliminators import CrontabEliminator
from tests.mock_crontab_lib import mock_command_executor_method, mock_entity_cron_job


class TestCrontabEliminator(unittest.IsolatedAsyncioTestCase):
    """Test for the eliminators."""

    def setUp(self) -> None:
        """Set up the test."""
        self.crontab_eliminator = CrontabEliminator(CommandManager("augusto", "augusto"))

    async def test_remove_job(self) -> None:
        """Test correctly functioning of command manager when remove a cron job in the crontab file."""
        with mock.patch(mock_command_executor_method, return_value=[]):
            await self.crontab_eliminator.delete_cron_job(mock_entity_cron_job.format_to_use_in_sed())
