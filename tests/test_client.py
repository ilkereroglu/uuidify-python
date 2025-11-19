import pytest
import requests_mock
from uuidify import UuidifyClient, UuidifyError, APIError, ConnectionError, DecodeError

BASE_URL = "https://api.uuidify.io"

@pytest.fixture
def client():
    return UuidifyClient(base_url=BASE_URL)

def test_uuid_v4_single(client):
    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URL}", json={"uuid": "test-uuid-v4", "generated_at": "2023-01-01T00:00:00Z"})
        
        result = client.uuid_v4()
        
        assert result == "test-uuid-v4"
        assert m.last_request.qs['algorithm'] == ['uuid']
        assert m.last_request.qs['version'] == ['v4']
        assert m.last_request.qs['count'] == ['1']

def test_uuid_v4_batch(client):
    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URL}", json={
            "uuids": ["uuid-1", "uuid-2"],
            "generated_at": "2023-01-01T00:00:00Z"
        })
        
        result = client.uuid_v4(count=2)
        
        assert result == ["uuid-1", "uuid-2"]
        assert m.last_request.qs['count'] == ['2']

def test_uuid_v7_single(client):
    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URL}", json={"uuid": "test-uuid-v7"})
        
        result = client.uuid_v7()
        
        assert result == "test-uuid-v7"
        assert m.last_request.qs['version'] == ['v7']

def test_ulid_single(client):
    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URL}", json={"ulid": "test-ulid"})
        
        result = client.ulid()
        
        assert result == "test-ulid"
        assert m.last_request.qs['algorithm'] == ['ulid']
        assert m.last_request.qs['version'] == ['ulid']

def test_api_error_400(client):
    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URL}", status_code=400, json={"error": "Invalid count"})
        
        with pytest.raises(APIError) as excinfo:
            client.uuid_v4(count=-1)
        
        assert "API Error 400" in str(excinfo.value)
        assert "Invalid count" in str(excinfo.value)

def test_api_error_500(client):
    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URL}", status_code=500, text="Internal Server Error")
        
        with pytest.raises(APIError) as excinfo:
            client.uuid_v4()
        
        assert "API Error 500" in str(excinfo.value)

import requests

# ... imports ...

def test_connection_error(client):
    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URL}", exc=requests.exceptions.ConnectTimeout)
        
        with pytest.raises(ConnectionError):
            client.uuid_v4()

def test_decode_error(client):
    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URL}", text="Not JSON")
        
        with pytest.raises(DecodeError):
            client.uuid_v4()
