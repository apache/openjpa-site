Title: OpenJPA Up Close and Personal

<a name="OpenJPAUpCloseandPersonal-Summer2007MeetingInformation"></a>


## Summer 2007 Meeting Information

The meeting is on the 6th and 7th of August, 2007.

<a name="OpenJPAUpCloseandPersonal-Agenda"></a>

### Agenda

<a name="OpenJPAUpCloseandPersonal-Monday6August"></a>

#### Monday 6 August

<table>
<tr><th>Time</th><th>Title</th><th>Description</th><th>Presenter</th><th>Sponsor</th><th>Presentation</th></tr>
<tr><td class="border">9:30 - 10:00</td><td class="border">Introductions</td><td class="border"> </td><td class="border"> </td><td class="border"> </td><td class="border"> </td></tr>
<tr><td class="border">10:00 - 12:00</td><td class="border">OpenJPA Architecture</td><td class="border">High-level walk-through of OpenJPA architecture, including all the maven modules and the major internal abstractions.</td><td class="border">Patrick Linskey / Abe White</td><td class="border">Patrick Linskey</td><td class="border"><a href="http://people.apache.org/~pcl/2007/08/OpenJPAArchitecture.ppt">Microsoft PowerPoint</a><br/>
<a href="architecture-notes.html">Notes</a></tr>
<tr><td class="border">12:00 - 1:00</td><td class="border">Lunch</td><td class="border">BEA Cafeteria or elsewhere in the area</td><td class="border"> </td><td class="border"> </td><td class="border"> </td></tr>
<tr><td class="border">1:00 - 2:30</td><td class="border">FindBugs Presentation</td><td class="border">Discussion with Bill Pugh (FindBugs) about how best to use FindBugs on OpenJPA, including a focus on how to use it for "new" bugs as code changes come in, vs. fixing the issues that already exist.</td><td class="border">Bill Pugh</td><td class="border">Craig Russell</td><td class="border"><a href="findbugs-presentation-notes.html">notes</a>
</td></tr>
<tr><td class="border">3:00 - 4:30</td><td class="border">Query Processor</td><td class="border">There are a lot of query JIRA issues; some background might enable more people to help out</td><td class="border">Marc Prud'hommeaux</td><td class="border">Craig Russell</td><td class="border"><a href="http://people.apache.org/~mprudhom/OpenJPAQueryFramework.ppt.gz">Microsoft PowerPoint</a><br/>
 <a href="http://people.apache.org/~mprudhom/OpenJPAQueryFramework.key.zip">Apple Keynote</a>
</td></tr>
<tr><td class="border">5:00 - 5:30</td><td class="border">Day One Wrap-Up</td><td class="border">Figure out how we want to change the schedule
for the next day</td><td class="border"> </td><td class="border"> </td><td class="border"> </td></tr>
<tr><td class="border">7:00 - ???</td><td class="border">Dinner and Socializing</td><td class="border">Presumably in San Jose</td><td class="border"> </td><td class="border">Patrick
Linskey</td><td class="border"> </td></tr>
</table>


<a name="OpenJPAUpCloseandPersonal-Tuesday7August"></a>

