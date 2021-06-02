Title: JPA 2.0 Development Process

<a name="JPA2.0DevelopmentProcess-JPA2.0DevelopmentProcess"></a>

# JPA 2.0 Development Process 

<a name="JPA2.0DevelopmentProcess-JPA2.0Roadmap"></a>

## JPA 2.0 Roadmap
The OpenJPA roadmap and iteration detail for developing JPA 2.0
functionality is documented [here](jpa-2.0-roadmap.html)
.  The process to be used for this development effort will be documented on
this Development Process page.

<a name="JPA2.0DevelopmentProcess-Overview"></a>

## Overview
JPA 2.0 is currently being defined by the Java Community Process under [JSR-317](http://jcp.org/en/jsr/detail?id=317)
.  The most recent public draft is dated 03/13/2009.  Members of the Apache
OpenJPA project continue to monitor and actively participate in JSR-317. 
OpenJPA has recently branched off its 1.x efforts and is targeting its next
release, OpenJPA 2.0, to in addition to providing new features, be fully
spec compliant with JPA 2.0.  While the JPA 2.0 spec is still in the review
process, the OpenJPA project will begin implementing JPA 2.0 capabilities
as defined by the draft specification.	This will help to ensure a timely
delivery of JPA 2.0 functionality in addition to providing experience-based
feedback to the JPA committee.

<a name="JPA2.0DevelopmentProcess-JPA2.0Highlights"></a>

## JPA 2.0 Highlights
The latest draft of the JPA 2.0 specification includes many updates to JPA,
from minor updates to major functional enhancements.  Some of these updates
and enhancements include:

* Collections of embeddables and basic types
* Derived Identity support
* Relationship support within embeddables
* Enhancements to persistent map collection support
* Standard properties for query timeout and persistence configuration
* Lock mode configuration on entity manager and query
* Cache interface to access L2 cache
* Criteria API for programmatic query definition
* Many JPQL enhancements


<a name="JPA2.0DevelopmentProcess-Contributions"></a>

## Contributions
The OpenJPA 2.0 release needs contributions in the areas of development,
testing, and documentation.  If you are simply interested in trying out new
capabilities of JPA 2.0, contributing to the test suite is a great way to
do that; while making a significant contribution to the project.

<a name="JPA2.0DevelopmentProcess-Process"></a>

## Process

* All new features, spec related or other improvements must have an
corresponding JIRA.  Large items should be broken down into manageable
sub-tasks.  The JIRA should include design details, decision rationality,
and testing information.
* Use [test driven development](http://en.wikipedia.org/wiki/Test-driven_development)
 (write tests before code).  Test driven development can be extremely
beneficial for gaining an initial understanding the requirements of the
feature and will help ensure that the feature is adequately tested.  Too
often, tests are the last thing to be written so they can end up incomplete
or worse yet, forgotten.  Test driven development in OpenJPA is now more
feasible with the recent enhancement in [OPENJPA-766](https://issues.apache.org/jira/browse/OPENJPA-766)
.
* Documentation updates/additions, when necessary, must accompany new
function.
* As of iteration 5, OpenJPA 2.0 development will be based on four week
iterations (or sprints).  Each iteration will include a set of new features
and enhancements.  Features must have accompanying tests and documentation
and go through a code review.  A feature must fit within the iteration
period.  Larger and/or complex tasks may need to be broken down such that
they can be contributed as individual, consumable features. For example,
JPA 2.0 defines relationship support within an embedded.  If this task is
deemed complex due to the need to support multiple relationship types,
relationship type one-to-one could be made available in one iteration and
the many-to-one relationship type could be added in subsequent iteration.
* A call for participation will be posted prior to the start of each
iteration.  An iteration plan will be composed based on who can participate
and what they plan to contribute.
* Code reviews will be conducted using the standard Commit-Then-Review
(CTR) process (for OpenJPA committers), unless a pre-commit code review is
specifically requested.  Artifacts submitted by non-committers must be
reviewed before they are committed.
