#!/bin/bash
modelfile=$1
echo "created model from $modelfile:"
cat $modelfile
echo "OLLAMA STUFF"
ollama create phd_answerer -f $modelfile
