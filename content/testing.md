Title: Testing

<a name="Testing"></a>


# Running and [Writing](writing-test-cases-for-openjpa.html) Tests with OpenJPA

OpenJPA's unit tests are written using JUnit. For a template for a simple
test case, see the code for [TestPersistence.java](http://svn.apache.org/viewvc/openjpa/trunk/openjpa-persistence-jdbc/src/test/java/org/apache/openjpa/persistence/simple/TestPersistence.java?view=markup)
.

If you want to contribute your own test case then follow the [guidelines](writing-test-cases-for-openjpa.html)
.

Once you have downloaded and built OpenJPA (see [Building](building.html)
), you can run individual tests using the "test" goal to maven. For
example:

    mvn test -DfailIfNoTests=false -Dtest=TestPersistence
    
 <table class="note"><tr>
  <td valign="top"> <IMG src="images/warning.gif" width="16" height="16" border="0">
  <td>By default Maven will fail if there are no testcases found in any
module you build. The examples solve this by specifying
-DfailIfNoTests=false but you can also change your personal default by
adding the following to ${user.home}/.m2/settings.xml :

 
    	<profile>
    	    <id>enable-no-tests</id>
    	    <activation>
    		<activeByDefault>true</activeByDefault>
    	    </activation>
    	    <properties>
    		<failIfNoTests>false</failIfNoTests>
    	    </properties>
    	</profile>
    	
 </tr></table>

To get more debugging information (e.g., to see the SQL that is being
executed against the database), you can enable trace-level logging from the
command line using the "openjpa.Log" system property. For example:

    $ mvn test -DfailIfNoTests=false -Dtest=TestPersistence -Dopenjpa.Log=DefaultLevel=TRACE
    
    [INFO] Scanning for projects...
    [INFO] Reactor build order: 
    ...
    690  test  TRACE  [main] openjpa.jdbc.SQL - <t 4261185, conn 3061987> executing prepstmnt 12659709 
       INSERT INTO AllFieldTypes (id, arrayOfStrings, booleanField, byteField, charField, dateField, 
       doubleField, floatField, intField, longField, shortField, stringField) 
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) [params=(long) 601, (null) null, (int) 0, (byte) 0, 
       (int) 0, (null) null, (double) 0.0, (float) 0.0, (int) 0, (long) 0, (short) 0, (null) null]
    701  test  TRACE  [main] openjpa.jdbc.SQL - <t 4261185, conn 3061987> [11 ms] spent
    701  test  TRACE  [main] openjpa.jdbc.JDBC - <t 4261185, conn 3061987> [0 ms] commit
    702  test  TRACE  [main] openjpa.jdbc.JDBC - <t 4261185, conn 0> [0 ms] close
    ...
    $

<a name="Testing-SettingadditionalLogparameters"></a>

## Setting additional Log parameters

There are several parameters that are used by OpenJPA Log. Here are some
that might be of value when debugging test cases. Note that the logger
names are case sensitive while the log levels are not.

* DefaultLevel sets the level for all loggers that are not otherwise set
* file sets the file name for logging output
* Enhance logs messages from the enhancer
* Metadata logs messages from the metadata processor
* Tool logs messages from the schema synchronization tool
* SQL logs messages from the SQL generator
* JDBC logs messages related to JDBC
* Schema logs messages related to schema
* Runtime logs messages related to runtime
* Query logs messages related to queried
* DataCache logs messages related to caching

Log levels specify the minimum log message that is output. All log messages
with a level higher than the log level set for a logger are output. So if
INFO is specified, log messages of level INFO, WARN, ERROR, and SEVERE are
output.

* TRACE
* INFO
* WARN
* ERROR
* FATAL

For example, to avoid enhancement warnings, get detailed SQL information,
and write the log data to a file:

    mvn test -Dtest=TestPersistence -Dopenjpa.Log=Enhance=ERROR,SQL=TRACE,file=openjpa.log
    
# Testing against alternate databases
    
