import re

def check_email(email):
    # 이메일 주소 패턴 정의
    # 정규 표현식
    # raw string notation
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # re.search() 함수로 이메일 주소 체크
    match = re.search(email_pattern, email)

    if match:
        return True
    else:
        return False

# 샘플 이메일 주소 10개
sample_emails = [
    'user@example.com',
    'john.doe123@gmail.com',
    'info@company.co.kr',
    'test_email@domain.net',
    'invalid_email',
    'missing@dotcom',
    'name@.dotmissing',
    '@missingusername.com',
    'user@.missingtld.',
    'user@company..doubleperiod'
]

# 샘플 이메일 주소를 체크하고 결과 출력
for email in sample_emails:
    result = check_email(email)
    print(f'{email}: {"Valid" if result else "Invalid"}')
