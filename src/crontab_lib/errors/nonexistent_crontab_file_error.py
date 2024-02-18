"""This exception represents the error of trying to access a crontab file that does not exist."""


class NonexistentCrontabFileError(Exception):
    """This exception represents the error of trying to access a crontab file that does not exist."""

    def __init__(self, user: str):
        """Initialize the NonexistentCrontabFileError.

        Args:
            user: The user who doesn't have a crontab file.
        """
        self.message = f"The user {user} doesn't have a crontab file."
        super().__init__(self.message)