By default, OpenJPA uses the [Derby](http://db.apache.org/derby/)
database for testing. The `openjpa-persistence-jdbc/pom.xml` POM
declares various pre-defined databases against which tests can be executed.
For example, to test against the stand-alone [HSQLDB](http://hsqldb.org/)
 database, you can run with the "test-hsqldb" profile:
    
    mvn test -DfailIfNoTests=false -Dtest=TestPersistence -Ptest-hsqldb

For databases that are not in the pre-defined list, you can manually
specify connection parameters to use for testing under the "test-custom"
profile. You will need to manually provide the driver class and specify all
of the connection parameters. For example, to test against Oracle, you
might run:


    mvn test -DfailIfNoTests=false -Dtest=TestPersistence -Ptest-custom \
      -Dopenjpa.custom.driverjar=$(pwd)/drivers/jdbc-oracle-10_2_0_1_0.jar \
      -Dopenjpa.custom.driverclass=oracle.jdbc.driver.OracleDriver \
      -Dopenjpa.custom.url=jdbc:oracle:thin:@HOST:PORT:DBNAME \
      -Dopenjpa.custom.username=USERNAME \
      -Dopenjpa.custom.password=PASSWORD


If you frequently need to test against another database, you can
permanently declare the database connection parameters in the
`~/.m2/settings.xml` file under a custom profile. For example:


    <settings>
        <profiles>
    	<profile>
    	    <id>test-oracle</id>
    	    <properties>
    		<test-custom>true</test-custom>    	       
            <openjpa.custom.driverjar>${user.home}/.m2/privaterepos/jdbc-oracle-10_2_0_1_0.jar</openjpa.custom.driverjar>
            <openjpa.custom.driverclass>oracle.jdbc.driver.OracleDriver</openjpa.custom.driverclass>    	       
            <openjpa.custom.url>jdbc:oracle:thin:@HOST:PORT:DBNAME</openjpa.custom.url>
    		<openjpa.custom.username>USERNAME</openjpa.custom.username>
    		<openjpa.custom.password>PASSWORD</openjpa.custom.password>
    	    </properties>
    	</profile>
        </profiles>
    </settings>


This profile can then be executed by running:

    mvn test -DfailIfNoTests=false -Dtest=TestPersistence -Ptest-custom,test-oracle

<a name="Testing-RunningJUnitsinEclipse"></a>

# Running JUnits in Eclipse

You'll probably want to setup a Debug Configuration in Eclipse for running
the JUnit testcases.

1. Run --> Debug Configurations...  Create a new JUnit configuration

    ![eclipse_dbgcfg_1.png](images/eclipse_dbgcfg_1.png)

1. For the Test tab - Give the configuration a Name, select a Project and
Test class, and you'll probably want to select the "Keep JUnit running..."
option.

    ![eclipse_dbgcfg_2.png](images/eclipse_dbgcfg_2.png)

1. For the Arguments tab - Press the Variables... button. This will allow us
to define variables that can be shared across other Release/Debug
Configurations within this workspace.

    ![eclipse_dbgcfg_3.png](images/eclipse_dbgcfg_3.png)

1. For the Select Variable window - Press the Edit Variables... button.

    ![eclipse_dbgcfg_4.png](images/eclipse_dbgcfg_4.png)

1. For the Preferences windows - Press New... to add two variables.
    ![eclipse_dbgcfg_5.png](images/eclipse_dbgcfg_5.png)

        Name = openjpa.trace
        Value = -Dopenjpa.Log=DefaultLevel=TRACE
        Description = Set OpenJPA logging to TRACE

    ![eclipse_dbgcfg_6.png](images/eclipse_dbgcfg_6.png)

        Name = connect.derby
        Value = -Dopenjpa.ConnectionDriverName=org.apache.derby.jdbc.EmbeddedDriver
            -Dopenjpa.ConnectionURL=jdbc:derby:target/database/openjpa-derby-database;create=true
        Description = Connection properties for Derby

    ![eclipse_dbgcfg_7.png](images/eclipse_dbgcfg_7.png)

1. After the above are created and saved, add the new variables as VM Arguments.

        ${openjpa.trace}
        ${connect.derby}

    ![eclipse_dbgcfg_8.png](images/eclipse_dbgcfg_8.png)
