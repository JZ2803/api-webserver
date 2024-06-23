from datetime import date
from init import app, db, bcrypt
from flask import Blueprint
from models.activity import Activity
from models.activity_type import ActivityType
from models.comment import Comment
from models.customer import Customer
from models.enrolment import Enrolment
from models.plant import Plant
from models.species import Species
from models.species_type import SpeciesType
from models.user import User

db_commands = Blueprint('db', __name__)

@db_commands.cli.command("create")
def db_create():
    db.create_all()
    print("Created tables")

@db_commands.cli.command("seed")
def db_seed():
    species_types = [
        SpeciesType(
            name="Tree"
        ),
        SpeciesType(
            name="Succulent"
        ),
        SpeciesType(
            name="Cactus"
        ),
        SpeciesType(
            name="Foliage plant"
        ),
        SpeciesType(
            name="Flowering plant"
        )
    ]
    db.session.add_all(species_types)
    db.session.commit()

    species = [
        Species(
            name="Fiddle-leaf fig",
            species_type=species_types[0]
        ),
        Species(
            name="Bear's paw",
            species_type=species_types[1]
        ),
        Species(
            name="Prickly pear",
            species_type=species_types[2]
        ),
        Species(
            name="Devil's ivy",
            species_type=species_types[3]
        ),
        Species(
            name="Peace lily",
            species_type=species_types[4]
        )
    ]
    db.session.add_all(species)

    customers = [
        Customer(
            first_name="Alice",
            last_name="Jones",
            email="aj5678@email.com",
            phone_no="0404123123"
        ),
        Customer(
            first_name="Janet",
            last_name="Brown",
            email="janbrown@email.com",
            phone_no="0404987888"
        ),
        Customer(
            first_name="Barry",
            last_name="White",
            email="b_white23@email.com",
            phone_no="0498345873"
        ),
        Customer(
            first_name="William",
            last_name="Digg",
            email="wdigg1@email.com",
            phone_no="0491324756"
        ),
        Customer(
            first_name="Sam",
            last_name="Lee",
            email="sam.lee@email.com",
            phone_no="0413763495"
        ),
        Customer(
            first_name="Rebecca",
            last_name="Gregson",
            email="bec_g1@email.com",
            phone_no="0464873651"
        )
    ]
    db.session.add_all(customers)
    db.session.commit()

    plants = [
        Plant(
            species=species[0],
            customer=customers[0]
        ),
        Plant(
            species=species[0],
            customer=customers[1]
        ),
        Plant(
            species=species[1],
            customer=customers[2]
        ),
        Plant(
            species=species[2],
            customer=customers[3]
        ),
        Plant(
            species=species[3],
            customer=customers[4]
        ),
        Plant(
            species=species[4],
            customer=customers[5]
        )
    ]
    db.session.add_all(plants)
    db.session.commit()

    enrolments = [
        Enrolment(
            start_date=date(2023, 9, 9),
            end_date=date(2023, 12, 1),
            plant=plants[0]
        ),
        Enrolment(
            start_date=date(2024,5, 23),
            end_date=date(2024, 5, 20),
            plant=plants[1]
        ),
        Enrolment(
            start_date=date(2023, 12, 3),
            end_date=date(2023, 12, 30),
            plant=plants[2]
        ),
        Enrolment(
            start_date=date(2023, 12, 18),
            end_date=date(2023, 12, 24),
            plant=plants[3]
        ),
        Enrolment(
            start_date=date(2024, 1, 15),
            end_date=date(2024, 2, 18),
            plant=plants[3]
        ),
        Enrolment(
            start_date=date(2024, 4, 29),
            end_date=date(2024, 6, 4),
            plant=plants[3]
        ),
        Enrolment(
            start_date=date(2024, 2, 3),
            end_date=date(2024, 2, 28),
            plant=plants[4]
        ),
        Enrolment(
            start_date=date(2024, 5, 21),
            end_date=date(2024, 6, 3),
            plant=plants[5]
        )
    ]
    db.session.add_all(enrolments)

    users = [
        User(
            email="flora.wilson@plantdaycare.com",
            password=bcrypt.generate_password_hash("purpleelephant45").decode('utf8'),
            is_admin=False
        ),
        User(
            email="daisy.mcdonald@plantdaycare.com",
            password=bcrypt.generate_password_hash("blueclouds99").decode('utf8'),
            is_admin=False
        ),
        User(
            email="basil.ericson@plantdaycare.com",
            password=bcrypt.generate_password_hash("bentumbrella81").decode('utf8'),
            is_admin=True
        )
    ]
    db.session.add_all(users)
    db.session.commit()

    comments = [
        Comment(
            text="Test comment 1",
            date_created=date.today(),
            enrolment=enrolments[3],
            user=users[1]
        )
    ]
    db.session.add_all(comments)

    activity_types = [
        ActivityType(
            name="Water"
        ),
        ActivityType(
            name="Fertilise"
        ),
        ActivityType(
            name="Prune"
        )
    ]
    db.session.add_all(activity_types)
    db.session.commit()

    activities = [
        Activity(
            date_performed=date.today(),
            activity_type=activity_types[1],
            enrolment=enrolments[1]
        )
    ]
    db.session.add_all(activities)
    db.session.commit()

    print("Seeded database")

@db_commands.cli.command("drop")
def db_drop():
    db.drop_all()
    print("Dropped tables")