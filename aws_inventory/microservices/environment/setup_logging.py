import os
import logging


class Logger:
	def __init__(self, *args):
		self.start = args[0]
		self.log_file = args[1]

	def conf_logger(self):
		if os.path.isabs(self.log_file):
			os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
			
		logging.basicConfig(
			filename=self.log_file,
			level=logging.INFO,
			format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
			datefmt='%Y-%m-%d %H:%m:%S',
		)
		logger = logging.getLogger()
		logging.getLogger('boto3').setLevel(logging.WARNING)
		logging.getLogger('botocore').setLevel(logging.WARNING)
		logger.info('Starting Regency logger %s', self.start)
		
		return logger
