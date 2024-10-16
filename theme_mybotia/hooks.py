app_name = "theme_mybotia"
app_title = "Theme Mybotia"
app_publisher = "ZeN"
app_description = "Desc"
app_email = "philippe.zenone@free.fr"
app_license = "apache-2.0"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "theme_mybotia",
# 		"logo": "/assets/theme_mybotia/logo.png",
# 		"title": "Theme Mybotia",
# 		"route": "/theme_mybotia",
# 		"has_permission": "theme_mybotia.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/theme_mybotia/css/theme_mybotia.css"
app_include_js = "/assets/theme_mybotia/js/theme_mybotia.js"

# include js, css files in header of web template
# web_include_css = "/assets/theme_mybotia/css/theme_mybotia.css"
# web_include_js = "/assets/theme_mybotia/js/theme_mybotia.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "theme_mybotia/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "theme_mybotia/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "theme_mybotia.utils.jinja_methods",
# 	"filters": "theme_mybotia.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "theme_mybotia.install.before_install"
# after_install = "theme_mybotia.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "theme_mybotia.uninstall.before_uninstall"
# after_uninstall = "theme_mybotia.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "theme_mybotia.utils.before_app_install"
# after_app_install = "theme_mybotia.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "theme_mybotia.utils.before_app_uninstall"
# after_app_uninstall = "theme_mybotia.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "theme_mybotia.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"theme_mybotia.tasks.all"
# 	],
# 	"daily": [
# 		"theme_mybotia.tasks.daily"
# 	],
# 	"hourly": [
# 		"theme_mybotia.tasks.hourly"
# 	],
# 	"weekly": [
# 		"theme_mybotia.tasks.weekly"
# 	],
# 	"monthly": [
# 		"theme_mybotia.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "theme_mybotia.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "theme_mybotia.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "theme_mybotia.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["theme_mybotia.utils.before_request"]
# after_request = ["theme_mybotia.utils.after_request"]

# Job Events
# ----------
# before_job = ["theme_mybotia.utils.before_job"]
# after_job = ["theme_mybotia.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"theme_mybotia.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

