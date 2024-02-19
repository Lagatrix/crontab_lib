"""Test the crontab modifier."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager

from crontab_lib.managers.modifiers import CrontabModifier
from tests.mock_crontab_lib import mock_command_executor_method, mock_entity_cron_job


class TestCrontabModifier(unittest.IsolatedAsyncioTestCase):
    """Test the crontab modifier."""

    def setUp(self) -> None:
        """Set up the test."""
        self.crontab_modifier = CrontabModifier(CommandManager("augusto", "augusto"))

    async def test_add_job(self) -> None:
        """Test correctly functioning of command manager when modify a cron job in the crontab file."""
        with mock.patch(mock_command_executor_method, return_value=[]):
            await self.crontab_modifier.modify_cron_job(mock_entity_cron_job.format_to_use_in_sed(),
                                                        mock_entity_cron_job.format_to_use_in_sed())
