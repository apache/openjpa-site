Title: Source Code


<a name="Source-Code"></a>


<a name="SourceCode-SourceCode"></a>

# Source Code

OpenJPA uses [gitbox](https://gitbox.apache.org/), two-master setup of git repositories, allowing committers to utilize two different
avenues of committing code to the Apache Software Foundation; through GitHub or through the ASF. All repositories present on gitbox
are available on GitHub with write-access enabled, including rights to open/close/merge pull requests and address issues.

<a name="SourceCode-WebAccess"></a>

### Web Access

The source code for OpenJPA can be freely browsed at:

 * [https://gitbox.apache.org/repos/asf?p=openjpa.git](https://gitbox.apache.org/repos/asf?p=openjpa.git)
 * [https://github.com/apache/openjpa](https://github.com/apache/openjpa)

<a name="SourceCode-Anonymousaccess"></a>

### Anonymous access

OpenJPA source can be checked out anonymously with this command:


    $> git clone https://gitbox.apache.org/repos/asf/openjpa.git

or

    $> git clone https://github.com/apache/openjpa.git

or

    $> git clone git@github.com:apache/openjpa.git

<a name="SourceCode-DeveloperAccess"></a>

### Developer Access

OpenJPA committers are allowed to push commits against gitbox via their own ASF account.<br/>
Before being able to push against GitHub, respective accounts must be linked together via
the [account linking service](https://gitbox.apache.org/setup/).

For anyone, the GitHub repository can be cloned and pull requests can be submitted: contributions are always welcome!

<a name="SourceCode-CompilingSource"></a>

# Compiling Source

Once you've got the code you'll probably want to build it; for instructions
see [Building](building.html)
.

We also have [Automated Builds](automated-builds.html)
 setup for several branches of OpenJPA.


<a name="SourceCode-SourceCodingStandards"></a>

# Source Coding Standards

The community has agreed upon some common code formatting standards, which
we request that everyone follows when contributing patches and checking in
changes to the svn repository.	Some of these are enforced during the
build, like 120 character line length by using the Checkstyle plugin and
checking for required Apache License, v2.0 source headers by using the apache-rat
plugin.  Please checkout the [Coding Standards](coding-standards.html)
 page for more details.

