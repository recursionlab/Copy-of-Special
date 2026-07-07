
Beyond the Prompt: Quantizing AI into Proactive Operators. The evolution of AI as a strict mathematical phase transition. Proactive AI: Elevating Agent Skills to Macroscopic Operators. Quantizing AI into Executable Skills as Math Operators. All rights w/ Authors: "A Comprehensive Survey on Agent Skills: Taxonomy, Techniques, and Applications" Yingli Zhou, Shu Wang, Yaodong Su, Wenchuan Du, Yixiang Fang Member, IEEE, Xuemin Lin Fellow, IEEE from The Chinese University of Hong Kong, Shenzhen Agentic Coding Needs Proactivity, Not Just Autonomy Nghi D. Q. Bui and Georgios Evangelopoulos from Google Labs

## Transcript

Hello community. So great that you are back. Let's talk about the next level of artificial intelligence. No, we're not

talking about autonomous AI system. Come on. We are going to talk about the next step. A proactive AI, a continuous

monitoring AI that actively sets its own action. And we have two brand new study

here. One is from the Chinese University of Hong Kong and the other is from Google. So let's dive in. Now can assure

you the next token prediction will not completely disappear but we do not have time for this anymore in our classical

transform architecture. No it is now relegated here to the if you want cognitive control layer while the action

space where you decide which action to take here is now if you want coarse grained into a higher order symbolic

operator field and these are of course our skills. Now you know in theoretical physics you

don't do actually for each macroolelecule a complete quantum electronamic analysis or simulation for

every single quark or electron of luron you know you use approximation. So you

decouple now let's say the fast light degrees of the freedom let's say the electrons from the slow heavi.

So you try to make your life easy if you code here your solution. Guess what

we're going to do maybe the same thing here. Now let's say in modern AI LLM next

token prediction is here the fast probabilistic electron cloud. Now it's

brilliant at fuzzy reasoning some intent interpretation and navigating unstructured state spaces. However, if

you force this electron cloud to compute a real heavy rigid mechanism here of a

nuclear of executing here a multi-step API protocol or whatever the system

becomes highly entropic it will start to hallucinate and finally it will

collapse. So this is not our goal. Now let's talk about agent skills

because agent skills you will see in our study here act like the heavy nuclei. So

you know skills no skill mds beautiful localized stable and the beauty is

deterministic procedural bundles of whatever we have. So the LLM nang waste

the token hallucinating how to write an API call character by character. Now the

LLM next token prediction is elevated if you want to an orchestration level. Now

because now its only job is to compute the transition amplitudes between the different microscopic skills between the

deterministic procedural bundles and not anymore between each next token. This is

just here not intelligent enough anymore. No, if you want to learn more about skills and how I see skills here.

Yeah. EIG vectors quantum error codes industrial EI skill MD is not enough and how Q1

handles your agent skill MD outperforms entropic I have a lot of videos but let's come back to the basics so in

classical LLM agents like a react agent the agent follows here a microscopic

perception reasoning and an action loop no simple so when observation leads here

to a reasoning state generated here token by token mapping to a low-level atomic action

like a raw tool call. This is our old system and the authors of the first paper and you will see identified it

doing this at a micro level creates a massive procedural gap because think

about it the phase space of all possible generation is simply too large to have

here a false computation and the probability of an unbroken chain of flawless execution you know it it will

decay exponentially given here a particular sequence length. So this is

maybe not the way to go. So therefore what about this idea we introduce here a

skilled tupole here where the outs or perform no a mathematical projection. So

what they do and to be absolutely clear they now say think about my example here

with the electron cloud and here the nuclear say they pull now the protodual

knowledge out of the LM's implicit parametric memory from its neural

weights and externalize it into an explicit modular vector state.

This is a step to significant become at first almost a deterministic system and

second extreme fast. We don't have any more the bottleneck of predictor next token. Yeah. So skill tuple beautiful.

So when the agent operates it evaluates here the applicability of some constraints C against the current

observation over the time t. And if a match is found let's say like a rag like

retrieval methodology. And yes, this is the reason why my last two videos were on rag because we will use something

like rag here, maybe also here for this particular skill manifold. The agent

executes all the procedure that defined by m our main document here and the code

