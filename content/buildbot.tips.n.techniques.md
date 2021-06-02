Title: BuildBot Tips and Techniques


<a name="Buildbot.Tips.and.Techniques"></a>

# Tips on Using Apache BuildBot for OpenJPA Documentation Build

## Get Help from Infrastructure team

* Open an [INFRA JIRA issue](https://issues.apache.org/jira/browse/INFRA) to request:
    * new requirements and set up for the build system
    * creating new build queue

* Here's an [example JIRA](https://issues.apache.org/jira/browse/INFRA-7738) that was used to enable the 2.3.x doc builds.
    * note the Buildbot component and the openjpa label
    * also note that we as OpenJPA committers have commit karma for the [openjpa.conf](https://svn.apache.org/repos/infra/infrastructure/buildbot/aegis/buildmaster/master1/projects/openjpa.conf) file required for this doc buildbot

## Use IRC to communicate with openjpa-bot server

* From a browser or an IRC application, join the #asftest channel in server [irc://irc.freenode.net](irc://irc.freenode.net).
     * /join #asftest

* Direct message the openjpa-bot
     * /msg openjpa-bot status
     * If openjpa-bot member does not exist, then ask about it on the #asftest channel.  They are very helpful.

* On most irc clients this will open a direct dialog with the openjpa-bot member and you can use the commands outlined below

### Get Help

  	Enter> openjpa-bot: help
	openjpa-bot	Get help on what? (try 'help <foo>', or 'commands' for a command list)
	
	Enter> openjpa-bot: commands
	openjpa-bot	buildbot commands: commands, dance, destroy, excited, force, hello, help, \
	    last, list, mute, notify, source, status, stop, unmute, version, watch
	
	Enter> openjpa-bot: help force
	openjpa-bot	Usage: force build [--branch=branch] [--revision=revision] [--props=prop1=val1,prop2=val2...] \
	    <which> <reason> - Force a build
	
### Get BuildBot status

    Enter> openjpa-bot: status    
	openjpa-bot	openjpa-1.0.x-docs: idle, last build 7h21m20s ago: failed
	openjpa-bot	openjpa-1.2.x-docs: idle, last build 7h23m18s ago: build successful
	openjpa-bot	openjpa-1.3.x-docs: idle, last build 7h30m12s ago: build successful
	openjpa-bot	openjpa-2.0.x-docs: idle, last build 7h37m27s ago: build successful
	openjpa-bot	openjpa-2.1.x-docs: idle, last build 7h46m19s ago: build successful
	openjpa-bot	openjpa-2.2.1.x-docs: idle, last build 8h09m07s ago: build successful
	openjpa-bot	openjpa-2.2.x-docs: idle, last build 7h56m22s ago: build successful
	openjpa-bot	openjpa-trunk-docs: idle, last build 8h22m07s ago: build successful
	
### Submit build

    Enter> openjpa-bot: force build openjpa-1.0.x-docs "a description here....."    
	openjpa-bot	build #35 forced
	openjpa-bot	I'll give a shout when the build finishes
	openjpa-bot	build #35 of openjpa-1.0.x-docs is complete: Success [build successful] \
	    Build details are at http://ci.apache.org/builders/openjpa-1.0.x-docs/builds/35
 
