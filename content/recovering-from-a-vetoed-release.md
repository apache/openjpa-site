Title: Recovering from a vetoed release

<a name="Recoveringfromavetoedrelease-Recoveringfromabadreleaseoravetoedrelease"></a>


## Recovering from a bad release or a vetoed release

Recovering from a bad release actually isn't that difficult. You'll have to delete the bad tag in SVN and rollback the version numbers in all of our pom.xml files. 

<a name="Recoveringfromavetoedrelease-Deletethetaginsvn"></a>

### Delete the tag in svn
    $ svn del https://svn.apache.org/repos/asf/openjpa/tags/1.2.0 -m "Rollback release"

### Rollback version numbers
If you have perl installed you can do this in a single command for example to rollback from 1.2.1-SNAPSHOT to 1.2.0-SNAPSHOT

    $ perl -pi -e "s;<version>1.2.1-SNAPSHOT</version>;<version>1.2.0-SNAPSHOT</version>;g" \
        pom.xml */pom.xml */*/pom.xml

If you do not have perl installed you can use a similar tool to edit multiple files or edit them all by hand.
