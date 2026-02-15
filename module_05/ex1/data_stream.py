from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union, Dict


class DataStream(ABC):

    def __init__(self, stream_id: Optional[str], stream_type: Optional[str]) -> None:
        self._stream_id = stream_id
        self._stream_type = stream_type
        self.processed_data = 0

    def get_stream_id(self) -> Optional[str]:
        return self._stream_id
    
    def set_stream_id(self, new_stream_id: Optional[str]) -> None:
        self._stream_id = new_stream_id
    
    def get_stream_type(self) -> Optional[str]:
        return self._stream_type

    def set_stream_type(self, new_stream_type: Optional[str]) -> None:
        self._stream_type = new_stream_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria == None:
            return []

        if isinstance(self, SensorStream):
            filtered_data = []
            for item in data_batch:
                split_item = item.split(':')
                if len(split_item) != 2:
                    raise Exception('Error: data should be in this form \'key:value\'')
                try:
                    value = float(split_item[1])
                except (ValueError, TypeError):
                    raise Exception('Error: data values should be of type int or float')
                if split_item[0] != criteria:
                    continue
                filtered_data.append(value)
            return filtered_data




        elif isinstance(self, TransactionStream):
            pass
        elif isinstance(self, EventStream):
            pass
        else:
            raise Exception('Error: type of the stream should be one of these [SensorStream, TransactionStream, EventStream]')

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return{
            'id': self.get_stream_id(),
            'type': self.get_stream_type(),
            ''
        }


class SensorStream(DataStream):

    sensor_counter = 0
    def __init__(self, stream_id: Optional[str]):
        super().__init__(stream_id, 'Environmental Data')
        SensorStream.sensor_counter += 1

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_data = len(data_batch)
        return f'Processing sensor batch: {data_batch}'


class TransactionStream(DataStream):

    transaction_counter = 0
    def __init__(self, stream_id: Optional[str]):
        super().__init__(stream_id, 'Financial Data')
        TransactionStream.transaction_counter += 1

    def process_batch(self, data_batch: List[Any]) -> str:
        return f'Processing transaction batch: {data_batch}'


class EventStream(DataStream):

    event_counter = 0
    def __init__(self, stream_id: Optional[str]):
        super().__init__(stream_id, 'System Events')
        EventStream.event_counter += 1

    def process_batch(self, data_batch: List[Any]) -> str:
        return f'Processing event batch: {data_batch}'


class StreamProcessor:
    pass


def main() -> None:
    print('=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===')

    print('\nInitializing Sensor Stream...')
    try:
        data = ['temp:22.5', 'humidity:65', 'pressure:1013']
        x = SensorStream('SENSOR_001')
        print(f'Stream ID: {x.get_stream_id()}, Type: {x.get_stream_type()}')
        print(x.process_batch(data))
        print(x.filter_data(data, 'temp'))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()