deps:
	pip install -r test_requirements.txt
test:
	#PYTHONPATH= py.test
	- python -m unittest lost_hat_tests.LostHatTests