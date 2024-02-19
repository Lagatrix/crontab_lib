"""Delete cron job from the crontab file."""

from shell_executor_lib import CommandManager


class CrontabEliminator:
    """Delete cron job from the crontab file."""

    def __init__(self, command_manager: CommandManager):
        """Initialize the CrontabEliminator.

        Args:
            command_manager: To make commands in the shell.
        """
        self.__command_manager: CommandManager = command_manager

    async def delete_cron_job(self, cron_job: str) -> None:
        """Delete a cron job from the crontab file.

        Args:
            cron_job: Cronjob to be deleted.

        Raises:
            CommandError: If the exit code is not unexpected.
        """
        await self.__command_manager.execute_command(
            f"( crontab -l | sed '{cron_job}'; ) | crontab -", False)
