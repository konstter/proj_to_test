import pytest


@pytest.mark.prb
def test_admin_created(create_admin):
    print(f'[{create_admin.name}] has been created...')
    assert create_admin.created is True


@pytest.mark.prb
def test_admin_name(create_admin):
    assert create_admin.name[:5] == 'Admin'


@pytest.mark.prb
def test_admin_customers_list(create_admin):
    assert create_admin.customers == []
