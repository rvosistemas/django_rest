test_coverage_api_rest:
	@echo "Running tests with coverage..."
	@coverage run --source=api_rest manage.py test
	@coverage report -m
	@coverage html
	@echo "Done."

clean_pycache:
	@echo "Cleaning pycache..."
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -exec rm -rf {} \;
	@echo "Done."