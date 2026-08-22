"""Typed exceptions for WalletTracker."""


class wallettrackerError(Exception):
 """Base error for the whole package."""

 exit_code = 1


class ConfigurationError(wallettrackerError):
 """Raised when configuration is invalid or missing."""

 exit_code = 2


class ValidationError(wallettrackerError):
 """Raised when input data fails validation."""

 exit_code = 3


class NotFoundError(wallettrackerError):
 """Raised when a requested resource does not exist."""

 exit_code = 4


class ConflictError(wallettrackerError):
 """Raised when an operation conflicts with existing state."""

 exit_code = 5


class RateLimitError(wallettrackerError):
 """Raised when a rate limit is exceeded."""

 exit_code = 6


class TimeoutError(wallettrackerError):
 """Raised when an operation takes too long."""

 exit_code = 7


class UnsupportedError(wallettrackerError):
 """Raised for unsupported inputs or platforms."""

 exit_code = 8


class StateError(wallettrackerError):
 """Raised when internal state is inconsistent."""

 exit_code = 9


def guard(condition, message, exc=ValidationError):
 """Raise exc(message) when condition is False."""
 if not condition:
 raise exc(message)