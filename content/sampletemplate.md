Title: SampleTemplate

<a name="SampleTemplate-AtemplateforOpenJPASamples"></a>


# A template for OpenJPA Samples

<a name="SampleTemplate-Introduction"></a>

## Introduction

A paragraph describing the basic purpose of the presented sample. In
general, the purpose of a sample could be, but not limited to,

* to highlight some new feature introduced in a release (e.g. Bean
Validation or Criteria API)
* to describe wiring between frameworks e.g. JSF and JPA, GWT and JPA
* to demonstrate operation within a container e.g. OSGi, Spring, Tomcat
or JEE
* a combination of the above

For example,<br/> 
   "this sample demonstrates usage of new Bean Validation API in a
multi-tier web application" 
or "this sample integrates client-side Google Web Toolkit architecture with
sever-side JPA application".

The functional features of the samples such as "This OpenBooks example
can be used to place order and browse books" -- are not that important in
this context but can be mentioned.

<a name="SampleTemplate-Installation"></a>

## Installation

State the availability of the sample. For example,

* Is the distribution available as a downloadable archieve? If packaged
in an archieve, all source code, build instructions must be available in
the distribution itself. A *README.txt* should be inside and outside the
distribution.

* Is the sample to be checked out from code repository? In such cases,
building the sample should be done with Ant or Maven. Prefer Ant to make
the dependencies and steps more visible. 

**The steps in this section should be clear and concise for an user to
follow them to build, deploy and run the sample.** 

  
<a name="SampleTemplate-Environment"></a>

## Environment

   Enumerate the software artifacts required to build, deploy and run the
sample. The artifacts should be categorized into build time and run time
dependencies. 

<a name="SampleTemplate-Configuration"></a>

## Configuration

Often building a sample will require the user to configure dependencies
(such as OpenJPA libraries or JDBC Driver), for his/her local environment.
The ANT build scripts for a sample must accept configurable properties via
*build.properties* or similar configurable mechanics. The properties
configuration file itself should be documented to explain the dependencies
and how the build script use them. Maven based build scripts can make these
dependencies more implicit and saves the user to explicitly satisfy such
dependencies. However, ANT based builds are preferred over Maven for the
samples, so that the build steps and dependencies are made more visible to
the user.
 
<a name="SampleTemplate-BestPractices"></a>

## Best Practices

The samples, besides demonstration of a feature, are a suitable vehicle
of showing good development practices in JPA application programming model
such as persistent domain modeling or architectural practices. It is
recommended that such best practices be mentioned in several places:
 
* in the source code 
* build scripts 
* a separate document that enumerates them in one place.

<a name="SampleTemplate-Caveats"></a>

## Caveats

The complete develop-build-run cycle of a sample will often bring out the
special considerations. For example, reported common errors in deployment
in a container and their remedies or certain undesirable usage patterns.
The description of a sample should highlight these special considerations
rather than making the exercise appear as a series of perfectly easy steps.
The caveats can be further highlighted by linking them to relevant JIRA
issues or forum discussions or external blogs etc.  
