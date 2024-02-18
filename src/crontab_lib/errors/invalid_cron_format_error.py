"""This exception represents an error if a cron job has a bad syntax."""


class InvalidCronFormatError(Exception):
    """This exception represents an error if a cron job has a bad syntax."""

    def __init__(self, cron_job: str):
        """Initialize the InvalidCronFormatError.

        Args:
            cron_job: The problematic cron job.
        """
        self.message = f"The cron job ${cron_job} is not valid"
        super().__init__(self.message)
