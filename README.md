# physics_office_tv

django model

1. 제목 - title
2. 작성자 - author
3. 홍보기간 - period - 달력형식이면 좋겠다. start, end 두개의 필드
4. 게시여부 - boolean
5. 에디터 - django-tinymce
6. 작성일 - created
7. 최종수정일 - modified

mkdir work/physics*office_tv && cd \$*
mkdir backend frontend
git init
vi .gitignore
venv/
\*.pyc
**pycache**/

python -m venv venv
source venv/Script/activate
pip install django djangorestframework
mkdir env
pip freeze > ./env/requirements.txt
cd backend
django-admin startproject sdid
django-admin startapp tv
pip install django-tinymce4-lite

# urls.py 에서 include 쓸려면 추가해 줘야 한다.

from django.urls import include

# rest_framework, tinymce 를 urls.py 에 추가해 줬는데 에러남

# python manager createsuperuser 는 python manager migrate 하고 해야 한다

# python manager runserver - 오래 안 쓰긴 했나보다.

# app 은 manager.py 과 같은 level directory 에 있어야 함 ....

# utls.py 에서 tinymce 를 추가해 주지 않아도 admin 메뉴에서 사용할 수 있다.
