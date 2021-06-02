Title: JPA 2.1 Development Process


<a name="JPA2.1DevelopmentProcess-JPA2.1DevelopmentProcess"></a>

# JPA 2.1 Development Process

<a name="JPA2.1DevelopmentProcess-JPA2.1Roadmap"></a>

## JPA 2.1 Roadmap
The OpenJPA roadmap and iteration detail for developing JPA 2.1
functionality is documented [here](jpa-2.1-roadmap.html)
.  The process to be used for this development effort will be documented on
this Development Process page.

<a name="JPA2.1DevelopmentProcess-Overview"></a>

## Overview
JPA 2.1 has been defined by the Java Community Process under 
[JSR-338](http://jcp.org/en/jsr/detail?id=338).  The final specification is dated 
04/02/2013.  OpenJPA needs to branch off is current JPA 2.0 efforts from trunk and is targeting its next
release, OpenJPA 2.4, to be fully spec compliant with JPA 2.1.

<a name="JPA2.1DevelopmentProcess-JPA2.1Highlights"></a>

## JPA 2.1 Highlights
The latest JPA 2.1 specification includes many updates to JPA,
from minor updates to major functional enhancements.  Some of these updates
and enhancements include:

*  Formal Stored Procedure support
*  SynchronizationType to control when to enlist with transaction
*  CDI support for Entity Listeners
*  Type Conversions (similar to OpenJPA's Externalizer)
*  Further explanation of how to return managed and unmanaged data from NativeQueries
*  JPQL updates
*  Support for TREAT (downcasting)
*  Criteria API refactoring (hopefully just internal impacts)
*  Allow use of packaged scripts:  ddl-create-script, ddl-drop-script, ddl-load-script
*  Schema generation (similar to OpenJPA's capability)
*  Annotation updates:  @Converter, @ForeignKey, @Index

<a name="JPA2.1DevelopmentProcess-Contributions"></a>

## Contributions
The JPA 2.1 Development release needs contributions in the areas of development,
testing, and documentation.  If you are simply interested in trying out new
capabilities of JPA 2.1, contributing to the test suite is a great way to
do that; while making a significant contribution to the project.

<a name="JPA2.1DevelopmentProcess-Process"></a>

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
or worse yet, forgotten.
.
* Documentation updates/additions, when necessary, must accompany new
function.
* JPA 2.1 development will be based on two week
iterations (or sprints).  Each iteration will include a set of new features
and enhancements.  Features must have accompanying tests and documentation
and go through a code review.  A feature must fit within the iteration
period.  Larger and/or complex tasks may need to be broken down such that
they can be contributed as individual, consumable features. 
* A call for participation will be posted prior to the start of each
iteration.  An iteration plan will be composed based on who can participate
and what they plan to contribute.
* Code reviews will be conducted using the standard Commit-Then-Review
(CTR) process (for OpenJPA committers), unless a pre-commit code review is
specifically requested.  Artifacts submitted by non-committers must be
reviewed before they are committed.
