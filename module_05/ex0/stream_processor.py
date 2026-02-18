from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional
from sys import stderr


class DataProcessor(ABC):
    """Abstract base class for all data processors."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the input data and return a summary string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate input data before processing."""
        pass

    def format_output(self, result: str) -> str:
        """Format the final output string."""
        return f'Output: {result}'


class NumericProcessor(DataProcessor):
    """Processor for numeric iterable data."""

    def process(self, data: Any) -> str:
        """Calculate sum and average of numeric values."""
        s = 0
        data_len: Optional[int] = len(data)
        for n in data:
            s += n
        a = s / data_len
        return f'Processed {data_len} numeric values, sum={s}, avg={a}'

    def validate(self, data: Any) -> bool:
        """Check that data is a non-empty iterable of non-negative numbers."""
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
        """Format the final output string."""
        return super().format_output(result)


class TextProcessor(DataProcessor):
    """Processor for plain text data."""

    def process(self, data: Any) -> str:
        """Count characters and words in text."""
        data_len = len(data)
        words = len(data.split(' '))
        return f'Processed text: {data_len} characters, {words} words'

    def validate(self, data: Any) -> bool:
        """Check that input is a string."""
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        """Format the final output string."""
        return super().format_output(result)


class LogProcessor(DataProcessor):
    """Processor for log entries with levels."""

    def process(self, data: Any) -> str:
        """Format log messages based on data."""
        data = data.split(' ', 1)
        if data[0] == 'ERROR:':
            return f'[ALERT] ERROR level detected: {data[1]}'
        if data[0] == 'INFO:':
            return f'[INFO] INFO level detected: {data[1]}'

    def validate(self, data: Any) -> bool:
        """Validate log format and data."""
        if not isinstance(data, str):
            return False
        if not (data.startswith('ERROR:') or data.startswith('INFO:')):
            return False
        if len(data.split(' ')) < 2:
            return False
        return True

    def format_output(self, result: str) -> str:
        """Format the final output string."""
        return super().format_output(result)


def main() -> None:

    print('=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===')

    data: Dict[str, Union[List, str]] = {
        'numeric': [1, 2, 3, 4, 5],
        'text': 'Hello Nexus World',
        'log': 'ERROR: Connection timeout'
    }
    try:
        print('\nInitializing Numeric Processor...')
        process1 = NumericProcessor()
        data_numeric = data['numeric']
        print(f'Processing data: {data_numeric}')
        if process1.validate(data_numeric):
            print('Validation: Numeric data verified')
            print(process1.format_output(process1.process(data_numeric)))
        else:
            print('Validation: Numeric data Not verified')
    except Exception:
        print('Error was caught but programme continues', file=stderr)

    try:
        print('\nInitializing Text Processor...')
        process2 = TextProcessor()
        data_text = data['text']
        print(f'Processing data: "{data_text}"')
        if process2.validate(data_text):
            print('Validation: Text data verified')
            print(process2.format_output(process2.process(data_text)))
        else:
            print('Validation: Text data Not verified')
    except Exception:
        print('Error was caught but programme continues', file=stderr)

    try:
        print('\nInitializing Log Processor...')
        process3 = LogProcessor()
        data_log = data['log']
        print(f'Processing data: "{data_log}"')
        if process3.validate(data_log):
            print('Validation: Log entry verified')
            print(process3.format_output(process3.process(data_log)))
        else:
            print('Validation: Log entry NOT verified')
    except Exception:
        print('Error was caught but programme continues', file=stderr)

    try:
        print('\n=== Polymorphic Processing Demo ===')
        print('\nProcessing multiple data types through same interface...')

        processes: Dict[str, Union[List, str]] = {
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
        print('Error was caught but programme continues', file=stderr)

    print('\nFoundation systems online. Nexus ready for advanced streams.')


if __name__ == '__main__':
    main()
