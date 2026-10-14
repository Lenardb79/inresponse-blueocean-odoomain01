{
    "name": "InResponse Debrand",
    "version": "19.0.1.0.0",
    "summary": "Remove Odoo branding from title, login, portal, user menu and email footers",
    "author": "InResponse Holdings LLC",
    "license": "LGPL-3",
    "depends": ["web", "web_enterprise", "mail", "portal"],
    "data": ["views/templates.xml"],
    "assets": {
        "web.assets_backend": ["inresponse_debrand/static/src/js/debrand.js"],
    },
    "installable": True,
}
