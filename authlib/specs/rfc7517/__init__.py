"""
    authlib.specs.rfc7517
    ~~~~~~~~~~~~~~~~~~~~~

    This module represents a direct implementation of
    JSON Web Key (JWK).

    https://tools.ietf.org/html/rfc7517
"""
from .jwk import JWK, JWKAlgorithm

__all__ = ['JWK', 'JWKAlgorithm']
