import os
import traceback
import platform
from pathlib import Path
from datetime import datetime


def local_environment():
	"""
	This function will look for `local.ini` file in project root dir to determine if
	the project resides in local env of developers, if not certain features will work as is.

	Note: empty `local.ini` will suffice
	"""
	try:
		proj_root_dir = Path(__file__).parent.parent
		local_file = os.path.join(proj_root_dir, 'local.ini')
		
		if os.path.exists(local_file):
			return True
	
	except Exception as err:
		traceback.print_exc()
		raise err
	
	return


def log_location(log_name, custom_log_path=None):
	"""
	This function makes logging platform neutral
	@TODO :param: custom_log_path value should fetch value from .local
	file soon
	"""
	start = datetime.now()
	log_path = None
	log_date = start.strftime("%Y_%m_%d_%H_%M_%S")
	log_file = log_name + f"_{log_date}.log"
	
	if local_environment():
		if fingerprint_platform() == "Windows":
			log_path = str(Path(__file__).parent.parent) + f"\\{log_file}"
		else:
			log_path = str(Path(__file__).parent.parent) + f"/{log_file}"
	else:
		if fingerprint_platform() == "Windows":
			log_path = f"D:\\PYWS\\log_files\\{log_name}\\{log_file}"
		else:
			log_path = f"/opt/regency/log/{log_name}/{log_file}"
	
	return log_path


def fingerprint_platform():
	os_location = platform.system()
	
	return os_location