import os

bind = f"0.0.0.0:{os.environ.get('PORT', '10000')}"
workers = 4
timeout = 120
worker_class = "sync"
accesslog = "-"
errorlog = "-"
chdir = "." 