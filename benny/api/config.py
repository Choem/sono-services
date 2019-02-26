import os

# Config class with rules that contain the key pair values
class Config:
    def __init__(self):
        # Define dictionary where all the key pair values are stored
        self._rules = dict()

        # Read file from local .env path
        local_env_path = '.env'
        self._read_file(local_env_path)        

        # Read file from shared .env path if dev is True
        shared_env_path = './../../shared/.env.development'
        if self._rules['DEVELOPMENT'] in 'True':
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
                        # Split the line with the delimiter into key value pairs and append to rules
                        pair = line.split('=')
                        self._rules[pair[0]] = pair[1]
        else:
            # How strict you want to be when finding a file
            if strict:
                raise FileNotFoundError('This file was not found %s' % path)

    @property
    def rules(self):
        return self._rules
        