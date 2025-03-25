import psutil

def list_processes():
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
        print(f'PID: {proc.info[pid]}, Name: {proc.info[name]}, CPU: {proc.info[cpu_percent]}%, Memory: {proc.info[memory_percent]}%')

if __name__ == '__main__':
    list_processes()
