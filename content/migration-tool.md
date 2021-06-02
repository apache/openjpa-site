Title: Migration Tool

<a name="MigrationTool-MigrationTool"></a>

# Migration Tool

This command-line utility translates proprietary mapping descriptors to
standard JPA mapping descriptors.

<a name="MigrationTool-Download"></a>

## Download

The latest OpenJPA Tools JAR file can be download from the [SNAPSHOT Repository](https://repository.apache.org/content/repositories/snapshots/org/apache/openjpa/tools/openjpa-tools/0.1.0-SNAPSHOT/)
 or can be built from the source code in [svn](https://svn.apache.org/repos/asf/openjpa/tools/trunk)
 by using Maven 2.2.1 and Java SE 6.


<a name="MigrationTool-Usage:"></a>

## Usage:


      $ java org.apache.openjpa.tools.MigrationTool -input xyz.xml [-output xyz.orm.xml] [-actions migration-actions.xml]  [-verbose true]

where

<table >
<tr>
<td class="border">-input </td>
<td class="border"> input location of the proprietary XML mapping descriptor
resource. The resource is looked up in the current classpath. If not
located as a resource, then looked up as an input file in relative to the
current directory. This option is mandatory
</td>
</tr>
<tr>
<td class="border">-output</td>
<td class="border"> output location of the translated mapping descriptor file. This
option is not mandatory. If unspecified, the output is simply printed on
the standard console. 
</td>
</tr>
<tr><td class="border">-actions</td>
<td class="border"> the actions to be performed on every element of the input
descriptor elements. These actions are specified as XML elements compliant
to a <A href="http://fisheye6.atlassian.com/browse/openjpa/tools/trunk/openjpa-tools/src/main/resources/META-INF/migration-actions.xsd?r=HEAD" class="external-link" rel="nofollow">XML schema</A>. A template of these actions for a _subset_ of Hibernate elements is
included in <A href="http://fisheye6.atlassian.com/browse/openjpa/tools/trunk/openjpa-tools/src/main/resources/META-INF/migration-actions.xml?r=HEAD" class="external-link" rel="nofollow">migration-actions.xml</A>. 
This option is not mandatory. The archetype for translating Hibernate
mapping descriptor is used as a default.
</td>
</tr>
<tr><td class="border">-verbose</td><td class="border">prints detailed trace of what the tool is doing. This option is
not mandatory. If unspecified,	detailed messages are not printed.</td></tr>
</table>


<a name="MigrationTool-Discussion"></a>

## Discussion

This tool takes each top-level element of the input mapping descriptor and
applies one or more actions to translate it to a standard JPA mapping
descriptor.
For example, consider the input fragment

    <class name="com.approuter.deploy.Project" table="PROJECTS" select-before-update="false">
      <id name="id" type="java.lang.Long" column="ID">
    	<generator class="native" />
      </id>
    </class>


This fragment will be translated by the tool as follows:


    <entity class="com.approuter.deploy.Project">
        <table name="PROJECTS"/>
        <attributes>
          <id name="id">
    	     <column name="ID"/>
    	     <generated-value strategy="AUTO"/>
          </id>
        </attributes>
    </entity>


The series of actions that translated this fragments are as follows:

* The input element *<class>* is translated to *<entity>* element. 
* The *name* attribute of input element *<class>* is translated to *class* attribute. The value of the attribute remained intact.
* the *table* attribute of input element *<class>* is translated to a new element *<table>*. The value of the *table* attribute appeared as *name* attribute in the translated element.
* the attribute *select-before-update* is ignored as it does not have a direct counterpart in standard JPA mapping descriptor. Actually this attribute controls runtime behavior and it is debatable whether a mapping descriptor is the proper place for such an attribute.
* a new element *<attributes>* appeared in the translated document which had no equivalent counterpart in the original document.
* the *column* attribute of input element *<id>* is translated to a new element *<column>*. The value of the *column* attribute appeared as *name* attribute in the translated element.
* the input element *<generator>* is translated to *<generated-value>* element. 
* the *class* attribute of input element *<generator>* is translated to a *strategy* attribute. The value of the attribute is translated from *native* to *AUTO*.



The translation was carried out by a series of _generic_, _parameterized_ _actions_. The actions are specified in [migration-actions.xml](http://fisheye6.atlassian.com/browse/openjpa/tools/trunk/openjpa-tools/src/main/resources/META-INF/migration-actions.xml?r=HEAD). Here is a snippet from that archetype to define those generic actions and their parameters.

    <actions for="class">
    	<rename-node to="entity"/>
    	<rename-attr from="name" to="class"/>
    	<promote-attr from="table" to="table" as="name"/>
    	<ignore-attr name="select-before-update"/>
    	<ignore-attr name="type"/>
    	<insert-node name="attributes"/>
    </actions>
    <actions for="id">
        <rename-node to="id"/>
        <rename-attr from="name" to="name"/>
        <promote-attr from="column" to="column" as="name">
    		<consume-attr from="length" to="length"/>
    		<consume-attr from="unique" to="unique"/>
        </promote-attr>
        <ignore-attr name="type"/>
    </actions>
    <actions for="generator">
        <rename-node to="generated-value"/>
        <rename-attr from="class" to="strategy">
    		<map-value from="native"   to="AUTO"/>
    		<map-value from="assigned" to="IDENTITY"/>
         </rename-attr>
    </actions>


The schema that specifies what actions are supported and their parameters are defined in a [XML schema](http://fisheye6.atlassian.com/browse/openjpa/tools/trunk/openjpa-tools/src/main/resources/META-INF/migration-actions.xsd?r=HEAD).

<span class="info">
   This tool is at experimental stage of development and does not cater to
all possible variations that such a translation may require. However, that
is why the design allows new custom actions be defined and applied to cater
to more complex use cases. 
</span>
 
