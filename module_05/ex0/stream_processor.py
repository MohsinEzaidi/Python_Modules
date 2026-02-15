from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f'Output: {result}'


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        s = 0
        data_len = len(data)
        for n in data:
            s += n
        a = s / data_len
        return f'Processed {data_len} numeric values, sum={s}, avg={a}'

    def validate(self, data: Any) -> bool:
        try:
            if len(data) == 0:
                return False
            for n in data:
                if int(n) < 0:
                    return False

        except (ValueError, TypeError):
            return False
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        data_len = len(data)
        words = len(data.split(' '))
        return f'Processed text: {data_len} characters, {words} words'

    def validate(self, data: Any) -> bool:
        if data.__class__.__name__ != 'str':
            return False
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        data = data.split(' ', 1)
        if data[0] == 'ERROR:':
            return f'[ALERT] ERROR level detected: {data[1]}'
        if data[0] == 'INFO:':
            return f'[INFO] INFO level detected: {data[1]}'

    def validate(self, data: Any) -> bool:
        if data.__class__.__name__ != 'str':
            return False
        if not (data.startswith('ERROR:') or data.startswith('INFO:')):
            return False
        if len(data.split(' ')) < 2:
            return False
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def main() -> None:

    print('=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===')

    try:
        print('\nInitializing Numeric Processor...')
        process1 = NumericProcessor()
        data = [1, 2, 3, 4, 5]
        print(f'Processing data: {data}')
        if process1.validate(data):
            print('Validation: Numeric data verified')
            print(process1.format_output(process1.process(data)))
        else:
            print('Validation: Numeric data Not verified')
    except Exception:
        print('Error was caught but programme continues')

    try:
        print('\nInitializing Text Processor...')
        process2 = TextProcessor()
        data = 'Hello Nexus World'
        print(f'Processing data: "{data}"')
        if process2.validate(data):
            print('Validation: Text data verified')
            print(process2.format_output(process2.process(data)))
        else:
            print('Validation: Text data Not verified')
    except Exception:
        print('Error was caught but programme continues')

    try:
        print('\nInitializing Log Processor...')
        process3 = LogProcessor()
        data = 'ERROR: Connection timeout'
        print(f'Processing data: "{data}"')
        if process3.validate(data):
            print('Validation: Log entry verified')
            print(process3.format_output(process3.process(data)))
        else:
            print('Validation: Log entry NOT verified')
    except Exception:
        print('Error was caught but programme continues')

    try:
        print('\n=== Polymorphic Processing Demo ===')
        print('\nProcessing multiple data types through same interface...')

        processes = {
            'numeric': {
                'process': NumericProcessor(), 'data': [1, 2, 3]
            },
            'text': {
                'process': TextProcessor(), 'data': 'Hello Worlds'
            },
            'log': {
                'process': LogProcessor(), 'data': 'INFO: System ready'
            }
        }

        i = 1
        for p in processes.values():
            process = p['process']
            data = p['data']
            if process.validate(data):
                print(f'Result {i}: {process.process(data)}')
            else:
                print(f'Result {i}: Data NOT verified')
            i += 1

    except Exception:
        print('Error was caught but programme continues')

    print('\nFoundation systems online. Nexus ready for advanced streams.')


if __name__ == '__main__':
    main()
