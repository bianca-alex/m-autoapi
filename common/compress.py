import os
import zipfile
from common.settings import get_runtime_path
from common.settings import get_report_path
from datetime import datetime

class Compressor:
    def __init__(self, directory_path, output_path):

        self.directory_path = os.path.join(get_report_path(),directory_path)
        self.output_path = os.path.join(get_runtime_path(), output_path + ".zip")

    def compress(self):
        
        with zipfile.ZipFile(self.output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(self.directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, self.directory_path))

if __name__ == "__main__":
    # 示例用法
    directory_path = '/path/to/directory'  # 要压缩的目录路径
    output_path = '/path/to/output.zip'  # 压缩文件的输出路径

    compressor = Compressor(directory_path, output_path)
    compressor.compress()
