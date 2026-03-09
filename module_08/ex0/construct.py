import sys
import site
import os


def main() -> None:
    # check if we are in the environment or not
    if sys.prefix != sys.base_prefix:
        print('\nMATRIX STATUS: Welcome to the construct')

        print(f'\nCurrent Python: {sys.executable}')
        #sys.prefix gives us the full path of the used python
        #but we only wants the name of the environment
        #which is the last folder in the given path
        print(f'Virtual Environment: {os.path.basename(sys.prefix)}')
        print(f'Environment Path: {sys.prefix}')

        print('\nSUCCESS: You\'re in an isolated environment!')
        print('Safe to install packages without affecting the global system.')

        print('\nPackage installation path:')
        #site.getsitepackages() gives us a list of the site packages
        #but the one we want is the very first one in the list
        print(site.getsitepackages()[0])

    else:
        print('\nMATRIX STATUS: You\'re still plugged in')

        print(f'\nCurrent Python: {sys.executable}')
        print('Virtual Environment: None detected')

        print('\nWARNING: You\'re in the global environment!')
        print('The machines can see everything you install.')

        # Instructions to use the python environment 
        print('\nTo enter the construct, run:')
        print('python -m venv matrix_env')
        print('source matrix_env/bin/activate # On Unix')
        print('matrix_env')
        print('Scripts')
        print('activate # On Windows')

        print('\nThen run this program again.')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Error:', e)
