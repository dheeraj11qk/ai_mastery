from collections import defaultdict
from copy import deepcopy

from app.models import Message


class InMemorySessionStore:
    def __init__(self, max_messages: int) -> None:
        self.max_messages = max_messages
        self._sessions: dict[str, list[Message]] = defaultdict(list)

    def get_history(self, session_id: str) -> list[Message]:
        return deepcopy(self._sessions[session_id])

    def append_turn(self, session_id: str, user_message: str, assistant_message: str) -> list[Message]:
        history = self._sessions[session_id]
        history.append(Message(role="user", content=user_message))
        history.append(Message(role="assistant", content=assistant_message))

        if len(history) > self.max_messages:
            self._sessions[session_id] = history[-self.max_messages :]

        return self.get_history(session_id)

    def clear(self, session_id: str) -> bool:
        return self._sessions.pop(session_id, None) is not None

    def snapshot(self, session_id: str) -> list[Message]:
        return self.get_history(session_id)
