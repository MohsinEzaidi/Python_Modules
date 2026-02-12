def ft_archive_creation(file_name: str = 'ew_discovery.txt') -> None:
    """
    Open a text file, write archive entries to it,
    then display its contents.
    """
    try:
        with open(file_name, 'w') as file:
            print(f'Initializing new storage unit: {file.name}')
            print('Storage unit created successfully...\n')
            print('Inscribing preservation data...')

            file.write('[ENTRY 001] New quantum algorithm discovered\n'
                       '[ENTRY 002] Efficiency increased by 347%\n'
                       '[ENTRY 003] Archived by Data Archivist trainee\n')

        with open(file_name, 'r') as read_file:
            print(read_file.read())

        print('Data inscription complete. Storage unit sealed.')
        print(f'Archive \'{file.name}\' ready for long-term preservation.')

    except PermissionError as e:
        print('ERROR: You dont have the'
              f' right permissions for file \'{e.filename}\'')


if __name__ == '__main__':
    print('=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n')
    try:
        ft_archive_creation()
    except Exception as e:
        print(f'ERROR: {e}')
