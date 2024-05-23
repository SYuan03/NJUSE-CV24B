import os


def rename_images(directory, prefix):
    # 获取目录下的所有文件
    files = os.listdir(directory)

    # 对每个文件进行重命名
    for i, file in enumerate(files, start=1):
        # 构造新的文件名
        new_name = f"{prefix}_{i}.jpg"
        # 获取旧文件的完整路径
        old_file_path = os.path.join(directory, file)
        # 获取新文件的完整路径
        new_file_path = os.path.join(directory, new_name)
        # 重命名文件
        os.rename(old_file_path, new_file_path)
        print(f'Renamed file {old_file_path} to {new_file_path}')


# 使用函数
# rename_images('./images', 'bdl')
rename_images('./images/query', 'q')
