# iil-testkit

**Shared Test Factory Package for all Platform Django repos** — [ADR-100](https://github.com/achimdehnert/platform/blob/main/docs/adr/ADR-100-iil-testkit-shared-test-factory-package.md)

## Installation

```bash
pip install iil-testkit
```

Or in `requirements-test.txt`:
```
iil-testkit>=0.1.0
```

## Usage

### Factories

```python
# tests/factories.py — import shared, extend repo-specific
from iil_testkit.factories import UserFactory
import factory

class BookProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "bfagent.BookProjects"
    user = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda n: f"Book {n}")
```

### Fixtures

```python
def test_should_view_dashboard(auth_client):
    response = auth_client.get("/dashboard/")
    assert response.status_code == 200
```

Available fixtures: `db_user`, `staff_user`, `admin_user`, `api_client`, `auth_client`, `staff_client`

### Assertion Helpers

```python
from iil_testkit.assertions import assert_redirects_to_login, assert_htmx_response

def test_should_redirect_unauthenticated(api_client):
    response = api_client.get("/protected/")
    assert_redirects_to_login(response)
```

### Naming Convention (ADR-057)

Auto-registered pytest plugin warns when test functions don't follow `test_should_*`:

```
PytestWarning: Naming convention: 'test_login' should start with 'test_should_'
```

Suppress with: `pytest --no-naming-check`

## Architecture

See [ADR-100](https://github.com/achimdehnert/platform/blob/main/docs/adr/ADR-100-iil-testkit-shared-test-factory-package.md).
