import pytest

from lettings.models import Address


@pytest.fixture()
def myaddress() -> Address:
    address = Address.objects.create(
        number=100,
        street="My street",
        city="My city",
        state="My state",
        zip_code=10000,
        country_iso_code="USA",
    )
    return address
