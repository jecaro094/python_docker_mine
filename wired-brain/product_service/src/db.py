import configparser

from flask_sqlalchemy import SQLAlchemy

from config import config, log

db = SQLAlchemy()


def read_db_config(db_path, pass_path):
    """
    Returns database parameters required to connect to the database
    Reads database configuration from files detailed in paths (input parameters)
    :param db_path: Path to database configuration file.
    :param pass_path: Path to where the db password is stored.
    :return: database configurations as dictionary
    """
    config = configparser.ConfigParser()
    config.read(db_path)
    db_config = config["mysql"]

    db_password = open(pass_path)
    db_config["password"] = db_password.read()

    return db_config


def get_db_url():
    """
    Returns database url
    """
    db_config = read_db_config(db_path=config.DB_PATH, pass_path=config.DB_PASS_PATH)
    db_url = f"mysql://{db_config['username']}:{db_config['password']}@{db_config['host']}:3306/{db_config['database']}"
    log.info(f"Connection to database: {db_url}")
    return db_url