or our auxiliary resources we call r. So what this means mathematically the

action space transitions now from a continuous like distribution over the vocabulary V of size let's say 65,000

text tokens to a discrete mark of decision process or MDP over a finite

basis set of skills. You see how simple mathematics can make the simple things

in life. So this means the policy pi pi theta now optimizes here over the skills

s and instead of computing it a microscopic power model acts as a high level scheduleuler binding it available

to the operational inputs of our operator skills. This is here the first study May 8, 2026, Chinese University of

Hong Kong Shenzhen. Real nice. And they start with a comprehensive survey of

agent skills. Everything that we know up until today, you will find in this paper. Highly recommended. So basic

ideas agents handle the high level reasoning and the planning. So this is also here where you have here this

monster LLMC our GBD 5.5 over our Opus F 4.7 while the skills then on the other

hand form now the operational layer that enables a reliable reusable and composable execution and maybe you run

this on your local LLMs like I don't know you look here maybe at a gamma 4.

So let's go to the definition because a lot of questions are received from my viewers. Hey, skills and tools and API

calls and MCP. Is this not all the same? No, it is not all the same. Let's have a look. Tools such as search engines, code

interpreters, databases, domain specific APIs that you have extend the agents far

beyond their parametric memory alone. No, this is why we invented rag and then

our tools in standards that we have established such as the mall context protocols or MCP further reduce here the

integration friction by providing a unified mechanisms for the discovery and the invocation across heterogeneous

provided that you find on the internet. A tool exposes you if you want an atomic capability. It specifies what can be

done but it does not specify how it should be used. careful. So a search

tool does not say when search is preferable to the memory retrieval if you have a multi- aent system. An API

tool does not say what to do when the schema changes and a cord interpreter

does not say how the output should be validated. So you have clearly defined boundaries.

MCP and similar infrastructure standards solve also only an interoperability

problem not the procedural problem that we're going to have a look at of turning multiple tool calls into a robust

validatable and stable workflow. The articy of this first paper give us

here a definition that is interesting exactly in the idea that I started this

video. So say rather than treating your tool calls as an isolated operation

system store and reuse successful procedures that the orers now define explicitly as skills. You might know

them as kill MD file or soul MD files or whatever you have. No, but what is the

exact mathematical definition? A skill is a reusable procedural artifact with

bounded scope that externalizes task focused knowhow. Not only what can be

done but when to act, how to execute, what uristic or failure modes matter and

how to judge completion. Formally skill is modeled as I showed you as a tuple s

and we have M as our root instruction document. That is here what the agent can load and follow. R is of course here

a set of auxiliary resources, our reference documents, our reusable

templates, executable scripts or domain artifacts that it can that extend what the skill accomplishes beyond M alone.

And C C encodes another application conditions that govern when the skills

should be retrieved and applied expressed as metadata, natural language descriptions or simply vector embeddings

in high dimensional vector spaces. So this is a very general representation that we can start with.

Agent skills are now increasingly managed through some dedicated internet platforms. You can find skill net glow

skill up whatever you found and maybe this list is already out of date because

new resources are available for you. Now let's have a look at agent skill and they give us here in this paper some

illustrative example. You have here prepare grounded literature review. Step one a tool call

to a literature database searching. Step two the reasoning the topic clustering.

Step three another tool call. Step four summarization with the tool call to the paper sightings or whatever. Or you go

with pure coding here. You have the same tool call reasoning tool call tool call

fix investigating a data anomaly. You got the idea.

Now skills differ from our tools and MCP servers. No, because they encode

situated procedural knowledge, triggers, sequencing, fallbacks, pitfalls, and appear as bounded reusable artifacts

that can be loaded, inspected, shared, revised without becoming here an undifferiated handbook. Skills need not

to be tool centric. You have cognitive skills like a review checklist. No, or

anal an analysis workflow definition mainly uses here the internal knowledge of an LLM but still supplies structure

and reuse beyond some ad hoc prompting prompt optimization and tools expose operation skills

package you know for using them in context. Beautiful. Now that paper gives

us a real deep definition of skill representation. We classify how agent skills are

packaged here. Each guild consists of an instruction based main document M already have seen this tuple. No. Then

the auxiliary resources R and the trigger conditions C. Semmetically skill

