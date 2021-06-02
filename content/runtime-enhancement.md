Title: Runtime Enhancement

The first runtime enhancement method is to provide a _javaagent_ when launching the JVM that OpenJPA is going run in.


    -javaagent:<openjpa_jar_location>

For Eclipse, specify the above _javaagent_ value on the Run Configuration page.

For ANT, provide the _javaagent_ value as a _jvmarg_ when launching an application. Below is a snippet that shows how to pass in the _javaagent_ when launching a Java SE application that uses OpenJPA.

        <path id="jpa.enhancement.classpath">
            <pathelement location="bin"/>
            <!-- lib contains all of the jars that came with the OpenJPA binary download -->
            <fileset dir="lib">
                <include name="**/*.jar"/>
            </fileset>
        </path>
        ...
        <target name="drive" depends="clean, build">
            <echo message="Running test with run time enhancement."/>
            <java classname="main.Driver" failonerror="true" fork="yes">
                <jvmarg value="-javaagent:${openJPA-jar}"/>
                <classpath refid="jpa.enhancement.classpath"/>
            </java>
        </target>
