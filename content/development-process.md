Title: Development Process

<a name="DevelopmentProcess-*DRAFT*OpenJPADevelopmentProcess"></a>

# *DRAFT* OpenJPA Development Process

<a name="DevelopmentProcess-Trackingissuesandchanges"></a>

## Tracking issues and changes
* A JIRA issue is required for any substantive change.
In order to keep the list of JIRA issues under control, it is expected that
any controversial issue or user request for a feature or design change be
discussed on the dev list prior to entering it into JIRA.
* JIRA issues are not needed for small (e.g., typos) changes.
* Issue discussions
The preferred place of discussion on issues is the JIRA created for the
task.  If discussions occur on the dev list outside the JIRA, a link to the
beginning of the mail thread on the issue should be placed in the JIRA
issue so that users looking through JIRA can easily view the thread of
discussion on an issue. Please keep the Subject line the same so that the
email thread hangs together.  If discussion occurs on the dev list, it's
also recommended that a summary/conclusion on the thread be recorded in the
JIRA issue itself.

<a name="DevelopmentProcess-CodeReviews"></a>

## Code Reviews
* for public API changes:

    [RTC](http://apache.org/foundation/glossary.html#ReviewThenCommit)
 These changes have potentially broad effects on developers and users, and
therefore will require a code review and vote. Since some of these changes
will affect the API docs ('specs'), everyone within the community is
encouraged to review and vote. The Committer votes are binding, but the
sentiment of the entire community will be strongly considered.

* for all other changes:

    [CTR](http://apache.org/foundation/glossary.html#CommitThenReview)
 Although CTR is what is specified, developers should feel comfortable
requesting the list for peer review before committing.

<a name="DevelopmentProcess-Testing"></a>

### Testing
* Developing test cases and running test suites are desired but not
required prior to an integration.  If unit tests are created for a change,
the developer is encouraged to add them to the JIRA issue for sharing.
* When fixing a bug, it is strongly encouraged to attach to the JIRA a test
case that fails prior to the fix and succeeds after the fix is applied.
When the fix is committed, the test case should be committed as well.