externalized procedural knowledge include operational structure branching uristic normative constraints with M

serving as the primary human readable representation or skill MD file. Now

they have here some representation. Of course you can have textbased, you can

be code based and you can be a hybrid based and your skill representation and they give you here all the different

methodologies and other publication they found here

for this particular sequence. So if you want to have a look at the literature I highly recommend this and look at what

they just found at hybrid base from Jarvis here. Unbelievable. The next is the skill acquisition.

This is the process of constructing or generating new skills. And here the authors tell us listen we can be human

derived like those. We have an experience derived methodology like 1 2 3 my good 1020 here. We can be task

derived like here met GPT self-discover or sw agent. And we have a corpus

derived here like auto guide or hugging GPT if you remember this years ago. So

they really give you here a beautiful overview of all the possibilities.

If you want to see this here more here in an image oriented presentation, the skill acquisition methods. So we have

the human derived skill acquisition, the experience derived skill acquisition, the task derived skill acquisition and

the corpus derived skill acquisition. And please have a look here at all those images.

The next one is the retrieval of our skills. No, as I've shown you here, skill hub and whatever you prefer, but

careful, they can be heavily infested here with malware and whatever. So,

yeah, this is really not here a secure operation at all. Skill retrieval and

skill selection. Let's clearly define what is what. Skill retrieval concerns

how a large skill pool is reduced to a manageable candidate set for your particular task. For example, through

semantic matching, lexical lookup, generative access or structure averse

search. You have your keyword search. You have all the rag possibilities you can find. You have here to find here

from a large skill pool. Your manageable candidate set. And this reminds you perfectly here of the complete retrieval

augmented generation rag methodology from the old times when we had a vector lookup.

And then the skill selection in contrast concerns which candidate skills should

ultimately now be invoked whether multiple skills should be composed and how such choices should adapt to the

current observation to the sub goal to the budget that we have to the resources that are available for us and you

understand exactly what we're talking about. So you see rag comes back to bite us here also the more I think how many

skills we have 100,000 200,000 skills available on the internet this is just going crazy

so just cross reference rag is going to come beautifully

skill retrieval and skill selection here the screenshot from the image the orers provide us here dense retrieval sp

retrieval generative retrieval structural retrieval So this is here what we would call a graph rack search

in the skill selection for your particular job. You have your costs, your costs, your utility, all the

feedbacks you have maybe from other users, the context they were selection and then a skill composition if you need

four or five different skill elements here for your particular complexity.

Here the artist give us also here beautiful here uh literature recommendation. And here you go from

dense embedding spores and keywords retrieval to generative retrieval like tool lm or skill weaver autoskll here

skill net structure aware with hierarchical dependency graph here like skill net here and context aware skill

composition me skill momento skill skill bench and my goodness look at all this

literature that is available for you now what is absolutely fascinating skill evolution how does it evolve so

evolution asks how an already formed skilled artifact and let's go simple with a skill markdown file is revised

validated optimized shared and governed after it has been formed no

but it can also be a skill folder a program API toolbox function skill graph structure whatever you're working and

here the artists give us here this division here into skill revision skill validation policy coupling repository

evolution and runtime governance beautiful you have here If you want to see the skill revision,

skill validation, everything here also as a screenshot here in a visualization. Beautiful. So this survey is really

providing here a great overview over examined LM based agent systems through

the lens of agent skills. Remember reusable procedural artifacts that

coordinate our tools that we have our memory that is available the runtime context here the resources your budget

whatever are here the boundary conditions for your systems and yeah while the agents handle here the

highlevel reasoning and the real complex planning how to execute a particular job

how to reduce the complexity of a single task into lower complexity 5 6 10

subtasks skills from the operational layer now enable a reliable and composable executioner. As I told you,

maybe you go with a propriator huge LLM here for a complex reasoning and the

planning task and maybe for the skill execution you go with a local cheaper smaller language model and I have a

particular video that shows you which are the best small language model for this particular task.

Interesting. But now let's take really a look into the future with our second

preprint. And now we want to have here an AI system that is always on. So not

open claw. Let's go to the next step. What is the next category here? The level three of AI that we can now find

not autonomous driving. What is the next level after autonomous driving? So this

