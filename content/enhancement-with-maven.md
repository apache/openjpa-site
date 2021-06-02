Title: Enhancement with Maven

<a name="EnhancementwithMaven-Usingtheopenjpa-maven-plugin"></a>

## Using the openjpa-maven-plugin

The full OpenJPA Maven plugin documentation can be found [here](http://openjpa.apache.org/builds/3.1.2/openjpa-maven-plugin/index.html).

For example, to enhance you source entity classes after they have been
compiled (but exclude any POJO classes that rely upon orm.xml maappings),
add the openjpa-maven-plugin to the <build> section of your pom.xml, like -

        <build>
        ...
        <plugin>
            <groupId>org.apache.openjpa</groupId>
            <artifactId>openjpa-maven-plugin</artifactId>
            <version>3.1.2</version>
            <configuration>
                <includes>**/entities/*.class</includes>
                <excludes>**/entities/XML*.class</excludes>
                <addDefaultConstructor>true</addDefaultConstructor>               
                <enforcePropertyRestrictions>true</enforcePropertyRestrictions>
            </configuration>
            <executions>
                <execution>
                    <id>enhancer</id>
                    <phase>process-classes</phase>
                    <goals>
                        <goal>enhance</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
        ...
        </build>


There are other goals available to create the Entity to SQL mapping and
Entity to XML Schema mapping, which are documented under the [Goals section](https://openjpa.apache.org/builds/3.1.2/openjpa-maven-plugin/plugin-info.html)
 on the plugin website.

<a name="EnhancementwithMaven-Usingthemaven-antrun-plugin"></a>

## Using the maven-antrun-plugin

You can use the maven-antrun-plugin to launch the OpenJPA enhancer task
using ANT.  The steps are nearly identical to the ones for [Enhancing with ANT](enhancement-with-ant.html)
 (again, you may not need to move the persistence.xml file to the build
directory, but I did for this write-up).


    <build>
        <!-- Copy the persistence.xml file to the build dir -->
        <!-- You can skip this step if you put the persistence.xml in src/main/resources/META-INF instead of src/main/java/META-INF -->
        <resources>
          <resource>
            <directory> src/main/java </directory>
            <includes>
              <include> **/*.xml </include>
              </includes>
          </resource>
        </resources>
        <plugins>
        .....        
          <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-antrun-plugin</artifactId>
            <version>1.2</version>
            <executions>
                <execution>
                   <phase>process-classes</phase>
                   <configuration>
                      <tasks>
                          <taskdef name="openjpac" classname="org.apache.openjpa.ant.PCEnhancerTask" classpathref="maven.compile.classpath"/>
                          <openjpac>
                             <classpath refid="maven.compile.classpath"/>
                          </openjpac>
                      </tasks>
                   </configuration>
                   <goals>
                       <goal>run</goal>
                   </goals>
                </execution>
            </executions>
          </plugin>
        </plugins>
        ....
     </build>



