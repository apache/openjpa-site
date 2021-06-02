Title: Running OpenJPA Examples

<a name="RunningOpenJPAExamples-RunningtheOpenJPAExamples"></a>


# Running the OpenJPA Examples

The examples are packaged so that they run after extracting the openjpa
binary distribution. Running directly from the source tree may take some
work (not documented here). 

1. Build the openjpa binaries 

        $ mvn clean install

1. extract the binary distribution to a temporary directory

        $ cd openjpa-project/target/site/downloads/
        $ unzip -qq -d temp *binary*.zip
        $ cd temp/$openjpa-version/examples

1. run the helloJPA sample

        $ cd hellojpa
        $ ant
        $ cd ..

1. run the relations sample

        $ cd relations
        $ ant
        $ cd ..

1. run the reversemapping sample

<table class="info"><tr>
      <td valign="top"><img src="images/information.gif" width="16" height="16" border="0">
      <td>Currently only works on unix platforms
</tr></table>

        $ cd reversemapping
        $ ant
        $ cd ..
        


