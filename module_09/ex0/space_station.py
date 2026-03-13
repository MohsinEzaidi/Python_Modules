from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(default_factory=datetime.now)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    try:
        space_station = SpaceStation(
            station_id='ISS001',
            name='International Space Station',
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            is_operational=True,
            notes=None
        )

        print('Space Station Data Validation')
        print('========================================')
        print('Valid station created:')
        print(f'ID: {space_station.station_id}')
        print(f'Name: {space_station.name}')
        print(f'Crew: {space_station.crew_size} '
              f'{"people" if space_station.crew_size > 1 else "person"}')
        print(f'Power: {space_station.power_level}%')
        print(f'Oxygen: {space_station.oxygen_level}%')
        print('Status: '
              f'{"" if space_station.is_operational else "Not "}Operational')

        print('\n========================================')
    except ValidationError as e:
        print('Expected validation error:')
        print(e.errors()[0]['msg'])
    except Exception as e:
        print('Error:', e)

    try:
        space_station = SpaceStation(
            station_id='ISS002',
            name='International Space Station',
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            is_operational=True,
            notes=None
        )

        print('\nSpace Station Data Validation')
        print('========================================')
        print('Valid station created:')
        print(f'ID: {space_station.station_id}')
        print(f'Name: {space_station.name}')
        print(f'Crew: {space_station.crew_size} '
              f'{"people" if space_station.crew_size > 1 else "person"}')
        print(f'Power: {space_station.power_level}%')
        print(f'Oxygen: {space_station.oxygen_level}%')
        print('Status: '
              f'{"" if space_station.is_operational else "Not "}Operational')

        print('\n========================================')
    except ValidationError as e:
        print('Expected validation error:')
        print(e.errors()[0]['msg'])
    except Exception as e:
        print('Error:', e)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Error:', e)
