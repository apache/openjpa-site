Title: Quick Start


<a name="QuickStart-QuickStartGuide"></a>


Quick Start Guide
=============================

We know it can be hard to find the right help sometimes and search engines
can be overwhelming, so we will try to put the most commonly asked for
topics with some overview and links to more in-depth resources here for you
to checkout, before wasting your time searching through our [Documentation](documentation.html)
 and [Mailing Lists](mailing-lists.html) for help.


<a name="QuickStart-RuntimeDependencies"></a>


## Runtime Dependencies

To use OpenJPA as a stand-alone Java component or with a lightweight
non-Java EE framework, please refer to the following [Build and Runtime Dependencies](build-and-runtime-dependencies.html)
 page for the supported levels of Java SE.

To use OpenJPA in a Java EE application server, please refer to the
following [Integration](integration.html)
 page for the known platforms that either include OpenJPA or have been
tested with OpenJPA.


<a name="QuickStart-JPAExamples"></a>

## JPA Examples

OpenJPA provides some simple examples as part of the binary distribution on
the [Downloads](downloads.html) page. The following [Samples](samples.html)
 page provides quick start instructions on how to build and run these
samples, along with pointers to other JPA samples from the Apache Geronimo
project.


<a name="QuickStart-EnhancingEntities"></a>

## Enhancing Entities

The JPA spec requires some type of monitoring of Entity objects, but the
spec does not define how to implement this monitoring. Some JPA providers
dynamically generate new subclasses or proxy objects that front the user's Entity
objects, while others use *byte-code weaving* technologies to
enhance the actual Entity class objects.  OpenJPA supports
both [enhancement](entity-enhancement.html)
 methods, but strongly suggests using the *byte-code weaving* enhancement. 
The following [Entity Enhancement](entity-enhancement.html)
 page includes more details on both enhancement types, along with examples
on how to setup *build time* enhancement in ANT, Maven and Eclipse
environments.


<a name="QuickStart-Tools"></a>

## Tools

OpenJPA provides several design-time and runtime tools, to perform such
tasks as entity enhancement, schema mapping, generating metamodel classes
and to help migrate from other JPA providers.
Please checkout the [Tools](tools.html) page for more details.


<a name="QuickStart-FAQ"></a>

## FAQ

Some common questions concerning the history, architecture and usage of
OpenJPA can be found on the [FAQ](faq.html) page.


<a name="QuickStart-TaketheRedPill"></a>

## Take the Red Pill

If you want to dive into the rabbit-hole (Hey, It's open source!), then
checkout the [Found a Bug](found-a-bug.html)
 page, which covers everything from posting questions to our mailing lists,
to getting the source code and building it, and creating bug patches....

  
  

