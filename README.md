# uuidify-python — Fast UUID & ULID generation for Python apps
> Official Python client for the [UUIDify API](https://github.com/ilkereroglu/uuidify).

[![PyPI](https://img.shields.io/pypi/v/uuidify.svg)](https://pypi.org/project/uuidify/)
[![Python Versions](https://img.shields.io/pypi/pyversions/uuidify.svg)](https://pypi.org/project/uuidify/)
[![License](https://img.shields.io/pypi/l/uuidify.svg)](https://github.com/ilkereroglu/uuidify-python/blob/main/LICENSE)
[![Python Tests](https://github.com/ilkereroglu/uuidify-python/actions/workflows/test.yaml/badge.svg)](https://github.com/ilkereroglu/uuidify-python/actions/workflows/test.yaml)

Minimal, idiomatic Python client for generating UUIDv1/v4/v7 and ULID identifiers through UUIDify’s globally distributed API.

---

## Install
```bash
pip install uuidify
```

## Usage
```python
from uuidify import UuidifyClient, UuidifyError

client = UuidifyClient()

try:
    # Generate a single UUIDv4
    uuid_val = client.uuid_v4()
    print(f"UUIDv4: {uuid_val}")

    # Generate multiple UUIDv7s
    uuids = client.uuid_v7(count=5)
    print(f"UUIDv7s: {uuids}")

    # Generate a ULID
    ulid_val = client.ulid()
    print(f"ULID: {ulid_val}")

except UuidifyError as e:
    print(f"An error occurred: {e}")
```

## Features
- ✅ Drop-in `UuidifyClient` with overridable base URL and API Key.
- ⚡️ Fetch UUIDv1/v4/v7, ULID, or batch payloads with one call.
- 🧵 Uses `requests` for reliable HTTP communication.
- 🎯 Typed error system (`UuidifyError`, `APIError`, `ConnectionError`) for clean retries and observability.
- 🧩 Synced with UUIDify’s OpenAPI spec, ensuring long-term compatibility.
- 🧪 Fully typed and tested.

## Why UUIDify
UUIDify is a latency-optimized unique identifier service. With this SDK you get:

- A highly available UUID/ULID generator distributed across regions.
- Predictable performance without maintaining your own randomness infrastructure.
- Consistent REST semantics you can test locally and promote to production seamlessly.

## Service & Documentation
- Main service repository: [github.com/ilkereroglu/uuidify](https://github.com/ilkereroglu/uuidify)
- API documentation & schema: [`openapi.yaml`](https://github.com/ilkereroglu/uuidify/blob/main/api/openapi.yaml)

## License
MIT License © [ilkereroglu](https://github.com/ilkereroglu)
