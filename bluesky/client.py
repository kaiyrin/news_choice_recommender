"""Bluesky connection. Credentials come from environment variables named in config.yaml."""
from __future__ import annotations

import os



def login(cfg: dict):
    from atproto import Client                               # lazy import
    handle = os.environ.get(cfg.get("handle_env", "BSKY_HANDLE"), "")
    password = os.environ.get(cfg.get("password_env", "BSKY_APP_PASSWORD"), "")
    if not (handle and password):
        raise RuntimeError("Set the Bluesky handle/app-password environment variables named in config.yaml")
    client = Client()
    client.login(handle, password)                          
    return client
