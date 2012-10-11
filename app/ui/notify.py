#
# Optional desktop notifications.
#

import logging


try:
	import notify2 as _notify

	available = True  # assumed to be working since the import succeeded
	_active = False  # not yet active
	_app_title = None


	def init(app_title, active=True):
		"""Init the notifications system."""
		global _app_title
		_app_title = app_title
		return set_active(active)


	def set_active(active=True):
		global available, _active
		if available:
			if active:
				if not _active:
					try:
						_notify.init(_app_title)
						_active = True
					except:
						logging.exception("initializing desktop notifications")
						available = False
			else:
				if _active:
					try:
						_notify.uninit()
					except:
						logging.exception("stopping desktop notifications")
						available = False
					_active = False
		return _active


	def active():
		return _active


	def show(status_code, title, text='', icon=None):
		"""Show a notification with title and text."""
		if available and _active:
			notification = _notify.Notification(title, text, icon or title)
			try:
				notification.show()
			except Exception:
				logging.exception("showing notification %s", notification)


except ImportError:
	logging.warn("python-notify2 not found, desktop notifications are disabled")
	available = False
	active = False
	def init(app_title, active=True): return False
	def active(): return False
	def set_active(active=True): return False
	def show(status_code, title, text, icon=None): pass