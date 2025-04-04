import os

# Server socket
bind = f"0.0.0.0:{os.environ.get('PORT', '10000')}"

# Worker processes
workers = 4
worker_class = 'sync'

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# Timeout
timeout = 120
chdir = "." 