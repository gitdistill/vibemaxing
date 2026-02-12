# Define through discussion prompt template

## pi command: 
`/def <$1>`

## usage example
`/def we need to better define how cyclescrape should work`
_TODO: add 2 more examples_

## additional context: 
always load: `GOALS.md`

## general workflow pattnern:
`<interview or analysis>` then `<propose>` (these can loop), until: `<humanapproval>` then `<action>`

## discussion types:

- troubleshoot
- define problem
- evaluate solution
- investigate & analyze
- get alignment between user and agent

## logic:

if $1 is blank
- ask the user "what are we discussing?"
- then check reponse against below or infer

if $1 contains "troubleshoot"
- workflow: 
    - troubleshoot(loop)
    - validate bug (human approval)
    - update beads (action)

if $1 contains "define" or "problem statement"
- workflow: 
    - define problem (loop)
    - validate problem statement (human approval)
    - update `...goals.md` (action)

if $1 contains "solution" or "evaluate"
- workflow
    - evaluate solutions (loop)
    - make decision (human approval)
    - update `...arch.md` or `...spec.md` (action)

if $1 contains "investigate" or "analyze"
- workflow
    - investigate/analyze (loop)
    - review analysis (human approval)
    - update any (action)

if $1 contains "alignment" or "not aligned" or "misalignment"
- workflow
    - get alignment (loop)
    - make decision (human approval)
    - update any (action)

if $1 does not contain any of the above 
- try to infer from initial command argument prompt message

if you can't infer
- try to guess

if you can't guess
- ask the user


## tools:

- websearch _TODO: need to add exa-search pi extension_
- read only bash commands (read, find logs, etc.)
- then for actions
    - write tools for .md only
    or
    - bd commands for task creation and task details (based on discussion)

_TODO: do we need to add stuff around these:_

- rules
    - not implementing, no code files
    - adopt stuff from /plan pi package
    - you can only propose, user must approve
    - discussion is not done till the user switches to another (for e.g. `/doc`) via command or ends the session or says we are done

- compaction and handoff process?


