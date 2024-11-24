from typing import Any, Dict


class BaseHeader:
    def set_value(self, value: Any) -> None:
        pass

    def get_headers(self) -> Dict[str, str]:
        pass
