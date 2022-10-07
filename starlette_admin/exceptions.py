from typing import Dict, Optional


class StarletteAdminException(Exception):
    pass


class FormValidationError(StarletteAdminException):
    def __init__(self, errors: Dict[str, str]) -> None:
        self.errors = errors

    def has(self, name: str) -> bool:
        return self.errors.get(name, None) is not None

    def msg(self, name: str) -> Optional[str]:
        return self.errors.get(name, None)


class LoginFailed(StarletteAdminException):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg = msg
