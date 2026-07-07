# Phase Transitions in Agent Memory: Recurrent Memory

[![](https://yt3.ggpht.com/EocTonB0FyVFCLmoHoSBsCBtS4LutlIUQC7FdjY6e5Rfm5vQGEBgLIWGj9WkD73qxA1UZeO577Q=s48-c-k-c0x00ffffff-no-rj)](https://www.youtube.com/@code4AI)

[Discover AI](https://www.youtube.com/@code4AI)

88.4K subscribers

Join

Subscribe

78

Share

Ask

Save

Download

1,585 views May 20, 2026 [#aiagents](https://www.youtube.com/hashtag/aiagents) [#aiexplained](https://www.youtube.com/hashtag/aiexplained) [#airesearch](https://www.youtube.com/hashtag/airesearch)

All rights w/ authors: "RecMem: Recurrence-based Memory Consolidation for Efficient and Effective Long-Running LLM Agents" Zijie Dai1 Shiyuan Deng2* Sheng Guan3 Yizhou Tian1 Xin Yao4 Xiao Yan5 James Cheng1 from 1 Department of Computer Science and Engineering, The Chinese University of Hong Kong 3 School of Computer Science, Beijing University of Posts and Telecommunications 2 Huawei Cloud, 4 Huawei Theory Lab, 5 Institute for Math and AI, Wuhan University arXiv:2605.16045 [#airesearch](https://www.youtube.com/hashtag/airesearch) [#aiexplained](https://www.youtube.com/hashtag/aiexplained) [#aimemory](https://www.youtube.com/hashtag/aimemory) [#aiagents](https://www.youtube.com/hashtag/aiagents)

Discover AI explores Recurrent Memory 


## Transcript

Hello community. So great that you are

back. Let's talk again about memory.

Today we talk about a subconscious

memory in our artificial intelligence.

Then we have a face transition threshold

activated by a mathematical trigger and

we will generate something beautiful a

semantic memory and an episodic memory

in a way you have never seen it before.

So we have a brand new study May 15,

2026. This here is department of

computer science and engineering, school

of science, Huawei cloud, Huawei lab,

Institute of Mathematic and EI by the

Wuhan University. But the main part is

here by the Chinese University of Hong

Kong. They talk about recurrence-based

memory, REC memory. And this is here

memory consolidation for an efficient

and effective longunning LLM agents. So

again the same topic LLM agents that

don't go for 2 seconds, 5 seconds. No,

you really work with this AI agent with

these LLMs for hours. You have

conversations multiple hours or you have

tasks that go over days long running LLM

agents and we need memory because last

time here some viewers ask what if I go

without any memory then you start from a

blank sheet then you've lost everything

of your history with your EI system.

Now, now you remember memory systems

often organize the user agent

interaction of your last three weeks

with your AI as a retrieval external

memory that are crucial for longunning

agents by overcoming your delimitated

context windows of an LLM. Let's say you

only have 250k tokens in your context

window or only 1 million token like you

have currently with some Geminina

objects. So, we have to go file-based

memory, external memory. Okay. So

existing memory systems invoke LLMs to

process every incoming interaction for a

memory extraction and such an eager

memory consolidation scheme leads you to

a substantial token consumption

especially if we are limited within our

context windows. Remember we have here

only a limited amount of token for our

prompt structure.

Now what happens? This is our beautiful

LLM and yeah this is here never mind

that we have here a layer specific

memory allocation. This is yeah this

will happen next week on this channel

but just say we have an LLM not a

typical transformer with some layer.

Beautiful. And then we need here some

knowledge that has already been stored.

So we have a huge external memory a vast

knowledge store. And in my last video, I

showed you how we can build it here with

a graph structure, a knowledge graph

structure or a temporal graph. But now,

let's assume we just have files. We have

a file cabinet. Beautiful. And now I

want to continue where I left off three

weeks ago. And I won't have this in the

complexity of all my memory models

because I'm looking here for some

specific causal augmentation traces. I

don't want to go here back to a [snorts]

point I don't know 3 weeks time and I

just uh upload here all the file again.

No, I want to have them in context with

the temporal development. So you

remember whenever you start up your AI

system whenever you connect let's say

it's a Monday morning it goes and it

loads you all the personality that you

defined that you want your FAI system to

behave. You have the classical system

prompt, but you also want to have here

all your interaction history of the last

weeks or maybe of the last three months.

So it loads here some particular memory

that it thinks is essential just for the

startup. So let's say it loads its

quotation mark personality and then I

come and I have a particular task and

this task I'm working now continuously

for more than three months but I want

also all the other insights from the

last three months are integrated now. So

let's say you define a specific query

now operational and the IOS already

encountered something like this let's

say 3 weeks ago and now it loads the

complete skill set and it's job specific

newly designed skills from last time in

this memory fragments that it now

selects and this is now file based

remember this is not tensor weight based

we do not have supervised finetuning or

reinforcement learning we are operating

here on a file-based system we just go

with in context learning for our context

window for our prompt to the LLM.

Beautiful. So you see you load memory

you load memory for a particular task

and you don't want to start on a blank

canvas a blank sheet of paper again when

you say okay now we continue and you

don't want just to load up some points

from 3 weeks ago because then you would

miss here all the interconnect of the

memory all the inside if you work in

science what happened in the last 3

weeks you want to have this interwoven

with where you left off 3 weeks ago

In my last video and we had a look at

this at temporal complexity for multihop

and multi-temporal structures here.

Beautiful. But today we have a look at

something brand new. So this is now and

now the question is with this paper here

we have now a new solution. So let's

look at this. They talk about memory

consolidation and it is not like in my

last video with a temporal tree

structure that we integrate here to

temporal flow of the memory buildup but

they go with a classical memory

consolidation done by an LLM. So we will

lose a little bit of the temporal

density and the temporal linearity. But

let's have a look what the authors show

us. They say hey we have a new solution.

Great. mid of May 2026 wreck recurrent

memory stores the incoming interaction

you know the human EI let's say it's a

conversation in a this is now a

subconscious memory layer what they call

it I don't like the term subconscious

this is a human term has no subconscious

layers we code the layers and the layers

are there but okay so in subconscious

memory layers and encode them using some

lightweight embedding models for the

retrieval

And I smiled and said, "Hey, that's

great. We know everything about

embedding models." No,

just think about it in the good old

times. So remember 5 years ago, 7 years

ago, token or word embeddings. No, we

had a vector space XY Z or maybe we had

a 1,00 dimensional space and the

embedding space the semantic similar

items are close together like here cat,

dog, wolf, tiger or here apple, banana,

orange, mango. This was the reason why

we've chosen token embeddings, word

embeddings or whatever to have a

semantic meaning and those uh objects

that have a close semantic meaning or

position in this mathematical vector

space close to each other. Whatever

close means.

So what we do now is simple. Now we

encode memory elements or memory

fragments to be more specific. This

means higher complexity elements now in

a mathematical vector space. Great. We

know how to do this. This is I have 50

videos on sentence transformer on expert

optimization and coding and PyTorch

whatever. So we know this.

And now LLMs are only invoked to extract

the episodic and the semantic memory and

I will show you this in a moment at a

very particular time when and they call

it a sustained recurrence are observed

for a semantically similar interaction.

So this is not that it's breaking with

the history of what you have now. You

have a human AI conversation and then

this is here concatenated to your memory

markdown file. This is just added. No, a

linear addit. Linear added, linear

addit. And they say no, we wait here for

a certain threshold to happen. Linear

recurrences, you know, recurrence of the

fibu, not G numbers would be just an

example. Yeah.

So semantically similar, you know

immediately if you're a subscriber of my

channel. Hey, this means in a

mathematical vector space, for example,

in the co in the simplest place, here

cosine similarity. Of course it depends

on the metric of the space and whatever

it is but you know similar this is a

formula we know

episodic and semantic memory such

recurrent space consolidation works

because these interaction correspond to

a semantic cluster with a rich

information. So okay we have to have a

critical density and thus a worth as the

order tell us the extraction and then

the summarization.

So we have to have a critical density in

our semantic and episodic memory

structures before we start here a

sustain based on a sustained recurrence

here do those extraction and

summarization

but how do you do this exactly in detail

we want to code this no so the authors

tell us here we propose a

recurrencebased consolidation a memory

consolidation a compactification

to save token costs by conducting

the memory consolidation only when and

this is the important fact it does not

just concatenate to the memory markdown

file every time something happens a

conversation happens no continuous

linearly it says no I don't want to

waste these tokens because those tokens

I need in my context window for the

conversation so memory consolidation

only when an incoming interaction can

find a sufficient number of semantically

similar or related interaction

So we do have a critical density here.

Okay, let's go with this. And I know

some of you ask me because you sent me

this, hey, how does any machine know

when or what is semantically similar now

in a higher complexity field? Well,

simply it learned it from its

pre-training data set. Machines don't

know anything just by chance or come up

with a solution. There's an massive

pre-training exercise and then you have

postraining. So this has to be trained

thousand million trillions of examples.

A machine doesn't know anything here

just by itself. It's massive trailing.

Or if you want to see this in my words I

would say hey what goes together with

what other sematic elements in a given

domain specific linguistic complexity.

This is how we know it. Great.

So this means if we summarize this now

here since we are here at my words I say

this recurrence memory introduces here

recurrence based phase transition if you

think about physics no at ideal gas for

example only spanning the compute on

particular states of the system that

demonstrate a sustained topological

density a critical density over time. So

we do have a little bit here of a

temporal development in this but we just

go for the critical t density.

Now how to do this? They decided to go

here for three distinct manifolds.

Now manifolds is something that lives in

mathematic and maybe a computer

scientist would say hey I built a data

store. So they built the orus built

three stores a subconscious store an

episodic store and a semantic store. I

know because we have the code for this.

Great. So subconscious is more or less

in physics a heat buff here. Then

episodic store is the micro state the

narrative that is going to build up

here. But we have a backup a backup for

a very particular case and this will be

the fine grained semantic store. Now

let's have a look at this. The

subconscious store I don't like the word

subconscious but let me go with the

orus. All incoming interaction are

simply protected here into a cheap

latent embedding space out of vector

space and left in the buffer. No heavy

LLM computation occurs here. We just put

in vectors. This is it.

Then we have now the interesting

episodic store. If and only if the local

density of some virtual particles

vectors of course in the subconscious

buff here in our vector store exhibits

some constructive interference

meaning the user repeatedly brings up

the exact same topic over time then a

phase transition is triggered. So this

means the LLM is now invoked to coar

grain this reoccurrent micro state into

a persistent microcoscopic event

narrative. So this is where the

compification, the summarization and all

the beauty happen over the LLM and

hopefully the LLM has been a domain

specific knowledge on this and knows

exactly how to summarize this and how to

compactify your memory here in a way

that you have a maximum information gain

in your limited token number here of

your AI prompt structure. Great. But I

told you, hey, there's something else.

No, there's kind of a backup solution.

So what is number three? Number three is

the semantic store because the episodic

summarization destroys of course a lot

of microscopic information some precise

details like a specific date or a

specific name that is not reoccurren the

semantic store now acts here as a parity

preserving layer as physics would say or

simply hey I don't want to lose any

information so it extract now the exact

isolated atomic factor little little

details from the collapse episode. So

they are not lost to entropy.

So if we have here 10,000 books now in

this semantic store, this is going to be

huge because over there you have all

isolated atomic facts as single vector

in a vector representation

that are currently excluded from the

compactification and the summarization

that is happening in number two the

episodic store. Now let's see why. Now

let's say in a simple example you know I

tell my machine it's not true but away

the human user is allergic to peanuts.

Now this is an information that is not

recurrent. This is just a single

information point in time. Full stop.

But this is essential because the should

exactly know if it's your AI companion

what are your strengths your weaknesses

what are you allergic to for a medical

record for example. Yeah. So this means

these atomic facts are saved in the

semantic store here as isolated vectors

for precise highfidelity future

retrieval. But at the end of this video

I will come back to the limitation that

this will impose on the complete system.

So again in my simple words I'm a simple

person. We only apply the expensive

integration operation. This means the

LLM itself for the memory

compactification when the localized

semantic density in a particular

mathematical space crosses a predefined

critical threshold

and in this particular case the authors

call this a data count. So this is our

threshold number say okay makes sense

now great so now we have prepared

everything and now it's time to start it

up and now we have query time. So let's

have a look

at query time. The system simply applies

here the dense retrieval budgets for our

three stores

subconscious episodic and semantic store

creating here a highly dimensional

context window for the generative pass.

So whatever you decide on your

particular budget what is your computer

infrastructure this is it. So now

suddenly we have three data stores that

are now if you want queried and

integrated and updated and compactified

here and summarized here and compressed

and this is it.

Okay, interesting.

Let's look at the result. Is it working?

I mean this is the only thing that's

really important. What is it? The real

world result.

So here we go. Very simple. I just give

you really the the end result for the

task accuracy.

You see here our rack memory here. If we

go for the overall task accuracy with an

LLM as a judge, yes, it outperforms

other old classical memory systems. What

a surprise. But interesting is the

memory construction cost. No. to the

consolidation tokens in thousands here

and here you see compared with the other

old memory methodologies here our

recurrent memory is simply outperforming

here hardly using just 200,000 tokens

here for all those operation for a

particular benchmark I'm going to show

you in a second so the authors argue now

that this adds now to their hypothesis

treating memory as a densitydriven phase

transition in physics

is so much more insightful and gives you

better coding insight rather than you

would just have a continuous linear

integration of your memory MD files

where you just concatenate new

information and they give you here four

three particular benchmark I'm going to

show you here an 87% reduction in the

mathematical operation now this is huge

this is really huge 87% reduction here

in the operation you have to perform

here on system, but remember you have to

build the stores. No. So, yeah. Okay.

So, you might consider this for your

total cost of the system.

In my last video, hopefully this is

yesterday for you. The new topological

whack for the temporal AI memory. We

evaluated HMA'M. What a coincidence that

we're talking about memory all the time

on three public long-term agent memory

benchmarks. And here in this video

today, it is exactly the same. We have

the locomo. We have those benchmarks

here. So you have the benchmark data for

the methodology yesterday here in this

video and today. Yeah, it is guess what?

The same benchmark data. So let's have a

closer look because we have multiple

parameters. No. So I want to show you

two of them. So we have here the overall

score versus here our data similarity

and the overall score versus your data

count. And you might say what is this?

This is simple. We have an overall

question and answer performance score

here on the y-axis

against two phase transition parameter

of recurrent memory. At first here in

yellow we have the geometric similarity

threshold data sim for similarity and in

orange we have the recurrent threshold

data count that I already introduced to

you. Now let's have a look at this. We

have a clear sensitivity of this system

for let's say data sim defines the

geometric clustering radius here for

data sim. You see if the we have here a

beautiful peak here in the overall score

here of data sim being seven for this

particular system of course only but you

see if the geometric radius is too wide

so let's say our data sim is six here

unrelated state pollute now the

consolidation of the memory this means

our overall score diminishes no because

if you have unrelated state it just

pollute here your result. You don't want

this. On the other side here, if it is

too tight, let's say data is 85, the

system suffers from sparse fragmented

matrices that never trigger now the

reoccurrence. They never made it here

into the higher compactification

manifold and therefore are neglected. So

your overall score goes down again. So

they found here for particular task

there's a sweet spot. So you have to

find a sweet spot for your particular

domain knowledge for your comp for your

specific uh complexity for your manifold

coration and all this stuff. Great.

Second

the data count the critical mass that is

optimal here for data count you see it

is about five.

So this means the consolidation only

fires if the size of the local cluster

reaches here a critical mass and this is

our data count. So this gives us here

information about here if you want here

the critical mass or the critical

density of the objects we're talking

about. You see beyond five we have the

model becomes too conservative resulting

in a steep drop in accuracy as

legimotive recurring patterns are

trapped here in the subconscious door

and not make it here into our recurrence

count. Yeah, they are not clustered

together and therefore we suffer here in

the performance of the overall score.

Okay, great. But what are now the

insights? What have we learned? And

let's formulate it just for fun in a

scientific framing. I think the first

point I find it interesting that this

recurrent memory methodology proves here

a profound architectural point about

intelligent agents. the immediate memory

integration that we have currently with

all the systems you work now where you

just have a concatonation to your memory

MD file or maybe NEI is already

optimizing your compification to the

concatenation itself. This immediate

memory integration is mathematically

flawed for careful long horizon

stability.

Whenever you work long time, days,

hours, months, then you will get a

problem because

true intelligence, yeah, I'm not sure

that this is true intelligence, but

okay, I go with the definition, requires

here a low energy latent reservoir. And

this is nothing else than our

subconscious memory store that the

authors introduce. So it is not okay

just to add add whatever it happens for

your job specific complexity.

But you have to wait. You have to wait

till this fills up and then you see some

patterns emerging. If you don't wait

here that you get a statistical relevant

data set here in your particular on your

particular manifold and then you can do

here the compactification or you know

the clustering

you need a certain minimum amount of

data and low energy latent reservoir. So

this means I think we must allow inputs

to remain uncorrelated

and superimposed until the statistical

recurrence forces your wave function

collapse. Here I would say as a

theoretical physicist but as a data

scientist or AI you would say a

consolidation happens on memory

complexity into a structured reality

mapping here into the episodic store or

the semantic store. And I think this

prefer this aligns here perfectly with

the physical reality. Now persistent

macro structure that we see in physics

only crystallize from states that

resonate over time.

What are the limitation and just be

clear there are limitation and this is

not to make this method in any way bad

or no it's just it has limits and we

learn from these limits and if we can

eliminate those uh limitations then we

can make the model even better. So just

think about it. The entire recurrence

memory architecture is predicated on a

single cognitive assumption that

information worthy of long-term

abstraction compactification

summarization

is only when it tends to recur.

So this means if I only mention it once

in a conversation with Maya, it will not

be compactified.

And you say, "Yeah, great. But we have

here no exactly therefore the

subconscious memory store that relies on

pure dense vector retrieval. No. Now you

know that the vector embeddings

notoriously struggle with hard negations

or some precise constraint. Now we are

still here working in a statistical

model. And if you only have one isolated

lonely traveling data point in your

vector space, you cannot really rely

100% on the correctness of this

representation. Or if the LLM hasn't

structurally consolidated the rule into

the semantic memory, the agent simply

might hallucinate or violate the

constraint during any later task.

And again the authors claim that this

subconscious store acts as their safety

net. And I understand it and I like the

idea. But I think this methodology that

they choose here as a simple old old

class fashion vector store is not

powerful enough. No relying on a raw

vector search for isolated high-stake

facts defeats you the purpose of an

intelligent memory architecture.

And of course, if you want to have a

little bit of nitty-gritty, yeah, there

are the problems. No, because the rack

mam state transitions are governed here

by brittle static thresholds rather than

the parametric learning. But of course,

yeah, this would be too expensive here

in the learning process itself and its

retrieval mechanism fragments the

context in the v orbiter uristic

budgeting that as I showed you here. You

see there are so many option and axis

where we can further optimize this thing

but I wanted to show you this paper

because I think there's some brilliant

ideas not that you have to build three

additional stores for just your memory

compactification

but you see how we are fighting in AI

research to come up with better

solutions for the memory integration

into the context window this is limited

so I hope you had a little bit of fun I

hope there was some new information.

Would be great to see you in my next

video.


