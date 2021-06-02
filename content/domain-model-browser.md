Title: Domain Model Browser

<a name="DomainModelBrowser-PersistentDomainBrowser"></a>

# Persistent Domain Browser

A graphic visualization of persistence domain classes.


    $ java org.apache.openjpa.tools.metamodel.MetamodelBrowser


<a name="DomainModelBrowser-Classpath"></a>

## Classpath
  The runtime classpath must include

* OpenJPA runtime libraries
* The parent directory of persistence unit descriptor (META-INF/persistence.xml)
* The directory of compiled domain classes

<div class="info">

* The persistence unit descriptor must enumerate the domain classes in its `<class>` tag.
* Database connection is not required.

</div>



<a name="DomainModelBrowser-Atypicalsnapshot"></a>

## A typical snapshot 

![](images/mmb.PNG)
