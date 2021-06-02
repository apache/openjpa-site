Title: Enhancement with ANT

The following shows how to define a OpenJPA enhancer task and how to invoke
the task in ANT.

First you'll need to compile the Entites. (Note: as a prereq to running the
enhance task, I copied my persistence.xml file to my /build directory. You
might not need to do this, but the persistence.xml has to be in the
classpath.)

Next you'll need to configure the enhancer task and a classpath where the
task can be found.

The final step is to call the enhance task. A snippet is provided below:

    	<path id="jpa.enhancement.classpath">
    	    <pathelement location="bin"/>
    
    	    <!-- lib contains all of the jars that came with the OpenJPA binary download -->
    	    <fileset dir="lib">
    		<include name="**/*.jar"/>
    	    </fileset>
    	</path>
    
    
    	<target name="enhance" depends="build">
    	<!-- This is a bit of a hack, but I needed to copy the persistence.xml file from my src dir
    	    to the build dir when we run enhancement -->
    	<copy includeemptydirs="false" todir="bin">
    	    <fileset dir="src" excludes="**/*.launch, **/*.java"/>
    	</copy>
    
    
    	<!-- define the openjpac task -->
    	<taskdef name="openjpac" classname="org.apache.openjpa.ant.PCEnhancerTask">
    	    <classpath refid="jpa.enhancement.classpath"/>
    	</taskdef>
                
    	<!-- invoke enhancer the enhancer -->
    	<openjpac>
    	    <classpath refid="jpa.enhancement.classpath"/>
    	</openjpac>
    	<echo message="Enhancing complete."/>
        </target>

The persistence.xml doesn't have to be complete. The required elements are
the persistence-unit (any legal name will do), and the provider (you have
to identify openjpa). You can identify the classes to be enhanced either in
this file or in the enhancer task ant project.

        <?xml version="1.0" encoding="UTF-8"?>
        <persistence version="1.0" xmlns="http://java.sun.com/xml/ns/persistence" 
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
            xsi:schemaLocation="http://java.sun.com/xml/ns/persistence 
            http://java.sun.com/xml/ns/persistence/persistence_1_0.xsd">
            <persistence-unit name="enhance" transaction-type="RESOURCE_LOCAL">
       
                <provider>org.apache.openjpa.persistence.PersistenceProviderImpl</provider>
                <class>com.egg.sample.model.Employee</class>
            </persistence-unit>
       </persistence>


