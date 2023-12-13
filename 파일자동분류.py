import os
import shutil

def move_files_by_extension(src_folder, dest_folder, extensions):
    # 폴더가 존재하지 않으면 생성
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # 소스 폴더에서 파일 목록을 얻음
    files = [f for f in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, f))]

    for file in files:
        # 파일의 확장자를 소문자로 가져옴
        ext = os.path.splitext(file)[-1].lower()

        # 지정된 확장자에 해당하는 파일을 이동
        if ext in extensions:
            src_path = os.path.join(src_folder, file)
            dest_path = os.path.join(dest_folder, file)

            # 파일 이동
            shutil.move(src_path, dest_path)
            print(f"Moved: {file} to {dest_folder}")

# 'C:\Users\student\Downloads'에서 이미지 파일을 'C:\Users\student\images' 폴더로 이동
move_files_by_extension(r'C:\Users\student\Downloads', r'C:\Users\student\Downloads\images', ['.jpg', '.jpeg'])

# 'C:\Users\student\Downloads'에서 CSV 및 Excel 파일을 'C:\Users\student\data' 폴더로 이동
move_files_by_extension(r'C:\Users\student\Downloads', r'C:\Users\student\Downloads\data', ['.csv', '.xlsx'])

# 'C:\Users\student\Downloads'에서 PDF 파일을 'C:\Users\student\docs' 폴더로 이동
move_files_by_extension(r'C:\Users\student\Downloads', r'C:\Users\student\Downloads\docs', ['.pdf'])