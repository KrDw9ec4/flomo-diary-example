import json


def read_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在。")
        return None
    except json.JSONDecodeError:
        print(f"文件 {file_path} 解析失败。")
        return None


def update_json(file_path, updated_data):
    current_data = read_json(file_path)

    if current_data is not None:
        current_data.update(updated_data)

        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(current_data, json_file, ensure_ascii=False, indent=4)
        print(f"文件 {file_path} 更新成功。")
