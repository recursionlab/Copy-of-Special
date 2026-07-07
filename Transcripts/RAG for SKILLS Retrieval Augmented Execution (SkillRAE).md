Standard AI engineering assumed that if you simply feed an LLM the correct tool repository, it has enough "reasoning" power to figure out the execution. SkillRAE proves this is mathematically naive. The LLM is essentially a raw CPU. Delivering uncompiled, isolated tools into its context window forces the LLM to do dependency resolution on the fly, which it fails at. The new insight is that Retrieval is not enough; execution requires Compilation. By explicitly rescuing and grafting boundary conditions (subunits) into a logically bound, low-token payload, we bypass the LLM's stateless amnesia and give it a fully resolved blueprint. all rights w/ authors: SkillRAE: Agent Skill-Based Context Compilation for Retrieval-Augmented Execution Xiangcheng Meng Shu Wang Yixiang Fang∗ from The Chinese University of Hong Kong, Shenzhen arXiv:2605.**10114**


## Transcript

Hello community. So great that you are

back today. Let's talk about something

crazy. We need now a rec system for

skills. Yes, you heard me right. Because

up until now, no standard AI engineering

was if you simply feed here an AI with

the correct tool repo, it has enough

reasoning power to figure out the

execution. And now we have a brand new

study that tells us, well, this is

mathematically naive. So let's start.

And we just continue where we left off

with my last video. We were talking

about quantizing EI into executable

skills as mathematical operators. And

you already see we went here from an act

action space transition here from a

continuous like distribution to a

discrete mark of decision process. We

have a finite base set of skills. And

now we continue especially if you're

working with open flow autonomous AI

systems. No, those based agents

increasingly rely on skill libraries.

hopefully reusable skill libraries to

sulfere the artifact rich task such as

documentcentric workflows data intensive

analysis of whatever you have in your

particular domain now there is a claim I

could not verify it that about 4,700 new

skills are added per day to the global

skill repos here which is crazy we are

here miday 2026

so we need a rack system now for skills

and guess what we have the first

publication And it is called ray. So you

know that in skill bench our classical

benchmarking how well agent skills work

across diverse task. This is here the

study. This is version three for March

2026. We saw if we have here I think it

was 86 task here across 11 domains

paired with corated skills. How good

does our systems perform? And you have

here everything from a hiko 4.7 to an

ous 4.6 six, Gemini three and you see

here without the skills here the first

block this is not prominent then with

the skills the dominant performance here

and then with self-generated skills we

are back almost to no skills which is

quite a consistent behavior across all

the different morals so self-generated

skills you know exactly what you have to

think about is now let's come back to

the standard rack it's like asking an LM

to answer here a question from a PDF and

you need to retrieve new updated

information that is not available in

your parametric knowledge. No. So you

retrieve static information and for a

physicist standard drag is like looking

up a fundamental constant of a whatever

a table whatever you have the mass of an

electron. So you retrieve text you

concatenate it to the prompt of the LLM

and the LLM reads it. But of course the

information is passive. Now in this new

skill you're retrieving operators. So

this means executable functions, code

blocks, API calls. So now we are

completely different. We need a

different mathematical space for this.

But luckily in my last video, we already

prepared for this. So I'm not just

retrieving here a particular physical

constant here or a parameter. No, you

are now actually retrieving differential

operators or if you would like to see it

through a glossy of theoretical physics,

you retrieve kind of a Hamiltonian of a

system.

Now skill ray is essentially a retrieve

augmented generation system but now

mathematically projected out of the

space of this passive factual knowledge

of this textual into the space of an

active procedural operator and this is

the reason why we call it not rack but

retrieval augmented execution since we

have executable operators in front of us

and therefore it is called ray. Great.

So we have a new study the Chinese

University of Hong Kong and Chen senior

skillway agent skill-based context

compilation for retrieval augmented

execution May 11 2026.

Now as I told you skill bench here what

is here typical agent skill how is it

presented? We have here some natural

language description together with some

optional linked files. know our skillmd

file, our assets, our pipex template,

our references here, our search MD, our

scripts, our search cool scholar, Python

files. This is here the classical agent

skills that we are talking about. If

you're not really familiar, I have quite

a lot of videos here on skill and

multiskll files here. Why skill is not

enough and one of my last video was here

super intelligent rack system, a

classical rack system here for meta and

yeah AI vectors as the human defined

skills. We already built those

mathematical spaces. But now we go a

step further.

In the classical rack system, the system

operates like a bulk scoop. Now it

calculates a global interaction

potential. You know our famous cosine

similarity between the task and some

available. And now let's not call it

vectors because let's say these are

macro molecules, you know,

three-dimensional objects. and dump now

