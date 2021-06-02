Title: OpenJPAEclipseEnhancementBuilder

<a name="OpenJPAEclipseEnhancementBuilder-OpenJPAEclipseTooling"></a>

# OpenJPA Eclipse Tooling

<a name="OpenJPAEclipseEnhancementBuilder-HowtousetheOpenJPAEclipseToolingBuilderforBytecodeEnhancement"></a>

## How to use the OpenJPA Eclipse Tooling Builder for Bytecode Enhancement

Once you have [installed the OpenJPA Eclipse tooling](openjpaeclipseinstallation.html)
, here is how to add the Bytecode Enhancement Builder to a Java project:

1. right-click on Project, click "Add/Remove Bytecode Enhancer"
1. in the Enable OpenJPA dialog which will be shown: (TBD: Attach screenshot
here, once ugly [OPENJPA-1521](https://issues.apache.org/jira/browse/OPENJPA-1521)
 is resolved?)
    1. choose if OpenJPA libraries should be added to project, this will copy
the OpenJPA JARs from the Eclipse plug-in into a lib directory of the Java
project, and add them as Referenced Libraries. (In a normal existing
project you'll already have them via Maven or whatever so you'll not use /
want to deactivate this; for new or test projects this is convenient.)
    1. choose enhancement options, if you need any. These are the [same options as the CLI PCEnhancer supports](http://openjpa.apache.org/builds/latest/docs/manual/ref_guide_pc_enhance.html#ref_guide_pc_enhance_build)
.
1. menu Project > Properties (or right-click on Project > Properties) should
now show the "OpenJPA PC-Enhancer Project Builder" added after the usual
"Java Builder"
1. when Eclipse builds (compiles) the project, classes will now be byte-code
enhanced


<a name="OpenJPAEclipseEnhancementBuilder-KnownLimitations"></a>

### Known Limitations

* persistence.xml is ignored, the plug-in / builder only looks for
annotations (@Entity, @MappedSuperclass, @Embeddable, @ManagedInterface) to
decide if a class actually needs enhancement
* any error markers (the lines shown in the Problems view) are on the
.class resource, instead of on the source .java class, which would be more
convenient
* the Builder runs even on classes which are red and compilation issues,
because the Eclipse compiler still tries to produce a .class file, and may
log weird error messages in that case


<a name="OpenJPAEclipseEnhancementBuilder-Troubleshooting,Tips&Recommendations"></a>

### Troubleshooting, Tips & Recommendations

* If the Builder has trouble during enhancement, it normally logs useful
messages / exception stack traces to the Eclipse Error Log. Use menu Window
\> Show View \> Error Log to display it. If you don't have the Error Log
view, this could be because you have an Eclipse with the PDE (Plug-in
Development Environment), get that. The Eclipse Error Log can also be
exported from this view, e.g. to send it to the mailing list.  Further
debugging & informational log messages can be enabled via the .project
file, see below.

* If your Eclipse dies due to "java.lang.OutOfMemoryError: Java heap space"
/ "java.lang.OutOfMemoryError: PermGen space" issues, you may need to add
e.g. "-XX:PermSize=64m -XX:MaxPermSize=256m -Xms128m -Xmx512m" to your
eclipse.ini (each option on a separate line) for the enhancement builder

* In order to be sure that you're actually using build time enhancement,
and not enhancing dynamically at run-time, you may wish to set the
openjpa.RuntimeUnenhancedClasses=unsupported property in your
persistence.xml or wherever you bootstrap OpenJPA (see [Omitting the OpenJPA enhancer](http://openjpa.apache.org/builds/latest/docs/manual/ref_guide_pc_enhance.html#ref_guide_pc_enhance_unenhanced_types)
)


<a name="OpenJPAEclipseEnhancementBuilder-Options"></a>

### Options

* More verbose logging for the Builder can be enabled via a configuration
option in .project.  This option is only intended for troubleshooting &
debugging, because it seems to significantly (!) slow down the builder, and
something goes wrong with the Progress view (Monitor stuff) causing it to
not update correctly anymore, and appear to keep running (although it's
not).

        <projectDescription>
        ...
        <buildSpec>
        ...
    	<buildCommand>
    	    <name>org.apache.openjpa.eclipse.OpenJPAEnhancerBuilder</name>
    	    <arguments>
    		<dictionary>
    		    <key>debugLogs</key>
    		    <value>true</value>
    		</dictionary>


   The debugLogs = true will lead to message such as these to be shown in the
   Error Log (the order sometimes appears to get messed up) :


        OpenJPA Enhancement (Full Build, collecting resources) took 0ms, found 3 classes potentially needing enhancement
        OpenJPA Enhancer ran on but did not have to bytecode enhance /test-project/bin/ch.vorburger.jpa/SomeEntityTest.class
        OpenJPA Enhancer ran on and actually bytecode enhanced /test-project/bin/ch.vorburger.jpa/SomeEntity.class
        OpenJPA Enhancer ran on but did not have to bytecode enhance /test-again/bin/ch.vorburger.jpa/NotToEnhance.class
        OpenJPA Enhancement (Full Build) took 47ms, for 3 potential classes, of which 1 were actually enhanced


* The builder has been written with efficiency in mind and underwent some
profiling & optimization, e.g. it correctly does only Incremental Builds
when possible.	However, for projects with a lot of classes, this Builder
may slow down the project. This is because it still has to byte-code
inspect (load and analyze) each .class to determine if it needs
enhancement.  If the JPA entities in your project follow some naming
convention (e.g. all ending in *Entity, or all in a certain package), then
the builder can be configured to "match" only certain classes using
Ant-like patterns, by manually adding the following to the existing
.project file of the Eclipse Java project:


        <projectDescription>
        ...
        <buildSpec>
        ...
    	<buildCommand>
    	    <name>org.apache.openjpa.eclipse.OpenJPAEnhancerBuilder</name>
    	    <arguments>
    		<dictionary>
    		    <key>include1</key>
    		    <value>**/*Entity.class</value>
    		</dictionary>
    		<dictionary>
    		    <key>include2</key>
    		    <value>**/*EntityRef.class</value>
    		</dictionary>


* The above two options can be mixed by adding several `<dictionary>` inside the `<arguments>`.
