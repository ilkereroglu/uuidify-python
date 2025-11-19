class UuidifyError(Exception):
    """Base exception for all uuidify errors."""
    pass


class APIError(UuidifyError):
    """Exception raised when the API returns an error response (4xx or 5xx)."""
    
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"API Error {status_code}: {message}")


class ConnectionError(UuidifyError):
    """Exception raised when a network error occurs."""
    pass


class DecodeError(UuidifyError):
    """Exception raised when the response cannot be decoded."""
    pass
