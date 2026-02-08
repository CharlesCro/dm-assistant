import reflex as rx
import os
from dotenv import load_dotenv

# Load variables from a .env file if you're using one
load_dotenv()

config = rx.Config(
    app_name="dm_assistant",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    db_url="sqlite:///reflex.db",

)