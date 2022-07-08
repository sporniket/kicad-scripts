#!/bin/bash
# Automated test of symbol-generator-ic
# Transform a reference source file, and compare the final result with the reference target file

# inits
TOOL_PATH=".."
SRC="${1}.md"
SRC_NAME="$(basename ${SRC} .md)"
NAME_JSON="${SRC_NAME}.json"
NAME_ITEM="${SRC_NAME}.symbol"
NAME_ITEM_PHY="${SRC_NAME}.phy.symbol"
NAME_ITEM_SOCKET="${SRC_NAME}.socket.symbol"
TARGET="${SRC_NAME}.lib"
TARGET_EXPECTED="${SRC_NAME}.lib.expected"

if [ ! -d tmp ]; then
  echo "Creating tmp directory..."
  mkdir tmp
fi

${TOOL_PATH}/jsonFromDatasheet.py ${SRC} tmp/${NAME_JSON} \
&& ${TOOL_PATH}/libItemFromJsonDatasheet.py tmp/${NAME_JSON} tmp/${NAME_ITEM} \
&& ${TOOL_PATH}/libItemPhyFromJsonDatasheet.py tmp/${NAME_JSON} tmp/${NAME_ITEM_PHY} \
&& ${TOOL_PATH}/libItemPhyFromJsonDatasheet.py --passive tmp/${NAME_JSON} tmp/${NAME_ITEM_SOCKET} \
&& ${TOOL_PATH}/compileSymbols.py tmp/${NAME_ITEM} tmp/${NAME_ITEM_PHY} tmp/${NAME_ITEM_SOCKET} tmp/${TARGET}

if [ -f ${TARGET_EXPECTED} -a "0" -eq $(diff -Z tmp/${TARGET} ${TARGET_EXPECTED} | wc -l) ]; then
  echo "OK"
  exit 0
fi

echo "KO : $(diff -Zq tmp/${TARGET} ${TARGET_EXPECTED})"
diff  --color=always -Z tmp/${TARGET} ${TARGET_EXPECTED}
exit 1
