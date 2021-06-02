Title: Coding Standards

<a name="Coding-Standards"></a>


<a name="CodingStandards-CodingStandards"></a>

# Coding Standards

<a name="CodingStandards-ASFRequirements"></a>

## ASF Requirements

<a name="CodingStandards-Copyrightnoticesforsubmittedpatches"></a>

### Copyright notices for submitted patches

Please see [http://www.apache.org/legal/src-headers.html](http://www.apache.org/legal/src-headers.html)
 for details of the following summary.

Apache does not require you to assign ownership or copyright for any
patches that you submit via the above process. You retain ownership for all
such patches. But Apache does require you to grant Apache a license to use
the patch. To do this for new files, do not include a copyright statement
in the file but include this license as comments in the header of your
source contribution - [http://www.apache.org/legal/src-headers.html#headers](http://www.apache.org/legal/src-headers.html#headers)
If you require that distributions of the project include your copyright
notice, you should include with your patch an update to the NOTICE file at
trunk/openjpa-project/NOTICE.txt documenting for which files you are
notifying your copyright.

<a name="CodingStandards-LicenseandNoticefiles"></a>

### License and Notice files

Please see [http://www.apache.org/licenses/](http://www.apache.org/licenses/)
 for details of the following summary.

All release artifacts published by an Apache project (JAR/WAR/EAR, zip,
tar, ...) must include License and Notice files.  A Disclaimer file must be
included for any artifacts included form the incubator.


<a name="CodingStandards-GeneralFormattingConventions"></a>

## General Formatting Conventions

OpenJPA adheres to Sun's _Code Conventions for the Java Programming
Language_, which is available at [http://java.sun.com/docs/codeconv/](http://java.sun.com/docs/codeconv/)

1. Maximum line length is 120 characters (this is a deviation from the Java
standards).
1. Use spaces instead of tabs.
1. Indendation size is 4 spaces.
1. Do not insert a new line before opening brace. Insert a new line before
closing brace.
1. Use fully qualified import statements, i.e. do not use asterisks.

<a name="CodingStandards-EclipseUsers"></a>

## Eclipse Users

<a name="CodingStandards-FormatterProfile"></a>

### Formatter Profile
The profile can be downloaded from here - [OpenJPA-formatting-preferences.xml](artifacts/OpenJPA-formatting-preferences.xml)
**Updated 2009-06-29 (Eclipse Galileo)** [OpenJPA-eclipse-galileo-formatting.xml](artifacts/OpenJPA-eclipse-galileo-formatting.xml)

1. Window -> Preferences
1. Java -> Code Style -> Formatter
1. Click on import and select the _OpenJPA-formatting-preferences.xml_ file
downloaded above.
1. Press OK after importing

<a name="CodingStandards-CodeTemplate"></a>

### Code Template
The latest version with the required ASL header format can be downloaded
here - [OpenJPA-code-style-template.xml](artifacts/OpenJPA-code-style-template.xml)

1. Window -> Preferences
1. Java -> Code Style -> Code Templates
1. Click on import and select the _OpenJPA-code-style-template.xml_ file
downloaded above.
1. Press OK after importing

<a name="CodingStandards-SubmittingaPatch"></a>

## Submitting a Patch

If you make changes to OpenJPA, and would like to contribute the to the
project, you should create a patch via svn and post it to the [OpenJPA JIRA issue tracker](http://issues.apache.org/jira/browse/OPENJPA)
. To create a patch, simply execute the following command:


    $> svn diff > your-changes.patch


*Note:* You may also use Eclipse to create a patch (Team -> Create
Patch...), but this may require committers to modify the patch to match
their project layout (workspace per branch or all branches in one
workspace) and some committers may not be using Eclipse/Subclipse.

<a name="CodingStandards-TestCases"></a>

## TestCases

When we make a change it's generally a good idea to include a jUnit
testcase which demonstrates the desired behavior. Changes that only affect
a specific database or only operate in a certain environment (ie DB2 on
Z/OS, or only when used with SunOne) are exceptions to the rule. 

The testcase should be self validating via jUnit asserts. Writing messages
to system.err or system.out is discouraged - they lead to the impression
that some manual interpretation of the results must be done. Messages like
these are useful when developing the tests or when diagnosing problems but
should not be committed. 
