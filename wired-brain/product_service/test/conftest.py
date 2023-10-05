import os
import tempfile
from unittest.mock import MagicMock, patch

import pytest
from app import app
from flask import Flask
from sqlalchemy import exc

SQL_EXCEPTION = exc.SQLAlchemyError


@pytest.fixture
def test_client():
    yield app.test_client()


def raise_exception():
    raise SQL_EXCEPTION
