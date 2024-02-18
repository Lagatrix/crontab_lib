"""Manage cron jobs in the crontab file."""
from shell_executor_lib import CommandManager

from crontab_lib import CronJob, NonexistentCrontabFileError
from crontab_lib.managers.getters import CrontabGetter


class CrontabManager:
    """Manage cron jobs in the crontab file."""

    def __init__(self, command_manager: CommandManager) -> None:
        """Initialize the CrontabManager.

        Args:
            command_manager: To make commands in the shell.
        """
        self.__user = command_manager.user
        self.__crontab_getter = CrontabGetter(command_manager)

    async def get_cron_jobs(self) -> list[CronJob]:
        """Get the cron jobs from the crontab file.

        Returns:
            The cron jobs from the crontab file.

        Raises:
            NonexistentCrontabFileError: If the user doesn't have a crontab file.
            CommandError: If the command return an unknown exit code.
        """
        if await self.__crontab_getter.user_has_crontab_file():
            return await self.__crontab_getter.get_cron_jobs()
        raise NonexistentCrontabFileError(self.__user)