#### Tuesday 7 August
<table>
<tr><th>Time</th><th>Title</th><th>Description</th><th>Presenter</th><th>Sponsor</th><th>Presentation</th></tr>
<tr><td class="border">9:30 - 10:00</td><td class="border">Day Two Kick-Off / New Agenda Item Review</td><td class="border">Discuss what we'd
like to talk about today, what we'd like to focus on that came up
yesterday, and other topics that have occurred to people since yesterday</td><td class="border"> </td><td class="border">
</td><td class="border"> </td></tr>
<tr><td class="border">10:00 - 10:30</td><td class="border">JIRA triage</td><td class="border"> </td><td class="border"> </td><td class="border">Craig Russell</td><td class="border"> </td></tr>
<tr><td class="border">10:30 - 11:00</td><td class="border">XML column support</td><td class="border"> </td><td class="border">Catalina Wei</td><td class="border">Patrick Linskey</td><td class="border"> <a href="artifacts/JPA XMLColumn mapping.ppt">JPA XMLColumn Mapping.ppt</a>
</td></tr>
<tr><td class="border">11:30 - 12:00</td><td class="border">API Design and Forwards-Compatibility</td><td class="border">OpenJPA has a number of APIs that we expect to be visible to developers. These should be stable over time, and should be well-designed to meet the needs of our developers. This is currently not always the case (OpenJPAEntityManagerFactory extends a billion interfaces, for example, our event frameworks sometimes require code changes for people who implement the event interfaces, and we use a combination of enums and symbolic constants even in our org.apache.openjpa.persistence interfaces). I'd like to discuss this to raise awareness about the issue, and also discuss how to improve things in the short term. I'd also like to bring up the idea of an API jar that should contain enough for the average development team to link against.</td><td class="border">Patrick Linskey</td><td class="border">Patrick Linskey</td><td class="border"><a href="apidiscussionfollowup.html">APIDiscussionFollowUp</a>
</td></tr>
<tr><td class="border">12:00 - 1:00</td><td class="border">Lunch</td><td class="border">BEA Cafeteria or elsewhere in the area</td><td class="border"> </td><td class="border"> </td><td class="border"> </td></tr>
<tr><td class="border">1:30 - 2:00</td><td class="border">Fluid</td><td class="border">SDO bindings to OpenJPA</td><td class="border">Pinaki Poddar</td><td class="border"> </td><td class="border"> </td></tr>
<tr><td class="border">2:15 - 2:45</td><td class="border">Where to next?</td><td class="border">OpenJPA 1.0, OpenJPA 1.1, JPA 2.0, SDO, etc.</td><td class="border"> </td><td class="border">
</td><td class="border"> </td></tr>
<tr><td class="border">3:00 - 3:45</td><td class="border">Joins</td><td class="border">There are a lot of issues around joins. In particular,
subqueries seem to have issues. Discuss.</td><td class="border">Abe White</td><td class="border"> </td><td class="border"> </td></tr>
<tr><td class="border">4:00 - 4:30</td><td class="border">Metadata Resolution</td><td class="border">Metadata lookup, classloaders, static
caches, etc.</td><td class="border"> </td><td class="border"> </td><td class="border"> </td></tr>
<tr><td class="border">4:30 - 5:30</td><td class="border">Update pathway</td><td class="border">Updates, statement batching, reordering, etc.</td><td class="border">
</td><td class="border"> </td><td class="border"> </td></tr>
<tr><td class="border">5:30 - 6:00</td><td class="border">Wrap-Up</td><td class="border"> </td><td class="border"> </td><td class="border"> </td><td class="border"> </td></tr>
</table>

<table>
<tr><td class="border">???</td><td class="border">mappingtool</td><td class="border">What do the options do? What about new options?</td><td class="border"> </td><td class="border"> </td><td class="border"> </td></tr>
</table>

The sponsor is the person proposing the agenda item, and is responsible for
making sure that a given agenda item actually happens. The sponsor is not
necessarily the person actually presenting / leading the discussion for a
given item.

<a name="OpenJPAUpCloseandPersonal-Venue"></a>

### Venue

