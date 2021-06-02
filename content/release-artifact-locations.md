Title: Release Artifact Locations


<a name="Release-Artifact-Locations"></a>

## Release Artifact Locations

These mappings locate where the release artifacts are being stored:
 
<table class="info"><tr>
  <td valign="top"><img src="images/information.gif" width="16" height="16" border="0">
  <td> Content in //people.apache.org/www/openjpa.org is now under Apache's control. This
folder used to contain build and documentation contents. After CMS migration, this folder is
restricted and become read-only.  
</tr></table>


1. [https://svn.apache.org/repos/asf/openjpa/site/trunk](https://svn.apache.org/repos/asf/openjpa/site/trunk)

    <table>
    <tr><th> Folder </th><th> Descriptions</th></tr>
    <tr><td class="border"> <a href="https://svn.apache.org/repos/asf/openjpa/site/trunk">/</a> </td><td class="border"> Eclipse project home with CMS server start command and build scripts </td></tr>
    <tr><td class="border"> <a href="https://svn.apache.org/repos/asf/openjpa/site/trunk/content">/content</a> </td><td class="border"> OpenJPA home pages (*.mdtext) supported by Apache's Content Management System (CMS)</td></tr>
    <tr><td class="border"> <a href="https://svn.apache.org/repos/asf/openjpa/site/trunk/content/.htaccess">/content/.htacess</a> </td><td class="border"> OpenJPA web pages redirect definitions; use to forward nightly documentation builds to non-svn controlled storage.</tr>
    <tr><td class="border"> <a href="https://svn.apache.org/repos/asf/openjpa/site/trunk/content/artifacts">/content/artifacts</a> </td><td class="border"> files for download from pages</td></tr>
    <tr><td class="border"> <a href="https://svn.apache.org/repos/asf/openjpa/site/trunk/content/images">/content/images</a> </td><td class="border">pictures used by .html</td></tr>
    <tr><td class="border"> <a href="https://svn.apache.org/repos/asf/openjpa/site/trunk/templates/standard.html">/templates/standard.html</a> </td><td class="border">overall frame with navigation, header and footer</td></tr>
    </table>

2. [https://svn.apache.org/repos/infra/websites/production/openjpa/content](https://svn.apache.org/repos/infra/websites/production/openjpa/content) 

    <table>
    <tr><th> Folder </th><th> Descriptions</th></tr>
    <tr><td class="border"> <a href="https://svn.apache.org/repos/infra/websites/production/openjpa/content">/</a> </td><td class="border"> *.html pages converted from *.mdtext after commits.</tr>
    <tr><td class="border"> <a href="https://svn.apache.org/repos/infra/websites/production/openjpa/content/builds">/builds</a> </td><td class="border"> Manuals, Javadoc and RELEASE-NOTES.html of all the official OpenJPA releases.</tr>
    <tr><td class="border"> <a href="https://svn.apache.org/repos/infra/websites/production/openjpa/content/docs">/docs</a> </td><td class="border"> Manuals and Javadoc of incubating OpenJPA releases.</tr>
    <tr><td class="border"> <a href="https://svn.apache.org/repos/infra/websites/production/openjpa/content/mail">/mail</a> </td><td class="border"> Mail archives.</tr>
    </table>   

3. [//people.apache.org/www/openjpa.apache.org/content](https://openjpa.apache.org)

    <table>
    <tr><th> Folder </th><th> Descriptions</th></tr>
    <tr><td class="border"> <a href="https://openjpa.apache.org">/</a> </td><td class="border"> Published contents from <a href="https://svn.apache.org/repos/infra/websites/production/openjpa/content">https://svn.apache.org/repos/infra/websites/production/openjpa/content</a></tr>
    <tr><td class="border"> <a href="https://openjpa.apache.org/builds">/builds</a>, <a href="https://openjpa.apache.org/docs">/docs</a> and <a href="https://openjpa.apache.org/mail">/mail</a> </td><td class="border"> Published contents from https://svn.apache.org/repos/infra/websites/production/openjpa/content/[builds|docs|mail]</tr>
    </table>

4. [https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa](https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa)

    <table>
    <tr><th> Folder </th><th> Descriptions</th></tr>
    <tr><td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa">/\*\*-SNAPSHOT</a> </td><td class="border"> Nightly build binary and source contents from [Jenkin](https://builds.apache.org/)</tr>
    <tr><td class="border"> OPENJPA.\*</td><td class="border"> [Jenkin](https://builds.apache.org/) OpenJPA build jobs</tr>
    </table>
  
5. [//people.apache.org/www/www.apache.org/dist/openjpa](http://www.apache.org/dist/openjpa)

    <table>
    <tr><th> Folder </th><th> Descriptions</th></tr>
    <tr><td class="border"> <a href="http://www.apache.org/dist/openjpa">/\*\*</a> </td><td class="border"> Current distribution content.</tr>
    </table>
  
6. [//people.apache.org/www/archive.apache.org/dist/openjpa](http://archive.apache.org/dist/openjpa)

    <table>
    <tr><th> Folder </th><th> Descriptions</th></tr>
    <tr><td class="border"> <a href="http://archive.apache.org/dist/openjpa">/\*\*</a> </td><td class="border"> Archive contents from //people.apache.org/www/www.apache.org/dist/openjpa; read only.</tr>
    </table>

  