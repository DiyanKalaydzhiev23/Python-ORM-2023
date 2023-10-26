import os
import zipfile


def delete_old_zip(zip_name):
    """
    Delete the zip file if it already exists.

    :param zip_name: Name of the zip file to be deleted.
    """
    if os.path.exists(zip_name):
        os.remove(zip_name)
        print(f"Deleted old {zip_name}")
    else:
        print(f"{zip_name} does not exist, skipping delete.")


def zip_current_level(exclude_list, zip_name="output.zip"):
    """
    Zip every folder and file at the current level.

    :param exclude_list: List of folders and files to be excluded.
    :param zip_name: Name of the resulting zip file.
    """

    # Delete old zip if it exists
    delete_old_zip(zip_name)

    # Get all folders and files in the current directory
    items = os.listdir()

    # Remove items from the exclude_list
    items_to_zip = [item for item in items if item not in exclude_list]

    # Create a zip archive
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for item in items_to_zip:
            if os.path.isfile(item):
                zipf.write(item)
            elif os.path.isdir(item):
                for dirpath, dirnames, filenames in os.walk(item):
                    for filename in filenames:
                        file_path = os.path.join(dirpath, filename)
                        arcname = os.path.relpath(file_path, start='.')
                        zipf.write(file_path, arcname=arcname)


if __name__ == "__main__":
    # List of folders and files to be excluded
    exclude_list = ["venv", ".idea", "templates"]

    zip_current_level(exclude_list)
    print(f"Files and folders zipped into 'output.zip' excluding {exclude_list}")