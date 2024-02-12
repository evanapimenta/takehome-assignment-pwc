import pytest
from main import format_address


@pytest.mark.parametrize("address,expected", [
    ("Miritiba 339", {"Miritiba": "339"}),
    ("Babaçu 500", {"Babaçu": "500"}),
    ("Cambuí 804B", {"Cambuí": "804B"}),
    ("Rio Branco 23", {"Rio Branco": "23"}),
    ("Quirino dos Santos 23b", {"Quirino dos Santos": "23b"}),
    ("4, Rue de la Republique", {"Rue de la Republique": "4"}),
    ("100 Broadway Av", {"Broadway Av": "100"}),
    ("Calle Sagasta, 26", {"Calle Sagasta": "26"}),
    ("Calle 44 No 1991", {"Calle 44": "No 1991"}),
])
def test_address_format(address, expected):
    assert format_address(address) == expected