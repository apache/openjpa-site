Title: OpenJPA Release Policy

<a name="OpenJPAReleasePolicy-OpenJPAReleasePolicy"></a>

# OpenJPA Release Policy

<a name="OpenJPAReleasePolicy-ReleaseNumbering"></a>

## Release Numbering
The release number consists of three digits separated by decimal points,
followed by an optional status e.g. 2.1.6-beta2. The first digit is the
major release number; the second is the minor release number; the third is
the patch number. The optional status is an indicator of the release
status, e.g. -alpha2, -rc1, etc. Generally, the status indicator is only
used for major releases, e.g. 1.0.0-rc1 but is available for any release at
the release manager's discretion.

<a name="OpenJPAReleasePolicy-SNAPSHOTReleases"></a>

## SNAPSHOT Releases
During development of a release, nightly builds are typically done and
published under the SNAPSHOT rubric. The SNAPSHOT will contain the latest
result of building the release, regardless of the release status. For
example, while developing release 2.1.6, the version 2.1.6-SNAPSHOT will be
the latest result even though the status changes from -alpha, -alpha2,
-beta, -beta2, -rc1, -rc2. The last nightly before release would still be
2.1.6-SNAPSHOT. 

<a name="OpenJPAReleasePolicy-BackwardCompatibility"></a>

## Backward Compatibility
Backward compatibility means that user programs compiled against one
release will still compile and execute with another release. Generally, the
objective is to maintain backward compatibility for minor releases and
patch releases but not major releases. For example, 2.1.5 will execute when
run with e.g. 2.1.6 but there is no guarantee that the reverse is true,
i.e. that user programs compiled against 2.1.6 will compile or run against
2.1.5.

<a name="OpenJPAReleasePolicy-MajorRelease"></a>

## Major Release
Major releases have the minor and patch numbers set to 0. Major releases
contain functionality changes compared to earlier major releases and may
break backward compatibility if necessary. Once a major release is issued,
a branch is created for maintenance, replacing the patch number with "x". 

<a name="OpenJPAReleasePolicy-MinorRelease"></a>

## Minor Release
Minor releases have the patch number set to 0. Minor releases contain
functionality changes compared to earlier minor releases within the same
major release, but do not break backward compatibility.

<a name="OpenJPAReleasePolicy-PatchRelease"></a>

## Patch Release
Patch releases contain bug fixes compared to the previous patch, minor, or
major release on which they are built. Patch releases increment the patch
number compared to the most recent patch release. Backward compatibility is
maintained.
