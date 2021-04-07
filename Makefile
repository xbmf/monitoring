#!make
include .env.test
export $(shell sed 's/=.*//' .env.test)

.PHONY: consumer-format consumer-install producer-install consumer-test producer-test producer-format install format test

consumer-format :
	pushd consumer && python -m black . && popd
consumer-install:
	@echo "installing consumer started"
	pushd consumer && pip install -r requirements.txt && popd
	pushd consumer && python import.py && popd
	@echo "installing consumer finished"

consumer-test:
	@echo "testing consumer started"
	pushd consumer && python -m green -vvv -s 1 . && popd
	@echo "testing consumer finished"

producer-format :
	pushd producer && python -m black . && popd

producer-install:
	@echo "installing producer started"
	pushd producer && pip install -r requirements.txt && popd
	@echo "installing producer finished"

producer-test:
	@echo "testing producer started"
	@pushd producer && python -m green -vvv -s 1 . && popd
	@echo "testing producer finished"

install : consumer-install producer-install
	cp ca.pem ./consumer
	cp ca.pem ./producer
	@echo "installing finished"
test : consumer-test producer-test
	@echo "test finished"
format : consumer-format producer-format
	@echo "formatting completed"
