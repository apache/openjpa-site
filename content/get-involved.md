Title: Get Involved

<a name="Get-Involved"></a>


<a name="GetInvolved-JointheApacheOpenJPACommunity"></a>

## Join the Apache OpenJPA Community

The Apache OpenJPA project is being built by the open source community for
the open source community - we welcome your input and contributions!

<a name="GetInvolved-Whatwearelookingfor"></a>

### What we are looking for

 * Source code and fixes contributions
 * Test cases for issues encountered during application development 
 * Documentation assistance
 * Product and feature suggestions
 * Detailed and constructive feedback
 * Articles and whitepapers

<a name="GetInvolved-HowdoIContribute?"></a>

### How do I Contribute?

 * To discuss Apache OpenJPA topics check out the [Mailing lists](mailing-lists.html)
.
 * Bugs and other issues can be posted on the project [JIRA](http://issues.apache.org/jira/browse/OPENJPA)
.

<a name="GetInvolved-IhaveencounteredanissuewithOpenJPA.WhatdoIdonow?"></a>

### I have encountered an issue with OpenJPA. What do I do now?

  * Post a message to OpenJPA User's list to discuss the issue.
  * Search existing [issues](http://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&mode=hide&pid=12310351)
 to see whether someone had already encountered the same issue.
  * If this issue is never encountered before, create a [JIRA issue](http://issues.apache.org/jira/browse/OPENJPA)
.
  * Develop a test case to demonstrate the issue.  Here are some [useful tips and guidelines](writing-test-cases-for-openjpa.html)
 on how to develop a test case to contribute to OpenJPA repository. 
  * Attach the new test to JIRA issue. 
  * Check out the [Found a Bug](found-a-bug.html)
 page for more details on creating and submitting patches.

<a name="GetInvolved-HowDoIGetChangesIntoOpenJPA"></a>

### I have encountered an issue with OpenJPA and have fixed it in the
OpenJPA source code. How do I get the changes into OpenJPA?

 * Create a [JIRA issue](http://issues.apache.org/jira/browse/OPENJPA)
 that describes the changes you've made (you'll need an Apache JIRA account
to do this).
 * Check out the OpenJPA source code and make your changes. 
 * Create test cases to validate your changes. Here are some [useful tips and guidelines](writing-test-cases-for-openjpa.html)
 on how to develop a test case to contribute to OpenJPA repository. 
 * *'svn add'* any new files.
 * Run *'mvn test -Dtest=<MyTestCase>'* to validate your change. You need
to specify the test to run by its simple name without package name.
 * Run the checkin tests by running *'mvn test'* for any possible
regression. This should take 20-50 minutes or so depending on the release
branch.
 * Check out the [Found a Bug](found-a-bug.html)
 page for more details on creating and submitting patches.
 * Wait for a committer to review and check in your changes.
