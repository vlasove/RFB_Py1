pip install flake8 autopep8 pylint

# Для запуска flake8
flake8 test.py
# Для запуска autopep8
# 1.1 С ПРОСМОТРОМ ИЗМЕНЕНИЙ
autopep8 test.py
# 1.2 С ПРИМЕНЕНИЕМ ИЗМЕНЕНИЙ
autopep8 --in-place test.py


# Для запуска pylint
python -m pylint test.py