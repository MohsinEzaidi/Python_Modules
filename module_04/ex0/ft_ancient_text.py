def ft_ancient_text(file_name: str = 'ancient_fragment.txt') -> None:
    """Read a text file and print its contents."""
    try:
        with open(file_name, 'r') as file:
            print(f'Accessing Storage Vault: {file_name}')
            print('Connection established...\n')
            print('RECOVERED DATA:')

            data = file.read()
            if data == '':
                print(f'The file \'{file_name}\' has NO DATA in it')
            else:
                print(data)
            print('\nData recovery complete. Storage unit disconnected.')
    except FileNotFoundError:
        print('ERROR: Storage vault not found. Run data generator first.')
    except PermissionError as e:
        print('ERROR: You dont have the right'
              f' permissions for the file \'{e.filename}\'')


if __name__ == '__main__':
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    try:
        ft_ancient_text()
    except Exception as e:
        print(f'ERROR: {e}')
