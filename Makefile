clean:
	rm -rf build/ dist/ change_finder.egg-info/
build: clean
	python setup.py bdist_wheel --universal
install:
	pip install ./dist/*.whl
test: install
	py.test --pep8 .
