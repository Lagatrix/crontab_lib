"""Manage cron jobs in the crontab file."""
from shell_executor_lib import CommandManager, CommandError

from crontab_lib import CronJob, NonexistentCrontabFileError, InvalidCronFormatError
from crontab_lib.managers.getters import CrontabGetter
from crontab_lib.managers.inserters import CrontabInserter


class CrontabManager:
    """Manage cron jobs in the crontab file."""

    def __init__(self, command_manager: CommandManager) -> None:
        """Initialize the CrontabManager.

        Args:
            command_manager: To make commands in the shell.
        """
        self.__user = command_manager.user
        self.__crontab_inserter = CrontabInserter(command_manager)
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

    async def add_cron_job(self, cron_job: str) -> None:
        """Add a cron job in the crontab file.

        Args:
            cron_job: The cron job to be added.

        Raises:
            InvalidCronFormatError: If the cron job has an invalid format.
            CommandError: If the exit code is not unexpected.
        """
        try:
            if await self.__crontab_getter.user_has_crontab_file():
                await self.__crontab_inserter.add_cron_job(cron_job)
            else:
                await self.__crontab_inserter.add_cron_job_in_new_file(cron_job)
        except CommandError as command_error:
            if "errors in crontab file" in command_error.response:
                raise InvalidCronFormatError(cron_job)
            raise command_error
