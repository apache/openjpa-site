Title: OpenJPAEclipseToolingDevAndBuild

<a name="OpenJPAEclipseToolingDevAndBuild-OpenJPAEclipseTooling"></a>

# OpenJPA Eclipse Tooling

<a name="OpenJPAEclipseToolingDevAndBuild-HowtodeveloponandbuildtheOpenJPAEclipseTooling"></a>

## How to develop on and build the OpenJPA Eclipse Tooling

<a name="OpenJPAEclipseToolingDevAndBuild-IDE"></a>

### IDE

1. get Eclipse with PDE
1. check out the [https://svn.apache.org/repos/asf/openjpa/devtools/trunk/](https://svn.apache.org/repos/asf/openjpa/devtools/trunk/)
(not just the individual project directories, but really the trunk, so that
you also have the pom.xml at the root...).  If you use Subversive (or
Subclipse) from within Eclipse to do the check-out, you'll have to remove
the project from the workspace again after checkout, without delete on
disk, so that you can import the individual projects in the next step.
1. open the individual projects in Eclipse
(org.apache.openjpa.eclipse.feature, org.apache.openjpa,
org.apache.openjpa.eclipse, openjpa-eclipse-testproject,
org.apache.openjpa.eclipse.tests, org.apache.openjpa.eclipse.site) -
_*requires correct .project and .classpath files currently missing from
SVN*_


<a name="OpenJPAEclipseToolingDevAndBuild-HeadlessMaven-basedbuild(withoutrequiringEclipseIDE)"></a>

### Headless Maven-based build (without requiring Eclipse IDE)

1. download Maven 3.0 from [http://maven.apache.org/download.html](http://maven.apache.org/download.html).  Please
note and make sure you do get & use Maven 3.0 (latest at the time of
writing this Maven 3.0-alpha-6), and not just a Maven 2.2.1, which will NOT
WORK.
1. check-out the [https://svn.apache.org/repos/asf/openjpa/devtools/trunk/](https://svn.apache.org/repos/asf/openjpa/devtools/trunk/)
(not just the individual project directories, but really the trunk, so that
you also have the pom.xml at the root...)
1. do a "mvn install" at the root.  This will be VERY SLOW at first
invocation, as it downloads LOT'S (really; including many Eclipse
artefacts) into your local maven repo. Subsequent calls will as usual be
much faster.
1. in the directory "org.apache.openjpa.eclipse.site/target/site" there will
be a completely ready Eclipse Update Site (which is what gets be pushed to
some HTTP server and the URL of which is given to end-users to install the
whole thing)

This should ideally be set-up on a public build server, e.g. on the
[http://hudson.zones.apache.org/hudson/](http://hudson.zones.apache.org/hudson/) ?
