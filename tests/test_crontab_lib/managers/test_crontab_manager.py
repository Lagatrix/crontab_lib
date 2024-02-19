"""Test the crontab manager."""
import unittest
from unittest import mock

from shell_executor_lib import CommandManager, CommandError

from crontab_lib import CrontabManager, NonexistentCrontabFileError, InvalidCronFormatError
from tests.mock_crontab_lib import (mock_command_executor_method, mock_crontab_file, mock_entity_cron_job_list,
                                    mock_entity_cron_job)


class TestCrontabManager(unittest.IsolatedAsyncioTestCase):
    """Test the crontab manager."""

    def setUp(self) -> None:
        """Set up the test."""
        self.crontab_manager = CrontabManager(CommandManager("augusto", "augusto"))

    async def test_get_cron_jobs(self) -> None:
        """Test correctly functioning when get cron jobs in crontab file."""
        with mock.patch(mock_command_executor_method, return_value=mock_crontab_file):
            self.assertEqual(await self.crontab_manager.get_cron_jobs(), mock_entity_cron_job_list)

    async def test_get_cron_jobs_of_nonexistent_file(self) -> None:
        """Test correctly functioning when user hasn't a crontab file."""
        with mock.patch(mock_command_executor_method, side_effect=CommandError(1, "crontab: no crontab for augusto")):
            with self.assertRaises(NonexistentCrontabFileError):
                await self.crontab_manager.get_cron_jobs()

    async def test_insert_cron_job_in_existent_file(self) -> None:
        """Test correctly functioning when insert a cron job in crontab file."""
        with mock.patch(mock_command_executor_method, side_effect=([], [])):
            await self.crontab_manager.add_cron_job(mock_entity_cron_job)

    async def test_insert_cron_job_in_new_file(self) -> None:
        """Test correctly functioning when insert a cron job in crontab file."""
        with mock.patch(mock_command_executor_method, side_effect=(CommandError(1, ""), [])):
            await self.crontab_manager.add_cron_job(mock_entity_cron_job)

    async def test_insert_cron_job_with_invalid_format(self) -> None:
        """Test error when insert a cron job with invalid format."""
        with mock.patch(mock_command_executor_method, side_effect=([], CommandError(1, """bad minute
        errors in crontab file, can't install."""))):
            with self.assertRaises(InvalidCronFormatError):
                await self.crontab_manager.add_cron_job(mock_entity_cron_job)

    async def test_insert_cron_job_with_unknown_error(self) -> None:
        """Test error when insert a cron job with unknown error."""
        with mock.patch(mock_command_executor_method, side_effect=([], CommandError(1, "unknown error"))):
            with self.assertRaises(CommandError):
                await self.crontab_manager.add_cron_job(mock_entity_cron_job)

    async def test_edit_cron_job(self) -> None:
        """Test correctly functioning when edit a cron job in crontab file."""
        with mock.patch(mock_command_executor_method, return_value=[]):
            await self.crontab_manager.edit_cron_job(mock_entity_cron_job, mock_entity_cron_job)

    async def test_edit_cron_job_with_invalid_format(self) -> None:
        """Test error when edit a cron job with invalid format."""
        with mock.patch(mock_command_executor_method, side_effect=([], CommandError(1, """bad minute
        errors in crontab file, can't install."""))):
            with self.assertRaises(InvalidCronFormatError):
                await self.crontab_manager.edit_cron_job(mock_entity_cron_job, mock_entity_cron_job)

    async def test_edit_cron_job_of_nonexistent_crontab_file(self) -> None:
        """Test error when edit a cron job of nonexistent crontab file."""
        with mock.patch(mock_command_executor_method, side_effect=CommandError(1, "crontab: no crontab for augusto")):
            with self.assertRaises(NonexistentCrontabFileError):
                await self.crontab_manager.edit_cron_job(mock_entity_cron_job, mock_entity_cron_job)

    async def test_edit_cron_job_with_unknown_error(self) -> None:
        """Test error when edit a cron job with unknown error."""
        with mock.patch(mock_command_executor_method, side_effect=([], CommandError(1, "unknown error"))):
            with self.assertRaises(CommandError):
                await self.crontab_manager.edit_cron_job(mock_entity_cron_job, mock_entity_cron_job)

    async def test_remove_cron_job(self) -> None:
        """Test correctly functioning when remove a cron job in crontab file."""
        with mock.patch(mock_command_executor_method, side_effect=([], [])):
            await self.crontab_manager.delete_cron_job(mock_entity_cron_job)

    async def test_remove_cron_job_of_nonexistent_crontab_file(self) -> None:
        """Test error when remove a cron job of nonexistent crontab file."""
        with mock.patch(mock_command_executor_method, side_effect=CommandError(1, "crontab: no crontab for augusto")):
            with self.assertRaises(NonexistentCrontabFileError):
                await self.crontab_manager.delete_cron_job(mock_entity_cron_job)

    async def test_remove_cron_job_with_unknown_error(self) -> None:
        """Test error when remove a cron job with unknown error."""
        with mock.patch(mock_command_executor_method, side_effect=([], CommandError(1, "unknown error"))):
            with self.assertRaises(CommandError):
                await self.crontab_manager.delete_cron_job(mock_entity_cron_job)
