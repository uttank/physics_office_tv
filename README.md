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
