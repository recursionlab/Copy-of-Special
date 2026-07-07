# Next Stage of AI Scientist: NanoResearch (Skills, Mem, RL)

[![](https://yt3.ggpht.com/EocTonB0FyVFCLmoHoSBsCBtS4LutlIUQC7FdjY6e5Rfm5vQGEBgLIWGj9WkD73qxA1UZeO577Q=s48-c-k-c0x00ffffff-no-rj)](https://www.youtube.com/@code4AI)

[Discover AI](https://www.youtube.com/@code4AI)

88.4K subscribers

Join

Subscribe

108

Share

Ask

Save

Download

2,307 views May 14, 2026 [#scientist](https://www.youtube.com/hashtag/scientist) [#airesearch](https://www.youtube.com/hashtag/airesearch) [#aiscience](https://www.youtube.com/hashtag/aiscience)

This video shifts the perspective from Research Automation to Collaborative Agent-Human Co-evolution. An AI scientist shouldn't be a generic paper-generating factory; it must be a dynamic system whose parameter space continuously warps to internalize the unique research procedures or workflows and resource constraints of the specific lab it is deployed in. All rights with authors: NanoResearch: Co-Evolving Skills, Memory, and Policy for Personalized Research Automation Jinhang Xu†1, Qiyuan Zhu†1,2, Yujun Wu†1,3, Zirui Wang†1,4, Dongxu Zhang†1,5, Jianxin Tang, Marcia Tian6, Yiling Duan1, Siyuan Li4, Jingxuan Wei1, Sirui Han∗2, Yike Guo∗2, Odin Zhang∗7, Conghui He∗1, Cheng Tan∗1 from 1 Shanghai Artificial Intelligence Laboratory, 2 The Hong Kong University of Science and Technology, 3 Peking University, 4 Zhejiang University, 5 Xi’an Jiaotong University, 6 East China University of Science and Technology, 7 The Chinese University of Hong Kong arXiv:2605.10813



## Transcript

Hello community. So great that you're

back. Yes, today we talk about AI

scientists and we go absolutely crazy

today. So it is about AI and autonomous

scientific discovery. AI it will

discover new things. No. So what we call

also as an AI scientist but you know

that the existing AI scientists are

trapped in a makovia and one sizefits

all paradigm. They treat every new

research project as an isolated starting

a t equals z event and produce some

uniformly some generic paper. But we're

going to change this today because today

we going to say wait a minute in the

last minute we talked about proactive AI

by Google and today today we're going to

have a look how we can implement this

how we can make this an individual human

researcher AI companion that really

understands here a highly specific

methodological constraint that you as a

researcher want. Maybe you prefer some

mathematical formalism. Maybe you prefer

some way of of doing your experiments.

So today we go a step further and we

built here a individual human EI

scientist that works closely with the

researcher. And this is it. Nano

research go evolving. And now hold on to

your socks skills memory and the policy

for personalized research automation.

And this is here by my goodness.

Shanghai artificial intelligence

laboratory, Hong Kong University of

Science and Technology, Piking

University, Jay Young University, Jaong

University, East China University of

Science and Technology, and the Chinese

University of Hong Kong. Beautiful. May

11. So they do finally hear the triple.

Now we go for the skill MD file or for

the complete memory update. And we do

not stop there. We don't stop here in

here, the hardness of the eye. We go

really down to the LLM and we optimize

here the policy how the LLM is learning.

We do have some reinforcement learning

now of the LLM itself. So all the

elements we know are now modified. A lot

of questions all about hey where is the

code? Well yes of course here is the

code enjoy it MIT license. Now you know

current automated researcher like

scientist version two or whatever you

like behave like an agotic system with a

high temperature. So every time you give

it a prompt, they explore the entire

vast face space of possible

methodologies ultimately producing here

in general an average microscopic output

that looks exactly the same for

everyone. No, there is no

individualization.

The eye is looking for one generic

solution, but it is ignoring if you are

researcher that likes to experiment. If

you are researcher that is really going

just for the theoretical proof, or maybe

you're a researcher that says, "Hey, I

want to do all ablation studies. is I

want to play around. I want to have here

trigger that activates some components

and deactivate some others. No. So

current if you want AI researchers here

are memoryless makovia.

Let's change this.

Nano research now introduces a path

dependency. It learns what the LLM has

already learned. What is already here

either a positive or a negative

experience here as an AI scientist. And

there was some symmetry breaking. Yes,

of course. The moment we have an

autonomous learning, a self-arning LLM,

we will go and we will break the

symmetry. So if you are an experimental

physicist who demands some rigorous

ablation or if you are a theorist who

prefer a wild mathematical architecture,

now it will stop producing your average

paper and it will really adapt to your

personal style. So this means we couple

here our multi- aent system plus

harnesses plus everything to the human

style to the to the specific human users

like a localized heat buff if you

physics. So you know now the companies

want to sell us here individualized LLM.

They want to sell us here their

particular memory their particular

skills and of course we should save

everything in the cloud platform. So

therefore I will try to do everything on

my local machine. Is this possible? Now

the beauty here is we have a threelevel

co-evolution here in this AI scientist.

For my knowledge, the first one that

they tried it accumulates here the hard

constraint into the skill bank and into

the memory modules plural and crucially

uses here your natural language

feedback. So this is really your

individual machine now to physically

alter here the own parameter the LLM

tensor weights here via reinforcement

learning. So we do have now the human in

the loop and this is you and the machine

will learn on your feedback. So I think

I work daily with those machines. So if

I use it now for I don't know some

months, three, four, five months, maybe

a year, the machine should really know

exactly how I like jobs to be done and

how I prefer to think. So let's do the

learning. Skill bank is easy. Now we

have a skill MD file. Memory can be easy

too. But how the hell if you have no in

ICL no in context learning if you really

go here for a reinforcement learn tensor

weight learning methodology now it gets

interesting.

So here we have a screenshot here from

the original study. Here on the first

line you see everything is the same and

I say and now comes our another research

now and now we have here the skill and

the policy and the memory that are now

optimized if you are rigorous

experimentter exploratory researcher or

a pragmatic submitter. You can now have

your personal style and this AI system

will learn with you. And you might say

how is this possible? What is the

mathematics? How is the optimization

engine? How can we code this? No at

first mathematics and we see the

mathematics then we know how to code and

what to code. So let's start. So the

first is easy to skill on the memory

distillation you see distillation. So

yeah we do have here an evolution. We do

have here if you want here a teacher

student learning happening. Yeah,

because at the end of each single

research trajectory, let's call it TOAO,

which will include all the action that

the AI scientist performed the critique,

the self critique of the system and some

the outcome that was then given here the

feedback but the human operator. We have

here an agent, our orchestrator, no, the

EI boss who does not just wipe now the

context window clean, but now we say,

hey, this was important information here

that happened here in this learning

cycle. So this orchestrator agent will

now distill the macroscopic invariant

rules let's call it the skills and

project specific facts into the

permanent storage into our memory.

So you see it's simple now we have an

update mechanism for the skills as you

see here and for the memory given your

complexity your domain knowledge it will

build on your preferences

now before each task. Now if we go here

in the next round and this is an

iterative iterative AI scientist you

have now orchestrator. It retrieves now

the top case skills and the top memories

that are re relevant now to the next

current context via a uristic scoring

function. This is a very simple

function. And now we combine the keyword

matching the tag alignment the recency

maybe even and the weights adapted here

to the target.

So we have now the next step not the

same knowledge basic knowledge or only

the parametric knowledge of the LLM but

now we'll go with skill retrieval and

memory retrieval and if you have seen my

last video you know exactly what I mean

with skill retrieval we talked in detail

about it yeah and then we have the

adaptive planning phase

this is not interesting while here as

our skills and our memory capture broad

procedural knowledge project facts we

further internalize here a fine grain

user specific preferences here and at

the end of each stage and I'm going to

show you the stages in a moment the user

provides now immediate natural language

feedback so I just go I type here just

my comment or speak here to the in my

natural language which we encode then

directly into the orchestrator planner

model pyata so this is here the

classical policy the orchestrator is now

simple our ll LM that we used here to

fine-tune to train now on this comment.

So where the risk being compressed or

retrieved this was the old case when we

just looked at an update or you had a

concatenation to your skill MD files or

to your memory MD file. No, now we bring

it so that it is not happening into the

LLM itself. And here the boss if you

want AI system here of our multi- aent

system the orchestrator agent and he now

learns exactly the mistakes the positive

steps the negative steps how we prefer

science or whatever job you want to have

to be learned at

so free form language feedback this is

my human user feedback rather than any

scalar rewards or some preference pairs.

So how do you do this now? And they

adopt now the self distillation policy

optimization.

This is the first time I've seen this in

this massive way. So an SDPO which

convert your single feedback instance

into a dense token level learning signal

without any reward. Well, we might say,

"Yippee, yeah, finally." No, we just can

go straight forward here to the

learning. And you might say, "Oh, wow.

Straightforward is interesting." But

don't you worry. Yes, of course, they

give you the SDPO gradient here, your

Naba data for an SDPO allergic level

policy gradient, and you say, "What the

hell is this?" So either you have a look

at my video where I explain you AI

mathematic or you just go here and this

is from February 2026

to this particular paper here from it

MIT University of Turk Switzerland

aligning the language model from user

interaction and here exactly they show

us your new method for learning directly

from the user interaction through a self

distillation and in this paper they go

step by step and they explain exactly

how they do it. How to build a

methodology?

Well, what is possible via a self

distillation? Think about this. A self

distillation is is such a genius idea.

No,

they go here with the classical formula

and they show you here our knobler then.

Exactly. And you say ah now I understand

how this happened. You have here that we

have the hindsight policy. PI data acts

as a teacher and is treated here as a

fixed target during each update for

which we define a detached hindsight

model. Pi data bar this is here defined

in a particular way. You have an annex

in this paper that goes into the

mathematical proof of this formula. So

if you want to learn more about this,

this is the paper I would recommend to

you. But let's come back to our topic

here in this video. So there as you see

following six. So they just use here

this um formula from the other

observation and they use it now here

simply for the self distillation and

here of course for the advantage

function. This is our advantage function

and here we have our feedback function f

of course. So you see we just stand on

the shoulders of giants and we continue

to build on the knowledge here of the

geniuses before us.

The beauty again no reward model the

users provide here natural language

feedback you tell the machine hey I

don't think this is the way to go I

would prefer another mathematical method

I would prefer you go here you compare

these two methods or I prefer you would

to switch completely something else you

just give it a feedback f at the end of

each stage which then the agent here our

observer agent our boss agent

internalizes it into its planner policy

thereby with this formula We know how to

code this formula turning the explicit

feedback into persistent preferences. So

we really let the LLM learn this not in

context learning not write it into a

skillmd file not do it like a memory

somewhere and save it in the in the

hornness of the LLM. No really change

the tensor weights finally of your

transformer layers. Beautiful.

So again let's take a step back and

let's have a look at this beautiful u

screenshot here from the oris. So we

have a user

and this uh girl is now programming here

an AI scientist. She has certain

preferences. She has a certain budget

here budget. She has a target venue

style. She has certain topics that she

would like to address here in this

scientific endeavor. And the idea is

simple. Yeah. At first we retrieve all

the AI it retrieves you all the skills

and memory maybe needed for this

particular job. So if you have seen my

last video rack for skills retrieval

augmented execution of mathematical

operator that are now the skill

operators here and this is called skill

array for retrieval augmented execution.

This is exactly what you could

substitute year step one for. The eye

finds via rack the best skills available

let's say on the internet on a skill

database whatever you have then we have

the strategic element the EI now starts

to come up with a plan ideation

experiment writing review beautiful

then we have the coordinate stage so you

dispatch here the stage agents whatever

is now decided to do in the orchestrator

is here if you want the mastermind point

and after this happen you see you come

back and you have here again the skills

here maybe there are some new

methodology you found here you could

have here a code verification so you

have now a new skill so you distill now

this new skill into your system and you

add a new skill here to the skill

database that you have or the extraction

here of the memory show a new path

forward show a new complexity a new

solution, then write it down into the

memory and you have a new memory MD file

or whatever you prefer. But now you see

what we have. We have constantly here an

update and a retrieve from our three

elements that learn continuously the

memory with the past hypothesis. Notice

the failure look at the results lock

down the constraint. Second all the

skill MD files or whatever you have for

literature search for debugging certain

patterns for writing some templates here

they are evaluated compared and the best

one is selected for tool use strategy

APIs whatever you have and then this is

here if you want the real interesting

thing here the update here of the policy

of our core LLM of your orchestrator

agent here's the real intelligence

here's the real learning happening the

planet behavior has an adaptation the

schedule preference has an update and

the user feedback this is this feedback

is now really integrated in the future

behavior of our orchestrator. So these

two

elements here, the beautiful user and

the beautiful orchestrator become now a

beautiful couple that is now working

together here for this EI scientist. And

you can be quite sure as a user that the

orchestrator agent is behaving in a way

you like it that this is what you prefer

to do an individualization.

Congratulation. Oh, wait a minute. Here

we have now the stages. Officially there

are three stages. Never mind. You can

insert some. You can play around with

this. You have normally you you start

with a stage one the ideation. Then you

do the coding, the verification, the

real world experiments. Then you have

the writing, the summarization, the

understanding, the whatever you want now

to publish and then you have maybe a

paper. But let's have a closer look.

So the stage one is simple. Now idea

generation and planning. This is what we

know. There's nothing specific except no

system now queries academic databases.

Here it uses quantitative evidence

extraction, beautiful existing papers to

prevent LM from hallucinating some other

baselines. And now it starts to generate

a pool of hypothesis based on existing

papers. It goes the next step. No. And

it uses an automated normality novelty

verifier to filter out ideas that

already exist that have already been

published. And after we have a pool of

hypothesis how to proceed we have a

planning phase. So the surviving

hypothesis is translated now into strict

JSON formatted experience blueprint how

to use the data set what architectures

we should build ablation studies to

verify how to code this how to whatever

second validation optimization. Now we

are in the lab if you want you have the

coding phase guided by the blueprint.

The system clones now the repos. stages

here. The data set generates a

self-contained code base, all the mouse,

all the training loops, all the

evaluation matrix. You as a human have

already given here feedback that you

like metric one, you do not like metric

three and adhere strictly here to the

user's preferred coding style. Or if you

already have here like say in cloud code

and interaction here with 1 2 3 months,

I think cloud code has exactly

understood how you like to have your

coding style implemented. And then you

have the execution at the debugging

phase. You have an autonomous debugger,

another LLM that looks now here at the

created

code and either yeah debugs it, verifies

it, extends it, whatever until you can

successfully execute this. And stage

three is simply now it writes it down,

it summarizes here, drafts here. If you

want a manuscript deliberately an

architectural choice to prevent here

catastrophic forgetting if you go here

with or you do not want a context window

overflow you want to ensure that the

introduction aligns perfectly with the

conclusion. So we have now a section by

section writing phase here by and then

of course we have another standalone

that acts now as an external review and

we have the review phase and you got it.

The interesting thing is you have user

profiles now. So you have the same study

here whatever it is never mind you see I

hard and then you decide a user profile

who is doing now who is now this EI

researcher and maybe here the main

characteristic of the first researcher

is evidence first of the second

researcher is maybe ablation focused for

practical methods for clean ablation for

directly implementation reviewer

friendly or maybe you say hey I want my

eye researcher purely data set driven so

You can steer this. You can define your

own par your own preferences or I would

like to try this out. Go exactly with

the complement of my behavior. No,

because I know how I do things. But I

like a compliment of mine who does

exactly the thing opposite. Experiment

much much aggressively. Try some crazy

ideas

and do not stay here with the

confinement here of classical scientific

behavior. No. So you see the blueprint

then is really different. The AI

scientist really comes up with different

solution for evidence first. For

example, we have a fixed multiscale CNN

convolutional neural network or for the

second one a temporal feature gating or

a temporal routing. So you see it really

depends what you how you define the AI

researcher the preference

profile here themsel. Then the code yeah

either they go with a fixed encoder or

you go with a pluggable gate structure

or you go with some adaptive routing

whatever methodology the will now

implement here in this scientific

experiment really depend here on the

user profile no and of course it will be

written the paper will also reflect your

particular profile okay let's have a

look at the results how good is it let's

compare it here so here we go if we have

here the ablation results

What is the most important? You see the

nano research in the full implementation

here for the alignment phase or for

novelty or whatever profile whatever

parameter you choose. Okay, it is let's

go with alignment. Yeah, 8.1.

So without the skill bank you would only

reach 7.9. Without memory you would

almost reach 8.07.

without the plan 78 and without the

preference alignment eight.

I mean yeah this is and you really

cannot leave this out now no can choose

what to take because the beauty is

really here the interaction above all

but of course what we interested in if

we compare to two other AI scientist and

here you have in this line the AI

scientist version two or the EVO

scientist and here you have all the

performance parameter and here we go

here with the average API with the token

with the runtime with the GPU hours and

interestingly with the costs and now

they show you here okay if we compare

this now here on a token level on an API

call level of a runtime level the

runtime is shorter GPU hours is almost

half the cost therefore of course is

also massively reduced okay so this is

what they show us here for the quotation

mark performance sheet they go here API

I call token runtime costs here and GPU

hours. No.

Okay.

But I think this is it. No. So let's

reflect about this. So because the agent

is now crystallizing yet a successful

debugging path and procedural codes into

some permanent reusable skills in memory

that this EI scientist now builds up

with the time. Yeah, it spends

drastically fewer search tree iteration

guessing how to compile here the code

base in later rounds. It will reuse here

the skills that it found to be helpful.

It will reuse here the memories that it

found to be helpful in the past. So it

is behaving more or less like a student

researcher that is understanding I build

upon my knowledge. I build upon my

successful puffs and it just goes on

makes sense.

You see also that now this preprint

shifts your respect the perspective of

an AI scientist from a pure research

automoton and a machine that does some

automation to a collaborative agent

human co-evolution and you might say yes

of course it needs now the human because

otherwise the machine would not be able

to selfdevelop itself to self-learn

because we have chosen here exactly for

the reinforcement learning now the self

DPO algorithm. So of course this

really brings us back here to the video

from yesterday. Yesterday I showed you

here skillway. Yeah, skill we address

the immediate the static problem of how

to assemble a perfect executable context

out of a vast internet of tools and it

is a rack compiler.

And this video today I have chosen for a

very particular reason because you can

say that skillway defines here the

spatial solution at a time t equals

zero. So skillway from yesterday I

showed you how to provide the optimal

topological projection to select the

right macros and grafted the right micro

dependencies the subunits of our skills

and now nano research in my

interpretation

defines now the temporal solution over

the time development. So you see

skillway t equals z and for the time

evolution nano research they go

perfectly hand in hand. Read both paper

in parallel if you really want to see it

and take care about this particular fact

and if you say no I see it the other way

please write a comment otherwise

nano researchers addresses here this

evolutionary problem of an AI scientist

now you don't want to start from fresh

every time you start up the machine

again so as the agent writes here

research paper it discovers novel

procedural steps successful debugging

patches it learns new skills by trial

and error. Why not? And then it distills

these into the new discrete MD files

into new skills and the new memory files

to aband then to its permanent skill

banks that it uses here at a later time

step. But the most important fact is now

it also was integrated here via

reinforcement learning into the

parametric knowledge of the LLM itself.

Simple example nano research conduct a

research experiment runs six hours gets

a feedback from the physicist and writes

now as a very specific pietorch training

loop let's say you need this now so

maybe it says okay great this is all I

needed for today so you save this loop

here as a new skill in your private

skill bank and the very next day the

scientist comes back and says okay AI

scientist switch on and it understands

immediately when the agent needs now to

write a new paper or performs a new

research. Now the orchestrator agent

starts again looking around asking for

the best tools that is available in his

environment and now we understand with

this new skill let's say it's a skill

empty file available is now taken care

of now and skill rate takes over passing

here the nano research skill bank into a

multiscale graph see yesterday's video

retrieving that specialized pytor loop

that we built grafting on a specific

specific subunit constraints for the

physics labs GPU cluster and compiling

it perfectly into the agent context

window. You really build upon what you

did last yesterday, the day before

yesterday and so on. So you see this is

here if you want iterative self-arning

process here for a multi- aent system

that is performance here performing here

research task whatever you define is

research here an AI scientist

what I really love is this tree level

evolution

whenever the paper is finished or

whenever the first day is finished no at

the end of any stage and the human has

provided feedback and critique and

whatever Ever the system here really

triggers its evolution in the following

way. If you want to remember one sheet,

this is it. Skills. This AI now

abstracts the coding fixes it invented

in the stage two process into some

reusable skill MD files and saves it in

its skill bank memory. For the memory,

it analyzes what went wrong. It locks

all the failed hypothesis from stage one

into the project history. So it does not

repeat that ends any time again. It

learns from it mistake and policy it

uses now and here we come that the human

interface is so important. The human

feedback is so important here. the

human's free form feedback to

mathematically adjust its neural weight

tensors via SDPO ensure that in the next

paper its innate intuition better

matches here the users scientific taste