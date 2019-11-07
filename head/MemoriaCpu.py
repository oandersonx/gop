import psutil

print(psutil.cpu_percent())


print(psutil.virtual_memory())

for proc in psutil.process_iter():
        try:
            # Aqui ele pega o nome do processo
            processName = proc.name()
            if processName == 'EXCEL.EXE':
                print(processName , ' ::: ', proc.memory_info().vms) # Esse último comando é para pegar o consumo de VMS pelo processo
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass