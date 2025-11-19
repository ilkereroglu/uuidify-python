import requests
from typing import List, Optional, Union, Any, Dict
from .exceptions import APIError, ConnectionError, DecodeError


class UuidifyClient:
    """
    A client for the UUIDify API.
    
    Allows generating UUIDs (v1, v4, v7) and ULIDs.
    """

    def __init__(self, base_url: str = "https://api.uuidify.io", api_key: Optional[str] = None):
        """
        Initialize the client.

        Args:
            base_url: The base URL of the UUIDify API.
            api_key: Optional API key for authentication (if required in future).
        """
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "uuidify-python/0.1.0",
            "Accept": "application/json",
        })
        if api_key:
            self.session.headers.update({"Authorization": f"Bearer {api_key}"})

    def _request(self, params: Dict[str, Any]) -> Any:
        """
        Internal method to make HTTP requests to the API.

        Args:
            params: Query parameters for the request.

        Returns:
            The parsed JSON response.

        Raises:
            APIError: If the API returns a 4xx or 5xx status code.
            ConnectionError: If a network error occurs.
            DecodeError: If the response cannot be parsed as JSON.
        """
        try:
            response = self.session.get(self.base_url, params=params, timeout=10)
        except requests.RequestException as e:
            raise ConnectionError(f"Failed to connect to UUIDify API: {e}") from e

        if not response.ok:
            try:
                error_data = response.json()
                message = error_data.get("error", response.text)
            except ValueError:
                message = response.text
            raise APIError(response.status_code, message)

        try:
            return response.json()
        except ValueError as e:
            raise DecodeError(f"Failed to decode API response: {e}") from e

    def _parse_response(self, data: Dict[str, Any], key_single: str, key_multi: str, count: int) -> Union[str, List[str]]:
        """
        Helper to extract the ID(s) from the response.
        """
        if count == 1:
            return data[key_single]
        return data[key_multi]

    def uuid_v1(self, count: int = 1) -> Union[str, List[str]]:
        """
        Generate UUIDv1 identifiers.

        Args:
            count: Number of UUIDs to generate (default: 1).

        Returns:
            A single UUID string if count is 1, otherwise a list of UUID strings.
        """
        params = {"algorithm": "uuid", "version": "v1", "count": count}
        data = self._request(params)
        return self._parse_response(data, "uuid", "uuids", count)

    def uuid_v4(self, count: int = 1) -> Union[str, List[str]]:
        """
        Generate UUIDv4 identifiers.

        Args:
            count: Number of UUIDs to generate (default: 1).

        Returns:
            A single UUID string if count is 1, otherwise a list of UUID strings.
        """
        params = {"algorithm": "uuid", "version": "v4", "count": count}
        data = self._request(params)
        return self._parse_response(data, "uuid", "uuids", count)

    def uuid_v7(self, count: int = 1) -> Union[str, List[str]]:
        """
        Generate UUIDv7 identifiers.

        Args:
            count: Number of UUIDs to generate (default: 1).

        Returns:
            A single UUID string if count is 1, otherwise a list of UUID strings.
        """
        params = {"algorithm": "uuid", "version": "v7", "count": count}
        data = self._request(params)
        return self._parse_response(data, "uuid", "uuids", count)

    def ulid(self, count: int = 1) -> Union[str, List[str]]:
        """
        Generate ULID identifiers.

        Args:
            count: Number of ULIDs to generate (default: 1).

        Returns:
            A single ULID string if count is 1, otherwise a list of ULID strings.
        """
        params = {"algorithm": "ulid", "version": "ulid", "count": count}
        data = self._request(params)
        return self._parse_response(data, "ulid", "ulids", count)