[BEA headquarters in San Jose](http://maps.google.com/maps?hl=en&safe=off&client=firefox-a&q=bea&near=San+Jose,+CA&fb=1&cd=1&ie=UTF8&ei=QGmhRq7MBImUjQO27-nGCA&cid=37379388,-121922929,10392251224970924111&li=lmd&z=14&t=m)
 (near SJC)
2315 North First Street
San Jose, CA

There is plenty of parking. The meeting room is in Building 1, which is the
further-south building, abutting both First Street and Charcot Avenue. If
you drive up First Street from the south, your best bet is to turn left on
Charcot and then right into the parking lot. The receptionist in Building 1
will point you in the direction of the conference room.

We have wireless internet available, so it should be easy to stay in touch
in the break periods. Hopefully, all the sessions will be sufficiently
riveting that nobody will be playing around on the internets during the
sessions.

Dial-in information:

> Toll Free Dial-In Number (US & Canada): (866) 484-4232 <br/>
> International Dial-In Number: (702) 894-2358<br/>
> Conference Code: 1774023

> Webex information for day 1:<br/>
> Meeting number: 923 554 073 <br/>
> Meeting password: openjpa <br/>
> <a href="https://bea.webex.com/bea/j.php?ED=94343937&UID=0">https://bea.webex.com/bea/j.php?ED=94343937&UID=0</a> 

> Webex information for day 2:<br/>
> Meeting number: 924 199 496 <br/>
> Meeting password: openjpa <br/>
> <a href="https://bea.webex.com/bea/j.php?ED=94344132&UID=0">https://bea.webex.com/bea/j.php?ED=94344132&UID=0</a>

If you're new to webex meetings and plan to join via webex, it's probably a
good idea to go to that link ahead of time to get things set up.


<a name="OpenJPAUpCloseandPersonal-AttendeeList/LocalTransportationLogistics"></a>

### Attendee List / Local Transportation Logistics

<table>
<tr><th>Attendee</th><th>Location</th><th>Carpool needed?</th><th>Carpool space</th><th>Lodging</th></tr>
<tr><td class="border">Patrick Linskey</td><td class="border">San Jose</td><td class="border">No</td><td class="border"> 0 </td><td class="border">Crowne Plaza 282 Almaden Blvd.</td></tr>
<tr><td class="border">Craig Russell</td><td class="border">Mountain View </td><td class="border">No </td><td class="border"> </td><td class="border"> </td></tr>
<tr><td class="border">Marc Prud'hommeaux</td><td class="border">San Jose</td><td class="border">No</td><td class="border"> </td><td class="border">Crowne Plaza 282 Almaden Blvd.</td></tr>
<tr><td class="border">Christoph Bussler</td><td class="border">San Jose</td><td class="border">No</td><td class="border"> </td><td class="border"> </td></tr>
<tr><td class="border">Pinaki Poddar</td><td class="border">San Francisco</td><td class="border">Yes</td><td class="border"> </td><td class="border">Galleria Park, 191 Sutter Street</td></tr>
<tr><td class="border"> Bill Pugh </td><td class="border"> Palo Alto </td><td class="border"> No </td><td class="border"> No </td><td class="border"> </td></tr>
<tr><td class="border"> Michael Dick </td><td class="border"> Remote (Rochester, MN)  </td><td class="border"> No </td><td class="border"> No </td><td class="border"> </td></tr>
<tr><td class="border"> Albert Lee </td><td class="border"> Remote (Rochester, MN)  </td><td class="border"> No </td><td class="border"> No </td><td class="border"> </td></tr>
<tr><td class="border"> Teresa Kan </td><td class="border"> Remote (Rochester, MN)  </td><td class="border"> No </td><td class="border"> No </td><td class="border"> </td></tr>
<tr><td class="border"> Kevin Sutter </td><td class="border"> Remote (Rochester, MN)  </td><td class="border"> No </td><td class="border"> No </td><td class="border"> Tuesday, Aug 07, Only
</td></tr>
<tr><td class="border"> Joe Weinstein </td><td class="border"> Moraga CA </td><td class="border"> No </td><td class="border"> No </td></tr>
<tr><td class="border"> David Wisneski </td><td class="border"> San Jose CA </td><td class="border"> No </td><td class="border"> No </td><td class="border"> No </td></tr>
<tr><td class="border"> Catalina Wei </td><td class="border"> San Jose CA </td><td class="border"> No </td><td class="border"> No </td><td class="border"> No </td></tr>
<tr><td class="border"> Daniel Lee </td><td class="border"> San Jose CA </td><td class="border"> No </td><td class="border"> No </td><td class="border"> No </td></tr>
<tr><td class="border"> Aditi Das </td><td class="border"> San Francisco CA </td><td class="border"> No </td><td class="border"> No </td><td class="border"> No </td></tr>
