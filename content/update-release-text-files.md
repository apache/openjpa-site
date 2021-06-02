Title: Update release text files


<a name="Updatereleasetextfiles-Updatingreleasetextfiles."></a>

# Updating release text files.

<a name="Updatereleasetextfiles-ObtainingthelistofresolvedissuesfromJIRA.&nbsp;"></a>

## Obtaining the list of resolved issues from JIRA.&nbsp;

1. Go to the main JIRA releases page at [http://issues.apache.org/jira/browse/OPENJPA?report=com.sourcelabs.jira.plugin.portlet.releases:releases-projecttab](http://issues.apache.org/jira/browse/OPENJPA?report=com.sourcelabs.jira.plugin.portlet.releases:releases-projecttab)
1. Under Unreleased find the version you're about to release and click on
"Release Notes".
Keep this page open since it contains a nice reference point for many of
the documents you will edit.

<a name="Updatereleasetextfiles-Updatetextfiles"></a>

## Update text files

* openjpa-projects/CHANGES.txt
    * Update the overview paragraph with the new version and a brief description of the release.
    * Remove the previous changes section and replace with a url to the location in SVN. _This is similar to what HTTPD does in its CHANGES file_
    * Create a new section : OpenJPA x.y.z changes and copy the JIRA issues resolved in this section. You may want to do some minor editing by hand to ensure the file respects the 80 character column width guideline.
* openjpa-project/RELEASE-NOTES.html
    * Similar to CHANGES.txt you need to update the version number and provide a brief description of the release.
    * Remove the previous list of changes for the previous release. Replace this with a link to the last release's file in SVN.
    * Add a new section. This can be copied from the JIRA page with one exception (see the next step).
    * Update the links at the top of the file. If you've copied changes from JIRA you'll see a section like this :

             <h2> Bug </h2>
             
        Replace it with :

             <h4><a name='Bug'>Bug</h4>

        You should also check the links at the top to make sure they are all valid.

* openjpa-project/NOTICE.txt
NOTICE.txt "usually" does not need to be updated. The exceptions are when a new dependency has been introduced (ie a new version of Serp) or if a new source file containing a copyright notice is introduced.

* openjpa-project/LICENSE.txt
Similar to NOTICE.txt this file does not require updating in each release. It should contain the current version of the Apache license, and any other licenses mentioned in NOTICE.txt.

* openjpa-project/README.txt
This file rarely needs updating - just make sure the URL is accurate.

* openjpa-project/BUILDING.txt
This file rarely needs updating. 