the top 10 heaviest most relevant

molecules of course vectors into the

prompt. The problem is the agent needs

to synthesize now a specific reaction.

It might only require a tiny functional

group here on this complex

macroolelecule on this sphere. Maybe

only a subunit here that is located on

the macroolelecule that was not scooped

up. So we have a problem. We are missing

here some functions. We are missing some

operators. We are missing skills. We are

missing the ability to perform the job.

So if this was here this image here in

rack now guess what we build a graph. Of

course what else can we do in AI? No. So

the offline stage is we have a skill

repo. I don't know 10,000 skill or

whatever you prefer in your domain or

whatever you have as a standard repo.

And then we build a skill graph. This is

offline.

So we have of course skill community. So

we have different levels of granulation.

Then we have the pure skills that you

know and then we have all the subunits

of the skills. And this is now the

interesting part. We don't go with the

prefabricated skill MD files. We analyze

it. We see there's a lot of redundancy.

There's a lot of nonsense. There's a lot

of things we cannot verify coding. And

therefore yeah we have to clean up here

our skill repo.

Now the authors treat here the skill

library that we have as a multiscale

interacting system and act as a if you

want intelligent compiler if you see it

in computer science or an enzy if you go

to biotech. So they map now the state

space at three levels as I told you the

communities the bclusters the skills the

skills would be here our macroolelecules

and then the subunits. And if you go

with the biotech image here, these are

the functional groups that are on the

sphere of the macroolelecules and these

are just some subs skills or subunits.

Now they select now here for building

the graph the best macro skills but then

they cleave highly relevant or subunits

here from unselected skills also on and

graph them onto the selected one. So

this is now interesting. So you say I do

not go with a predefined skill structure

or with some predefined uh description

of what to do because they found out

that the quality of the skills that you

find on the internet is is is different

can vary. So we built now the

multi-level skill graph offline from all

the source kill MD files that you have

access or you said these are my files or

that you built up yourself. No. So the

graph builder extracts now the

normalized procedural element and

constraint subunit from each skill

dduplicates them globally. We don't need

duplicates and connects each retain

subunit back to the source skills. So we

build a graph and then we embed some

subunits here. And you're not going to

believe how we do it with the old method

of a sentence transformer embedding our

espert system. I guess I have more than

50 videos here at the very beginning of

my channel on espert. So we are back to

this methodology and the skill

description of course embedded here with

the same model at the retrieval time and

the skill communities are constructed by

embedding here the skill representation

and they're applying here a k means

clustering algorithm. So everything that

you know that you are familiar with. So

we have offline build our graph and now

online we have now our task request here

from a human that's me and now something

is happening. We have now we have to

build here of course the manifold and

then on this manifold we have a top down

retrieval and a bottom up retrieval. Now

just to make it here very simple I will

give you the mathematical definition in

a moment. The top down retrieval is

simple. No you just go here in a

classical way and you say okay I'll

select the skills that have I don't know

the keyword quantum in it.

But we also have a bottom-up retrieval

going here on the graph finding here

there's a specific subunit U3 on a skill

that was not selected here by the top

down approach. So we also go here down

to the subunits analyze the subunits and

say wait a minute this subunit to an

unconnected skill would be highly

helpful for the task and we bring it up.

So this means bottom up retrieval here

from this particular subunit of a skill

or a subskll. Then yeah we form yeah new

graph we have the older the relevant

skill and the subunits beautiful and

then yeah we just go and do our exercise

here.

So let's have a look because we have to

code this now. So what is the

mathematics? How can we materialize

this? So we have an offline the manifold

construction here. Our skill repo is

formally structured here as a

multi-level bipartite graph. The graph

is here simply of some elements. So

let's have a look. The first one is here

the skill communities. No the highle

execution the invariant groupings. Then

with s we represent the skill nodes

themselves. Those are the executable

macros. If you want you represent here

the subunit modes the localized pro

procedural instruction. Then of course

we have to have our edges in a graphner.

Those are the edges mapping the

microscopic skills to the microscopic

subunits. Very important. And then

finally we do have to have a

deterministic mapping of the skills to

the parent community.

So with this graph structure we already

can start. And now as I told you we have

a dual signal retrieval a bottom up and

a top down.

So given now we have a task query system

calculates an effective Hamiltonian for

the skill selection using now and you

guess what a superp position of course

what else of our top down the macro and

the bottom up the micro signals.

Now for the bottom up signal here

project relevance here from the subunit

space back to the skill space. This is a

simple projection that you are familiar

with and if you want to know sigma is

here our embedded similarity and 1

divided by deu is here kind of a

dampening factor. Why? Think of it. It

is something like an inverse frequency

penalty ensuring that the highly

