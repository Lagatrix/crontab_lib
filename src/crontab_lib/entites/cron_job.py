"""This entity represents a cron job."""
from dataclasses import dataclass


@dataclass
class CronJob:
    """This class represents a cron job.

    Attributes:
        minute: str: The minute the command will be executed.
        hour: str: The hour the command will be executed.
        day_of_month: str: The day of the month the command will be executed.
        month: str: The month the command will be executed.
        day_of_week: str: The day of the week the command will be executed.
        command: str: The command to be executed.
    """
    minute: str = "*"
    hour: str = "*"
    day_of_month: str = "*"
    month: str = "*"
    day_of_week: str = "*"
    command: str = ""

    def format_to_use_in_sed(self) -> str:
        """This method returns the string representation of the cron job to be used in the sed command.

        Returns:
            The cron job formatted.
        """
        return str(self).replace('/', '\\/').replace('*', '\\*')

    def __str__(self) -> str:
        """This method returns the string representation of the cron job."""
        return f"{self.minute} {self.hour} {self.day_of_month} {self.month} {self.day_of_week} {self.command}"
