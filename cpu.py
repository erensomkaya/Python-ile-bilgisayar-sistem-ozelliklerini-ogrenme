import psutil
cpu = psutil.cpu_count()
memory = psutil.virtual_memory()
print(f":çekirdek sayısı= {cpu}\n")
print(f"used_memory = {memory[3]}\n")
print(memory)