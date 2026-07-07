# NEW: From AI Skills to "Skill Programs"

[![](https://yt3.ggpht.com/EocTonB0FyVFCLmoHoSBsCBtS4LutlIUQC7FdjY6e5Rfm5vQGEBgLIWGj9WkD73qxA1UZeO577Q=s48-c-k-c0x00ffffff-no-rj)](https://www.youtube.com/@code4AI)

[Discover AI](https://www.youtube.com/@code4AI)

88.4K subscribers

Join

Subscribe

128

Share

Ask

Save

Download

3,022 views May 21, 2026 [#aiskills](https://www.youtube.com/hashtag/aiskills) [#artificialintelligence](https://www.youtube.com/hashtag/artificialintelligence) [#skilldevelopment](https://www.youtube.com/hashtag/skilldevelopment)

HASP, a framework that represents classical AI skills now (next evolution) as reusable state-action intervention functions. Instantiated as Program Functions (PFs), skills become executable modules that can directly intervene on the agent’s next decision, provide structured signals for post-training, and grow as validated external AI MEMORY. All rights w/ authors: Harnessing LLM Agents with Skill Programs Hongjun Liu1, Yifei Ming2, Shafiq Joty2, Chen Zhao1 from 1 New York University, 2 Salesforce AI Research


## Transcript

Hello community. Hey, I have good news for you today. No mathematics at all.

Just pure physics. So let's have a look. Skills. You know them. Now we do

something with skills. We make skills programmable in a way you cannot imagine. So let's start. Here we have

our standard prompting. Now this is what you know prompt optimization context on

whatever. And the idea is simple. Now we have here the failure manifolds. Nowhere

deep down there in the red. You do not want to go there. The hallucination. So if you have a little particle here in an

energy field coming here along beautiful and you have some instruction and the

instruction here the little mountains here protecting here that the particle would fall into the failure manifold.

But unfortunately here the instruction falling of your particular LLM is not really high. So as you see here in the

energy landscape these mountains are not high enough. So the particle if you want has a quantum tunneling effect. It just

goes through it ignores your instructions because there are so many other instruction. You have instruction

from the skills from the system prompt general hundreds of instruction and your particular instruction do not do this

and go down this failure manifold is ignored. So what is the solution? The solution is

on the other side. We go and we activate again Maxwell's demon from 1867.

Yes, we go back in time 150 years and we will use something physics to find a

solution so that the particle travels on and finds you the optimal solution or it

comes closer to the global attractor of the system manifolds. Isn't this beautiful? So let's have a look. If you

are a little bit confused, well, what we do currently is a standard prompt engineering. No, you give an

instruction. You say remember to verify your answer before finalizing and you hope that the LLM will follow your

instruction. Guess what? It doesn't because there are so many other instructions. So this means we can

imagine this prompt engineering here as a kind of a weak diffused potential field here to the energy landscape in

general. So when a particle let's say it's traveling along this energy landscape and it sees now a diffused

potential field says hey do not go in here follow my instruction it just

tunnels through because the system's temperature is non zero and the latent momentum here of our particle let's say

the particle is of course our bad reasoning trace of an LLM can be high the agent easily tunnels right through

this gentle potential barrier committing here to a hallucinator state or just

terminating prematurely. So we have something that we do not want here. We

have here our failure manifolds. You see we're working here with within deep some

physical interpretation landscapes here and field operator and whatsoever. Now what is the solution? It is called here

the has framework here and the idea is simple in physics. You know 1867 Maxwell

Damon was already helpful for us in temper dynamics. So we use now the same idea to come up with a brand new

solution in AI. Yes, we are about 150 years behind but never mind. So the authors introduce a set of program

functions the PFS that monitor the agent exact phase space micro state [snorts]

and when the agent now proposes an action in its sequence you know that approaches now a known failure manifold

in our mathematical space. Now our program function, our PFS explicitly

kick into place. They explicitly intercept now the particle. They say here a force field. Hey, wait a minute.

This is the wrong way. So we will accelerate you. We will provide you with a momentum that you just cross over this

failure manifold and we send you on the way to the optimal solution.

So this program function this PF holds the stoastic generation of the LLM and

rewrites if you want the coordinate trajectory of our particle. Isn't this

fascinating and who decides to do what again? Maxwell demon and you say wait a

minute so the brilliant idea is what we take now here a temporary solution and

this solution is just a gdunkan experiment. This does not exist at all. But it is helpful to come up with a new

solution. So we take here our 150y old Maxwell demon to force here the particle

back on the correct track. And this is locked now as a multi-dimensional energy gradient for the optimization of our AI

system. Isn't this a brilliant idea? So here you have him Maxwell here from

Wikipedia. Thank you Wikipedia. a sort of experiment introduced by the physics James Clark Maxwell 1867 and yes of

course it's the second law of thermodynamics that he wanted to show you with the entropy great if you're not

familiar with this it the idea is so simple imagine a container divided into two chambers filled with a ideal gas no

at 1867 at the same temperature and now we have a little demon sitting exactly

between here those those two uh chambers here and this controls

in theory a small door between the chambers. No. And the function is simple. The dimmer now analyzes the

system and allows the fast moving this mean the hot molecules to pass from one chamber to the other chamber

while blocking the slow moving the cold molecules on the other side. So what we end up with theoretically in 1867 the

idea was so on the one side we have the hot molecules because we separated them actively and on the other side we have

the slowmoving the cold molecules and thereby yes we cause a problem to the

total entropy of the isolated system of course no there's a beautiful solution

but let's take this idea now so here we go let's say here during the post

training now the underlying Hamiltonian this is of course the base LLM policy the pi data optimization is updated now

using this specific forced correction traces by the analog of our Maxwell

demon from 1867 no so let's do this gdunking experiment so we want to the

underlying field is wrapped so heavily so much stronger now that the unconstrained particle traveling along

here in the energy field hello here I am learns now in the training process to

avoid here the failure regions our dark red incinerated failure manifolds purely

by its own dynamics. So we have to provide training data pre-training data post- training data that this learning

this training can happen on this particular element and if you go post training I mean of course reinforcement

learning or distillation and here we have the new study New York University and Salesforce AI harnessing

LLM agents with skill programs now skill and non-animal skills that you know

skill become now more more powerful published May 18 2026 they tell us we

introduce HASP Harnessing LM agent with skill programs. Hasp a new framework that upgrades

skills into executable program function. Program function with a very specific

nature. Let me show you in a minute. So skills no change. Rather than offering

some passive advice how to do this, how to find the solution, huh? Our PFS act now as executable guard rails that

activate with a very specific trigger that is beautiful in physics on the failureprone states and will modify the

next action of our AI or maybe it needs just some corrective context that is

added here in our prompt. So this is nice. Either we modify the action so we

have a different path or we just add here some context and the LLM understands oops I have to do something

else not the action that I saw. Now the beauty is absolutely gorgeous has highly

modular. You can do this you can apply the inference time for a direct agent

loop intervention. We will have a look at this at first. But then as I told you even during the post training to provide

some structured supervision from the inference time examples we can use those traces as training example to train now

in a post-training our AI or if you want we can even use those traces here for

selfimprovement by evolving into validated teacher reviewed PFS.

So three different cases all are beautiful. Let's have a look. I mean

this is it the paper more or less. No, now there's only a little bit of mathematics or some detail

understanding. So if you like to go not to the mathematics section, please read

the paper for the mathematics. But if you want to just go to the detail understanding, welcome. Let's do this.

As always, we have to say what is exactly the problem that we want to solve. Full stop. The problem is our

current agents here recognize here hopefully the recurrent failing patterns

but they fail somehow to extract them into some reusable knowledge or some new

skills and apply those skills to adapt here the future behavior accordingly.

It's not really happening. No, especially if you go to more complex manifolds here, the skill complexity

cannot grow beyond a certain level of the algorithm itself. Now, as I showed you, you know, natural

response is to reuse past experience. Hey, what a coincidence that this is called memory. If you look at my last

three videos on memory optimization, what a coincidence that we talk again about memory here. Uh, past experience,

memory as skills. You see exactly where we're moving as behavioral knowledge abstracted from the prior agent

interaction. So we learn from the past failures from the past experiences of our agent. So we do have long running

agents. We don't have an agent. You switch on the AI machine and we start at z blank sheet. No we have all the memory

available and we have we have to learn from those mistakes. No but existing AI

agents already do so but only in a textual form. Yeah. This just injected

here some instruction into the prompt and you know instruction inserted into the prompt as an advice. This is just

here the little mountain chain here that is not tall enough to protect our particle from tunneling here into the

the the deep red one into the failure. So this makes the system highly

flexible. Yeah. but also largely advisory and sometimes the AI decides you know what I ignore your instruction

because I have other 95 instruction that I have to follow so if you tell me don't go there yeah know I ignore you

and now here this paper here skill programs tries to find a new solution to

exactly this problem so here we go our PF is a reusable state action

intervention function so this means given the current agent state and a

candidate next action that the LLM predicts it says hm wait a minute I

decide now whether the intervention is needed or not and if an intervention is needed I will

decide now based on my knowledge if I will modify or augment the policy of the

LLM in the training process given in the in the in the inference I have got

enough reasoning traces and correction in my training data set. So you see okay

so a force field accelerating the particle beautiful the golden optimal solution.

So this means skill the term skill changes it's no longer a passive guideline the model may choose to follow

and we have a skill library and the LLM says hey I choose skill 17 and 24. Now a

skill becomes an executable object by itself that can be triggered by an

algorithm. I will show you this algorithm in a second on demand and can intervene directly in the agent

loop. So it is not the eye that says I want skill 12. It is not something else.

What is it? So skills from prompted skills we move

now to something completely different. executable state action intervention

functions. Isn't this beautiful? We call them PFS. So existing skill prompting as a passive

text you know this great now we have a different we are now harnessing and ah

it is the harness who decides about it harnessing LLM agent with skill programs. So we transform the skills

that we have let's say 100 200 into pfs. The skill library goes now into a

program function. We will I'll show you the notion in a moment. Then we have the intervention of

our PFS in a policy loop structured intervention signal signal support to downstream P for the policy

internalization here for the training supervised fine-tuning here or distillation or a self-improving PF

evolution where we update the skills. So this means PF that activate on runtime states intervene through action

modification or beautiful context injection. So let's have a closer look.

So has operates now what is it? It is an external agent harness. It is not the

LLM itself. This means it is a control layer around the base agent. The core is

an LLM. So this means that each step the base policy of our LLM proposes an action.

The external harness retrieves now some real element pfs, evaluates their

activation predicates, executes the valid interventions and

feeds the revised action or injected context back into the agentic loop.

So this means at first of course we have to initialize our pfs from the failure cases in the training pool. So you

cannot start here from nothing. You have to have your training pool. Analyze the failure cases. Analyze solution,

possible solution, find the best solution, identify the skills and build up some knowledge about it. Great. Now,

as the particle or the LLM reasoning trace moves, an array of sensors

continuously monitors its position and velocity. No. So, you have now here in

the harness a continuous monitoring engine if you want. But it turns out

this engine is a simple Python script. So if the particle's proposed next step crosses here or comes closer to an

illegal threshold and this means here trying to finalize an answer without

retrieving sufficient data to direct system an active constraint instantly

fires now. So this means it mathematically overrides now some

external algorithm the coordinates of our flight path of our particle which is

an LLM reasoning trace to force it now into a valid sub manifold change the

course fly to the left fly higher lower whatever or it injects here a warning

field a higher barrier into the next observation state so the particle can selfcorrect here at t+1 for

it is so simple. If I show you this example, you immediately understand it. You have a question. We have music a two

hop entity resolution question. This is here the question. Beautiful. So our

react agent multiloop system our classical agent trajectory framework

here fails. Why? The search here at step zero has 16 words. And guess what? This

is too complex here for the eye. And you go on and you identify all that is

wrong. So the failure modes here that exonomized by the LLM is the query was

too broad. We had repeated search. We had the wrong entity focus. We had

reasoning hallucination and more. And now our new system step zero search

proposed a long query. And here we have immediately an external trigger that comes in and says stop. Before you even

start to generate any token, let's have a look. The PF retrieval failure fires.

Why? Because it triggers here an action that the search here has a length for

more than 15 words and says listen, if you have a length of more than 15 words, no, you have to do an action. You have

to go with some particular skill. So you see immediately or you say hey PF

says now decompose the complex question fires. No it says hey this is a multihop

question so search for each piece of information separately find the intermediate to enter this first and

then search for the final answer. So it doesn't even allow you to start with step zero to have this search with uh 16

words that says this is too complex for any I mean this is crazy no a search with 16 words is too complex for any

machine but okay let's go with this because as it turns out as they show us here yes with this intervention

quotation mark from the AI harness you get the correct result

there are a lot of other example please have a look at the paper but let's do now the abstraction ction. Let's go to

the main theory. Let's understand the main idea of this. So what we have? We

have here the framework. Great. So we have we have our query. This is my stupid query. Then I have the complete

toolkit informi. Then have all the skill libraries. 10,000 skills are available.

Then I have a teacher. More about this in a minute. And my current policy of the LLM, my PI data. I know this is this

is the strategy. It will deploy here the LLM to answer my question. And with this base policy we have now multiple turns

here but in a very specific sequence. Now at first we have the policy and the planner. The planner here is planning

here particular action A and then this action A is now investigated by the

harness of the eye and we have a PF intervention either the the PF

intervention is hey I don't like this action that is um suggested here by the

planner. I have an action override by our PF by our advanced skills or I have

a context injection. I pro provide additional context and if this is h

happened here then we go to the executor and then we have a verification and beautiful. So this is now at inter

inference time the retrieve program function guide multi-turn agent rollouts by modifying the action or injecting the

context while limiting the signal support policy internalization of the PF evolution. We're going to talk about this in a second. Just have a look what

is really happening in it is the harness. The harness is a Python script maintaining a registry of program

function objects. You have to define this. So at t equal 1

with the start the particle you know this is the llm reasoning trace in our example moves to a specific coordinate

in in the space and based only on that specific coordinate a localized boundary constraint. This means a specific

program function, our PF might activate to deflect it. It says, "Hey, careful.

If you continue on this route, you will move into the deep red here of a volcano. So careful. I have to deflect

you to a different path in the reasoning trace. So at t equal 2, the particle has

moved to a complete new region of the phase space. So a totally different boundary constraint. Now a different

program function might activate and says hey welcome to my region but I see you

want to do some search with a long complex uh structure. No you have to decompose the complexity into multiple

lower complexity queries. So this is an absolute interesting

sequence and we have to harness a Python script that is here maintaining here the registry of all the program function

objects that are available to you. If you want to see this here in written

down, this is here what I just told you here written down that that your AI or if you want to read it a second time.

Now how does it function? Every program function must inherit a strict interface

consisting only and this is the beauty. It is simple two methods. Should I activate boom yes no and intervene and

with the intervention. So this means a decision is simply made by should I activate yes or not. Should this PF fire

yes or not? And this function is explicitly engineered to be deterministic. And this is the first why

I said hey wow it is not an EI that I place there. It is a deterministic

scheme that I design. So either it evaluates a standard algebraic or a

programmatic predicate. So this means either it computes the string length of the query like I showed you 16 words in

your search query. You can't do this or checking if the history dictionary cons

already contains here a read action. But if the readaction count is zero, the

system says hey you have to read the data before you can argue about the data. So go back and do the reading

first. So you see this is the simple mechanism here.

And what I understood only after some minutes the authors explicitly forbid using neural LLM calls to decide whether

the boundary condition triggers no they say no we want to have a pure deterministic rule. They said the

harness is a pure order of one software execution. It is not a probabilistic

system and what they want to achieve with this is of course reduce the hallucination.

So here it is. Python should activate yes or not. If the search base is the

length uh over 15 then hey listen this is not possible. Yeah. So you see some

beautiful deterministic algebraic or computational structures. Great.

Now as we go on we go on go on we learn we have a lot of signals and now we have the pfder derived signals. This is

something about it's a four-dimensional state vector of course and we have the

timing we have the particular mode we have the correctness and we have now finally the outcome and these vectors

now flow into the or out of the inference loop to be specific this is our what we just achieved here in

inference and now we can use these traces as training data for either a

policy internalization with supervised fine-tuning or a self-improving

PF evolution. We update our skill library with new skills that we found in

our reasoning traces. No. So beautiful. Either we have now a trained policy

optimization. So we update the base policy and we start the loop again or we just do an update to the skill library

that we have. Now if the post training is available. So we we did our interference run. Everything is great

and now we go to the post training. Each PF execution provides a structured

record containing here the original action, the PF repair, the activated skills multiple and the

observed effect. And HA has now scores this event with structured PFD derived

criteria and uses here the resulting PF corrector traces to train out the studentbased policy via supervised

fine-tuning or rejection sampling or some on policy distillation teacher

student distillation whatever you like. So here is now the training. We bring

this now down to the weights. We want that the LLM now really learns this behavior that the harness was able now

to find the best traces. Even if you won't when you go to

self-improvement of your LRM revisits the failures under the current checkpoint summarizes the recurring

failure repair patterns into candidate PFs filters them through executable

validation and teacher review and updates the external skill libraries that were closing the loop between the

execution learning and library graph. So you can really use it for inference for

training in a classical sense supervised fine tuning or for self-improvement. This is such a nice idea.

Let's look at the result and I still have to talk about the teacher. Now the result we go for inference time

only first. So we have here the web search reasoning benchmark and the mathematical reasoning benchmark. And as

you see there's a lot more dynamic in the web search reasoning. So not so much in the pure mathematical logical

reasoning. So let's have a look at web search reasoning. Great training free only inference time methods. And you

have here all the models here all models are multiloop. Beautiful. And then here

the last two lines is intervention here the PF only. And now we have something with teacher. So let's talk about this.

But at first if we only go with HAP intervention PF only purely through dynamic execution of the PFS altering

now the trajectory of the particle of our reasoning trace mid-flight average accuracy jumps from the baseline

31.2 here with our agent multiloop to 51%.

So this proves the order to argue the massive capability elicitation that is possible without

touching our naba our any training. This is done inference just by finding here

the right PFS altering the trajectory mid-flight avoiding here the failure

trajectory here in our energy reservoir energy landscape and you might said great

and now comes the question but what happens when the boundary collision is semantically [snorts] not amantically

semantically ambitious the softman knows the particle is coming closer to a

failure manifold because the L&M search query is for example failing. But calculating now the optimal escape

vector requires some real complex semantic reasoning rather than a simple

algebraic reflection like hey the query should not have more than 16 words. So in those cases the artist decided to go

with a teacher AI model. So you say aha so you did not only rely here on

deterministic but you also want to have an intelligent if you want probabilistic

teacher so that teacher is now this external high energy oracle they went

with a GPD4 omni I don't know why instantiated temporarily to resolve these complex integrals here for the

escape vector that provides some additional momentum to the particle.

So you see instead of forcing your original classical Python harness to blindly guess how to fix a complex

logical error this situation where we do not have this Python script the harness

temporarily suspends now the simulation packages the localized face base coordinates and hands them over to the

teacher AI model and now the teacher the oracle computes the precise optimal corrective vector here cloud-based hands

it back to the doministic harness the harness learns what to do and tells it

now modifies the force field and the particle resumes its trajectory to the golden sunset on the global attractor

level. Beautiful. The second part is about training when

training happened. Let's compare this to a supervised training vanilla to a search R1 to whatever you have. No. And

then of course we do the training here or the or has decided to do the training with a simple rejection sampling RS.

Okay, great. You see all the bold numbers are here with HP evolve plus

rejection sampling. So it outperforms everything else that we have currently.

This means web search reasoning and mathematical reasoning. Great. Yeah. By the way, for HAP, we have here a Q1

2.57B instruct. A real old little tiny model here from Qentan 2.5. I don't know

why they don't use 3.6, but a 2.5 seems to be a standard somehow in the academic

circles. Yeah, unfortunately, we have to accept it. But imagine even with a Q 2.5, it outperforms whatever. Great.

Now if they look close and please have a look at the study yourself at the intervention patterns that are chosen

now by the hornness. What were those intervention patterns? Now they showed that it is actively more or less three

that were really doing the heavy work. Now so the first one 322 total triggers

here was decompose the complex question into multiple simpler sub questions. The

next one was hey you can't stop now little I you have an insufficient

exploration of the solution space you have to go on and search here your face

space maybe you find other minima maybe you find the global minima or extreme

therefore continue your search don't stop now and the third one was the

answer completeness was given or not given in our case no great so now you

understand exactly what's in the study and now I have to tell you but careful there are limitation and this is now my

personal reflections no so the idea is positive but you know

every positive has also a negative side note the LLM is permitted to be creative and probabilistic and proposing now the

solution but it is physically prevented from violating topological task

constraint like hey each search query has to have less than 15 birds by the

pipe harness by a deterministic partner harness

and the authors argue this is the exact mechanism that generates here hyper clean gradient signal then for the training for the supervised fine tuning

absolutely that is later used in the post training yes I agree with this if we have found a better path yes we

should use the better path yeah but the harness knows with absolute programmatic

certainty when the LLM made an error [clears throat] I'm a little bit skeptic

now. So I get the main idea. Yes, I don't want the LLM hallucinating traces

or whatsoever. So I have a deterministic control agent here. The partner harness.

This is a control shell around my LLM in the harness region. You can go with

Python or whatever C++ whatever you like. Here you find here your best skills that you can use from the skill

set or you let the system define new skills. you come up with a skill evolution schema as I've showed you in

my one of my last three videos everything is possible no but I think we should reduce our expectation that we

have now even a programmatic certainty I think this is just helping us to come

closer or reduce here the hallucination but yeah we have to take care about

exactly the detministic python horn structure the complexity the symbols and

uh Yeah, there are complexities on the way. Tons of complexities. So there's

this little limitation. I would say be a little bit careful when you use this methodology, but otherwise absolutely

fascinating. You see what we do currently in the eye research just to have a reduction of elucination for

LLMs. We talked about memory, we talked about skill development, we talked about Python harness modification and

topological task constraint. Isn't AI absolutely beautiful?