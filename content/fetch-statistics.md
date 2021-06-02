Title: Fetch Statistics

<a name="fetch-statistics"></a>

# Fetch Statistics

The OpenJPA Fetch Statistics Tool (FST) monitors persistent field access
and helps determine which fields in an application are not used. This tool
is a development / test time tool that can help a developer properly tune
an application.

<a name="FetchStatistics-Note"></a>

## Note

* Currently, FST only works with runtime enhancement (javaagent or in JEE
container hook).

* The persistent fields which satisfy all the following conditions will be
tracked :
    * The field is fetched eagerly.
    * The field is not a primary key.
    * The field is not defined as a version field.

<a name="FetchStatistics-Download"></a>

## Download

The latest OpenJPA FST jar file can be download from the [SNAPSHOT Repository](https://repository.apache.org/content/groups/snapshots/org/apache/openjpa/openjpa-fetch-statistics/)
 or can be built from the source code in [svn|https://svn.apache.org/repos/asf/openjpa/trunk/openjpa-tools/openjpa-fetch-statistics/]
 by using Maven 2.2.1 and Java SE 6.

<a name="FetchStatistics-Configuration"></a>

## Configuration
 * JSE - Append the path of openjpa-fetch-statistics-version-SNAPSHOT.jar
file to the classpath prior to lanuching the JVM.
 * [Websphere Application Server](websphere-application-server.html)
 * OSGi -- ?? -- Probably need another module that creates a proper bundle.

<a name="FetchStatistics-StatisticsCollectingandMonitoring"></a>

## Statistics Collecting and Monitoring

There will be a large performance impact when running this tooling. It is
not supported, nor recommended for production use. **This tool should not be
used on a production machine.**

* When this tool is configured, it will be active for all persistence units
in the JVM. Statistics will be dumped via the openjpa.Runtime channel with
the INFO level every 10 minutes, or when the JVM terminates. 

### Example output
        [7/13/12 9:05:44:265 CDT](7/13/12-9:05:44:265-cdt.html)
         00000072 Runtime	I   CWWJP9990I: openjpa.Runtime: Info: Successfully collected fetch statistics from Entities [org.apache.openjpa.test.Address]. The following fields are
        FetchType.EAGER and were never fetched [ total 7 ] : 
        org.apache.openjpa.test.Address.city
        org.apache.openjpa.test.Address.country
        org.apache.openjpa.test.Address.phone
        org.apache.openjpa.test.Address.state
        org.apache.openjpa.test.Address.street1
        org.apache.openjpa.test.Address.street2
        org.apache.openjpa.test.Address.zip

<a name="FetchStatistics-Configurationremoval"></a>

## Configuration removal
* Stop the JVM and reverse the steps completed to configure the tool.
