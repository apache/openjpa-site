Title: Release Management


<a name="ReleaseManagement-ReleaseManagement"></a>


# Release Management

If you are looking for JPA Specification Development, check this [page](jpa-specification-development.html) instead.

How to release OpenJPA, including staging, voting and publishing through
[Apache Trusted Releases (ATR)](https://releases.apache.org/), is described in
[RELEASING.md](https://github.com/apache/openjpa/blob/master/RELEASING.md) in the OpenJPA repository. Version numbering and compatibility
rules are in the [OpenJPA Release Policy](openjpa-release-policy.html).

The pages that described the release process of earlier versions (Nexus process for
1.2.x-2.x, SCP steps for 1.0.x-1.2.x) are superseded by RELEASING.md.

<a name="ReleaseManagement-WhereshouldIputmyfix?"></a>

## Where should I put my fix?
Fixes should be targeted and committed on master first. Any other open
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

<a name="ReleaseManagement-ContinuousBuilds"></a>

## Continuous Builds

Every pull request and every push to master is built with GitHub Actions on Derby and H2;
other databases and the Jakarta Persistence TCK run on a schedule. See the
[workflows](https://github.com/apache/openjpa/actions) of the OpenJPA repository.
