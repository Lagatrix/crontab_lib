"""Gets cron job from the crontab file."""
from shell_executor_lib import CommandManager, CommandError

from crontab_lib import CronJob


class CrontabGetter:
    """Gets cron job from the crontab file."""

    def __init__(self, command_manager: CommandManager) -> None:
        """Initialize the CrontabGetter.

        Args:
            command_manager: To make commands in the shell.
        """
        self.__command_manager = command_manager

    async def get_cron_jobs(self) -> list[CronJob]:
        """Ger cron jobs from the crontab file.

        Returns:
            A list of cron jobs.

        Raises:
            CommandError: If the command return an unknown exit code.
        """
        crontab_list: list[CronJob] = []
        data_list: list[str] = await self.__command_manager.execute_command('/bin/crontab -l', False)

        if len(data_list) == 0:
            return crontab_list

        for data_row in data_list:
            if data_row[0] != '#':
                data: list[str] = data_row.split(" ")
                crontab_list.append(CronJob(data[0], data[1], data[2], data[3], data[4], " ".join(data[5:])))

        return crontab_list

    async def user_has_crontab_file(self) -> bool:
        """Check if the user has a crontab file.

        Returns:
            If the user has a crontab file.
        """
        try:
            await self.__command_manager.execute_command('/bin/crontab -l', False)
        except CommandError:
            return False
        return True
