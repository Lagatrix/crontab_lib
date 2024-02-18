"""Mocks of the crontab."""
from crontab_lib import CronJob

mock_crontab_file = ["# m h  dom mon dow   command", "0 0 * * * tar -zcf /var/backups/home.tgz /home/",
                     "0 2 3-4 * * tar -zcf /var/backups/home.tgz /home/"]

mock_cron_job = "0 0 * * * /bin/echo 'hello'"

mock_entity_cronjob_list = [CronJob("0", "0", "*", "*", "*", "tar -zcf /var/backups/home.tgz /home/"),
                            CronJob("0", "2", "3-4", "*", "*", "tar -zcf /var/backups/home.tgz /home/")]
