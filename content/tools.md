Title: Tools

<a name="Tools-ToolsforOpenJPA"></a>

# Tools for OpenJPA
  
This page will host description of design-time and runtime tools for
OpenJPA.
The tools mentioned below are available as command-line utilities. In the
future, they may be made available as interactive graphical tools
integrated into popular IDEs such as Eclipse or IntelliJ. 

<a name="Tools-ExistingOpenJPATools"></a>

### Existing OpenJPA Tools

The OpenJPA distribution and runtime already comes with a series of useful
tools to:

* [Entity Enhancement](entity-enhancement.html)
 for enhancing the bytecode of POJO domain classes
* [reverse map](/builds/latest/docs/docbook/manual.html#ref_guide_pc_reverse)
 a database schema to Java source code 
* [create/synchronize](/builds/latest/docs/docbook/manual.html#ref_guide_mapping_mappingtool_examples)
 a Java persistent domain model to a database schema
* [generate](/builds/latest/docs/docbook/manual.html#d0e11103)
 canonical metamodel classes for strictly-typed Criteria queries


<a name="Tools-ToolsUnderDevelopment"></a>

### Tools Under Development

A new OpenJPA Tools subproject has been created to deliver a new set of
tools that are decoupled from a specific OpenJPA release.

* [Migration Tool](migration-tool.html)- translates proprietary mapping descriptors (such as Hibernate) to standard JPA mapping descriptors.
* [Entity enhancer for Eclipse](openjpaeclipseinstallation.html) provides a plugin which can be used to pre-enhance your entities when building in Eclipse.
* [Domain Model Browser](domain-model-browser.html)
* [JConsole DataCache Plugin](jconsole-datacache-plugin.html) - JConsole plugin to monitor openjpa.DataCache usage.
* [Fetch Statistics](fetch-statistics.html)  - monitors persistent field access and determines which fields are never used.


  
  

  
  
