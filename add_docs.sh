#!/bin/sh
# Copies the documentation of a release into this branch.
#
# parameter 1 is the project version, e.g. 4.2.0
# parameter 2 is the path to apache-openjpa-<version>-binary.zip from the release
# parameter 3 (optional) is the aggregated javadoc of the release, as a directory or
#             as a jar/zip, used when the binary zip contains no docs/javadoc (see
#             RELEASING.md in the openjpa repository for how to build it)
#
# Layouts:
# - up to 4.1.x the binary zip has docs/docbook (multi page manual with main.html,
#   manual.html and manual.pdf) and docs/javadoc
# - from 4.2.0 the manual is built with AsciiDoc: docs/multihtml/manual.html,
#   docs/html/manual.html and docs/manual.pdf; the javadoc is not in the zip
#
# Result: <version>/apache-openjpa/RELEASE-NOTES.html, <version>/apache-openjpa/docs/...
#         and <version>/apidocs/
set -e

if [ $# -lt 2 ]; then
    echo "usage: $0 <version> <apache-openjpa-version-binary.zip> [javadoc directory or jar]" >&2
    exit 1
fi
VERSION=$1
ZIP=$(cd "$(dirname "$2")" && pwd)/$(basename "$2")
JAVADOC=
if [ -n "$3" ]; then
    JAVADOC=$(cd "$(dirname "$3")" && pwd)/$(basename "$3")
fi
SRC=tmp/apache-openjpa-${VERSION}

mkdir "$VERSION"
cd "$VERSION"
mkdir tmp
unzip -q "$ZIP" "apache-openjpa-${VERSION}/*" -d tmp

mkdir apache-openjpa
mv "$SRC/RELEASE-NOTES.html" apache-openjpa/

if [ -d "$SRC/docs/docbook" ]; then
    mv "$SRC/docs/docbook" apache-openjpa/docs
else
    mkdir apache-openjpa/docs
    mv "$SRC/docs/multihtml" apache-openjpa/docs/multihtml
    mv "$SRC/docs/html" apache-openjpa/docs/html
    mv "$SRC/docs/manual.pdf" apache-openjpa/docs/manual.pdf
fi

if [ -d "$SRC/docs/javadoc" ]; then
    mv "$SRC/docs/javadoc" apidocs
elif [ -d "$JAVADOC" ]; then
    cp -R "$JAVADOC" apidocs
elif [ -n "$JAVADOC" ]; then
    mkdir apidocs
    (cd apidocs && unzip -q "$JAVADOC" -x 'META-INF/*')
else
    echo "WARNING: no javadoc in $2 and none given as third parameter" >&2
fi

rm -rf ./tmp
cd ..
