#!/usr/bin/python3
"""Lists all cities with their states."""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

from relationship_city import City
from relationship_state import State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username,
            password,
            database
        )
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = (
        session.query(City)
        .options(joinedload(City.state))
        .order_by(City.id)
        .all()
    )

    for city in cities:
        print(
            "{}: {} -> {}".format(
                city.id,
                city.name,
                city.state.name
            )
        )

    session.close()
