"""Manifest (LLM router) provider profile.

NORG fork: ports the HermesOverlay + PROVIDER_REGISTRY entries from the
pre-0.22 layout (upstream PR #18107, never merged) to the plugin layout.
Self-hosted routers override the endpoint with MANIFEST_BASE_URL.
"""

from providers import register_provider
from providers.base import ProviderProfile

manifest = ProviderProfile(
    name="manifest", aliases=("mnfst",), env_vars=("MANIFEST_API_KEY", "MANIFEST_BASE_URL"),
    base_url="https://app.manifest.build/v1",
)

register_provider(manifest)
