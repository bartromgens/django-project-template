import datetime
import gzip
import logging
import os
import shutil

from django.core import management
from django.conf import settings

from django_cron import CronJobBase, Schedule


logger = logging.getLogger(__name__)


class BackupDaily(CronJobBase):
    RUN_AT_TIMES = ['18:00']
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'website.cron.BackupDaily'

    def do(self):
        logger.info('run daily backup cronjob')
        try:
            management.call_command('dbbackup', '--clean')
            BackupDaily.create_json_dump()
        except Exception as e:
            logger.exception(e)
            raise

    @staticmethod
    def create_json_dump():
        filepath = os.path.join(settings.DBBACKUP_STORAGE_OPTIONS['location'], 'backup-' + str(datetime.date.today()) + '.json')
        filepath_compressed = filepath + '.gz'
        with open(filepath, 'w') as fileout:
            management.call_command(
                'dumpdata',
                '--all',
                '--natural-foreign',
                'website',
                'exampleapp',
                stdout=fileout
            )
        with open(filepath, 'rb') as f_in:
            with gzip.open(filepath_compressed, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        os.remove(filepath)
        BackupDaily.remove_old_json_dumps(days_old=30)

    @staticmethod
    def remove_old_json_dumps(days_old):
        for (dirpath, dirnames, filenames) in os.walk(settings.DBBACKUP_STORAGE_OPTIONS['location']):
            for file in filenames:
                if '.json.gz' not in file:
                    continue
                filepath = os.path.join(dirpath, file)
                datetime_created = datetime.datetime.fromtimestamp(os.path.getctime(filepath))
                if datetime_created < datetime.datetime.now() - datetime.timedelta(days=days_old):
                    os.remove(filepath)
