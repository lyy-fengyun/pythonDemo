import psutil

mem = psutil.virtual_memory()
mem.total,mem.used
