clean:
	rm -rf build/ dist/
build: clean
	python setup.py build bdist_wheel
test:
	PYTHONPATH=. py.test --pep8 .
