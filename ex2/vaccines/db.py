from typing import List

import psycopg2

from .models import CitizenVaccinationData, PreviousConditions


def create_table_if_doest_exist():
    conn = psycopg2.connect(host="localhost", database="Vaccinations",
                            user="postgres", password="1234")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS vaccinations (
          first_name TEXT NOT NULL,
          last_name TEXT NOT NULL,
          date_of_birth TEXT NOT NULL,
          address TEXT NOT NULL,
          city TEXT NOT NULL,
          zip_code INT,
          land_line TEXT NOT NULL,
          cellular_phone TEXT NOT NULL,
          infected BOOLEAN NOT NULL,
          diabetes BOOLEAN NOT NULL,
          cardio_vascular BOOLEAN NOT NULL,
          allergies BOOLEAN NOT NULL,
          other TEXT NOT NULL
        );
    """)
    conn.commit()

    cur.close()
    conn.close()

def insert_into_db(data: CitizenVaccinationData):
    conn = psycopg2.connect(host="localhost", database="Vaccinations",
                            user="postgres", password="1234")

    cur = conn.cursor()

    cur.execute("""
    INSERT INTO vaccinations (first_name, last_name, date_of_birth, address, city, zip_code, land_line,
            cellular_phone, infected, diabetes, cardio_vascular, allergies, other)
    VALUES (%(first_name)s, %(last_name)s, %(date_of_birth)s, %(address)s, %(city)s, %(zip_code)s, %(land_line)s,
            %(cellular_phone)s, %(infected)s, %(diabetes)s, %(cardio_vascular)s, %(allergies)s, %(other)s)
    """, {
        "first_name": data.first_name,
        "last_name": data.last_name,
        "date_of_birth": data.date_of_birth,
        "address": data.address,
        "city": data.city,
        "zip_code": data.zip_code,
        "land_line": data.land_line,
        "cellular_phone": data.cellular_phone,
        "infected": data.infected,
        "diabetes": data.previous_conditions.diabetes,
        "cardio_vascular": data.previous_conditions.cardio_vascular,
        "allergies": data.previous_conditions.allergies,
        "other": data.previous_conditions.other,

    })

    conn.commit()

    cur.close()
    conn.close()


def get_data() -> List[CitizenVaccinationData]:
    citizens_data = []

    conn = psycopg2.connect(host="localhost", database="Vaccinations",
                            user="postgres", password="1234")

    cur = conn.cursor()

    cur.execute("""SELECT first_name, last_name, date_of_birth, address, city, zip_code, land_line,
        cellular_phone, infected, diabetes, cardio_vascular, allergies, other FROM vaccinations
        """)
    rows = cur.fetchall()
    for row in rows:
        citizen_data = CitizenVaccinationData(first_name=row[0], last_name=row[1], date_of_birth=row[2],
                                              address=row[3], city=row[4], zip_code=row[5], land_line=row[6],
                                              cellular_phone=row[7], infected=row[8],
                                              previous_conditions=PreviousConditions(
                                                  diabetes=row[9], cardio_vascular=row[10],
                                                  allergies=row[11], other=row[12]))
        citizens_data.append(citizen_data)

    return citizens_data
