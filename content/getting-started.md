Title: Getting started

<a name="Gettingstarted-Notes"></a>

## Notes
These instructions detail the steps required to run a give sample for a number of different environments. You can substitute any of the directories in the \[binary download\](binary-download\.html)
\examples\ directory for __hellojpa__ in the instructions below to run a
different sample.

<a name="Gettingstarted-GettingStartedwiththeEclipse"></a>

## Getting Started with the Eclipse

1. Download the OpenJPA binary release from the [downloads](downloads.html)
 page and unpack it by double-clicking it.
1. Launch Eclipse (this sample was tested with Eclipse 3.2.1, but any recent
version should work).
1. Select the __File__ menu, traverse to the __New__ sub-menu, and select
__Project__.
1. On the __Select a wizard__ page, select __Java Project from Existing Ant
Buildfile__, then click the __Next__ button.
1. Hit the __Browse__ button next to the __Ant Buildfile__ field, and navigate
to the unpacked OpenJPA zip file on the desktop, then traverse through
__examples__, then __hellojpa__, and select the __build.xml__ file and hit the
__Open__ button.
1. Hit the __Finish__ button on the wizard.
1. A new project will open, containing the OpenJPA jar and all its
dependencies.
1. On the __Package Explorer__, expand the top-level folder, then the
__examples__ folder, then __hellojpa__.
1. Select the __build.xml__ file in the __hellojpa__ folder (note that there is
also a __build.xml__ file in the parent folder, which should not be
selected). Right-click the __build.xml__ file, and select the __Run As__
sub-menu, then select __Ant Build__.
1. The database will be initialized (using the stand-alone Derby database,
which is included with the OpenJPA distribution) and the __Main.java__ class
will be run. In the __Console__, you should see the text _Hello
Persistence!_.
1. Congratulations! You have run your first sample program using OpenJPA.
Examine the __Main.java__ example program, as well as the __Message.java__
entity class, play with them by adding fields and working on new
persistence operations. Have fun!

<a name="Gettingstarted-GettingStartedwiththeConsole"></a>

## Getting Started with the Console

1. Ensure that you have [Apache Ant](http://ant.apache.org/)
 installed (this sample was tested with ant 1.6.5, but any recent version
should work).
1. Download the OpenJPA binary release from the [downloads](downloads.html)
 page and unpack it by double-clicking it.
1. Launch a console, such as __cmd.exe__ on Windows, __Terminal.app__ on Mac, or
__xterm__ on UNIX.
1. Change directories to the Desktop, then cd to the unpacked OpenJPA
folder.
1. cd to the __examples__ subdirectory, then to the __hellojpa__ subdirectory.
1. Run __ant__, which will compile the classes and run the sample application.
At the end of the build, you should see the text _Hello Persistence!_.
1. Congratulations! You have run your first sample program using OpenJPA.
Examine the __Main.java__ example program, as well as the __Message.java__
entity class, play with them by adding fields and working on new
persistence operations. Have fun!

<a name="Gettingstarted-GettingStartedwithNetbeans"></a>

## Getting Started with Netbeans

1. Download the OpenJPA binary release from the [downloads](downloads.html)
 page and unpack it by double-clicking it.
1. Launch Netbeans (this sample was tested with Netbeans 5.5, but any recent
version should work).
1. Select the __File__ menu and select __New Project__.
1. On the __New Project__ page, select Category:__General__ Projects:__Java
Project with Existing Ant Script__, then click the __Next__ button.
1. Press the __Browse__ button next to the __Location__ field, and navigate to
the unpacked OpenJPA directory
1. Press the __Browse__ button next to the __Build Script__ field, and navigate
to the unpacked OpenJPA directory through __examples__, then __hellojpa__, and
select the __build.xml__ file and press the __Open__ button.
1. Type a name for the project, press __Set as Main Project__ and press the
__Next__ button on the wizard.
1. Press __Next__ to accept the __Build and Run Actions__.
1. On the __Source Package Folders__ page, press __Add Folder__, select the
__examples__ folder, and press __Next__.
1. On the __Java Sources Classpath__ page, press __Add JAR/Folder__ and select
the openjpa-x.x.x/lib/geronimo-jpa_3.0_spec-1.0.jar which contains the JPA
API classes which is used to compile against.
1. Press __Finish__
1. A new project will open, containing the OpenJPA jar and the examples
source files.
1. On the __Package Explorer__, expand the top-level folder, then the
__examples__ folder, then __hellojpa__.
1. Navigate to the __build.xml__ file in the __hellojpa__ folder (note that
there is also a __build.xml__ file in the parent folder, which should not be
used). Right-click the __build.xml__ file, and select the __Run Target__
sub-menu, then select __run__.
1. The database will be initialized (using the stand-alone Derby database,
which is included with the OpenJPA distribution) and the __Main.java__ class
will be run. In the __Console__, you should see the text _Hello
Persistence!_.
1. Congratulations! You have run your first sample program using OpenJPA.
Examine the __Main.java__ example program, as well as the __Message.java__
entity class, play with them by adding fields and working on new
persistence operations. Have fun!
