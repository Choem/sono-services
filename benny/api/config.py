import os

# Config class which reads the key pair values from the env
class Config:
    def __init__(self):
        # Read file from local .env path
        local_env_path = '.env'
        self._read_file(local_env_path)        

        # Read file from shared .env path if dev is True
        shared_env_path = '../../shared/.env.development'
        if os.environ.get('DEVELOPMENT') in 'True':
                self._read_file(shared_env_path, False)
        
    def _read_file(self, path, strict=True):
        # Look if the path is a file
        if os.path.isfile(path):
            # Disposable variable within scope that opens files with read perms
            with open(path, 'r') as env:
                # Lines array with each new line on a different index
                lines = [line.rstrip('\n') for line in env]
                # Loop throught lines
                for line in lines:
                    # Check if line is not empty and has a delimiter
                    if len(line) > 0 and '=' in line:
                        # Split the line with the delimiter into key value pairs and append to environ
                        pair = line.split('=')
                        os.environ[pair[0]] = pair[1]
        else:
            # How strict you want to be when finding a file
            if strict:
                raise FileNotFoundError('This file was not found {0}'.format(path))