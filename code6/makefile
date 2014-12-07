apr:
	./apriori -s4 -c50 -m2 -tr -R labels.txt docs.txt output.txt

accuracy:
	python test.py output.txt docs.txt results.txt

shell:
	python shell.py docs.txt labels.txt 60 3 50

