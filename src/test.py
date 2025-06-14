import os
import subprocess


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

def get_parent_pid():
    ppid = os.getppid()
    print(f"Parent Process ID (PPID): {ppid}")

def main():
    process_list = get_process_list()
    # root_files = get_root_file_list()
    # data = f"Process List:\n{process_list}\n\nRoot Directory Files:\n{root_files}"
    print("Process List:")
    print(process_list)
    get_parent_pid()


if __name__ == "__main__":
    main()