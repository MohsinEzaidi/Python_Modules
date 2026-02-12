import sys


def ft_stream_management() -> None:
    """
    Collect user input and demonstrate communication
    through standard output and error streams.
    """
    archivist_id = input('Input Stream active. Enter archivist ID: ')
    report = input('Input Stream active. Enter status report: ')

    print('\n[STANDARD] Archive status from '
          f'{archivist_id}: {report}', file=sys.stdout)
    print('[ALERT] System diagnostic: Communication '
          'channels verified', file=sys.stderr)
    print('[STANDARD] Data transmission complete\n', file=sys.stdout)

    print('Three-channel communication test successful.')


if __name__ == '__main__':
    try:
        print('=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n')
        ft_stream_management()
    except EOFError:
        print('\nEOFError: please enter the inputs correctly,'
              ' don\'t click (control + D)')
    except KeyboardInterrupt:
        print('\nKeyboardInterrupt: please enter the inputs correctly,'
              ' don\'t click (control + C) before the end of the program')
    except Exception as e:
        print(f'ERROR: {e}')
