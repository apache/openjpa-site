Title: Using Criteria API in DayTrader

<a name="UsingCriteriaAPIinDayTrader-UsingCriteriaAPIinDayTrader"></a>

# Using Criteria API in DayTrader

A current DayTrader project implementation in Apache Geronimo contains
several JPQL queries. These can easily be converted to JPA Criteria API
queries. A sample with this conversion can be created to run on either the
Apache Geronimo server or the WebSphere Application Server with the
built-in Derby database.


<a name="UsingCriteriaAPIinDayTrader-DownloadingDayTrader"></a>

## Downloading DayTrader

You must have Subversion installed in order to download the DayTrader implementation.Subversion can be downloaded from&nbsp;[http://subversion.apache.org/packages.html](http://subversion.apache.org/packages.html)
. Use the 2.1.3 version of DayTrader for this sample. Follow the following steps:

1. Create a root directory for the download. For this example, we will use a directory called *DayTrader*.
2. Create subdirectories **branches/2.1.3** under the **DayTrader** directory
3. cd to **DayTrader**
4. Issue the following subversion command:

        svn checkout https://svn.apache.org/repos/asf/geronimo/daytrader/branches/2.1.3 branches/2.1.3 .

<a name="UsingCriteriaAPIinDayTrader-BuildDayTrader"></a>

## Build DayTrader

You must have maven installed in order to build DayTrader. Maven can be downloaded from <http://maven.apache.org/download.html>. Unzip the file to a directory and run mvn.bat\|.sh in the bin
subdirectory to install. Add the bin subdirectory to you system path.

Maven needs a repository. Typically it is at the following:

* **Windows** - C:\Documents and Settings\<userid>\.m2\repository
* **Linux/unix** - \~/.m2/repository

From the **DayTrader/branches/2.1.3** directory, type "mvn clean install" to build the project. (Note: If you see errors that say "java.util.zip.ZipException: error in opening zip file", ignore them for this exercise.) 

<a name="UsingCriteriaAPIinDayTrader-ApplytheDayTraderPatch"></a>

## Apply the DayTrader Patch

The following patch can be applied using a system or downloaded *patch* utility. (For example, you can get a patch utility for Windows from&nbsp;[http://gnuwin32.sourceforge.net/packages/patch.htm](http://gnuwin32.sourceforge.net/packages/patch.htm)
.)

* Geronimo - [daytrader_geronimo.patch](artifacts/daytrader_geronimo.patch)
* WebSphere - [daytrader_websphere.patch](artifacts/daytrader_websphere.patch)

Download the appropriate patch and go to the *DayTrader/branches.2.1.3*
directory to apply it. For example, with the patch utility mentioned above,
you can type:

    patch \-p0 \-i <path-to>/daytrader_geronimo.patch

After you have applied the patch, you can see the changes from JPQL to the Criteria API in the java class org.apache.geronimo.samples.daytrader.ejb3.TradeSLSBBean. The changes are in the following 4 methods:

* getMarketSummary()
* getClosedOrders()
* getAllQuotes()
* getHoldings()

(Note: If you view these changes in eclipse, and you have previously run
"mvn eclipse:eclipse" to setup eclipse projects, you'll have to run this
command again in order for this file to compile.)

You can also [Apply an Eclipse Patch](apply-an-eclipse-patch.html)

<a name="UsingCriteriaAPIinDayTrader-Re-createtheDayTraderearfile"></a>

## Re-create the DayTrader ear file

From the **DayTrader/branches/2.1.3** directory, type "mvn clean install" to build the project.
                                                                 
<a name="UsingCriteriaAPIinDayTrader-RunDayTraderonGeronimo"></a>

## Run DayTrader on Geronimo

This writeup assumes some familiarity with Apache Geronimo. The download
and documentation can be found at [http://geronimo.apache.org.](http://geronimo.apache.org/)

Install and start the Geronimo server.

Add jpa2 plugins from repository [http://geronimo.apache.org/plugins/openjpa2](http://geronimo.apache.org/plugins/openjpa2). One way to do this is the following:

1. Go to the Geronimo console at http://<host>:8080/console and logon
2. Select _plugins_
3. Click on _Add Repository_ and add [http://geronimo.apache.org/plugins/openjpa2](http://geronimo.apache.org/plugins/openjpa2)
4. Click on _Update Repository List_
5. Make sure the new repository is selected. Then click on _Show Plugins in selected repository._ On that panel:
    1. Select _GeronimoPlugins, OpenJPA2::CAR 2.1.3-SNAPSHOT_ and _GeronimoPlugins, OpenJPA2::Deployer 2.1.3-SNAPSHOT_
    2. Click on _Install_
6. On the next screen, click on _Install_

Deploy the DayTrader application. This can be done through the console as follows:

1. Click on _Deploy New_
2. For _Archive_, browse to DayTrader/branches/2.1.3/modules/ear/target/daytrader-ear-2.1.3.ear
3. For _Plan,_ browse to DayTrader/branches/2.1.3/plans/dayTrader-derby-plan.xml
4. Check _Start app after install_
5. Click on _Install_

Re-start the server.

Make sure that the system module, org.apache.geronimo.configs/axis-deployer/2.1.5/car, is running.

Run DayTrader:

1. Go to http://<host>:8080/daytrader/
1. Click on the _Configuration_ tab and click on _(Re)-create DayTrader Database Tables and Indexes_
1. Click on the _Configuration&nbsp;_ tab and click on _(Re)-populate DayTrader Database_
1. Click on the _Trading & Portfolios_ tab, login, and start trading

<a name="UsingCriteriaAPIinDayTrader-RunDayTraderonWebSphere"></a>

## Run DayTrader on WebSphere

This writeup assumes some familiarity with WebSphere. Also, the script that
is provided assumes a local unmanaged node with a single server.

At a minimum, the WebSphere Application Server must be at version 7.0.0.9.
You must also have installed the Feature Pack for OSGi Applications and
Java Persistence API 2.0. Make sure you have a profile that is augmented
for JPA 2.0 function.

Download the following jython script. This script is used to configure the
objects needed by DayTrader (data sources, JMS queues and topics) and
install the application.

[daytrader_singleServer.py](artifacts/daytrader_singleserver.py)


Within the bin directory of the augmented profile:

1. Start the server.
1. Run the script using the following command:

        wsadmin -f <location ofdaytrader_singleServer.py> ${script options}

   You can display the list of available script options by specifying the option "--help".

1. Re-start the server.

Run DayTrader

1. On a web browser, go to http://localhost:<application-port>/daytrader/ (The default application port is 9080. But, you may have a different one if you created a new profile.)
1. Click on the _Configuration_ tab and click on _(Re)-create  DayTrader Database Tables and Indexes_
1. Click on the _Configuration&nbsp;_ tab and click on _(Re)-populate DayTrader Database_
1. Click on the _Trading & Portfolios_ tab, login, and start  trading
