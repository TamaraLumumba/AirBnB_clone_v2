#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import urllib.parse

from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    attributeibutes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes new instances of DBStorage.
        """
        try:
            user = os.environ.get('HBNB_MYSQL_USER')
            password = os.environ.get('HBNB_MYSQL_PWD')
            host = os.environ.get('HBNB_MYSQL_HOST')
            db = os.environ.get('HBNB_MYSQL_DB')
            env = os.environ.get('HBNB_ENV')
            attributes = [user, password, host, db]
            for attribute in attributes:
                if attribute is None:
                    print("Missing attributes env var")

            conn_str = "mysql+mysqldb://{}:{}@{}/{}".format(
                        user, password, host, db)
            # create engine and session object with connection string
            self.__engine = create_engine(conn_str, pool_pre_ping=True)

            # drop all tables in DB if test env
            if env == 'test':
                Base.metadata.drop_all(bind=self.__engine, checkfirst=True)
        except Exception as E:
            print("raised exception in init")
            print(E)

    def all(self, cls=None):
        """query on the current database session (self.__session) all objects
        epending of the class name (argument cls).

        key = <class-name>.<object-id>
        value = object

        Args:
            cls (any, optional): class. Defaults to None.

        Returns:
            dict: al objects
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """adds the object to the current database session (self.__session)
        therefore sets __object to given obj.

        Args:
            obj: given object
        """
        if obj and self.__session:
            self.__session.add(obj)

    def save(self):
        """commits all changes"""
        if self.__session:
            self.__session.commit()

    def delete(self, obj=None):
        """deletes objects from the current database session"""
        try:
            self.__session.delete(obj)
        except Exception:
            pass

    def reload(self):
        """creates all tables in the database (feature of SQLAlchemy)."""

        try:
            Base.metadata.create_all(self.__engine)
            session_factory = sessionmaker(bind=self.__engine,
                                           expire_on_commit=False)
            self.__session = scoped_session(session_factory)
        except Exception as E:
            print(E)

    def close(self):
        """removes our session"""
        self.__session.remove()
