# Contributing to uuidify-python

First off, thanks for taking the time to contribute! 🎉

## Getting Started

1.  **Clone the repository**
    ```bash
    git clone https://github.com/ilkereroglu/uuidify-python.git
    cd uuidify-python
    ```

2.  **Set up a virtual environment**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3.  **Install dependencies**
    ```bash
    pip install -e .
    pip install pytest requests-mock build
    ```

## Running Tests

We use `pytest` for testing. Ensure all tests pass before submitting a PR.

```bash
pytest
```

## Development Workflow

1.  Fork the repo and create your branch from `main`.
2.  If you've added code that should be tested, add tests.
3.  Ensure the test suite passes.
4.  Make sure your code follows the existing style.
5.  Issue that pull request!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
