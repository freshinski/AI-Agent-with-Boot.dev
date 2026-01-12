import os

def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_directory = os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_directory]) == working_dir_abs
    
    if valid_target_dir == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target_directory):
        return f'Error: "{directory}" is not a directory'

    file_info_lines = []
    try:
        for items in os.listdir(target_directory):
            item_path = os.path.join(target_directory, items)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)

            line = f"- {items}: file_size={size} bytes, is_dir={is_dir}"
            file_info_lines.append(line)
        return "\n".join(file_info_lines)

    except Exception as e:
        return f"Error: {str(e)}"