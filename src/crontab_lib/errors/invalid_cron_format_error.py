"""This exception represents an error if a cron job has a bad syntax."""
from crontab_lib import CronJob


class InvalidCronFormatError(Exception):
    """This exception represents an error if a cron job has a bad syntax."""

    def __init__(self, cron_job: CronJob):
        """Initialize the InvalidCronFormatError.

        Args:
            cron_job: The problematic cron job.
        """
        self.message = f"The con job ${str(cron_job)} is not valid"
        super().__init__(self.message)