is an interesting question and you're not going to believe that Google presented here a paper May 7, 2026

achantic coding and of course we focus now here on the simplest sector that we

have code we can verify falsify execute different languages everything is

available in code beautiful so atantic coding needs proactivity not just

autonomy Google labs So what is the idea by Google? They say

the next shift that we expect in artificial intelligence is not here that you have your clawed code that you have

your I don't know whatever systems you use. We move now to proactive agents.

Why should the wait till the user comes with a prompt with a task for the eye to

fulfill? The eye can be always on. The I can be scanning all your communication,

all your action, all your environment, all your competitor, all your industry continuously.

And the I can understanding here completely what you as a human, what is your intention, what is your job

professional or maybe private, what is your environment, what is your industrial professional level of coding,

how can the help you to become I don't know to the go to the next step. Let's

formulate it in this way. So this is what we're talking about proactive agents. You don't interact with the eye.

The eye now interacts with the human whenever the eye sees it fit.

So Google tells us continuously absorb repository tool chain workflow context. Remember we only here focused on coding.

Infer what matters from a highle developer needs. Identify emerging problems that you have maybe in your

pipeline or opportunities you simply did not notice or you forget or whatever

happened to you and then the eye decides what to do next before you as a human

type a narrowly specific prompt and this arrives then at the eye. So Google tells

us you know what we have here open claw always on we have this system that are

completely scanning as let's say an AI assistant your professional life your

private life whatever you do whatever is in your environment so they say okay we

do have some products and they that already moved from an initiation away here from the explicit prompt here

course automations or cloud code routines or jewels schedule task let coding agents done here from schedules

you know do we have the web hooks GitHub events the integration or monitored repo state whatever is the trigger it doesn't

matter yeah whatever is here an important trigger but they tell us here but this is this is what we have today

where if you look in the future we want to they are not yet situation aware

proactivities so we want to go the next step

and Google calls it a unit of proactive behavior here with an AI system they go here with the term of an insight. So you

see it really becomes important that we really understand exactly what we're talking about here in the definition of

our terms an insight a context grounded time-sensitive hypothesis about what

matters next for the human developer paired with a decision to notify the

human question the human draft something or stay silent. So this is interesting and interesting

if you read the paper. Google has a particular focus on stay silent which I

had to smile a little bit because they understand that sometimes you do not want your AI companion to do everything

for you. You know, you want as a human also to be still in the loop, make decisions, maybe meta decisions. But

yeah, so interestingly, Google gives us here this level of

agency. Level one, reactive agents run only when a human ask them to do

something when prompted by a human. Level two, what you have in open claw, your scheduleuler. Schedule agents

Monday at 9:00 do ABC D. Schedule agents run from schedules or predefined

triggers and may filter batch rank outputs do not learn across context par

developer interruption policy nothing. It just has a fixed schedule. It doesn't learn but it knows what is happening.

And then the third level is the situation aware agent. The agent that

knows everything about you as a human, as a person, as a professional coder, whatever. So this situation where agent

monitors a continuous event stream that is happening live compare expected

benefits with interruption cost treats silence as an explicit action smile and

update a pair developer model from feedback.

So this is now interesting. Think about this. Suddenly you are not anymore a member of the group of software

developer or coder or whatever you'd like to call you when you work with EI. Now this is an individual AI specific

targeted on your abilities on your knowledge what you can

do how you are connected what you are currently working on as a human. The eye knows this because the II is always on

and when you go to sleep the eye might have a look at all your documents, all your emails and whatever you have done

in the last 5 years. So great. Yeah, people who bought here a Mac Mini said, "Oh, maybe it was a good idea to have

here an isolated system." But this is not the point. Google tells us that this is coming. So what is here a prototype

of a proactive agentic coding engine? You have all your resources that you use during the day. you know the calendar,

GitHub, Slack, Docs, whatever app or system you use doesn't matter. No, and

you have a continuous stream that goes now into the eye because the eye you have given access

the eye to your complete computer realtime data ingestion from diverse external sources, your personal sources,

privacy, forget about it intelligence. Then we have our proactive engine. So

the we have the development state that is exactly understanding what is happening right now where you are as a

human right now where is are you with your task with your coding with your particular procedures and then we have

