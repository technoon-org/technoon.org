.PHONY: deps generate

deps:
	sudo apt install pandoc
generate:
	python3 generate.py
