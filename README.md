# T2A2: API Webserver - Plant Daycare Management

Code and comments have been written with reference to [PEP 8 – Style Guide](https://peps.python.org/pep-0008/).

## Table of contents

[R1. Explain the problem that this app will solve, and explain how this app solves or addresses the problem](#r1)

[R2. Describe the way tasks are allocated and tracked in your project](#r2)

[R3. List and explain the third-party services, packages and dependencies used in this app](#r3)

[R4. Explain the benefits and drawbacks of this app’s underlying database system](#r4)
	
[R5. Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app](#r5)

[R6. Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design. This should focus on the database design BEFORE coding has begun, eg. during the project planning or design phase.](#r6)

[R7. Explain the implemented models and their relationships, including how the relationships aid the database implementation. This should focus on the database implementation AFTER coding has begun, eg. during the project development phase.](#r7)

[R8. Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint: HTTP verb, Path or route, Any required body or header data, Response](#r8)

## R1. Explain the problem that this app will solve, and explain how this app solves or addresses the problem. <a id="r1"></a>

This API webserver app is a tracking and management tool for a plant day-care, a small business that provides care for plants during periods where their owners are unable to attend to them, for example, when going on holidays. As with most day-care businesses, there are a number of challenges and complexities involved in managing a plant day-care efficiently:

- <u>Administrative burden</u>: Tasks such as managing enrolments, tracking activities, and maintaining customer and staff details, are often the largest contributors to the administrative burden of running a day-care business (Spicer, 2020). These tasks are not value-adding and in order to operate efficiently, the day-care needs infrastructure to help minimise the amount of manual effort required to perform them, allowing staff to focus on more important tasks.
- <u>Communication gaps & transfer of information amongst staff</u>: At any point in time, the day-care will have a large number of plants in its care. With a constantly rotating roster of staff looking after the plants, it is easy for gaps in communication to form, and this could result in inefficient operation and costly consequences for the business. As such, it’s important that there is a platform for staff members to share information about the plants in care with each other (Murray, 2021).
- <u>Security and authorised management of records</u>:  Unauthorised access to records is a security concern in any system that stores customer information. This refers to situations where individuals gain access to data or resources without proper authorisation, which could lead to data leaks or unauthorised changes to data.
To address these problems, the app will provide the following functionalities:
- Staff can <u>store, access, update and delete information</u> on customers, plants, and enrolments:
    - Customers (including details such as name, email, phone number, plants belonging to them)
    - Plants (including details such as specie name and type, and enrolments)
    - Enrolments (including details such as start date, end date, activities performed during the enrolment)
- <u>Activities can be added to enrolment records</u>, allowing staff members to keep a track of what care activities have been performed for each, e.g. watering, fertilising, etc., and when these activities were performed. This allows the day-care to maintain a log of all activities performed throughout the day or for each specific plant throughout the duration of their enrolment.
- <u>Comments can be added to enrolment records</u>, allowing for a place to retain remarks about each plant and providing a platform for staff to share noteworthy information with each other. For example, if a staff member has watered a plant today and noticed some signs of a pest infestation, they can leave a comment on its enrolment record saying, “Noticed early signs of pest infestation whilst watering”. This way, all staff members can be informed of and have access to this information as they can simply search up the enrolment record for this plant in the database and the comment will show up.
- <u>Proper authorisation controls</u>, where only staff with administrator privileges can perform certain tasks such as changing account passwords, or deleting certain records. This ensures that actions can only be performed by authorised personnel.

## R2. Describe the way tasks are allocated and tracked in your project. <a id="r2"></a>

### Trello

Trello was the main tool utilised to help allocate and track tasks throughout the duration of the project. Before beginning the project, a Trello board was created to map out all the significant items/areas that would need to be considered in the project, each of which has their own card. 

![Trello board](/docs/trello-board.png)

To help make the board visually easier to process, the cards are bucketed into which project phase they fall into (e.g. planning, development, etc.) and the cards are prefixed with the respective phase. Each card itself contains a checklist of items representing the tasks that need to be completed and a due date by when all the tasks need to be completed, determined through initial assessment of time required for the tasks. 

![Trello card](/docs/trello-card.png)

### Project phases

A considerable amount of time was allocated to the planning phase at the beginning. This was necessary to ensure that all of the requirements for the project were taken into consideration and addressed by the features and functionalities of the resulting app. This phase of the project comprised of the following items (cards):

- Establishing the app idea and solution to the problem statement
- Establishing the entities and their relationships
- App features and functionalities scoping

Project planning tasks were followed by items relating to development of the app, for example:

- Flask app & database setup
- Creating models & schemas
- Implementing user authentication and JWT

Finally, this is followed by finalisation tasks including:

- Finalisation of GitHub repo
- Finalisation of README documentation

### Daily tracking & continued evaluation

Throughout the duration of the project, a daily assessment was performed at the end of the day to reflect on what tasks were completed and what issues were encountered, similar to a daily stand-up. Taking these things into consideration, due dates and timelines for outstanding tasks can be adjusted or reprioritised as necessary, and tasks for the next day are planned out. This daily tracking and continued evaluation ensures that any issues or roadblocks can be identified and handled efficiently and effectively, and any new opportunities can be identified and explored in a timely manner.

## R3. List and explain the third-party services, packages and dependencies used in this app. <a id="r3"></a>

The main third-party services, packages and dependencies used by the app are:

- <u>Flask</u>: The web framework utilised to build the plant day-care API webserver app. It is a lightweight, simple and flexible framework that allows easy routing and view functions, built in JSON data handling (serialising/deserialising), good integration with SQL databases through ORM libraries such as SQLAlchemy, and testing and debugging capabilities. It is a micro-framework written in Python that provides the essentials required for building web apps without imposing the use of specific tools or libraries (Deery, 2023), making it ideal for building an API webserver app where there might be specific requirements for data handling, authentication and so on.
- <u>SQLAlchemy & psycopg2</u>: Given the app is written in Python and uses PostgreSQL for its database, an object relational mapper (ORM) is required to allow interaction with the database through Python objects. SQLAlchemy is the ORM that has been used for this app, as it provides the necessary object-relational mapping capabilities (explained in more detail in R5) and supports integration with Flask.
psycopg2 is a database adapter that provides an interface for connecting to PostgreSQL databases, allowing Python apps to execute SQL queries, and offering functionalities such as managing database connections manually, connection pooling and parameterised queries. 
Ultimately, SQLAlchemy and psycopg2 work synergistically to simplify database setup, management and operations and allow for direct query execution (Abdullah, 2022). 
- <u>Marshmallow</u>: A library for object serialization and deserialization. Its functionalities include conversion of complex Python objects (e.g. instances of classes or dictionaries) into JSON-compatible data and vice versa, data validation through the use of schemas to specify structure and constraints, nested data handling and integration with web frameworks such as Flask (Bry, 2023). These capabilities are integral to the app as they help provide clear structure for defining data schemas, which help to maintain data integrity when performing database operations.
- <u>Flask JWT Extended</u>: A Flask extension that provides support for JSON Web Token (JWT) features. These tokens are a compact URL-safe means of representing claims to be transferred between two parties, signed using a secret key. The extension allows for the creation and encoding of JWTs, which is useful when generating tokens that contain user information, and JWT decoding and verification. It is quite customizable, allowing for modification of various aspects of JWTs such as token expiration times and secret keys for signing tokens. It meshes seamlessly with Flask’s request/response cycle, and has been utilised to protect routes/endpoints in the app by requiring a JWT, and overall simplifies authentication and authorisation processes.
- <u>Bcrypt</u>: A password hashing function based on the Blowfish cipher. It incorporates salting, which adds additional random data to a password, before hashing it using an adaptive hashing algorithm (Arias, 2021). Bcrpyt has been utilised in the app to hash user passwords before storing them in the database, as well as hashing user input password to check against the hashed password stored in the databased.
- <u>Python dotenv</u>: allows management of environment variables from an .env file. Environment variables are typically used to store configuration settings, API keys, database credentials and other sensitive information that should not be hard-coded into the source code. In the app, environment variables such as the SQLAlchemy database URI and JWT secret key have been stored in a .env file, separating the configuration from the code which makes changing configurations easier and enhancing security.

## R4. Explain the benefits and drawbacks of this app’s underlying database system. <a id="r4"></a>

This app utilises PostgreSQL for its database system. First developed in the late 1980s, it has since developed into one of the most established relational database management systems (RDBMS) available (Burdiuzha, 2023). As with any database system, it has its advantages and disadvantages, and so it is essential to consider the specific requirements of the project to weigh these against in order to make an informed decision on utilising PostgreSQL as the database system of choice for the app.

Some of its benefits include:

- <u>Open-source license & community support:</u> Being open-source, PostgreSQL carries no licensing cost and is free to use, modify and implement as seen fit, making it highly accessible to users ranging from individual developers to large enterprises (Dhruv, 2024). Additionally, it has a large community of active users, developers and contributors that support its continuous improvement and development. This open-source nature ensures that PostgreSQL remains reliable, secure and up-to-date whilst encouraging collaboration and innovation and support within the community.
- <u>Rich features & extensibility</u>: PostgreSQL supports a wide range of data types, including JSON, XML, arrays and user-defined types, making it convenient to model complex data structures. It possesses “robust feature sets including tablespaces, asynchronous replication, nested transactions, online/hot backups, and a refined query planner/optimizer” (Amazon Web Services, 2024), and its open-source community offers a vast ecosystem of extensions which offer multitude of additional capabilities including full-text search, geographic information systems (GIS) and advanced analytics. This extensible nature makes PostgreSQL highly adaptable, allowing developers to customised it to fit specific app requirements.
- <u>Data integrity & reliability</u>: Being ACID-compliant, PostgreSQL has high fault-tolerance. ACID refers to atomicity, consistency, isolation and durability, principles that enable reliable transaction processing. ACID compliance is achieved in PostgreSQL through features such as write-ahead logging, multi-version concurrency control (MVCC) and point-in-time recovery. Essentially, it ensures that transactions are executed reliably and the data in the database is accurate, even in the case of a system failure, safeguarding the integrity of the data.

On the other hand, some drawbacks are:

- <u>Large efforts required for performance optimisation</u>: Because of its feature-rich nature and its prioritisation of compatibility (Nguyen, 2024), PostgreSQL can require comparatively more effort and higher skill-level to set up and tune for optimal performance. Activities such as configuring various parameters and understanding complex features like query optimisation have a steep learning curve and may prove challenging for users with little database administration experience.
- <u>Speed</u>: As PostgreSQL is meant for complex queries, it is often slower than other database systems when it comes to executing simple queries. When handling large datasets, complicated queries and read-write operations, PostgreSQL is very efficient, however when it comes to simpler read-only commands, there are other databases that are designed for high-volume data operations, such as MySQL, which perform quicker (Shopsense Retail Technologies, 2024).
- <u>Steep learning curve</u>: With its offering of advanced features and SQL capabilities, PostgreSQL comes with a steep learning curve. In comparison to other database systems such as MySQL, PostgreSQL may involve a more complex infrastructure setup and troubleshooting experience and requires a deep understanding of its architecture, transaction management and performance optimisation procedures to fully master.

## R5. Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app. <a id="r5"></a>

This app utilises SQLAlchemy for its object-relational mapper (ORM) capabilities. As previously mentioned, an ORM translates between the data representations used by databases and those used in object-oriented programming (Ellingwood, 2024). SQLAlchemy does just this, “simplifying the connection between Python and SQL databases by automatically converting Python class calls into SQL statements, making it possible to query relational databases in a Pythonic way” (DataScientest, 2023).

Some of the features and functionalities of SQLAlchemy ORM include:

- <u>Establishing database connection</u>: In order to interact with the PostgreSQL database, a connection needs to be established first. Below is how SQLAlchemy is used to initialise the database connection in a Flask app:

    ```
    from flask import Flask

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = ‘postgresql+psycopg2://plant_admin:plant123@localhost:5432/plant_daycare'
    ```

- <u>Defining database models</u>: Database tables and relationships can be defined using Python classes. Each class represents a table in the database and instances of the class represent rows in the tables. Below is an example of defining the Plant model, which includes declaring the primary key, foreign keys and establishing the relationships with other tables.

    ```
    from sqlalchemy import ForeignKey
    from sqlalchemy.orm import Mapped, mapped_column, relationship
    from typing import List
    
    class Plant(db.Model):
    __tablename__ = 'plants'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    specie_id: Mapped[int] = mapped_column(ForeignKey('species.id'))
    specie: Mapped['Specie'] = relationship(back_populates='plants')
    
    customer_id: Mapped[int] = mapped_column(ForeignKey('customers.id'))
    customer: Mapped['Customer'] = relationship(back_populates='plants')
    
    enrolments: Mapped[List['Enrolment']] = relationship(back_populates='plant', cascade='all, delete')
    ```

    Here, the `Plant` class maps to a `plants table`. `id` is the primary key and `specie_id` and `customer_id` are foreign keys and they are all columns in the table. `specie`, `customer` and `enrolments` defines the relationship between classes.
    
- <u>Performing CRUD operations</u>: Create, read, update and delete operations can be performed on the database with use of the SQLAlchemy models and sessions. Below are examples concerning the `plants` table:

    Read operation:

    ```
    @plants_bp.route("/", methods=['GET'])
    def get_all_plants():
        stmt = db.select(Plant)
        plants = db.session.scalars(stmt).all()
        return PlantSchema(many=True).dump(plants)
    ```

    An SQLAlchemy statement to select all ```Plant``` objects (records from the ```plants``` table) from the database is created. The statement is executed and the ```.all()``` method returns the results as a list. The result is serialized into JSON format using the marshmallow schema ```PlantSchema```.

    Create operation:

    ```
    @plants_bp.route("/", methods=['POST'])
    def create_plant():
        plant_info = PlantSchema(only=['specie_id', 'customer_id']).load(request.json, unknown='exclude')
        plant = Plant(
            specie_id=plant_info['specie_id'],
            customer_id=plant_info['customer_id']
        )
    db.session.add(plant)
    db.session.commit()
    return PlantSchema().dump(plant), 201
    ```
    With the help of a marshmallow schema, the JSON data is loaded from the request body. A new `Plant` object is created with this information. The newly created `Plant` object is then added to the database session and then committed, which saves the changes to the database. A JSON response is returned, containing details of the newly created `Plant` record.

## R6. Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design. This should focus on the database design BEFORE coding has begun, e.g. during the project planning or design phase. <a id="r6"></a>

![Play daycare ERD](/docs/plant-daycare-ERD.png)

The above is an entity relationship diagram (ERD) for the app’s database depicting all the entities and relationships it comprises, using crow’s foot notation. Being a relational database, the design of the database was developed with the idea of normalisation in mind, so as to keep the data structured in an organised and consistent way and reduce data redundancy and dependency, in order to maintain the integrity of the data. This was achieved by stepping through the first three forms of normalisation during the database design process, explained below using the `Plants` entity and sample data as an example:

### First Normal Form (1NF)
In this form, the table has a primary key, each column has a unique name, and each cell only contains one value (atomicity). This form was the starting point of the database design for the `Plants` entity, where all the desired information fields were collated into a single table.

| plant_id | specie_name     | specie_type     | start_date | end_date   | first_name | last_name | email               | phone_no   |
| -------- | --------------- | --------------- | ---------- | ---------- | ---------- | --------- | ------------------- | ---------- |
| 1        | Fiddle-leaf fig | Tree            | 09/09/2023 | 01/12/2023 | Alice      | Jones     | aj5678@email.com    | 0404123123 |
| 2        | Fiddle-leaf fig | Tree            | 23/05/2024 | 20/05/2024 | Janet      | Brown     | janbrown@email.com  | 0404987888 |
| 3        | Bear’s paw      | Succulent       | 03/12/2023 | 30/12/2023 | Barry      | White     | b_white23@email.com | 0498345873 |
| 4        | Prickly pear    | Cactus          | 18/12/2023 | 24/12/2023 | William    | Digg      | wdigg1@email.com    | 0491324756 |
| 4        | Prickly pear    | Cactus          | 15/01/2024 | 18/02/2024 | William    | Digg      | wdigg1@email.com    | 0491324756 |
| 4        | Prickly pear    | Cactus          | 29/04/2024 | 04/06/2024 | William    | Digg      | wdigg1@email.com    | 0491324756 |
| 5        | Devil’s ivy     | Foliage plant   | 03/02/2024 | 28/02/2024 | Sam        | Lee       | sam.lee@email.com   | 0413763495 |
| 6        | Peace lily      | Flowering plant | 21/05/2024 | 03/06/2024 | Rebecca    | Gregson   | bec_g1@email.com    | 0464873651 |

### Second Normal Form (2NF)
Builds on 1NF by ensuring that all non-key columns are dependent on the primary key. As such, the table is split into several smaller tables based on the dependencies that exist.

- <u>Enrolments</u>: An `Enrolments` table is created, with the primary key of `enrolment_id` to identify each enrolment of a plant into the day-care’s care. Columns `start_date` and `end_date` are dependent on an enrolment, hence they are part of the table.

    | enrolment_id | start_date | end_date   |
    | ------------ | ---------- | ---------- |
    | 101          | 09/09/2023 | 01/12/2023 |
    | 102          | 23/05/2024 | 20/05/2024 |
    | 103          | 03/12/2023 | 30/12/2023 |
    | 104          | 18/12/2023 | 24/12/2023 |
    | 105          | 15/01/2024 | 18/02/2024 |
    | 106          | 29/04/2024 | 04/06/2024 |
    | 107          | 03/02/2024 | 28/02/2024 |
    | 108          | 21/05/2024 | 03/06/2024 |

- <u>Customers</u>: A `Customers` table is also created, with the primary key of `customer_id` to identify each customer. Columns `first_name`, `last_name`, `email` and `phone_no` all depend on the `customer_id`.

    | customer_id | first_name | last_name | email               | phone_no     |
    | ----------- | ---------- | --------- | ------------------- | ------------ |
    | 201         | Alice      | Jones     | aj5678@email.com    | 0404 123 123 |
    | 202         | Janet      | Brown     | janbrown@email.com  | 0404 987 888 |
    | 203         | Barry      | White     | b_white23@email.com | 0498 345 873 |
    | 204         | William    | Digg      | wdigg1@email.com    | 0491 324 756 |
    | 205         | Sam        | Lee       | sam.lee@email.com   | 0413 763 495 |
    | 206         | Rebecca    | Gregson   | bec_g1@email.com    | 0464 873 651 |

- <u>Plants</u>: As all the non-key attributes in the original `Plants` table have now been split out into their own tables, `Enrolments` and `Customers`, the `Plants` table now only contains the columns `specie_name` and `specie_type`, which are both dependent on the primary key `plant_id`. Foreign keys `enrolment_id` and `customer_id` are added, to associate the data that has been split out into the `Enrolments` and `Customers` tables back to the `Plants` table.

    | plant_id | specie_name     | specie_type     | enrolment_id | customer_id |
    | -------- | --------------- | --------------- | ------------ | ----------- |
    | 1        | Fiddle-leaf fig | Tree            | 101          | 201         |
    | 2        | Fiddle-leaf fig | Tree            | 102          | 202         |
    | 3        | Bear’s paw      | Succulent       | 103          | 203         |
    | 4        | Prickly pear    | Cactus          | 104          | 204         |
    | 4        | Prickly pear    | Cactus          | 105          | 204         |
    | 4        | Prickly pear    | Cactus          | 106          | 204         |
    | 5        | Devil’s ivy     | Foliage plant   | 107          | 205         |
    | 6        | Peace lily      | Flowering plant | 108          | 206         |

### Third Normal Form (3NF)
Additionally builds on 2NF, by further ensuring that there are no transitive dependencies, in other words, no non-key column should depend on another non-key column in the table. Applying this logic, the information in the Plants table can be refined into two separate tables.

- <u>Species & Specie_types</u>: In the 2NF `Plants` table, the columns `specie_name` and `specie_type` are transitively dependent on each other. This is the case because if, for example, the `specie_name` for a plant record was changed from ‘Prickly pear’ to ‘Fiddle-leaf fig’, the `specie_type` column would also have to change from ‘Cactus’ to ‘Tree’.

    To remove this transitive dependency, the `specie_name` and `specie_type` colums could be separated out into their own table, `Species`. This table would have primary key, `specie_id`, to identify each specie, and columns `name` and `type` which contain its name and type, respectively.
    However, in this new table, a transitive dependency would still exist between `name` and `type`. To eliminate this dependency, the `type` column can be further separated out into its own table, finally resulting in the two tables below, `Species` and `Specie_types`.

    <table>
    <tr><th>Species</th><th>Specie_types</th></tr>
    <tr><td>

    | specie_id | name            | type_id |
    | --------- | --------------- | ------- |
    | 301       | Fiddle-leaf fig | 401     |
    | 302       | Bear’s paw      | 402     |
    | 303       | Prickly pear    | 403     |
    | 304       | Devil’s ivy     | 404     |
    | 305       | Peace lily      | 405     |

    </td><td>

    | type_id | name            |
    | ------- | --------------- |
    | 401     | Tree            |
    | 402     | Succulent       |
    | 403     | Cactus          |
    | 404     | Foliage plant   |
    | 405     | Flowering plant |
    
    </td></tr> </table>

- <u>Plants</u>: With the `specie_name` and `specie_type` columns now separated into their own tables, they are now no longer in the `Plants` table and in order to link the species information back to the `Plants` table, the foreign key `species_id` is added. There are now no longer any transitive dependencies, making the tables conformative to 3NF.

    | plant_id | species_id | enrolment_id | customer_id |
    | -------- | ---------- | ------------ | ----------- |
    | 1        | 301        | 101          | 201         |
    | 2        | 301        | 102          | 202         |
    | 3        | 302        | 103          | 203         |
    | 4        | 303        | 104          | 204         |
    | 4        | 303        | 105          | 204         |
    | 4        | 303        | 106          | 204         |
    | 5        | 304        | 107          | 205         |
    | 6        | 305        | 108          | 206         |

## R7. Explain the implemented models and their relationships, including how the relationships aid the database implementation. This should focus on the database implementation AFTER coding has begun, eg. during the project development phase. <a id="r7"></a>

### Customer model
- Maps to a `customers` table in the database

    ```
    __tablename__ = 'customers'
    ```

- Table has columns `id` (primary key), `first_name`, `last_name`, `email` and `phone_no`

    ```
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String())
    last_name: Mapped[str] = mapped_column(String())
    email: Mapped[str] = mapped_column(Text())
    phone_no: Mapped[str] = mapped_column(String(10))
    ```

- Has an attribute called `plants`, which is a list of all plants belonging to a customer. When a `Plant` instance is accessed through a `Customer` instance, the `plants` attribute on the `Customer` instance will be automatically updated (back-populated) with the related `Plant` instances. Upon deletion of a customer, all related plants will also be deleted.

    ```
    plants: Mapped[List['Plant']] = relationship(back_populates='customer', cascade='all, delete')
    ```

### Plant model

- Maps to a `plants` table in the database

    ```
    __tablename__ = 'plants'
    ```

- Table has columns `id` (primary key), `specie_id` (foreign key) and `customer_id` (foreign key)

    ```
    id: Mapped[int] = mapped_column(primary_key=True)
    specie_id: Mapped[int] = mapped_column(ForeignKey('species.id'))
    customer_id: Mapped[int] = mapped_column(ForeignKey('customers.id'))
    ```

- Has an attribute called `specie`, which is the specie of the plant. When a `Specie` instance is accessed through a `Plant` instance, the specie attribute on the `Plant` instance will be automatically updated (back-populated) with the related `Specie` object.

    ```
    specie: Mapped['Specie'] = relationship(back_populates='plants')
    ```

- Has an attribute called `customer`, which is the customer whom the plant belongs to. When a `Customer` instance is accessed through a `Plant` instance, the `customer` attribute on the `Plant` instance will be automatically updated (back-populated) with the related `Customer` instance.

    ```
    customer: Mapped['Customer'] = relationship(back_populates='plants')
    ```

- Has an attribute called `enrolments`, which is a list of all `enrolments` made for this plant. When an `Enrolment` instance is accessed through a `Plant` instance, the `enrolments` attribute on the `Plant` instance will be automatically updated (back-populated) with the related `Enrolment` instances. Upon deletion of a plant, all related enrolments will also be deleted.

    ```
    enrolments: Mapped[List['Enrolment']] = relationship(back_populates='plant', cascade='all, delete')
    ```

### Enrolment model

- Maps to an `enrolments` table in the database

    ```
    __tablename__ = ‘enrolments’
    ```

- Table has columns `id` (primary key), `start_date`, `end_date` and `plant_id` (foreign key)

    ```
    id: Mapped[int] = mapped_column(primary_key=True)
    start_date: Mapped[date]
    end_date: Mapped[date]
    plant_id: Mapped[int] = mapped_column(ForeignKey('plants.id'))
    ```

- Has an attribute called `activities`, which is a list of all activities performed during an enrolment. When an `Activity` instance is accessed through an `Enrolment` instance, the `activities` attribute on the `Enrolment` instance will be automatically updated (back-populated) with the related `Activity` instances. Upon deletion of an enrolment, all related activities will also be deleted.

    ```
    activities: Mapped[List['Activity']] = relationship(back_populates='enrolment', cascade='all, delete')
    ```


- Has an attribute called `comments`, which is a list of all comments made by staff on an enrolment. When an `Comment` instance is accessed through an `Enrolment` instance, the `comments` attribute on the `Enrolment` instance will be automatically updated (back-populated) with the related `Comment` instances. Upon deletion of an enrolment, all related activities will also be deleted.

    ```
    comments: Mapped[List['Comment']] = relationship(back_populates='enrolment', cascade='all, delete')
    ```

### Specie model

- Maps to a `species` table in the database

    ```
    __tablename__ = ‘species’
    ```

- Table has columns `id` (primary key), `name` and `specie_type_id` (foreign key)

    ```
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())
    specie_type_id: Mapped[int] = mapped_column(ForeignKey('specie_types.id'))
    ```

- Has an attribute called `specie_type`, which is the broader specie type the specie is grouped into. When a `Specie_type` instance is accessed through a `Specie` instance, the `specie_type` attribute on the `Specie` instance will be automatically updated (back-populated) with the related `Specie_type` instance.

    ```
    specie_type: Mapped['SpecieType'] = relationship(back_populates='species')
    ```

- Has an attribute called `plants`, which is a list of all plants in the database of that specie. When a `Plant` instance is accessed through a `Specie` instance, the `plants` attribute on the `Specie` instance will be automatically updated (back-populated) with the related `Plant` instances. An error will be returned when attempting to delete a specie that has existing relations to any `Plant` instances.

    ```
    plants: Mapped[List['Plant']] = relationship(back_populates='specie', cascade='all, delete')
    ```

### Specie_type model

- Maps to a `specie_types` table in the database

    ```
    __tablename__ = ‘specie_types’
    ```

- Table has columns `id` (primary key) and `name`

    ```
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())
    ```

- Has an attribute called `species`, which is a list all species that belong to a specie type. When a `Specie` instance is accessed through a `Specie_type` instance, the `species` attribute on the `Specie_type` instance will be automatically updated (back-populated) with the related `Specie` instances. An error will be returned when attempting to delete a specie type that has existing relations to any `Specie` instances.

    ```
    plants: Mapped[List['Plant']] = relationship(back_populates='specie’)
    ```

### Activity model

- Maps to an `activities` table in the database

    ```
    __tablename__ = ‘activities’
    ```

- Table has columns `id` (primary key), `date_performed`, `activity_type_id` (foreign key), `enrolment_id` (foreign key) and `user_id` (foreign key)

    ```
    id: Mapped[int] = mapped_column(primary_key=True)
    date_performed: Mapped[date]
    activity_type_id: Mapped[int] = mapped_column(ForeignKey('activity_types.id'))
    enrolment_id: Mapped[int] = mapped_column(ForeignKey('enrolments.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    ```

- Has an attribute called `activity_type`, which describes the type of activity. When an `Activity_type` instance is accessed through an `Activity` instance, the `activity_type` attribute on the `Activity` instance will be automatically updated (back-populated) with the related `Activity_type` instance.

    ```
    activity_type: Mapped['ActivityType'] = relationship(back_populates='activities')
    ```

- Has an attribute called `enrolment`, which is the enrolment for which the activity was performed. When an `Enrolment` instance is accessed through an `Activity` instance, the `enrolment` attribute on the `Activity` instance will be automatically updated (back-populated) with the related `Enrolment` instance.

    ```
    enrolment: Mapped['Enrolment'] = relationship(back_populates='activities')
    ```

- Has an attribute called `user`, which is the staff member who performed the activity. When a `User` instance is accessed through an `Activity` instance, the `user` attribute on the `Activity` instance will be automatically updated (back-populated) with the related `User` instance.

    ```
    user: Mapped['User'] = relationship(back_populates='activities')
    ```

### Activity_type model

- Maps to an `activity_types` table in the database

    ```
    __tablename__ = ‘activity_types’
    ```

- Table has columns `id` (primary key) and `name`

    ```
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())
    ```

- Has an attribute called `activities`, which is a list of all instances of activities performed of an activity type. When a `Activity` instance is accessed through an `Activity_type` instance, the `activities` attribute on the `Activity_type` instance will be automatically updated (back-populated) with the related `Activity` instances. An error will be returned when attempting to delete an activity type that has existing relations to any `Activity` instances.

    ```
    activities: Mapped[List['Activity']] = relationship(back_populates='activity_type')
    ```

### Comment model

- Maps to a `comments` table in the database

    ```
    __tablename__ = ‘comments’
    ```

- Table has columns `id` (primary key), `text`, `date_created`, `enrolment_id` (foreign key) and `user_id` (foreign key)

    ```
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(Text())
    date_created: Mapped[date]
    enrolment_id: Mapped[int] = mapped_column(ForeignKey('enrolments.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    ```

- Has an attribute called `enrolment`, which is the enrolment on which the comment is made. When an `Enrolment` instance is accessed through a `Comment` instance, the `comment` attribute on the `Comment` instance will be automatically updated (back-populated) with the related `Enrolment` instance.

    ```
    enrolment: Mapped['Enrolment'] = relationship(back_populates='comments')
    ```

- Has an attribute called `user`, which is the enrolment on which the comment is made. When an `User` instance is accessed through a `Comment` instance, the `comment` attribute on the `Comment` instance will be automatically updated (back-populated) with the related `User` instance.

    ```
    user: Mapped['User'] = relationship(back_populates='comments')
    ```

### Comments

- Maps to a `comments` table in the database

    ```
    __tablename__ = ‘enrolments’
    ```

- Table has columns `id` (primary key), `email`, `password` and `is_admin`.

    ```
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(Text(), unique=True)
    password: Mapped[str] = mapped_column(String())
    is_admin: Mapped[bool] = mapped_column(Boolean(), server_default='false')
    ```

- Has an attribute called `comments`, which is a list of all comments made by the user. When a `Comment` instance is accessed through a `User` instance, the `comments` attribute on the `User` instance will be automatically updated (back-populated) with the related `Comment` instances. Upon deletion of a user, all related comments will also be deleted.

    ```
    comments: Mapped[List['Comment']] = relationship(back_populates='user', cascade='all, delete')
    ```

- Has an attribute called `activities`, which is a list of all comments made by the user. When a `Activity` instance is accessed through a `User` instance, the `activities` attribute on the `User` instance will be automatically updated (back-populated) with the related `Activity` instances. Upon deletion of a user, all related comments will also be deleted.

    ```
    activities: Mapped[List['Activity']] = relationship(back_populates='user', cascade='all, delete')
    ```

## R8 Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint: HTTP verb, Path or route, Any required body or header data, Response. <a id="r8"></a>

### Users

| **Description**   | Returns a list of all users in the database. |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | GET                                          |
| **Route**         | /users                                       |
| **Required data** | **Header:** Valid JWT<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** JSON object containing all user records in the database, including details such as id, email and whether or not the user is an admin |
| **Example**       | ![users: get all](/docs/users-get-all.png) |

| **Description**   | Generates and returns a JWT for a user. |
| ----------------- | ------------------------------------------- |
| **HTTP verb**     | POST                                        |
| **Route**         | /users                                      |
| **Required data** | **Header:** None<br>**Body:** User details (email and password) |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** JSON object containing the generated JWT<br><br>**HTTP status code:** 401 Unauthorized<br>**Body:** “Invalid email or password” error message if email and password combination does not match any records in the database." |
| **Example**       | ![users: login](/docs/users-login.png) |

| **Description**   | Creates a new user in the database.          |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | POST                                         |
| **Route**         | /users                                       |
| **Required data** | **Header:** Valid JWT, user must be an admin<br>**Body:** User details (email, password and whether or not the new user is to be an admin) |
| **Response**      | **HTTP status code:** 201 Created<br>**Body:** JSON object containing newly created user details (id, email, hashed password and whether or not the user is an admin) |
| **Example**       | ![users: create](/docs/users-create.png) |

| **Description**   | Deletes a user from the database. All comments and activities associated with the user will also be deleted. |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | DELETE                                       |
| **Route**         | /users/<int:id>                              |
| **Required data** | **Header:** Valid JWT, user must be an admin<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** “Deleted successfully” message upon successful deletion of user<br><br>**HTTP status code:** 404 Not Found<br>**Body:** “Not Found” error message if no record matching the user id provided was found |
| **Example**       | ![users: delete](/docs/users-delete.png) |

### Customers

| **Description**   | Returns a list of all customers in the database. |
| ----------------- | ------------------------------------------------ |
| **HTTP verb**     | GET                                              |
| **Route**         | /customers                                       |
| **Required data** | **Header:** Valid JWT<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** JSON object containing a list of all customer records in the database, including first name, last name, email and phone number for each customer |
| **Example**       | ![customers: get all](/docs/customers-get-all.png) |

| **Description**   | Returns a list of all plants belonging to a customer. |
| ----------------- | ------------------------------------------------ |
| **HTTP verb**     | GET                                              |
| **Route**         | /customers/<int:id>                              |
| **Required data** | **Header:** Valid JWT<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** JSON object containing the customer’s first name and last name, and a list of all their plants (id, specie name and specie type) and their respective enrolments (id, start date and end date)<br><br>**HTTP status code:** 404 Not Found<br>**Body:** “Not Found” error message if no record matching the customer id provided was found|
| **Example**       | ![customers: get one](/docs/customers-get-one.png) |

| **Description**   | Creates a new customer in the database.      |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | POST                                         |
| **Route**         | /customers                                   |
| **Required data** | **Header:** Valid JWT<br>**Body:** Customer details (first name, last name, email and phone number) |
| **Response**      | **HTTP status code:** 201 Created<br>**Body:** JSON object containing the newly created customer’s details (id, first name, last name, email and phone number) |
| **Example**       | ![customers: create](/docs/customers-create.png) |

| **Description**   | Updates an existing customer’s details in the database. |
| ----------------- | ------------------------------------------------ |
| **HTTP verb**     | PUT, PATCH                                       |
| **Route**         | /customers/<int:id>                              |
| **Required data** | **Header:** Valid JWT<br>**Body:** Any attribute and value in the customer’s record to be updated (first name, last name, email and phone number). Any unknown fields will be ignored. |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** JSON object containing the updated customer record (id, first name, last name, email and phone number)<br><br>**HTTP status code:** 404 Not Found<br>**Body:** “Not Found” error message if no record matching the customer id provided was found |
| **Example**       | ![customers: update](/docs/customers-update.png) |

| **Description**   | Deletes a customer from the database. All plants associated with the customer will also be deleted. |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | DELETE                                       |
| **Route**         | /customers/<int:id>                              |
| **Required data** | **Header:** Valid JWT, user must be an admin<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** “Deleted successfully” message upon successful deletion of customer<br><br>**HTTP status code:** 404 Not Found<br>**Body:** “Not Found” error message if no record matching the customer id provided was found |
| **Example**       | ![customers: delete](/docs/customers-delete.png) |

### Plants

| **Description**   | Returns a list of all plant records in the database. |
| ----------------- | ---------------------------------------------------- |
| **HTTP verb**     | GET                                                  |
| **Route**         | /plants                                              |
| **Required data** | **Header:** Valid JWT<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** JSON object with list of all plant records including its id, specie id, specie name and id of customer to whom it belongs |
| **Example**       | ![plants: get all](/docs/plants-get-all.png) |

| **Description**   | Returns all enrolment records associated with a plant. |
| ----------------- | ------------------------------------------------------ |
| **HTTP verb**     | GET                                                    |
| **Route**         | /plants/<int:id>                                       |
| **Required data** | **Header:** Valid JWT<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** JSON object with plant details (id, specie name, specie type and customer to whom it belongs) and a list of enrolments (id, start date and end date) associated with it<br><br>**HTTP status code:** 404 Not Found<br>**Body:** “Not Found” error message if no record matching the plant id provided was found |
| **Example**       | ![plants: get one](/docs/plants-get-one.png) |

| **Description**   | Creates a new plant in the database.         |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | POST                                         |
| **Route**         | /plants                                      |
| **Required data** | **Header:** Valid JWT<br>**Body:** Plant details (specie id and id of customer to whom it belongs) |
| **Response**      | **HTTP status code:** 201 Created<br>**Body:** JSON object containing the newly created plant’s details (id, specie id, specie name and id of customer to whom it belongs) |
| **Example**       | ![plants: create](/docs/plants-create.png) |

| **Description**   | Deletes a plant from the database. All enrolments associated with the plant will also be deleted. |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | DELETE                                       |
| **Route**         | /plants/<int:id>                             |
| **Required data** | **Header:** Valid JWT, user must be an admin<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** “Deleted successfully” message upon successful deletion of plant<br><br>**HTTP status code:** 404 Not Found<br>**Body:** “Not Found” error message if no record matching the plant id provided was found |
| **Example**       | ![plants: delete](/docs/plants-delete.png) |

### Enrolments
| **Description**   | Creates a customer, plant and enrolment record simultaneously. Used for first-time customers. |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | POST                                         |
| **Route**         | /enrolments/new                              |
| **Required data** | **Header:** Valid JWT<br>**Body:** Customer details (first name, last name, email and phone number), plant details (specie id) and enrolment details (start date and end date) |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** JSON object containing newly created records including customer details (id, first name, last name, email and phone number), plant details (id, specie name) and enrolment details (id, start date and end date) |
| **Example**       | ![enrolments: create new](/docs/enrolments-create-new.png) |

| **Description**   | Returns all comments and activities associated with an enrolment. |
| ----------------- | ------------------------------------------------------ |
| **HTTP verb**     | GET                                                    |
| **Route**         | /enrolments/<int:id>                                   |
| **Required data** | **Header:** Valid JWT<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** JSON object containing enrolment details (id, start date, end date, plant id) and all activities (including id, date performed, activity type and email of user who performed the activity) and comments (id, date created, comment text, and user who posted the comment) associated with it<br><br>**HTTP status code:** 404 Not Found<br>**Body:** “Not Found” error message if no record matching the enrolment id provided was found |
| **Example**       | ![enrolments: get one](/docs/enrolments-get-one.png) |

| **Description**   | Returns all current enrolments (i.e. where end date is in the future). |
| ----------------- | ---------------------------------------------------- |
| **HTTP verb**     | GET                                                  |
| **Route**         | /enrolments/current                                  |
| **Required data** | **Header:** Valid JWT<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** JSON object containing enrolment details (id, start date, end date, plant id) for all current enrolments |
| **Example**       | ![enrolments: get current](/docs/enrolments-get-current.png) |

| **Description**   | Creates a new enrolment for an existing plant in the database. |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | POST                                         |
| **Route**         | /enrolments/<int:plant_id>                   |
| **Required data** | **Header:** Valid JWT<br>**Body:** Enrolment details (state date, end date, plant id for which the enrolment is for) |
| **Response**      | **HTTP status code:** 201 Created<br>**Body:** JSON object containing the newly created enrolment record (id, start date, end date and plant id for which the enrolment is for)<br><br>**HTTP status code:** 404 Not Found<br>**Body:** “Not Found” error message if no record matching the enrolment id provided was found |
| **Example**       | ![enrolments: create](/docs/enrolments-create.png) |

| **Description**   | Updates an existing enrolment record in the database. |
| ----------------- | ------------------------------------------------ |
| **HTTP verb**     | PUT, PATCH                                       |
| **Route**         | /enrolments/<int:id>                             |
| **Required data** | **Header:** Valid JWT<br>**Body:** Any attribute and value in the customer’s record to be updated (start date and/or end date). Any unknown fields will be ignored |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** JSON object containing the updated enrolment record (id, start date, end date, id of plant for which the enrolment is for)<br><br>**HTTP status code:** 404 Not Found<br>**Body:** “Not Found” error message if no record matching the enrolment id provided was found |
| **Example**       | ![enrolments: update](/docs/enrolments-update.png) |

| **Description**   | Deletes an enrolment record from the database. All activities and comments associated with the enrolment will also be deleted. |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | DELETE                                       |
| **Route**         | /enrolments/<int:id>                         |
| **Required data** | **Header:** Valid JWT, user must be an admin<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** “Deleted successfully” message upon successful deletion of enrolment<br><br>**HTTP status code:** 404 Not Found<br>**Body:** “Not Found” error message if no record matching the enrolment id provided was found |
| **Example**       | ![enrolments: delete](/docs/enrolments-delete.png) |

### Specie types

| **Description**   | Returns a list of all specie types in the database.  |
| ----------------- | ---------------------------------------------------- |
| **HTTP verb**     | GET                                                  |
| **Route**         | /specie_types                                        |
| **Required data** | **Header:** None<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** JSON object containing all species type details (id and name) |
| **Example**       | ![specie_types: get all](/docs/specie-types-get-all.png) |

| **Description**   | Creates a new specie type in the database.   |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | POST                                         |
| **Route**         | /specie_types                                |
| **Required data** | **Header:** Valid JWT<br>**Body:** Specie type details (name) |
| **Response**      | **HTTP status code:** 201 Created<br>**Body:** JSON object with the newly created species type record (id and name) |
| **Example**       | ![specie_types: create](/docs/specie-types-create.png) |

| **Description**   | Deletes a specie type from the database. An error will be returned when attempting to delete a specie type that has existing relations to any Specie instances. |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | DELETE                                       |
| **Route**         | /specie_types/<int:id>                       |
| **Required data** | **Header:** Valid JWT, user must be an admin<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** “Deleted successfully” message upon successful deletion of specie type<br><br>**HTTP status code:** 404 Not Found<br>**Body:** “Not Found” error message if no record matching the specie type id provided was found |
| **Example**       | ![specie_types: delete](/docs/specie-types-delete.png) |

### Species

| **Description**   | Returns a list of all species in the database.       |
| ----------------- | ---------------------------------------------------- |
| **HTTP verb**     | GET                                                  |
| **Route**         | /species                                             |
| **Required data** | **Header:** None<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** JSON object containing all species and details including id, specie name and specie type name |
| **Example**       | ![species: get all](/docs/species-get-all.png) |

| **Description**   | Creates a new specie for an existing specie type in the database. |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | POST                                         |
| **Route**         | /species/<int:specie_type_id>                |
| **Required data** | **Header:** Valid JWT<br>**Body:** Specie details (name and specie type id) |
| **Response**      | **HTTP status code:** 201 Created<br>**Body:** JSON object with the newly created specie record (id, name and specie type name) |
| **Example**       | ![species: create](/docs/species-create.png) |

| **Description**   | Deletes a specie from the database. An error will be returned when attempting to delete a specie that has existing relations to any Plant instances. |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | DELETE                                       |
| **Route**         | /species/<int:id>                            |
| **Required data** | **Header:** Valid JWT, user must be an admin<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** “Deleted successfully” message upon successful deletion of specie<br><br>**HTTP status code:** 404 Not Found<br>**Body:** “Not Found” error message if no record matching the specie id provided was found |
| **Example**       | ![species: delete](/docs/species-delete.png) |

### Activity types

| **Description**   | Returns a list of all activity types in the database. |
| ----------------- | ----------------------------------------------------- |
| **HTTP verb**     | GET                                                   |
| **Route**         | /activity_types                                       |
| **Required data** | **Header:** None<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** JSON object containing all activity types (id and name) |
| **Example**       | ![activity types: get all](/docs/activity-types-get-all.png) |

| **Description**   | Creates a new activity type in the database. |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | POST                                         |
| **Route**         | /activity_types                              |
| **Required data** | **Header:** Valid JWT<br>**Body:** Activity type details (name) |
| **Response**      | **HTTP status code:** 201 Created<br>**Body:** JSON object with the newly created activity type (id and name) |
| **Example**       | ![activity types: create](/docs/activity-types-create.png) |

| **Description**   | Deletes an activity type from the database. An error will be returned when attempting to delete an activity type that has existing relations to any Activity instance. |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | DELETE                                       |
| **Route**         | /activity_types/<int:id>                    |
| **Required data** | **Header:** Valid JWT, user must be an admin<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** “Deleted successfully” message upon successful deletion of activity type<br><br>**HTTP status code:** 404 Not Found<br>**Body:** “Not Found” error message if no record matching the activity type id provided was found |
| **Example**       | ![activity types: delete](/docs/activity-types-delete.png) |

### Activities

| **Description**   | Creates an activity record for an existing enrolment. |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | POST                                         |
| **Route**         | /activities/<int:enrolment_id>               |
| **Required data** | **Header:** Valid JWT<br>**Body:** Activity details (date performed, activity type id and enrolment id) |
| **Response**      | **HTTP status code:** 201 Created<br>**Body:** JSON object containing newly created activity record including activity including its id, date performed, activity type id and name, and email of the user who performed the activity<br><br>**HTTP status code:** 404 Not Found<br>**Body:** “Not Found” error message if no record matching the enrolment id provided was found |
| **Example**       | ![activities: create](/docs/activities-create.png) |

| **Description**   | Deletes an activity record from the database. |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | DELETE                                       |
| **Route**         | /activities/<int:id>                         |
| **Required data** | **Header:** Valid JWT, user must be an admin<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** “Deleted successfully” message upon successful deletion of activity<br><br>**HTTP status code:** 404 Not Found<br>**Body:** “Not Found” error message if no record matching the activity id provided was found |
| **Example**       | ![activities: delete](/docs/activities-delete.png) |

### Comments

| **Description**   | Creates a comment on an existing enrolment. |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | POST                                         |
| **Route**         | /comments/<int:enrolment_id>               |
| **Required data** | **Header:** Valid JWT<br>**Body:** Comment details (text and date created) |
| **Response**      | **HTTP status code:** 201 Created<br>**Body:** JSON object containing newly created comment details including id, date created, text, id of enrolment to which it pertains and email of user who posted the comment<br><br>**HTTP status code:** 404 Not Found<br>**Body:** “Not Found” error message if no record matching the enrolment id provided was found |
| **Example**       | ![comments: create](/docs/comments-create.png) |

| **Description**   | Deletes a comment from the database. |
| ----------------- | -------------------------------------------- |
| **HTTP verb**     | DELETE                                       |
| **Route**         | /comments/<int:id>                         |
| **Required data** | **Header:** Valid JWT, user must be an admin<br>**Body:** None |
| **Response**      | **HTTP status code:** 200 OK<br>**Body:** “Deleted successfully” message upon successful deletion of comment**HTTP status code:** 404 Not Found<br>**Body:** “Not Found” error message if no record matching the comment id provided was found |
| **Example**       | ![comments: delete](/docs/comments-delete.png) |

## References
Abdullah, E 2022, How to Interact with Databases using SQLAlchemy with PostgreSQL - CoderPad, coderpad.io, viewed 28 June 2024, <https://coderpad.io/blog/development/sqlalchemy-with-postgresql/>.

Amazon Web Services 2024, What is PostgreSQL? – Amazon Web Services, Amazon Web Services, Inc., viewed 28 June 2024, <https://aws.amazon.com/rds/postgresql/what-is-postgresql/>.

Arias, D 2021, Hashing in Action: Understanding bcrypt, Auth0 - Blog, viewed 28 June 2024, <https://auth0.com/blog/hashing-in-action-understanding-bcrypt/>.

Bry 2023, Using Flask-Marshmallow for easy JSON Serialization, DEV Community, viewed 28 June 2024, <https://dev.to/brythewiseguy/flask-easy-mode-using-flask-marshmallow-for-serialization-3bbo>.

Burdiuzha, R 2023, What is PostgreSQL?, Medium, viewed 28 June 2024, <https://gartsolutions.medium.com/what-is-postgresql-2bbd8e4ada6a>.
DataScientest 2023, SQLAlchemy: What is it? What’s it for?, Data Science Courses | DataScientest, viewed 29 June 2024, <https://datascientest.com/en/sqlalchemy-what-is-it-whats-it-for>.

Deery, M 2023, The Flask Web Framework: A Beginner’s Guide, careerfoundry.com, viewed 28 June 2024, <https://careerfoundry.com/en/blog/web-development/what-is-flask/>.

Dhruv, S 2024, Pros and Cons of using PostgreSQL for Application Development, Aalpha, viewed 28 June 2024, <https://www.aalpha.net/blog/pros-and-cons-of-using-postgresql-for-application-development/>.

Ellingwood, J 2024, What is an ORM (Object Relational Mapper)?, Prisma’s Data Guide, viewed 29 June 2024, <https://www.prisma.io/dataguide/types/relational/what-is-an-orm>.

Murray, K 2021, How to Close the Communication Gaps in Your Preschool This School Year, The Child Care Success Company, viewed 28 June 2024, <https://www.childcaresuccess.com/how-to-close-the-communication-gaps-in-your-preschool-this-school-year/>.

Nguyen, H 2024, What is PostgreSQL and Everything You Need to Know, TECHVIFY Software, viewed 28 June 2024, <https://techvify-software.com/what-is-postgresql/>.

Shopsense Retail Technologies 2024, PostgreSQL vs MySQL: Critical Differences, www.boltic.io, viewed 28 June 2024, <https://www.boltic.io/blog/postgresql-performance-vs-mysql>.

Spicer, H 2020, 3 Common Problems Managers Face in Child Care, Tanda, viewed 19 June 2024, <https://www.tanda.co/blog/common-child-care-problems/>.
