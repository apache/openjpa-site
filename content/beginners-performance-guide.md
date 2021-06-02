Title: Beginners Performance Guide


<a name="IntroToTuningOpenJPA"></a>



<a name="BeginnersPerformanceGuide-OpenJPABeginnersPerformanceGuide"></a>

# OpenJPA Beginners Performance Guide

This guide is targeted at new users of OpenJPA that would like to know some
of the important performance tuning properties. Please do not mistake this
for an exhaustive tuning guide. This is just enough information to make a
developer dangerous, not lethal.

<a name="BeginnersPerformanceGuide-Enhancement"></a>

## Enhancement 

OpenJPA uses byte-code weaving technologies to enhance user created Entity
class objects at build time or dynamically at run time. This allows us to
efficiently handle these objects. 

Follow the [Entity Enhancement](entity-enhancement.html) instructions on how to properly enhance your Entities.

OpenJPA also has a feature that will auto-generate new subclasses or proxy
objects that front the user's Entity objects at run time, but *this feature
is not recommended for use*. There are numerous functional issues reported
and it doesn't perform nearly as well. If you ever see the following
message you are using the non-recommended subclassing approach to
enhancement.

> 3328  pu_name INFO   \[main\]  openjpa.Enhance - Creating subclass for "\[ class
org.apache.openjpa.entity.E1 , class org.apache.openjpa.entity.E2 \]". This
means that your application will be less efficient and will consume more
memory than it would if you ran the OpenJPA enhancer. Additionally, lazy
loading will not be available for one-to-one and many-to-one persistent
attributes in types using field access; they will be loaded eagerly
instead.

It is recommended to set the following property to ensure that you don't
use this enhancement approach.


    <properties> 
        <property name="openjpa.RuntimeUnenhancedClasses" value="unsupported"/>
    <properties>


<a name="BeginnersPerformanceGuide-ConnectionPooling"></a>

## Connection Pooling

As of the 2.1.0 release OpenJPA bundles [Apache Commons DBCP](http://commons.apache.org/dbcp/)
 as part of the binary download. When running in JSE environments a default
connection pool will be plugged in with the provided database configuration
properties (Once [OPENJPA-1764](https://issues.apache.org/jira/browse/OPENJPA-1764)
 is completed) . Most JEE container environments should provide some level
of connection pooling. 

In releases prior to 2.1.0 add DBCP to your classpath and use the following
example to figure out how to configure pooling.


    <persistence xmlns="http://java.sun.com/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0">
        <persistence-unit name="example-derby" transaction-type="RESOURCE_LOCAL">
    	<properties>
    	    <property name="openjpa.ConnectionProperties" 
    		value="DriverClassName=org.apache.derby.jdbc.ClientDriver,
    		  Url=jdbc:derby://localhost:1527/database, 
    		  MaxActive=100, 
    		  MaxWait=10000, 
    		  TestOnBorrow=true, 
    		  Username=user, 
    		  Password=secret"/>
    	    <property name="openjpa.ConnectionDriverName" 
    		value="org.apache.commons.dbcp.BasicDataSource"/>
    	</properties>
        </persistence-unit>
    </persistence>
    

<a name="BeginnersPerformanceGuide-Caching"></a>

## Caching


    <properties> 
        <property name="openjpa.DataCache" value="true"/>
        <property name="openjpa.QueryCache" value="true"/>
    <properties>


Insert details about what those two properties give me.
