from .context import mango
from .fakes import fake_seeded_public_key, fake_token

from decimal import Decimal


def test_constructor():
    owner = fake_seeded_public_key("owner")
    token = fake_token()
    value = Decimal(27)
    token_value = mango.TokenValue(token, value)

    actual = mango.OwnedTokenValue(owner, token_value)
    assert actual is not None
    assert actual.logger is not None
    assert actual.owner == owner
    assert actual.token_value == token_value
