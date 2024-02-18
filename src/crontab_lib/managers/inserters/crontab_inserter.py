"""Insert cron job in the crontab file."""
from shell_executor_lib import CommandManager


class CrontabInserter:
    """Insert cron job in the crontab file."""

    def __init__(self, command_manager: CommandManager):
        """Initialize the CrontabInserter.

        Args:
            command_manager: To make commands in the shell.
        """
        self.__command_manager = command_manager

    async def add_cron_job(self, cron_job: str) -> None:
        """Add a cron job in the crontab file.

        Args:
            cron_job: The cron job to be added.

        Raises:
            CommandError: If the exit code is not unexpected.
        """
        await self.__command_manager.execute_command(f'(/bin/crontab -l ; /bin/echo \'{cron_job}\') | /bin/crontab -',
                                                     False)

    async def add_cron_job_in_new_file(self, cron_job: str) -> None:
        """Add a cron job in new crontab file.

        Args:
            cron_job: The cron job to be added.

        Raises:
            CommandError: If the exit code is not unexpected.
        """
        await self.__command_manager.execute_command(f'/bin/echo \'{cron_job}\' | /bin/crontab -', False)
