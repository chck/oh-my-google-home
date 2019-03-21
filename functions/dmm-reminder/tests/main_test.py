import flask
import pytest
from flask import Request
from pytest_mock import MockFixture

from main import remind_dmm


def test_remind_dmm(mocker: MockFixture):
    req: Request = mocker.patch.object(flask, 'Request',
                                       args=dict(
                                           a=1,
                                           b=2,
                                       ))

    assert remind_dmm(req) == 'hello'


if __name__ == '__main__':
    pytest.main([__file__])
