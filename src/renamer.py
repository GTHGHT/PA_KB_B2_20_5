import os


def renamer(path):
    for folder in os.listdir(path):
        files = os.listdir(os.path.join(path, folder))

        for i, file in enumerate(files):
            os.rename(
                os.path.join(path, folder, file),
                os.path.join(path, folder, f"{i:04}{file[file.rfind('.'):]}")
            )


if __name__ == '__main__':
    train_path = r'C:\xampp\htdocs\PA\PA_KB_B2_20_5\datasets\train'
    val_path = r'C:\xampp\htdocs\PA\PA_KB_B2_20_5\datasets\val'
    renamer(train_path)
    renamer(val_path)
