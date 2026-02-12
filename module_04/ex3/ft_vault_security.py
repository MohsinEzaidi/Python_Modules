def ft_vault_security(file1: str = 'classified_data.txt',
                      file2: str = 'security_protocols.txt') -> None:
    """
    Access a secure vault by reading classified data and
    writing new security protocols, then display both files.
    """
    try:
        with open(file2, 'w') as f2:
            f2.write('[CLASSIFIED] New security protocols archived')

        print('Initiating secure vault access...')

        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            print('Vault connection established with failsafe protocols')
            print('\nSECURE EXTRACTION:')
            print(f1.read())

            print('\nSECURE PRESERVATION:')
            print(f2.read())

        print('Vault automatically sealed upon completion\n')
        print('All vault operations completed with maximum security.')
    except FileNotFoundError as e:
        print(f'ERROR: The file {e.filename} '
              'does not exist in this diractory')
    except PermissionError as e:
        print('ERROR: You don\'t have the'
              f' right permissions for file \'{e.filename}\'')


if __name__ == '__main__':
    try:
        print('=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n')
        ft_vault_security()
    except Exception as e:
        print(f'ERROR: {e}')
