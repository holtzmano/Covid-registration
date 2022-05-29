from dataclasses import dataclass

from django.db import models

@dataclass
class PreviousConditions:
    diabetes: bool
    cardio_vascular: bool
    allergies: bool
    other: str


@dataclass
class CitizenVaccinationData:
    first_name: str
    last_name: str
    date_of_birth: str
    address: str
    city: str
    zip_code: int
    land_line: str
    cellular_phone: str
    infected: bool
    previous_conditions: PreviousConditions