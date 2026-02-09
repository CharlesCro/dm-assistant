"""Handle Google Auth."""

import json
import os
import time

import reflex as rx
from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token
from httpx import AsyncClient

TOKEN_URI = "https://oauth2.googleapis.com/token"
CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", "")
REDIRECT_URI = os.environ.get("GOOGLE_REDIRECT_URI", "")


def set_client_id(client_id: str):
    """Set the client id."""
    global CLIENT_ID
    CLIENT_ID = client_id


async def get_id_token(auth_code) -> str:
    """Get the id token credential from an auth code.

    Args:
        auth_code: Returned from an 'auth-code' flow.

    Returns:
        The id token credential.
    """
    async with AsyncClient() as client:
        response = await client.post(
            TOKEN_URI,
            data={
                "code": auth_code,
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "redirect_uri": REDIRECT_URI,
                "grant_type": "authorization_code",
            },
        )
        response.raise_for_status()
        response_data = response.json()
        return response_data.get("id_token")

from typing import Any
class GoogleAuthState(rx.State):
    id_token_json: str = rx.LocalStorage()

    @rx.event
    async def on_success(self, id_token: dict):
        if "code" in id_token:
            # Handle auth-code flow
            id_token["credential"] = await get_id_token(id_token["code"])
        self.id_token_json = json.dumps(id_token)

    @rx.var(cache=True)
    def client_id(self) -> str:
        return CLIENT_ID or os.environ.get("GOOGLE_CLIENT_ID", "")

    @rx.var(cache=True)
    def tokeninfo(self) -> dict[str, Any]:
        try:
            if not self.id_token_json:
                return {}
            
            token_data = json.loads(self.id_token_json)
            if "credential" not in token_data:
                print("No credential found in token data")
                return {}
                
            return verify_oauth2_token(
                token_data["credential"],
                requests.Request(),
                self.client_id,
            )
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            self.id_token_json = ""
            return {}
        except ValueError as e:
            print(f"Token verification error: {e}")
            self.id_token_json = ""
            return {}
        except Exception as exc:
            print(f"Unexpected error verifying token: {exc!r}")
            if self.id_token_json:
                self.id_token_json = ""
            return {}

    @rx.var(cache=True)
    def client_id(self) -> str:
        client_id = CLIENT_ID or os.environ.get("GOOGLE_CLIENT_ID", "")
        if not client_id:
            print("WARNING: GOOGLE_CLIENT_ID not set!")
        return client_id

    @rx.event
    def logout(self):
        self.id_token_json = ""

    @rx.var(cache=False)
    def token_is_valid(self) -> bool:
        try:
            return bool(
                self.tokeninfo and int(self.tokeninfo.get("exp", 0)) > time.time()
            )
        except Exception:
            return False

    @rx.var(cache=True)
    def user_name(self) -> str:
        return self.tokeninfo.get("name", "")

    @rx.var(cache=True)
    def user_email(self) -> str:
        return self.tokeninfo.get("email", "")
