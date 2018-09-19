import os
from oauth2_provider.settings import OAuth2ProviderSettings

DEFAULTS = {
    "OIDC_CLAIM_PROVIDER": 'apps.oidc.claims.DefaultProvider',
    "OIDC_JWT_BUILDER": 'apps.oidc.jwt.DefaultBuilder',
    "OIDC_ISSUER": os.environ.get('OIDC_ISSUER', 'http://localhost'),
    "OIDC_KEY_STORAGE": 'apps.oidc.secrets.FileKeyStore',
}

USER_SETTINGS = {
    "OIDC_ISSUER": os.environ.get('OIDC_ISSUER', 'http://localhost'),
}

IMPORT_STRINGS = (
    "OIDC_CLAIM_PROVIDER",
    "OIDC_JWT_BUILDER",
    "OIDC_KEY_STORAGE",
)

oidc_settings = OAuth2ProviderSettings(user_settings=USER_SETTINGS, import_strings=IMPORT_STRINGS, defaults=DEFAULTS)