generated hub subunits no like this

standard when you have import OS lines

no that you don't have this as a

dominant element here since this is

shared by many skills. So you do not

arbitrarily inflate here the energy core

of a specific skills. This is it. So the

final selection energy is given here in

this formula. And here we have of course

our topdown community masking now. And

if a skill does not belong to the higher

scoring bulk cluster, it receives here a

severe structural penalty. So this is a

very simple idea. You can go you can

make it much more sharper, much more

complex. But if you want to go and start

simple, beautiful. Here we have it

explained top down retrieval and the

bottom up retrieval. And now we can

build our graph with the subunits that

are not in the selected skills at all.

But the system decided, hey, this is

absolutely fascinating. And I show you

the LLM models in a second.

But then, as I told you at the

beginning, we need more than the

classical rack. It's not enough just to

bring everything back into the prompt.

No, we have to have a context

compilation. If we talk about operators,

executable operators. So let's do this

if you want. This is the core

algorithmic novelty of this beautiful

paper. So K will be the top selected

skills. Suppose an unselected skill

contains however an incredible useful

subunit U. And now the compiler if you

want rescues. Now here our subunit U and

computes a deterministic local building

affinity to graft it onto the most

compatible selector skill SAR. So you

see we go here with a binding affinity

that you know maybe from from techn from

biotechnology

and of course you might say yeah that's

great the idea of course but if I have

no mathematic if I have no mathematical

expression formulas I cannot code it. So

what is the mathematics behind it? This

is a screenshot here explains everything

beautifully. This is how you attach

subunits to skills.

They have here this simple formula for

their idea and this is simply what they

are here optimizing here in this

mathematical representation. Have a look

at it. It is not complex. You have all

the details explained in appendix A2 of

the paper. It's not really the most

important thing. So let's continue.

Yeah, I got a lot of question in my last

video about the computer infrastructure

that you would need. Here I've given you

here what they stated here, what they

work with, a Linux server running

Ubuntu. Yeah. Then we have

56 physical cores, 112 logical threads,

one tip of RAM. They docker and they

have eight Nvidia RTX A5000 GPUs. Great.

So it is not overkill at all. This is

great. But let's have a look at now the

performance. So what is the result here?

And this is now the overall downstream

performance. So we have here our skill

bench and also our agent skill OS. So we

have two benchmark if you want. And

let's see if we compare it here to all

the difference methods that we have.

Skill agent skill OS or vanilla

retrieval or skill router one of the

best up until now. And now you see that

in the very last line here the skill

ray. So this method that we published

that you have had a look here in this

video is of course outperforming here

all the other methodologies.

So this is interesting. We build a skill

graph from all the available skills and

skill MD files. We really check in

detail all dependencies that we have and

we make sure that this is not just some

stuff we put into the prompt and send it

back to the LLM and the LLM simply has

to fail because this is not compatible

and this is not operational.

They worked with two different

combination and I want to show you this

here. They have here a codec with a GBD

5.2 two and a Gemini CRI with a Gemini 3

flash. So neither their flagship models

of 5.5 or 3.1. But you see here in

general the skillway the full version

has here with GPT 29.26

with Gemini 28.85. So I would say okay

it is comparable and then for the

ablation you see here without the bottom

up retrieval without the top down

retrieval and here you have the figures

without the context compilation and you

see now the importance if you would miss

one of the part how it would change here

the performance of the overall system

and we're already at the summary great

so standard AI engineering as we started

this video assumed if you simply feed an

LLM in the correct repos repository. The

LLM has enough reasoning power, enough

intelligence to figure out the

execution. Skillway proved that this is

mathematically naive. The LLM is

essentially just a raw CPU. If you

deliver some uncompiled isolated tools

into its context windows, it just forces

the LLM to do dependency resolution on

the fly, which it will fail at a very

high percentage rate. So the new insight

is retrieval is not enough. The

classical rag is not enough if you go

for operators because now you have to do

execution requires a compilation.

And now and put this here in the

parenthesis. Of course you can argue hey

wait a minute this execution is it

happening not in the harness of our

agent? Is it it is not in the core of

the agent LLM? No I mean we could move

it there but we just found out this

doesn't make sense. So suddenly we have

to have in the harness of an AI agent

compilation execution. So I would say

the intelligence of this AI harness will

increase significantly.

So maybe you place multiple EIS also in

the harness. Then you have the

coordination problem and you know all

this stuff. Anyway, let's stick here to

our topic by explicitly rescuing and

grafting here the boundary conditions.

This means the subunit, the details that

are so important into a logically bound

load token payload. We bypass the LLM

stateless amnesia and give it a fully

resolved blueprint. Isn't this

beautiful? Hope to see you in my next