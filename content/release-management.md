Title: Release Management


<a name="ReleaseManagement-ReleaseManagement"></a>


# Release Management

If you are looking for JPA Specification Development, check this [page](jpa-specification-development.html) instead.

<UL>
<LI><A href="apache-nexus-release-process-(1.2.x-2.1.x).html" title="Apache Nexus Release Process (1.2.x-2.x)">Apache Nexus Release Process (1.2.x-2.x)</A>
 <UL>
 <LI><A href="release-setup.html" title="Release Setup">Release Setup</A></LI>
 <LI><A href="release-artifact-locations.html" title="Release Artifact Locations">Release Artifact Locations</A></LI>
 </UL></LI>
<LI><A href="publishing-serp-to-maven-central-repository.html" title="Publishing Serp to Maven Central Repository">Publishing Serp to Maven Central Repository</A></LI>
<LI><A href="releasing-openjpa-1.0.x-or-1.1.x-(old-scp-steps).html" title="Releasing OpenJPA 1.0.x or 1.1.x (Old SCP Steps)">Releasing OpenJPA 1.0.x or 1.1.x (Old SCP Steps)</A>
 <UL><LI><A href="openjpa-release-policy.html" title="OpenJPA Release Policy">OpenJPA Release Policy</A></LI>
 </UL></LI>
<LI><A href="releasing-openjpa-1.2.x-(old-scp-steps).html" title="Releasing OpenJPA 1.2.x (Old SCP Steps)">Releasing OpenJPA 1.2.x (Old SCP Steps)</A>
 <UL>
 <LI><A href="recovering-from-a-vetoed-release.html" title="Recovering from a vetoed release">Recovering from a vetoed release</A></LI>
 <LI><A href="running-openjpa-examples.html" title="Running OpenJPA Examples">Running OpenJPA Examples</A></LI>
 <LI><A href="update-release-text-files.html" title="Update release text files">Update release text files</A></LI>
 <LI><A href="verifying-release-signatures.html" title="Verifying release signatures">Verifying release signatures</A></LI>
 </UL></LI>
</UL>


<a name="ReleaseManagement-WhereshouldIputmyfix?"></a>

## Where should I put my fix? 
Fixes should be targeted and committed on trunk first. Any other open
releases are fair game, but may require approval from a release manager. 

<a name="ReleaseManagement-RegardingReleaseManagers"></a>

## Regarding Release Managers
Once a formal release of OpenJPA has been approved, a release manager is assigned. The release manager is often (but not always) the same developer who performed the release. This release manager role is intended to be a long term branch maintainer who looks after the stability of a formal release. 

The release manager(s) is(are) responsible for targeting fixes into a given version of OpenJPA.

* Release managers may indicate this by targeting a JIRA issue for their branch or may issue a blanket statement that any fix will be accepted. 
* In general only the release manager(s) should target a JIRA issue for a branch which they support. 
    * An exception to this rule is if the RM has committed changes for their branch and forgot to update the JIRA issue. 
* Fixes should not be committed without RM approval. These changes may be reverted by the release manager. 

<a name="ReleaseManagement-Somegeneralguidelinesforreleasemanagers"></a>

## Some general guidelines for release managers
* Fixes which are committed to an earlier release should also be present
"up-stream". Ie a fix for 1.0.x should also appear in 1.2.x. 
* Issues may not apply to every release, so the previous guideline may not
always apply.

<a name="ReleaseManagement-ReleaseManagersforactivebranches."></a>

## Release Managers for active branches.
The current release managers for the active branches of OpenJPA are :

<table border="0.5">
<tr bgcolor="lightyellow"><th> branch </th><th> internal release number </th><th> release manager(s)</th><th> Contact
Release Manager before committing </th></tr>
<tr><td class="border"> 0.9.7-r547073 </td><td class="border"> </td><td class="border"> Srinivasa Segu </td><td class="border"> Yes </td></tr>
<tr><td class="border"> 1.0.x </td><td class="border"> 1.0.5-SNAPSHOT </td><td class="border"> Heath Thomann, Donald Woods </td><td class="border"> Yes </td></tr>
<tr><td class="border"> 1.1.x </td><td class="border"> 1.1.1-SNAPSHOT </td><td class="border"> Patrick Linskey, Abe White </td><td class="border"> Yes </td></tr>
<tr><td class="border"> 1.2.x </td><td class="border"> 1.2.3-SNAPSHOT </td><td class="border"> Heath Thomann, Donald Woods </td><td class="border">  Yes </td></tr>
<tr><td class="border"> 1.3.x </td><td class="border"> 1.3.0-SNAPSHOT </td><td class="border"> N/A (*) </td><td class="border"> No </td></tr>
<tr><td class="border"> 2.0.x </td><td class="border"> 2.0.2-SNAPSHOT </td><td class="border"> Donald Woods, Heath Thomann </td><td class="border"> Yes </td></tr>
<tr><td class="border"> 2.1.x </td><td class="border"> 2.1.1-SNAPSHOT </td><td class="border"> Heath Thomann </td><td class="border"> Yes </td></tr>
<tr><td class="border"> 2.2.x </td><td class="border"> 2.2.2-SNAPSHOT </td><td class="border"> Heath Thomann, Albert Lee </td><td class="border"> Yes </td></tr>
<tr><td class="border"> 2.2.1.x </td><td class="border"> 2.2.1.1-SNAPSHOT </td><td class="border"> Heath Thomann, Albert Lee </td><td class="border"> Yes </td></tr>
<tr><td class="border"> 2.3.x </td><td class="border"> 2.3.0-SNAPSHOT </td><td class="border"> Mark Struberg</td><td class="border"> No </td></tr>
<tr><td class="border"> 2.4.x </td><td class="border"> 2.4.2-SNAPSHOT </td><td class="border"> Mark Struberg</td><td class="border"> No </td></tr>
<tr><td class="border"> trunk </td><td class="border"> 3.0.0-SNAPSHOT </td><td class="border"> N/A (*)</td><td class="border"> No </td></tr></table>
 **\*** There are no formal releases for these branches.


<a name="ReleaseManagement-ContinuousBuilds"></a>

## Continuous Builds

We are using the Apache Hudson server for continuous builds of several releases.  Please checkout the [Automated Builds](automated-builds.html) page for more details.



