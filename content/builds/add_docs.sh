#!/bin/sh
# parameter 1 is the project version, e.g. 2.4.1
# parameter 2 is the path to the openjpa binary.zip
# 
# To build the openjpa binary.zip go to the tag and start with 
# $> mvn clean site install -DskipTests -Pjavadoc-profile,docbook-profile,test-derby

mkdir $1
cd $1
mkdir tmp

unzip $2 apache-openjpa-${1}/* -d tmp
mv tmp/apache-openjpa-${1}/docs/javadoc apidocs
mkdir apache-openjpa
mv tmp/apache-openjpa-${1}/RELEASE-NOTES.html apache-openjpa/
mv tmp/apache-openjpa-${1}/docs/docbook apache-openjpa/docs

rm -rf ./tmp
cd ..
