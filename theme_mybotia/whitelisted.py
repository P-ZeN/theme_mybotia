import frappe

@frappe.whitelist()
def custom_switch_theme(theme):
	if theme in ["Dark", "Light", "Automatic", "theme_mybotia"]:
		frappe.db.set_value("User", frappe.session.user, "desk_theme", theme)
