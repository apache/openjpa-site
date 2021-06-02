Title: Downloads


<a name="Downloads Nightly"></a>


<a name="Downloads-OpenJPANightly"></a>

# OpenJPA Nightly Downloads

Use the links below to download a nightly snapshot driver of Apache OpenJPA. Please
reference the [OpenJPA Downloads](downloads.html) page for the official OpenJPA releases.

For information on obtaining OpenJPA binaries, see the [Obtaining](obtaining.html)
 page. For information on building OpenJPA from source, see the [Building](building.html)
 page.

<a name="Downloads-NightlySnapshots"></a>

# Nightly Snapshots

These distributions are built and deployed nightly, and contain up-to-date
fixes and improvements. However, their stability cannot be guaranteed. Use
at your own risk.

## Snapshot builds 
Snapshot (nightly) builds for all active releases are published to the Apache snapshot repository.

**Version 1.2.x, 1.3.x, 2.0.x, 2.1.x, 2.2.x, 2.2.1.x, 2.3.x,2.4.x and trunk (3.1.x as of this writing)**
can be found in the snapshot repository on repository.apache.org. A maven
project can access this snapshot repository by adding the following
repository in pom.xml:

    <repositories>
        <repository>
            <id>apache.snapshots</id>
            <name>Apache Snapshot Repository</name>
            <url>http://repository.apache.org/snapshots</url>
            <releases>
            <enabled>false</enabled>
            </releases>
        </repository>
    </repositories>

If you are using the openjpa-maven-plugin then you also need to activate the pluginRepository.

    <pluginRepositories>
        <pluginRepository>
            <id>apache.snapshots</id>
            <name>Apache Snapshot Repository</name>
            <url>http://repository.apache.org/snapshots</url>
            <releases>
            <enabled>false</enabled>
            </releases>
        </pluginRepository>
    </pluginRepositories>


**Pre-packaged binaries for SNAPSHOT releases** are available in the
snapshot repository at the following locations:

<table>
<tr><th> SNAPSHOT version </th><th> binaries </th><th> source </th></tr>
<tr><td class="border"> 3.1.3 </td>
    <td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa/3.1.3-SNAPSHOT/">apache-openjpa-3.1.3-SNAPSHOT-binary.zip</a>
    <td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa/3.1.3-SNAPSHOT/">apache-openjpa-3.1.3-SNAPSHOT-source.zip</a>
</tr>
<tr><td class="border"> 2.4.4 </td>
    <td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa/2.4.4-SNAPSHOT/">apache-openjpa-2.4.4-SNAPSHOT-binary.zip</a>
    <td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa/2.4.4-SNAPSHOT/">apache-openjpa-2.4.4-SNAPSHOT-source.zip</a>
</tr>
<tr><td class="border"> 2.3.1 </td>
    <td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa/2.3.1-SNAPSHOT/">apache-openjpa-2.3.1-SNAPSHOT-binary.zip</a>
    <td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa/2.3.1-SNAPSHOT/">apache-openjpa-2.3.1-SNAPSHOT-source.zip</a>
</tr>
<tr><td class="border"> 2.2.3 </td>
    <td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa/2.2.3-SNAPSHOT/">apache-openjpa-2.2.3-SNAPSHOT-binary.zip</a>
    <td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa/2.2.3-SNAPSHOT/">apache-openjpa-2.2.3-SNAPSHOT-source.zip</a>
</tr>
<tr><td class="border"> 2.2.1.1 </td>
    <td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa/2.2.1.1-SNAPSHOT/">apache-openjpa-2.2.1.1-SNAPSHOT-binary.zip</a>
    <td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa/2.2.1.1-SNAPSHOT/">apache-openjpa-2.2.1.1-SNAPSHOT-source.zip</a>
</tr>
<tr><td class="border"> 2.1.2 </td>
    <td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa/2.1.2-SNAPSHOT/">apache-openjpa-2.1.2-SNAPSHOT-binary.zip</a>
    <td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa/2.1.2-SNAPSHOT/">apache-openjpa-2.1.2-SNAPSHOT-source.zip</a>
</tr>
<tr><td class="border"> 2.0.2 </td>
    <td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa/2.0.2-SNAPSHOT/">apache-openjpa-2.0.2-SNAPSHOT-binary.zip</a>
    <td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa/2.0.2-SNAPSHOT/">apache-openjpa-2.0.2-SNAPSHOT-source.zip</a>
</tr>
<tr><td class="border"> 1.3.0 </td>
    <td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa/1.3.0-SNAPSHOT/">apache-openjpa-1.3.0-SNAPSHOT-binary.zip</a>
    <td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa/1.3.0-SNAPSHOT/">apache-openjpa-1.3.0-SNAPSHOT-source.zip</a>
</tr>
<tr><td class="border"> 1.2.4 </td>
    <td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa/1.2.4-SNAPSHOT/">apache-openjpa-1.2.4-SNAPSHOT-binary.zip</a>
    <td class="border"> <a href="https://repository.apache.org/snapshots/org/apache/openjpa/apache-openjpa/1.2.4-SNAPSHOT/">apache-openjpa-1.2.4-SNAPSHOT-source.zip</a>
</tr>
</table>


