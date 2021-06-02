Title: FindBugs Presentation Notes

<a name="FindBugs-Presentation-Notes"></a>


Bill Pugh

(side note: compiling with "-target jsr14" will allow us to use generics
and compile to JDK 1.4 usable code)

Static analysis
    Analyzes program w/out executing
    Not a replacement for testing

Find bugs that are one step removed from a syntax error

Finding different categories of problems

"Embrace and fix your dumb mistakes"

Bad method calls: not using return parameters, not throwing newly
constructed exceptions,
 etc.

OpenJPA 38 issues (35 critical)

Checks for null when subsequent actions would cause an NPE (numerous found
in OpenJPA)

Bad practices, like hashCode() w/out equals()

Feedback about API-specific findbugs detectors (e.g., for JPA) would be
appreciated

OpenJPA is "good" to "average" in the number of bugs found.

OpenJPA:

 SimpleDateFormat is not thread-safe