and this is I think absolutely fascinating a developer so your personal

human profile your mental model who the developer is and what the

developer cares about. So your name is Alex. You have a particular focus here

on back end API on security. You have your topics Rust, GraphQL, distributed

systems. You have your personal preferences that low interruption mode and

everything. But you also have let's say areas where you are not the perfect coder. So it knows your strength, your

weaknesses, everything because this system is continuously monitoring whatever you do each single question

that you ask any system and it integrates this in its knowledge in its insight and now it understands

okay I have a coder that is uh not really an expert in the area A. So

whenever we have a new development here in area A, it will notify me or it will

question me. It will test me. It will give me here maybe here a puzzle to do

to see exactly where I am here with my knowledge, it will draft here. Maybe if

I wake up at 7:00 in the morning and I say, "Hello, my little uh proactive developer mental model. How are you?"

And the AI will respondse to me, hey, I noticed that you wanted to do today this and this coding. So I already have done

it overnight and now let's talk how we can further develop you as a human coder

because I have noticed you have the following 17 weaknesses. So life is

going to be beautiful with this always on AI and then you have your interaction

and and hopefully Apple will make Siri here really hear the beautiful interaction here way. So you have it

wherever you go, wherever room you enter in your house. No, you will have here

your conversation. It's a little a little bit strange this paper, but it is absolutely fascinating

if you look at the mathematical side because how do they imagine to train this system? So let S denote here the

developer state at a particular time t. This means the open buffer, the branch, the recent commits, the calendar, the sprint deadlines, the ticket status, the

communication context, everything that you have. Yeah. Let E denote here the event stream, the cross context event

stream since since ever since the last decision. And then AI groups invent into

code, project, communication, infrastructure, developer behavior. Yes, I forgot to mention that your emotional

and professional behavior is also recorded and therefore your part here of this decision process. And then let a

for an action have here the inside okay the action space that we have normally

in an optimization here of an AI model of an LLM and let's make it easy we just

have the following notify question draft and stay silent and again you see stay

silent this is yeah where I smile so the first three actions show here a classical insight that we defined and

Google wants to make sure that there is also here a particular inside when the AI I learned from your behavior with the

eye, this companion that you have right on your side every little second of your complete life that it should stay solid.

Mathematically it is of course here that we work with expectation here and in the simplest case the authors of Google tell

us hey look this is here our optimization that we have no like a classical LLM optimization when the LLM

is learning and it is kind of frightening that you can apply for this

human mental behavior model exactly the AI guidelines where the eye learned

copying near the complete internet but think about it yes of course whatever it found on the internet is from human. So,

okay, we use here the exact same a little bit further developed mathematical statements here like you

see here where O here is of course as you already guessed it here an outcome

and developer observable outcome of a particular action. A can be a response, a downstream code change, a recovered

context whatever you scores how useful that outcome is. Now to the human

developer while our data captures here. What the agent has learned about this particular developer you and the costs

the costs in dollars here is of course here the cost of breaking here the flow.

Interestingly they try to integrate here breaking the human flow. You know if you are focused here on a particular task

should the AI come now and interrupt you and say hey excuse me I just found that

you made a mistake. I just found well I already did the job for you you know and

yeah you are not here really the using the optimized mathematical uh structure but you were a little bit here

nonprofessional. No so try to find here a cost statement here

to really get here that perfect companionship running. Yeah.

So you know we have here a limited discrete action space notify. So this means a state change the question the

clarification the draft the pull request command the patch or the review thread and then stay silent choose not to

interrupt the human. So I think this is interesting but you know what we go up a

complexity level because now the policy optimization as I told you is a classical LLM training is now with an

added layer and this is here your human behavior because now it is not that you are the a group member where you can be

averaged over your behavior but now it is your individual daily second per

second behavior. An insight. An insight is define the

context ground the timesensitive hypothesis that the eye has about what matters next to you in your work in your

profession. What is your human reaction? What should the eye provide for you if

you have a particular goal? Whatever paired with an action that the eye is going to take and the eye is always on.

So maybe you're surprised when you wake up one day and the eye has a surprise

for you. As I told you, we have to add a complexity level because now we don't have our pit or our classical policy

optimization. But now we have to deal with an inside policy that Google calls it, selects now the action, chooses the

