#!/bin/bash
# Automated test of symbol-generator-ic
# Performs a suite of tests
test() {
	echo "================<[ ${1} ]>================"
	./validate-item.bash $2
}

test "it should generate symbols as expected" falcon_combel
test "it should not miss pins in the single unit functionnal symbol" pal20r6
