import re
from subprocess import run

def bump_version(version, level='patch'):
    major, minor, patch = map(int, version.split('.'))
    if level == 'major':
        major += 1
        minor = 0
        patch = 0
    elif level == 'minor':
        minor += 1
        patch = 0
    else:
        patch += 1
    return f"{major}.{minor}.{patch}"

def update_version_in_file(new_version):
    with open('version.py', 'r+') as f:
        content = f.read()
        f.seek(0)
        f.write(re.sub(r'(?<=VERSION = \')\d+\.\d+\.\d+', new_version, content))
        f.truncate()

def create_git_tag(version):
    run(['git', 'add', 'version.py'])
    run(['git', 'commit', '-m', f'Bump version to {version}'])
    run(['git', 'tag', version])
    run(['git', 'push', '--tags'])

if __name__ == '__main__':
    # Specify the version level: 'major', 'minor', or 'patch'
    version_level = 'patch'

    with open('version.py', 'r') as f:
        current_version = re.search(r"(?<=VERSION = ')\d+\.\d+\.\d+", f.read()).group()

    new_version = bump_version(current_version, level=version_level)
    update_version_in_file(new_version)
    create_git_tag(new_version)