evidence, frames a message and updates the future decision here from the human feedback. So now it is not that you have

just the coding as a topic to optimize coding, but now the insight is it is not

a multi- aent system. You as a human with your AI assistant, you are not multi- aent. You are in a different

cooperation pattern. Yeah. And the eye has to learn according to Google the

inside policy here the interplay between the eye and you as individual you as a

human. So this will be highly personal data. So I think

entropic or openi or google or whatever will provide us here with some highly

specific individual personal let's call it memory or knowledge or an inside

policy how ani should deal with you what is your preferred way to have an AI

companion right next to your site. Yeah, mathematics level three engine

inside instead produces here an inside stream that can be monitored, acted on, ignored, never shown, whatever. But we

have this stream every every global corporation can touch this data stream

and then they tell us with score whether that stream keeps an agent on the right path. So they want to steer here every

little second here what is happening. So they say let t be an index here of the

decision point capital t the number of decision point in a scenario s the current developer and the project state

pi pi data the surface policing being evaluated and they go now with three new

metrics. The first is an inside decision quality IDQ and this scores whether the

agent choose the right action at the right time. Did it provide you with the

right code piece before you ask it? Did the eye really understand looking at

what you are typing what your job is that now is the perfect time to provide you with the solution to the next step?

Yes. No. Inside decision you see beautiful. We can optimize this. We can learn this after hundreds and thousands

of hours of interaction with UI. UI will definitely learn this. It's a simple

formula. to other the context grounding score ask whether the shown insight is

supported by the right evidence this is interesting it means is this

really a faithful sync machine that you as a human really trust and how can it

optimize that you trust this machine more now this is a highly individual

thing and then of course the learning lift which I think is great measures whether The feedback improves your later

decisions. So if you tell the AI, hey I would prefer you behave in this way or

the AI tells you hey human I would prefer you do something in another way. You know you will have to find you know

this is like a marriage that you have here in a relationship. Hey, the learning lift and it can measures

because the AI is always on. Everything you type, everything you say is analyzed by the eye and the eye can absolutely

analyze and notify you when you're learning lift here is above average.

Isn't this what we always wanted? Okay, so here we go. Now together the matrix

ask you whether the agent choose you the right action used the right evidence to

present to you and improved itself after the feedback after you interacted and

said yeah I like this I do not like this you know this no so those are now our

additional elements that we have to train an AI on and we do it only on code

because code is simple code is verifiable code is executable there's no

interpretation, there's no whatever. So the framework above makes here the proactivity testable

before let's say Google deploys here a full level three coding agent. So you

see the future of AI is absolutely amazing

and it means that coding agents that we have cloud code today will mature here from the tools that execute prompted

task. Imagine a human asking a machine to do something into level three partners that may notice the drift, the

uncertainty or emerging opportunities before you as a human ask the machine to

do it before you have to type any prompt. And proactivity in aentic coding

should be judged not by how often an agent acts but whether it surfaces at the right the right insight at the right

time. No, I think this is interesting. I think Google has some insight here that

sometimes when an AI interrupt you proactively that humans do not really prefer to be interrupted 20 times by any

like in open claw when this open claw sync wants to tell you yeah that you as

a human okay so we have enough evidence and stay silent when the intervention is

unwarranted and at the end you will find in this preprint by Google Google lab sorry that

the proactivity in the aantic coding scheme should be judged not by how often an

agent acts now. No, but whether it surfaces here as an coding agent as claw

code whatever the right insight at the right time for you as a human being

having enough insight into your human thought process into your professional

level into your professional argumentation into the way you think as a human [clears throat]

because the eye has to learn this. It has to simulate this, has to detect a

pattern in your behavior so that the eye is able to become a better companion

with the time. So therefore, it needs a lot of evidence and there's also the

option what I like to stay silent when the eye intervention is simply not

really appreciated by the human being. I hope you had a little bit of insight

into what is coming to you in the next weeks or month. I found it absolutely fascinating to have here the let's call

it the Chinese view here looking back what we have up until now where we are

here with our skills tool our agentic skills our autonomous agents and then

look here at Google where they go now for proactive agents where you as humans

you don't have to ask anything anymore because this guy is monitoring you

completely hope to see you in my next