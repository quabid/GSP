from pathlib import PurePath
from .FileValidator import exists


class File:
    def __init__(this, path):
        this.file_path = None
        return this.set_path(path)

    def set_path(this, path):
        if not exists(path):
            print("\n\tPath {} does not exist\n".format(path))
            return {
                'status': False,
                'cause': "Path {} does not exist".format(path)
            }
        else:
            this.file_path = PurePath(path)
            return {'status': True}

    def extension(this):
        return this.file_path.suffix

    def name(this):
        return this.file_path.stem

    def full_name(this):
        return this.file_path.name

    def absolute_path(this):
        return this.file_path._flavour.pathmod.abspath(this.file_path)

    def __str__(this):
        return 'File Interroragtor'


class FileManager:
    def __inti__(this):
        this.files = dict()

    def add_file(this, path):
        new_file = File(path)

        if new_file['status']:
            if new_file.full_name() in this.files or new_file.absolute_path() in this.files:
                new_file = None
                return {'status': False, 'cause': 'File {} already exists'.format(path)}

            this.files.update({'name': new_file.full_name(), 'file': new_file})
            return {'status': True}
        else:
            print('\n\tFailed to add file {}\n\tCause:\t{}'.format(
                path, new_file['cause']))
            return {'status': False, 'cause': new_file['cause']}

    def remove_file(this, name):
        if name in this.files:
            del this.files[name]
            print('\n\tFile {} successfully removed\n'.format(name))
            return {'status': True}
        else:
            print('\n\tFile {} was not found\n'.format(name))
            return {
                'status': False,
                'cause': 'file {} was not found'.format(name)
            }

    def print_files(this):
        for i, f in enumerate(this.files, start=1):
            print('{}.\t{}'.format(i, f))

    def get_files(this):
        return this.files

    def file_count(this):
        return len(this.files)

    def __str__(this):
        return 'File Manager'
