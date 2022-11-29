import json
import pytest
from brasilvagastech.hello_world import app


@pytest.fixture()
def test_event():
    pass


def test_lambda_handler(test_event, mocker):

    ret = app.lambda_handler(test_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "hello world"
