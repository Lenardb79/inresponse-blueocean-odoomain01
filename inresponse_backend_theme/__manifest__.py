{
    "name": "InResponse Backend Theme",
    "version": "19.0.1.0.0",
    "summary": "Navy/blue/grey/black backend colors (light + dark mode)",
    "author": "InResponse Holdings LLC",
    "license": "LGPL-3",
    "depends": ["web", "web_enterprise"],
    "assets": {
        "web._assets_primary_variables": [
            ("after", "web/static/src/scss/primary_variables.scss",
             "inresponse_backend_theme/static/src/scss/primary_variables.scss"),
        ],
        "web.assets_web_dark": [
            "inresponse_backend_theme/static/src/scss/backend.dark.scss",
        ],
        "web.assets_backend": [
            "inresponse_backend_theme/static/src/scss/backend.scss",
        ],
    },
    "installable": True,
}
