Title: Running the Sun TCK for JPA


<a name="RunningtheSunTCKforJPA-RunningtheSunTCKforJPA"></a>


# Running the Sun TCK for JPA

Sun's Technology Compatibility Kit for JPA is available to OpenJPA
committers (other TCKs are available to Apache committers in general). 

<a name="RunningtheSunTCKforJPA-RequestingaccesstotheTCK"></a>

## Requesting	access to the TCK

1. Review the section "Testing with TCKs" on the [Apache JCP participation page](http://www.apache.org/jcp/priorhistory.html)
1. The OpenJPA project has already requested access. 
1. Sign the [Apache NDA](http://www.apache.org/jcp/ApacheNDA.pdf).
1. Send the signed form to ASF Secretary [secretary@apache.org](mailto:secretary@apache.org). 
  Per email with the Secretary, a scan (pdf) of the signed form is fine.
1. After the NDA has been accepted, then you need to request access to the TCK svn repository via a note to [jcp-open@apache.org](mailto:jcp-open@apache.org).
1. Monitor both your private e-mail and the jcp-open mailing list for the confirmation e-mail that you now have access to the TCK svn repository.
 

The most up to date and complete information can be found on the [Apache JCP participation page](http://www.apache.org/jcp/priorhistory.html). 

## Once you have a copy of the TCK you can execute the TCK bucket in maven.

1. [URL for latest JPA 2.0 TCK](https://svn.apache.org/repos/tck/sun-tcks/persistence/2.0/jpatck-2.0_15-Aug-2011.zip) (authorization gives you access to the full TCK tree)
1. Copy the JPA 2 tck to $\{user.home\}/.m2/privaterepos/jpatck-2.0_15-Aug-2011.zip
1. Run the integration-test maven goal from the openjpa-integration/tck directory:
 
        $  mvn integration-test -Ptck2-profile

More information on running the TCK can be found in the [pom.xml file for the tck module](http://svn.apache.org/repos/asf/openjpa/trunk/openjpa-integration/tck/pom.xml) and the corresponding [ant script for the current tck](http://svn.apache.org/repos/asf/openjpa/trunk/openjpa-integration/tck/tck2-20110815.xml).

## What to do with a new revision of the TCK

Periodically, the TCK is updated by Oracle.  This may be a maintenance release, or it may be due to a new release of the JPA specification.
In either case, there are a few steps that need to be performed to recognize and execute this updated TCK test bucket.

1. Create an xml file specific to the updated TCK.  The name is based off the TCK level and date of the release.
The easiest way is to copy an existing version (ie. tck2-20110815.xml).
1. Update this entry in the newly created xml file to point at the downloaded TCK zip file name:<br>
< property name="tck.level" value="jpatck-2.0_15-Aug-2011" \\>
1. Update the openjpa-integration/tck/pom.xml by modifying this entry appropriately:<br>
< tck2.level \>20110815< /tck2.level>
1. You may also need to create a new tckx-profile, if it's required for a new release of the specification.  I'll leave that as an exercise for
the next editor...

