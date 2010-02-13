
.PHONY: all

all: reqtree.png

.PHONY: reqtree.dot

reqtree.dot:
	./bin/rmtoo -m . -f doc/requirements/Config.py \
		-d doc/requirements -c dot -o reqtree.dot -l doc/latex

reqtree.png: reqtree.dot
	dot -Tpng -o reqtree.png reqtree.dot