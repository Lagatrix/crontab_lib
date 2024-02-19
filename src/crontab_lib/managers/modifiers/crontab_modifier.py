"""Modify cron jobs in the crontab file."""
from shell_executor_lib import CommandManager


class CrontabModifier:
    """Modify cron jobs in the crontab file."""

    def __init__(self, command_manager: CommandManager):
        """Initialize the CrontabModifier.

        Args:
            command_manager: To make commands in the shell.
        """
        self.__command_manager: CommandManager = command_manager

    async def modify_cron_job(self, new_cron_job: str, old_cron_job: str) -> None:
        """Modify a cron job in the crontab file.

        Args:
            new_cron_job: The new cron job to be added.
            old_cron_job: The old cron job to be removed.

        Raises:
            CommandError: If the exit code is not unexpected.
        """
        await self.__command_manager.execute_command(f'(/bin/crontab -l | /bin/sed \'{old_cron_job}/d\'; '
                                                     f'/bin/echo \'{new_cron_job}\') | /bin/crontab -',  False)
