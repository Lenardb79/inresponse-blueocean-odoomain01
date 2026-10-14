/** @odoo-module **/
// Item keys confirmed in odoo/odoo 19.0 web/static/src/webclient/user_menu/user_menu_items.js;
// "documentation" is added by web_enterprise. Removing only if present keeps this upgrade-safe.
import { registry } from "@web/core/registry";

const items = registry.category("user_menuitems");
for (const key of ["documentation", "support", "shortcuts", "odoo_account"]) {
    if (items.contains(key)) {
        items.remove(key);
    }
}

// title_service falls back to "Odoo" when no title parts are set; rewrite it.
const BRAND = "InResponse";
const fix = () => {
    if (document.title.includes("Odoo")) {
        document.title = document.title.replace(/Odoo/g, BRAND);
    }
};
const titleEl = document.querySelector("title");
if (titleEl) {
    new MutationObserver(fix).observe(titleEl, { childList: true, characterData: true, subtree: true });
}
fix();
