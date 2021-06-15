from .context import mango
from .fakes import fake_token

from decimal import Decimal


def test_constructor():
    actual = mango.BalanceSheet(fake_token(), Decimal(0), Decimal(0), Decimal(0))
    assert actual is not None
    assert actual.logger is not None