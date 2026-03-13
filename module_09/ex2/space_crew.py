from enum import Enum
from pydantic import BaseModel, ValidationError, Field, model_validator
from datetime import datetime


class Rank(Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(default_factory=datetime.now)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation_rules(self):
        if not self.mission_id.startswith('M'):
            raise ValueError('Mission ID must start with "M"')

        has_leader = any(
            [m.rank in [Rank.CAPTAIN, Rank.COMMANDER] for m in self.crew])
        if not has_leader:
            raise ValueError('Must have at least one Commander or Captain')

        if self.duration_days > 365:
            xp_members = [m for m in self.crew if m.years_experience >= 5]
            if len(xp_members) < len(self.crew) / 2:
                raise ValueError('Long missions (> 365 days) need 50%'
                                 'experienced crew (5+ years)')

        for member in self.crew:
            if not member.is_active:
                raise ValueError('All crew members must be active')

        return self


def main() -> None:
    try:
        member1 = CrewMember(
            member_id='CM001',
            name='Sarah Connor',
            rank=Rank.COMMANDER,
            age=32,
            specialization='Mission Command',
            years_experience=10
        )
        member2 = CrewMember(
            member_id='CM002',
            name='John Smith',
            rank=Rank.LIEUTENANT,
            age=40,
            specialization='Navigation',
            years_experience=15
        )
        member3 = CrewMember(
            member_id='CM003',
            name='Ali',
            rank=Rank.OFFICER,
            age=22,
            specialization='Engineering',
            years_experience=2
        )

        mission = SpaceMission(
            mission_id='M2024_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            duration_days=900,
            crew=[member1, member2, member3],
            budget_millions=2500.0
        )

        print('Space Mission Crew Validation')
        print('=========================================')
        print('Valid mission created:')
        print(f'Mission: {mission.mission_name}')
        print(f'ID: {mission.mission_id}')
        print(f'Destination: {mission.destination}')
        print(f'Duration: {mission.duration_days} days')
        print(f'Budget: ${mission.budget_millions}M')
        print(f'Crew size: {len(mission.crew)}')
        print('Crew members:')
        for member in mission.crew:
            print(f'- {member.name} ({member.rank.value}) '
                  f'- {member.specialization}')

        print('\n=========================================')
    except ValidationError as e:
        print('Expected validation error:')
        print(e.errors()[0]['msg'].replace('Value error, ', ''))
    except Exception as e:
        print('Error:', e)

    try:
        member1 = CrewMember(
            member_id='CM001',
            name='Sarah Connor',
            rank=Rank.OFFICER,
            age=32,
            specialization='Mission Officer',
            years_experience=10
        )
        member2 = CrewMember(
            member_id='CM002',
            name='John Smith',
            rank=Rank.LIEUTENANT,
            age=40,
            specialization='Navigation',
            years_experience=15
        )
        member3 = CrewMember(
            member_id='CM003',
            name='Ali',
            rank=Rank.CADET,
            age=22,
            specialization='Engineering',
            years_experience=2
        )

        mission = SpaceMission(
            mission_id='M2024_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            duration_days=900,
            crew=[member1, member2, member3],
            budget_millions=2500.0
        )

        print('\nSpace Mission Crew Validation')
        print('=========================================')
        print('Valid mission created:')
        print(f'Mission: {mission.mission_name}')
        print(f'ID: {mission.mission_id}')
        print(f'Destination: {mission.destination}')
        print(f'Duration: {mission.duration_days} days')
        print(f'Budget: ${mission.budget_millions}M')
        print(f'Crew size: {len(mission.crew)}')
        print('Crew members:')
        for member in mission.crew:
            print(f'- {member.name} ({member.rank.value}) '
                  f'- {member.specialization}')

        print('\n=========================================')
    except ValidationError as e:
        print('Expected validation error:')
        print(e.errors()[0]['msg'].replace('Value error, ', ''))
    except Exception as e:
        print('Error:', e)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Error:', e)
