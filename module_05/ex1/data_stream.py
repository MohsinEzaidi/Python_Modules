from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union, Dict
from sys import stderr


class DataStream(ABC):
    """Abstract base class for all data stream types."""

    def __init__(self, stream_id: Optional[str],
                 stream_type: Optional[str]) -> None:
        """Initialize stream with ID and type."""

        self._stream_id = stream_id
        self._stream_type = stream_type
        self.processed_data: int = 0

    def get_stream_id(self) -> Optional[str]:
        """Return the stream ID."""
        return self._stream_id

    def set_stream_id(self, new_stream_id: Optional[str]) -> None:
        """Update the stream ID."""
        self._stream_id = new_stream_id

    def get_stream_type(self) -> Optional[str]:
        """Return the stream type."""
        return self._stream_type

    def set_stream_type(self, new_stream_type: Optional[str]) -> None:
        """Update the stream type."""
        self._stream_type = new_stream_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of raw stream data."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on stream-specific rules."""
        self.processed_data += 1
        if isinstance(self, SensorStream):
            filtered_data = []
            for item in data_batch:
                split_item = item.split(':')
                if len(split_item) != 2:
                    raise Exception(
                        'Error: data should be in this form \'key:value\'')
                try:
                    value = float(split_item[1])
                except (ValueError, TypeError):
                    raise Exception(
                        'Error: data values should be of type int or float')
                except OverflowError:
                    print('Error: Value too large. Please keep it reasonable')
                if split_item[0] != criteria:
                    continue
                filtered_data.append(value)
            return filtered_data

        elif isinstance(self, TransactionStream):
            filtered_data = [0, 0]
            for item in data_batch:
                split_item = item.split(':')
                if len(split_item) != 2:
                    raise Exception(
                        'Error: data should be in this form \'key:value\'')
                try:
                    if split_item[0] == 'buy':
                        filtered_data[1] += int(split_item[1])
                    if split_item[0] == 'sell':
                        filtered_data[0] += int(split_item[1])
                except (ValueError, TypeError):
                    raise Exception('Error: data values should be of type int')
            return filtered_data

        elif isinstance(self, EventStream):
            return [event for event in data_batch if event == criteria]

        else:
            raise Exception(
                'Error: type of the stream should be one of these '
                '[SensorStream, TransactionStream, EventStream]')

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return basic metadata about the stream."""
        return {
            'id': self.get_stream_id(),
            'type': self.get_stream_type()
        }


class SensorStream(DataStream):
    """Handles environmental sensor data."""

    def __init__(self, stream_id: Optional[str]) -> None:
        """Create a sensor stream instance."""
        super().__init__(stream_id, 'Environmental Data')

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process sensor readings batch."""
        self.processed_data += len(data_batch)
        return f'Processing sensor batch: {data_batch}'


class TransactionStream(DataStream):
    """Handles financial transaction data."""

    def __init__(self, stream_id: Optional[str]) -> None:
        """Create a transaction stream instance."""
        super().__init__(stream_id, 'Financial Data')

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process transaction operations batch."""
        return f'Processing transaction batch: {data_batch}'


class EventStream(DataStream):
    """Handles system event data."""

    def __init__(self, stream_id: Optional[str]) -> None:
        """Create an event stream instance."""
        super().__init__(stream_id, 'System Events')

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process system event batch."""
        return f'Processing event batch: {data_batch}'


class StreamProcessor:
    """Processes multiple data streams in unified manner."""

    def process_all_streams(self, streams: List[DataStream],
                            data_batches: List[List[Any]]) -> List[int]:
        """Run filtering on all streams and count errors."""
        results = [0, 0, 0]
        for stream, data in zip(streams, data_batches):
            if isinstance(stream, SensorStream):
                try:
                    stream.filter_data(data)
                    print(f'- Sensor data: {len(data)} readings processed')
                except Exception as e:
                    results[0] += 1
                    print('-', e, file=stderr)
            elif isinstance(stream, TransactionStream):
                try:
                    stream.filter_data(data)
                    print('- Transaction data: '
                          f'{len(data)} operations processed')
                except Exception as e:
                    results[1] += 1
                    print('-', e, file=stderr)
            elif isinstance(stream, EventStream):
                try:
                    stream.filter_data(data)
                    print(f'- Event data: {len(data)} events processed')
                except Exception as e:
                    results[2] += 1
                    print('-', e, file=stderr)
            else:
                raise Exception(
                    'Error: All streams should be one of these '
                    '[SensorStream, TransactionStream, EventStream]')
        return results


def main() -> None:
    """A main function to test all data streams"""
    print('=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===')

    print('\nInitializing Sensor Stream...')
    try:
        data = ['temp:22.5', 'humidity:65', 'pressure:1013']
        criteria = 'temp'
        sensor = SensorStream('SENSOR_001')
        stats = sensor.get_stats()
        print(f"Stream ID: {stats['id']}, Type: {stats['type']}")
        print(sensor.process_batch(data))
        filtered_data = sensor.filter_data(data, criteria)
        print(f"Sensor analysis: {len(data)} readings processed, avg"
              f" {criteria}: {sum(filtered_data) / len(filtered_data)}"
              f"{'°C' if criteria == 'temp' else ''}")
    except Exception as e:
        print(e, file=stderr)

    print('\nInitializing Transaction Stream...')
    try:
        data = ['buy:100', 'sell:150', 'buy:75']
        criteria = 'net flow'
        transaction = TransactionStream('TRANS_001')
        stats = transaction.get_stats()
        filtered_data = transaction.filter_data(data, criteria)
        print(f"Stream ID: {stats['id']}, Type: {stats['type']}")
        print(transaction.process_batch(data))
        units = filtered_data[1] - filtered_data[0]
        print(f'Transaction analysis: {len(data)} operations, {criteria}: '
              f'{"+" + str(units) if units > 0 else str(units)} units')
    except Exception as e:
        print(e, file=stderr)

    print('\nInitializing Event Stream...')
    try:
        data = ['login', 'error', 'logout']
        criteria = 'error'
        event = EventStream('EVENT_001')
        filtered_data = event.filter_data(data, criteria)
        print(f"Stream ID: {stats['id']}, Type: {stats['type']}")
        print(event.process_batch(data))
        print(f'Event analysis: {len(data)} events, '
              f'{len(filtered_data)} {criteria} detected')
    except Exception as e:
        print(e, file=stderr)

    print('\n=== Polymorphic Stream Processing ===')
    try:
        print('Processing mixed stream types through unified interface...\n')
        stream_processor = StreamProcessor()
        sensor = SensorStream('1')
        data1 = ['temp:22.5', 'humidity:65', 'pressure:1013']
        transaction = TransactionStream('1')
        data2 = ['buy:100', 'sell:150', 'buy:75']
        event = EventStream('1')
        data3 = ['login', 'error', 'logout']

        data_batches = [data1, data2, data3]
        streams = [sensor, transaction, event]

        print('Batch 1 Results:')
        results = stream_processor.process_all_streams(streams, data_batches)
        print('\nStream filtering active: High-priority data only')
        print(f'Filtered results: '
              f'{results[0]} critical sensor alerts, '
              f'{results[1]} large transaction, '
              f'{results[2]} event alerts')
    except Exception as e:
        print(e, file=stderr)
    print('\nAll streams processed successfully. Nexus throughput optimal.')


if __name__ == '__main__':
    main()
