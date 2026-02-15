def ft_crisis_response(file_name: str) -> None:
    """
    Attempt to read a file and handle potential access or missing file errors,
    simulating a crisis response scenario.
    """
    try:
        with open(file_name, 'r') as file:
            print(f'SUCCESS: Archive recovered - ``{file.read()}''')
            print('STATUS: Normal operations resumed\n')

    except PermissionError:
        print('RESPONSE: Security protocols deny access')
        print('STATUS: Crisis handled, security maintained\n')

    except FileNotFoundError:
        print('RESPONSE: Archive not found in storage matrix')
        print('STATUS: Crisis handled, system stable\n')

    except Exception:
        print('An Error happened but the programe continues')


if __name__ == '__main__':
    try:
        print('=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n')
        print('CRISIS ALERT: Attempting access to \'lost_archive.txt\'...')
        ft_crisis_response('lost_archive.txt')

        print('CRISIS ALERT: Attempting access to '
              ' \'classified_vault.txt\'...')
        ft_crisis_response('classified_vault.txt')

        print('ROUTINE ACCESS: Attempting access to'
              ' \'standard_archive.txt\'...')
        ft_crisis_response('standard_archive.txt')

        print('All crisis scenarios handled successfully. Archives secure.')
    except Exception as e:
        print('ERROR: ', e)
