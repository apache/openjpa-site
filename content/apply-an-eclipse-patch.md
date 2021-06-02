Title: Apply an Eclipse Patch

<a name="ApplyanEclipsePatch-ApplyanEclipsePatchtoDayTrader"></a>

# Apply an Eclipse Patch to DayTrader

You can apply an Eclipse patch to DayTrader for the Criteria API changes

<a name="ApplyanEclipsePatch-SettingupEclipse"></a>

## Setting up Eclipse

First install eclipse by going to&nbsp;[http:/www.eclipse.org](http://www.eclipse.org)
 and downloading a  version of it. These instructions assume version 3.5.
Unzip the  downloaded file into a directory. You can start eclipse by
running  eclipse.exe in the eclipse directory.

Next install subclipse, the Subversion Eclipse Plugin:

1. In Eclipse, go to Help \-> Install New software
1. Click on Add button - Enter Subclipse for Name and [http://subclipse.tigris.org/update_1.6.x](http://subclipse.tigris.org/update_1.6.x)  for  location
1. Select the Subclipse Plugin and click Next \-> Next
1. Read and accept the license and click Finish

Generate eclipse files for the DayTrader project. From the
*DayTrader/branches/2.1.3* directory, type "mvn eclipse:eclipse"

Set the M2_REPO classpath variable in Eclipse:

1. Go to Window \-> Preferences \-> Java \-> Build Path \->  Classpath Variables
1. Add a new variable called M2_REPO, set to the maven repository directory..

Import DayTrader projects into Eclipse.

1. From Eclipse, Click on File \-> Import...
1. Under the General folder, select Existing Projects into Workspace  and click on Next.
1. Enter the root directory of *DayTrader/branches/2.1.3*
1. Select all projects and click Finish

<a name="ApplyanEclipsePatch-ApplyingthePatch"></a>

## Applying the Patch

Replace the following files in your local file system copy of  DayTrader:

* the pom.xml file in the root (*Daytrader/branches/2.1.3*)  directory with [pom.xml](artifacts/pom.xml).
* for Geronimo only - the createDerbyDB.bat\|.sh file in the *DayTrader/branches/2.1.3/bin/dbscripts/derby* directory with the appropriate one of the following:&nbsp;[createDerbyDB.bat](artifacts/createderbydb.bat) or [createDerbyDB.sh](artifacts/createDerbyDB.sh)

Apply these changes:

1. Re-run "mvn eclipse:eclipse" from your *Daytrader/branches/2.1.3* directory.
1. Refresh your eclipse workspace.

Apply the eclipse based patch using the following:

1. Download the appropriate patch:&nbsp;
     1. for Geronimo \-&nbsp; [daytrader_geronimo_eclipse.patch](dartifacts/aytrader_geronimo_eclipse.patch)
     1. for WebSphere - [daytrader_websphere_eclipse.patch](artifacts/daytrader_websphere_eclipse.patch)
1. In the Package Explorer view, select all daytrader projects
1. Right click and select Team \-> Apply Patch
1. Enter the path to the downloaded patch and click _Finish_
