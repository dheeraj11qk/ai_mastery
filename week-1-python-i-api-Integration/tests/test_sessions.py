from app.session_store import InMemorySessionStore


def test_sessions_are_isolated() -> None:
    store = InMemorySessionStore(max_messages=10)

    store.append_turn("alpha", "Hello", "Hi alpha")
    store.append_turn("beta", "Hello", "Hi beta")

    alpha_history = store.get_history("alpha")
    beta_history = store.get_history("beta")

    assert alpha_history[1].content == "Hi alpha"
    assert beta_history[1].content == "Hi beta"


def test_history_is_limited() -> None:
    store = InMemorySessionStore(max_messages=4)

    store.append_turn("alpha", "one", "two")
    store.append_turn("alpha", "three", "four")
    store.append_turn("alpha", "five", "six")

    history = store.get_history("alpha")

    assert len(history) == 4
    assert history[0].content == "three"
    assert history[-1].content == "six"
