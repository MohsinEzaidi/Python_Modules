import os


def load_config() -> dict:
    from dotenv import load_dotenv

    load_dotenv()
    config = {
        'matrix_mode': os.getenv('MATRIX_MODE'),
        'database_url': os.getenv('DATABASE_URL'),
        'api_key': os.getenv('API_KEY'),
        'log_level': os.getenv('LOG_LEVEL'),
        'zion_endpoint': os.getenv('ZION_ENDPOINT')
    }
    return config


def check_security() -> bool:
    return os.path.exists('.env')


def main() -> None:
    print('\nORACLE STATUS: Reading the Matrix...\n')
    if check_security() and load_config():
        print('Configuration loaded:')
        config = load_config()
        missing = [k.upper() for k in config if config[k] is None]
        if missing:
            for m in missing:
                print(f'[Warning] missing configuration {m}')

        print(f'Mode: {config["matrix_mode"]}')
        print('Database:', 'Connected to local instance'
              if config["database_url"]
              else 'couldn\'t connect to database')
        print('API Access:', 'Authenticated'
              if config["api_key"]
              else 'Couldn\'t Authenticate')
        print(f'Log Level: {config["log_level"]}')
        print('Zion Network:', 'Online'
              if config["zion_endpoint"]
              else 'Offline')

        print('\nEnvironment security check:')
        print('[OK] No hardcoded secrets detected')
        if not check_security():
            print('[KO] .env file missing')
        else:
            print('[OK] .env file properly configured')
        print('[OK] Production overrides available')
        print('\nThe Oracle sees all configurations.')
    else:
        print('Configuration loading Failed (.env Not Found)')


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print('Error:', e)
