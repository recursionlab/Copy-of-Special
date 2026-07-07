Why Geometric Structure Beats Pure Scaling in AI Models Why do modern AI models rely on massive scaling? And is scaling really the best way forward? In this video, we explore the difference between geometric structure and pure scaling in AI models. Many modern machine learning systems rely on scaling parameters, data, and compute power. But geometric structure may provide a more efficient and powerful alternative. We break down how structure-based architectures could outperform brute-force scaling and what this means for the future of artificial intelligence. Topics covered: • AI model scaling • geometric structure in neural networks • machine learning architecture • why scaling laws may not be enough • the future of AI models Subscribe for more AI research, machine learning insights, and future technology breakdowns. Link to Substack Article: [https://richardaragon.substack.com/p/...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbUNLNG45Ync1Z2JrV09PWThKbkJJWnp2WU5sZ3xBQ3Jtc0ttdUZfdG90YlhHM205QUtrelVYQ2pRMjNQSUdXM0FWQkQxS0phR2pkWFlPbm1LWl94clFMM1lIeXFGY1BnN1p6V2Zobnh1OXhGWlZJak9pSDJaNE9pZU16Y1pmVDAyS3hsaHZ2eC1xOHNOLVRBenU4RQ&q=https%3A%2F%2Frichardaragon.substack.com%2Fp%2Fgeometric-structure-vs-pure-scale%3Fr%3D23t7gr%26utm_campaign%3Dpost%26utm_medium%3Dweb%26triedRedirect%3Dtrue&v=n8vJvReDYqA) Link to Colab Notebook: [https://colab.research.google.com/dri...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbFFzOHRzMGh2NC0xSndFaTB1TjEzSlBtcUhTd3xBQ3Jtc0tsUFRfdGIxMHYtMF9XUE90QmR4QzBVZjNPVm43YnVTaTR1R3BsUFJqQVNiaFdkb0tPLVFqME5SOVQyWXY5cUhmclU0Rm5CVGg4RC1ESzg0N1VHbHdQaXFvLWdNMFFnTFdZeTlBWDB4a25GNXdpLVMzdw&q=https%3A%2F%2Fcolab.research.google.com%2Fdrive%2F1XGdj3X1X96bROiCE7Vn7YgXXC-jUWUXy%3Fusp%3Dsharing&v=n8vJvReDYqA) [#ArtificialIntelligence](https://www.youtube.com/hashtag/artificialintelligence) [#MachineLearning](https://www.youtube.com/hashtag/machinelearning) [#DeepLearning](https://www.youtube.com/hashtag/deeplearning) [#AIResearch](https://www.youtube.com/hashtag/airesearch) [#NeuralNetworks](https://www.youtube.com/hashtag/neuralnetworks) [0:00](https://www.youtube.com/watch?v=n8vJvReDYqA) Introduction [1:12](https://www.youtube.com/watch?v=n8vJvReDYqA&t=72s) What is AI Scaling [4:30](https://www.youtube.com/watch?v=n8vJvReDYqA&t=270s) The Problem with Pure Scaling [9:10](https://www.youtube.com/watch?v=n8vJvReDYqA&t=550s) Geometric Structure Explained [15:40](https://www.youtube.com/watch?v=n8vJvReDYqA&t=940s) Structure vs Scaling Comparison [21:30](https://www.youtube.com/watch?v=n8vJvReDYqA&t=1290s) Future of AI Models [24:50](https://www.youtube.com/watch?v=n8vJvReDYqA&t=1490s) Final Thoughts


## In this video

Chapters

Transcript

## Introduction

Hey everybody. So more and more people

in general have been asking me for uh

more like uh like verifiable proof

benchmarks etc around my framework which

is of like that's expected of course

right uh and then uh within that like

I've released like a lot of research

benchmarks etc that people could go off

of but I have like I haven't done it um

very explicitly um within this and then

so that's what I want to demonstrate

very specifically today is benchmark

testing geometric structure versus pure

scale directly. Uh and then showcasing

the results and uh how the experiment

went within that. Uh and then so overall

like I'm going to go off of a script

within this like so I I've gone both

ways with the script and without and

then like people have commented both

ways like uh like like when I don't use

a script it's like oh you should use a

script and then when I do it's like oh

you're just reading like an AI script or

whatever. Um so my preference is a

script if people are going to just

comment both ways. Uh so I'll I'll just

go with the script. So for the last

several years, the dominant story in AI

has been simple. If you want better

performance, make the model bigger. More

parameters, more data, more compute. And

## What is AI Scaling

to be fair, that story has worked. Scale

has produced systems with astonishing

breadth. But scale has also trained us

into a dangerous habit. Treating

intelligence as if it were mostly a

volume problem. as if the path to better

behavior is just more capacity poured

into the same basic container. Our

experiments suggest something else. Not

that scale is useless, not that larger

models never help, but that there are

regimes, especially multitask regimes

with internal conflict where structure

matters more than size. In those

settings, the decisive question is not

how big is the model, but how is the

model organized. That is the difference

between a pure scale and geometric

structure. The core idea, a model does

not just store information, it arranges

it. The arrangement matters. If two

tasks share the same representation too

aggressively, they interfere with each

other. The model h may have enough

parameters in principle yet still

perform worse because its internal

geometry is poorly organized. Knowledge

and behavior begin to collide inside the

same latent channels. Capacity exists

but capability is muddled. This is the

hidden weakness of pure scale. A larger

model can sometimes brute force its way

around that weakness. But brute force is

not the same thing as a clean solution.

If the internal organization remains

entangled, then adding parameters may

simply give the model more room to

compensate for confusion rather than

eliminate it. Geometric structure

attacks the problem at a deeper level.

Instead of only asking for more

capacity, it asks for better separation,

better routing, and cleaner task

organization inside the latent space

itself. That's the difference between a

bigger warehouse and a better city plan.

So, what exactly we tested? To examine

this directly, we built a controlled

multitask experiment. Each model

received the same type of synthetic

sequence input and had to perform two

different tasks on the same input. Task

one was a sentiment-like binary

classification task and task two was a

counting/structured extraction task.

These tasks were intentionally chosen

because they draw on different

abstractions while sharing the same

underlying sequence that makes them

useful for studying interference. One

task is more semantic. The other is more

exact and structured. Both compete for

representational resources.

We compared four model types. One was a

baseline small, a small shared encoder

with both tasks using the same pulled

representation. Two was a bigger

baseline, the same architecture but four

times bigger. Three was adapter only

small, the small the same small encoder

but with task specific adapters

branching off the shared representation.

And then four was a geometry small the

adapter version plus an orthogonality

pressure encouraging the task specific

representations to remain geometrically

## The Problem with Pure Scaling

separated. And then so within this and

highlighting this method within that

like this particular method this

framework overall is a very simplistic

um implementation of the geometry

framework. This setup lets us isolate

three different hypotheses. Does a

simple scaling help? Does branching or

task specific routing help? And does

explicit geometric separation help

beyond routing alone? Why this matters?

Most people assume that a larger model

should dominate a smaller one. And if

the smaller one wins, many assume it

must be some narrow flu. But that

assumption only holds if the main

bottleneck is raw capacity. In a

multitask, the bottleneck is often not

capacity, it's interference.

A model may know enough to solve both

tasks but fail because the same latent

machinery is being pulled in

incompatible directions. In that case,

scale is not solving the real problem.

It's just absorbing the damage and then

I'll showcase to you actually making

this particular problem worse via just

pure scale.

Geometric structure by contrast tries to

reduce the damage directly. That is why

this experiment matters. It's not just

about getting a slightly better score.

It's about asking whether a model can be

made better by organizing its internal

space more intelligently rather than

merely enlarging it. Before I move on

from this, just like the simplest

overall framing that I can put for this

and it like uh it's very straightforward

to me, right? So the current and

standard approach to AI is just blindly

uh uh like guiding the model and

optimizing the model via stoastic

gradient descent no matter what all the

time. That's all you do is you're just

blindly guiding based off of that. No

other measurements whatsoever. And then

the uh second thing is is that you're

like dumping all of this content into

one singular latent space, right? like a

and and and this just just this giant

big blob and there's literally no

internal structure within this blob

until the model creates that structure

itself. And then so just knowing that

just giving it some geometric helpers uh

is all that we're doing and testing

within that. And then so what the first

results showed in the initial regime the

geometry aware model performed extremely

well. It achieved the best average

accuracy, best test loss, strongest

sentiment performance, and almost

perfect count behavior. More

importantly, it did this with a model

that was still small. The larger

baseline, despite having roughly four

times the parameter count, did not

dominate it. The most striking result

was in representation overlap. The

shared baselines remained completely

entangled under the overlap measure.

Their task representations were

effectively the same space. The geometry

aware model by contrast rapidly drove

overlap down toward zero. This meant

that the structure was not decorative.

It was actually changing how the model

organized its internal representations.

That matters because a lot of

regularization tricks look impressive in

theory but do very little in practice.

This one clearly altered the latent

behavior. The first experiment suggested

a strong conclusion. Better internal

organization can outperform naive

scaling when the real problem is

interference rather than under capacity.

The key ablation, branching versus

orthogonality.

That first result was promising, but it

was not yet enough. A skeptic could

reasonably say maybe the win had nothing

to do with geometry. Maybe all of the

benefit came from adding task specific

branches. In other words, perhaps the

important ingredient was routing and not

separation. So we ran the correct

ablation. We added adapter only small

which had the same task specific

branching but no orthogonality pressure.

This clarified the story considerably.

Branching helped. That part became

obvious. Compared to the fully shared

small baseline, the adapter only model

improved test loss, improved such

accuracy slightly, and dramatically

reduced representation overlap. That

meant task specific routing alone

already changed the game. The model

benefited simply from not forcing both

tasks through the same exact final

representation channel. But branching

alone was not the whole story. When we

## Geometric Structure Explained

compared geometry small to adapter only

small, the orthogonality term still

added value. It further reduced overlap,

improved test loss, and improved

structured task performance and

sharpened calibration. In other words,

routing gave the model separate lanes.

Geometric pressure made those lanes

cleaner. That is a very important

distinction. It means that the

improvement was not just give each task

its own adapter which is like what

everyone is calling all of the

breakthroughs all of a sudden right the

model improved further when we encourage

those task representations to remain

genuinely distinct. So the emerging

picture became shared representation is

weak under interference. Branching

provides a major structural gain and

geometric separation provides an

additional refinement gain. That's

already a meaningful result. The harder

regime where scaling like absolutely

broke. The decisive test came when we

increased task conflict. We made the

data set substantially harsher. Stronger

anti-correlation between count and

sentiment. more negative distractors

when the count signal is high and weaker

clean positive signal and more noise.

Essentially the common things that are

being tried to solve for via scale,

right? If we uh if a model encounters

these problems, the common logic is is

that scale could overcome them. This is

where architecture gets tested for real.

Easy task can hide structural

weaknesses. Hard conflict exposes them.

And in the hard conflict regime, the

larger baseline got exposed badly. It

had the worst loss, the worst average

accuracy, and the worst sentiment

accuracy. And it still remained fully

entangled in representation space. That

is not subtle. That is exactly the kind

of result that challenges the pure scale

narrative. The adapter only model held

up much better. It preserved strong

performance and clearly improved task

separation. So routing mattered even

more once conflict increased. But the

geometryaware model delivered the

cleanest overall solution. It achieved

the best test loss by a meaningful

margin, the best calibration,

nearperfect structure performance, and

by far the strongest representational

separation.

There was a small trade-off. The adapter

only model slightly edged it on raw

average accuracy, but the geometry model

had the cleaner optimization profile,

cleaner calibration, and vastly stronger

latent factorization. That is what a

real structural bias often looks like.

It doesn't always maximize the flashiest

topline number. Instead, it produces a

more stable and internally coherent

solution. In the hard regime, the

conclusion became much stronger. When

task conflict becomes substantial, scale

alone does not solve the problem.

Structural organization does provably

what geometric structure really means

here. It's easy to hear a phrase like

geometric structure and imagine handwavy

mysticism. That is not what's happening

in this context. Geometric structure

means something concrete, task specific

routing instead of total sharing,

representational separation instead of

force overlap and latent organization

that reflects the task the fact that

different tasks require different

subspaces. This is a geometric claim

because it concerns the shape of the

internal manifold. It asks whether

different behaviors are being embedded

into the same region, pushed apart into

different regions, or routed through

distinct but related directions. A

network is not only a function

approximator, it's also a space

organizer. Once you see that, you

realize why scale is not enough.

Increasing the size of an entangled

space does not automatically make it

well structured. A larger tangled room

is still entangled. Geometric structure

is about giving that room a layout. Why

this suggests magnitude level gains?

Most optimization tweaks produce

incremental effects, tiny gains,

benchmark noise, cosmetic improvements.

But organization can create step

changes. Why? Because bad structure does

not merely reduce efficiency. It creates

systematic self-conlict.

It causes the model to spend its

capacity fighting itself. Once that

conflict is reduced, improvements can

appear disproportionate to the size of

the architectural change. That's why

structure versus scale framing matters

so much. If performance ceilings are

increasingly determined by internal

interference, then the next magnitude

level gains may not come primarily from

adding more parameters. They may come

from learning how to partition, route,

and geometrically organize intelligence

inside of the model. That would be a

very different future for AI design.

Instead of only asking how much larger

to grow the manifold, we would ask how

to shape it. And then to me the bottom

line within this is very simp the very

simplistic framing within this is that

so to me uh all of these models have

been scaled up to the moon right

uh claude gro like all of the current

deepseek etc. all the current models

right and then they they've been scaled

to the moon and they they have been

scaled with all of the data. Uh, and

then so now it's like, well, what do we

do from there to scale more and to scale

harder and to continue scaling? And then

for me, I'm saying, well, like you've

already scaled to the moon. Just take

advantage of that scale that already

exists. just you know like like

literally use the same exact

architecture that you have uh and then

just apply it like uh more structurally

literally uh and you'll get magnitudinal

gains out of the same parameter

performance and then so uh that's all it

is overall right it seems pretty

straightforward to me so the deeper

implication this is about more than one

experiment the broader implication is is

## Structure vs Scaling Comparison

that intelligence may depend less on raw

size than on the quality of internal

differentiation.

A system becomes more capable when it

can preserve distinct modes without

collapsing them together, route

different demands through different

internal pathways, avoid

representational interference, and

maintain coherence under conflicting

objectives. Those are architectural

properties, not just scale properties.

And if that is true, then the industry's

obsession with brute force growth may

eventually look incomplete. Not wrong

but incomplete.

Scale can buy breadth. Structure may buy

clarity. Scale can buy approximation.

Structure may buy organization.

Scale can buy more. Structure may buy

better.

What a fair conclusion looks like. A

fair conclusion is not scale is dead.

That would be lazy and false. A fair

conclusion is this. In low conflict

settings, scale can remain competitive

on some headline metrics. But in

multitask settings where internal

interference matters, geometric

structure can outperform pure scaling on

the metrics that most directly reflect

solution quality, which are loss,

calibration, reliability, and

representational separation. And in our

harder regime, the case became even

stronger. When conflict arises,

structural organization becomes more

impair important. While scale without

structure can fail dramatically and

that's a publishable idea in and of

itself, not because it proves a

universal law, but because it points at

a real fault line in current model

design.

As a final thought, the most important

lesson from these experiments is simple.

A model can fail not because it is too

small but because it is too entangled.

That is a different diagnosis and it

implies a different cure. Pure scale

asks for more mass. Geometric structure

asks for better form. If the future of

AI depends on reducing internal

conflict, then form may matter more than

mass far more often than we've been

willing to admit. And if that's true,

then the next major gains in

intelligence may come not from building

bigger minds, but from building minds

with cleaner geometry.

Diving into the the code specifically

here. I'll give you like access to the

full code notebook um if you want to

look this over. But uh I liked the the

PowerPoint um that I did the other day

and then so I have a PowerPoint

specifically going over u these results,

right? And so I'll give you access to to

the collab notebook, but I'll I want to

go over it this way. And so uh structure

versus scale. Why organization can

deliver disproportionate gains on a task

conflict problems utilizing the same

backbone plus routing plus geometric

separation beats a four times larger

shared baseline under harder conflict.

We run this for three runs. And as far

as the headline metrics, we can reduce

loss by 20 about 29% uh versus the like

the large model, the four time larger

model. Um we reduce separation was like

n above 95% like to to near zero. Uh and

then uh we improve uh sentiment accuracy

overall by about two point about 3%

three points.

The thesis is that scale adds capacity

while structure allocates it. Our

experiments isolate the difference

between more parameters and better

organization

for the structure first model. It was a

small same we use the same small

backbone task specific routing and

representation separation separation and

conflict conflicts were handled inside

of the network. What the experiment

showed was that when task conflict is

mild both can compete but when conflict

hardens the shared larger model

collapses first. That's this to me is

the important takeaway within this and I

I'm going to show this showcase this to

you within the the the results here in a

couple of slides, right? Where uh it's

the like the more overlap that you have

the larger mo it impacts the larger

model more than the smaller model. And

then so the core claim is that

meaningful gain comes from organization

and not just count. This is just the

full setup of the experimental design.

all of the parameters of the model

overall uh the models uh and then the

regimes framework etc.

And then these are the the um starting

to go into the results, right? And then

so this is the phase one experiment uh

where we essentially we go over the um

results in in different benchmarks.

First of all, geometry small like

absolutely slaughters everything else

with regards towards the validation loss

validation accuracy. It's the only one

that maintains consistent 100% accuracy

once it's trained and learned. You start

to you see that that collapse start to

occur with the bigger baseline, right?

It's the very first one to collapse

under this particular instance because

of the representation overlap. You can

see that within this there's like 100%

overlap uh within the representations

between of the bigger baseline model. Uh

and then with the geometry small it's

the only one that it reduces it to

literally like almost zero, right? Um

and then same thing here uh when we add

the the other models. Um and then like

do like the secondary test on the harder

results. Same thing overall the the the

um uh the uh red here is the in this

particular one is the geometry small

model. Uh and then it's uh getting it's

the most consistent and and best loss

also too like the adapter only small is

performant is very performant within

this but it doesn't beat out in the end

## Future of AI Models

and and throughout the the whole entire

test the the geometry small and then

especially you can see exactly why here

because of the separations right so just

by adding the adapter only small you do

get some separation within this and then

so to me that's like like the I'

mentioned it a lot at this point right

but like the JP Morgan Chase paper and a

few of the other recent papers that I've

gone over within this channel where they

like they're they've discovered that

this geometry exists and then they're

essentially performing this like the the

the uh uh like what I'm doing with the

like uh adapter only small right where

like essentially they're like um

accounting for it and then essentially

like adding another metric beyond just

SGD that's and then so you can see just

doing that alone decre like it decreases

representation ation overlap which is

good right like this like representation

overlap the lower the number the better

so 1.0 is a very bad number. Zero is a

very good number. Uh and then you can

see here that uh within like with the

adapter only it like it's it's able to

to train it down but it it levels off,

right? Like so it's like uh it's able to

train it down like a good about like

like it so it starts off like 20 points

and then it's able to reduce it about 20

points below that we'll call it. So like

uh it's like 20 30 points cuz it gets

down to like we'll call it like 50 um is

like um 50% overlap still in existence

there which explains like why it's not

performant later on the loss here right

whereas the geometry small is very

performant there

and then this is um just on the hard

conflict task specifically. Uh and then

on this one you can see here that

geometry small is the only one that

achieves that perfect baseline result uh

once like like uh once the structure is

is uh found right is is uh locked in uh

it's the only one and then you can see

that the very first one to collapse

within this the worst collapses happen

with the bigger baseline. and the bigger

baseline it like it it shoots up

accuracy very high right um and but

adapter only small actually beats it out

but like but it but it's accur like it

shoots there and then it it's the first

and and the biggest collapses um and

then same metrics that apply out within

this with regards towards that

representation overlap uh and then in

this in in this particular one I would

say that like adapter only small wins in

this particular test and then second

would be the the geometry aware adapter

uh in my mind like that that like this

the adapter after only small line is is

super clean on this one. Uh and it could

just be that particular test overall.

But uh essentially what's publishable

within this the strong claim is is that

in a controlled multitask interference

interference benchmark a small geometry

aware model matched or beat a much

larger shared representation baseline on

the outcomes that matter most under

conflict. Test loss calibration

representation separation and

robustness. A careful claim is is that

the gains are not universal raw topline

wins on every metric in every regime.

The contribution is that organization

becomes the decisive lever as

interference hardens. Meaning that like

the bigger the model gets, the more data

size data set that you have, the more

noise that's within it, everything that

comes with scaling, right? Like this.

So, uh the more that you want to scale,

the more that you need this geometric

structure as a design principle. If the

## Final Thoughts

bottleneck is a shared representation

conflict, more parameters mostly enlarge

the problem. Routing and separation make

the capacity usable. Uh publishable

framing is is that structure gives

outsiz gains because it changes where

computation happens and not just how

much exists.

Uh and then uh over here again I'll

leave you access to all the code here

which you can go through check it out

and run. And then this is where all

those um graphs that we're looking at

within that PowerPoint come from. So you

can get access to all of those as well

as all the benchmark numbers. Uh here

this is just pure benchmark testing,

right? That's all all we're doing within

here. Uh if you need a description of

the notebook, I give you clean uh exact

a full overall description uh as to

exactly what's going on within this.

Point of this overall is very

specifically to benchmark and prove out

this right geometric structure beats out

pure scaling on uh every single test

that we do within this. And it only

becomes bigger like a a uh more and more

improvement for a geometric structure

the more that you want to scale. And

that's kind of just how it shakes out. I

didn't do it. If you like this type of

content, please like and subscribe.

Thank you very much.



  

[

![Richard’s Substack](https://substackcdn.com/image/fetch/$s_!948S!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba8323c0-0a55-4bd8-b414-65a8f9cc3089_48x48.jpeg)



](https://richardaragon.substack.com/)

# [Richard’s Substack](https://richardaragon.substack.com/)

# Geometric Structure vs. Pure Scale

[](https://substack.com/@richardaragon)

[Richard Aragon](https://substack.com/@richardaragon)

Mar 11, 2026

[

![](https://substackcdn.com/image/fetch/$s_!4W_M!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F909b7411-8a46-4172-9992-ebd03a2ae428_1536x1024.png)



](https://substackcdn.com/image/fetch/$s_!4W_M!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F909b7411-8a46-4172-9992-ebd03a2ae428_1536x1024.png)

For the last several years, the dominant story in AI has been simple: if you want better performance, make the model bigger.

More parameters. More data. More compute.

And to be fair, that story has worked. Scale has produced systems with astonishing breadth. But scale has also trained us into a dangerous habit: treating intelligence as if it were mostly a volume problem. As if the path to better behavior is just more capacity poured into the same basic container.

Our experiments suggest something else.

Not that scale is useless. Not that larger models never help. But that there are regimes, especially multitask regimes with internal conflict, where **structure matters more than size**. In those settings, the decisive question is not “How big is the model?” but “How is the model organized?”

That is the difference between **pure scale** and **geometric structure**.

## The core idea

A model does not just store information. It arranges it.

The arrangement matters.

If two tasks share the same representation too aggressively, they interfere with each other. The model may have enough parameters in principle, yet still perform worse because its internal geometry is poorly organized. Knowledge and behavior begin to collide inside the same latent channels. Capacity exists, but capability is muddled.

This is the hidden weakness of pure scale.

A larger model can sometimes brute-force its way around that weakness. But brute force is not the same thing as a clean solution. If the internal organization remains entangled, then adding parameters may simply give the model more room to compensate for confusion rather than eliminate it.

Geometric structure attacks the problem at a deeper level.

Instead of only asking for more capacity, it asks for **better separation, better routing, and cleaner task organization** inside the latent space itself.

That is the difference between a bigger warehouse and a better city plan.

## What we tested

To examine this directly, we built a controlled multitask experiment.

Each model received the same type of synthetic sequence input and had to perform two different tasks on the same input:

- a sentiment-like binary classification task
    
- a counting / structured extraction task
    

These tasks were intentionally chosen because they draw on different abstractions while sharing the same underlying sequence. That makes them useful for studying interference. One task is more semantic. The other is more exact and structured. Both compete for representational resources.

We compared four model types:

1. **baseline_small**  
      
    a small shared encoder with both tasks using the same pooled representation
    
2. **bigger_baseline**  
      
    the same architecture, but with substantially more parameters
    
3. **adapter_only_small**  
      
    the same small encoder, but with task-specific adapters branching off the shared representation
    
4. **geometry_small**  
      
    the adapter version plus an orthogonality pressure encouraging the task-specific representations to remain geometrically separated
    

This setup lets us isolate three different hypotheses:

- does simple scaling help?
    
- does branching or task-specific routing help?
    
- does explicit geometric separation help beyond routing alone?
    

## Why this matters

Most people assume a larger model should dominate a smaller one. And if the smaller one wins, many assume it must be some narrow fluke.

But that assumption only holds if the main bottleneck is raw capacity.

In multitask systems, the bottleneck is often not capacity. It is **interference**.

A model may know enough to solve both tasks but fail because the same latent machinery is being pulled in incompatible directions. In that case, scale is not solving the real problem. It is just absorbing the damage.

Geometric structure, by contrast, tries to reduce the damage directly.

That is why this experiment matters.

It is not just about getting a slightly better score. It is about asking whether a model can be made better by **organizing its internal space more intelligently** rather than merely enlarging it.

## What the first results showed

In the initial regime, the geometry-aware model performed extremely well.

It achieved the best average accuracy, best test loss, strongest sentiment performance, and almost perfect count behavior. More importantly, it did this with a model that was still small. The larger baseline, despite having roughly four times the parameter count, did not dominate it.

The most striking result was in representation overlap.

The shared baselines remained completely entangled under the overlap measure. Their task representations were effectively the same space. The geometry-aware model, by contrast, rapidly drove overlap down toward zero. This meant the structure was not decorative. It was actually changing how the model organized its internal representations.

That matters because a lot of regularization tricks look impressive in theory but do very little in practice. This one clearly altered the latent behavior.

The first experiment suggested a strong conclusion:

**better internal organization can outperform naive scaling when the real problem is interference rather than under-capacity.**

## The key ablation: branching vs orthogonality

That first result was promising, but it was not yet enough.

A skeptic could reasonably say: maybe the win had nothing to do with geometry. Maybe all the benefit came from adding task-specific branches. In other words, perhaps the important ingredient was routing, not separation.

So we ran the correct ablation.

We added **adapter_only_small**, which had the same task-specific branching but no orthogonality pressure.

This clarified the story considerably.

Branching helped. That part became obvious.

Compared to the fully shared small baseline, the adapter-only model improved test loss, improved sentiment accuracy slightly, and dramatically reduced representation overlap. That meant task-specific routing alone already changed the game. The model benefited simply from not forcing both tasks through the exact same final representational channel.

But branching alone was not the whole story.

When we compared **geometry_small** to **adapter_only_small**, the orthogonality term still added value. It further reduced overlap, improved test loss, improved structured-task performance, and sharpened calibration. In other words, routing gave the model separate lanes; geometric pressure made those lanes cleaner.

That is a very important distinction.

It means the improvement was not just “give each task its own adapter.” The model improved further when we encouraged those task representations to remain genuinely distinct.

So the emerging picture became:

- shared representation is weak under interference
    
- branching provides a major structural gain
    
- geometric separation provides an additional refinement gain
    

That is already a meaningful result.

## The harder regime: where scale really broke

The decisive test came when we increased task conflict.

We made the dataset substantially harsher:

- stronger anti-correlation between count and sentiment
    
- more negative distractors when the count signal was high
    
- weaker clean positive signal
    
- more noise
    

This is where architecture gets tested for real. Easy tasks can hide structural weaknesses. Hard conflict exposes them.

And in the hard-conflict regime, the larger baseline got exposed badly.

It had the worst loss, the worst average accuracy, the worst sentiment accuracy, and still remained fully entangled in representation space.

That is not subtle. That is exactly the kind of result that challenges the pure-scale narrative.

The adapter-only model held up much better. It preserved strong performance and clearly improved task separation. So routing mattered even more once conflict increased.

But the geometry-aware model delivered the cleanest overall solution. It achieved the best test loss by a meaningful margin, the best calibration, near-perfect structured performance, and by far the strongest representational separation.

There was a small tradeoff: the adapter-only model slightly edged it on raw average accuracy. But the geometry model had the cleaner optimization profile, cleaner calibration, and vastly stronger latent factorization.

That is what a real structural bias often looks like. It does not always maximize the flashiest top-line number. Instead, it produces a more stable and internally coherent solution.

In the hard regime, the conclusion became much stronger:

**when task conflict becomes substantial, scale alone does not solve the problem. Structural organization does.**

## What “geometric structure” really means here

It is easy to hear a phrase like geometric structure and imagine hand-wavy mysticism. That is not what is happening.

In this context, geometric structure means something concrete:

- task-specific routing instead of total sharing
    
- representational separation instead of forced overlap
    
- latent organization that reflects the fact that different tasks require different subspaces
    

This is a geometric claim because it concerns the shape of the internal manifold. It asks whether different behaviors are being embedded into the same region, pushed apart into different regions, or routed through distinct but related directions.

A network is not only a function approximator. It is also a **space organizer**.

Once you see that, you realize why scale is not enough. Increasing the size of an entangled space does not automatically make it well-structured. A larger tangled room is still tangled.

Geometric structure is about giving that room a layout.

## Why this suggests magnitude-level gains

Most optimization tweaks produce incremental effects. Tiny gains. Benchmark noise. Cosmetic improvements.

But organization can create step changes.

Why? Because bad structure does not merely reduce efficiency. It creates systematic self-conflict. It causes the model to spend its capacity fighting itself.

Once that conflict is reduced, improvements can appear disproportionate to the size of the architectural change.

That is why the structure-vs-scale framing matters so much.

If performance ceilings are increasingly determined by internal interference, then the next magnitude-level gains may not come primarily from adding more parameters. They may come from learning how to partition, route, and geometrically organize intelligence inside the model.

That would be a very different future for AI design.

Instead of only asking how much larger to grow the manifold, we would ask how to shape it.

## The deeper implication

This is about more than one experiment.

The broader implication is that intelligence may depend less on raw size than on the **quality of internal differentiation**.

A system becomes more capable when it can:

- preserve distinct modes without collapsing them together
    
- route different demands through different internal pathways
    
- avoid representational interference
    
- maintain coherence under conflicting objectives
    

Those are architectural properties, not just scale properties.

And if that is true, then the industry’s obsession with brute-force growth may eventually look incomplete. Not wrong, but incomplete.

Scale can buy breadth. Structure may buy clarity.

Scale can buy approximation. Structure may buy organization.

Scale can buy more. Structure may buy better.

## What a fair conclusion looks like

A fair conclusion is not “scale is dead.”

That would be lazy and false.

A fair conclusion is this:

> In low-conflict settings, scale can remain competitive on some headline metrics. But in multitask settings where internal interference matters, geometric structure can outperform pure scaling on the metrics that most directly reflect solution quality: loss, calibration, reliability, and representational separation.

And in our harder regime, the case became even stronger:

> When conflict increases, structural organization becomes more important, while scale without structure can fail dramatically.

That is a publishable idea. Not because it proves a universal law, but because it points at a real fault line in current model design.

## Where this goes next

The natural next step is not just to add more tasks. It is to study the geometry itself more explicitly.

For example:

- vary orthogonality strength and map the tradeoff between top-1 accuracy and structural cleanliness
    
- replace orthogonality with contrastive or hyperbolic separation
    
- test whether different task families naturally prefer different latent geometries
    
- evaluate whether the same principles hold in real language or vision multitask settings
    
- examine whether “knowing” and “doing” are separable not just functionally, but geometrically
    

Those questions point toward a larger program.

If scale was the first great engine of modern AI, structure may be the next one.

## Final thought

The most important lesson from these experiments is simple:

**A model can fail not because it is too small, but because it is too entangled.**

That is a different diagnosis, and it implies a different cure.

Pure scale asks for more mass.

Geometric structure asks for better form.

If the future of AI depends on reducing internal conflict, then form may matter more than mass far more often than we have been willing to admit.

And if that is true, then the next major gains in intelligence may come not from building bigger minds, but from building minds with cleaner geometry.

---

#### Subscribe to Richard’s Substack

By Richard Aragon · Launched 2 years ago

My personal Substack

Subscribe

By subscribing, you agree Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

[](https://substack.com/profile/507894262-miles-hawthorne)[](https://substack.com/profile/429233497-grim-life)[](https://substack.com/profile/431310544-computer-future)[](https://substack.com/profile/266933392-karin-rodrigues)

5 Likes∙

[1 Restack](https://substack.com/note/p-190686399/restacks?utm_source=substack&utm_content=facepile-restacks)

#### Discussion about this post

[](https://substack.com/profile/431310544-computer-future?utm_source=comment)

[Computer Future](https://substack.com/profile/431310544-computer-future?utm_source=substack-feed-item)

[Computer Future](https://computerfuture.substack.com/?utm_source=substack-feed-item&utm_content=comment_metadata)[Mar 22](https://richardaragon.substack.com/p/geometric-structure-vs-pure-scale/comment/231852674 "Mar 22, 2026, 10:56 PM")

have you considered applying your theories to the concept of "the universe is a computer" or "markets are computers" ?

i suspect you'd find Peter Thiel and Elon for example to be exceedingly geometric thinkers and path planners in the graph of social structures, technology, and time. you can probably quantify investors and all of capitalism in such models, eventually mapping the geometry and thus quantifying "strategy" vs "luck"

maybe warren buffett was giving luck too much credit in his Ovarian Lottery etc?

Like

Reply

Share

[](https://substack.com/profile/88347987-relja-segvic?utm_source=comment)

[Relja Šegvić](https://substack.com/profile/88347987-relja-segvic?utm_source=substack-feed-item)

[Mar 12](https://richardaragon.substack.com/p/geometric-structure-vs-pure-scale/comment/227007121 "Mar 12, 2026, 6:35 PM")

Very interesting experiments, I would like to add a concern about how most of the time we want the model to have overlap between tasks, especially when the tasks are much more complex. I think that because that overlap is basically compression.

So what bothers me is that the crux of AI currently isn't separating tasks, but getting the model to correctly decide what to separate and what to overlap.

I don't really understand what you are doing in the geometric model, but you said that the geometric model tends to separate "task-specific representations", which indicates to me that there is some general "teacher" subspace of the latent space, and than there are the 2 tasks, and if this is correct, it answers my question (and it might also explain the gap between artificial task separation and the geometric separation). I'd like to see more information about how geometric model is implemented.

I hope you like the comment.

Like

Reply

Share

[The Geometry Beneath the Weights](https://richardaragon.substack.com/p/the-geometry-beneath-the-weights)

[Why Latent Space Cartography Represents a Fundamentally Different Paradigm for AI Research and Why the Industry Cannot Easily Follow](https://richardaragon.substack.com/p/the-geometry-beneath-the-weights)

Feb 25 • [Richard Aragon](https://substack.com/@richardaragon)

11

4

1

![](https://substackcdn.com/image/fetch/$s_!CXUG!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F153b07f7-35fe-476a-8a34-7d662ec57d7e_1024x1536.png)

[The Geometry of Insight: A Guide to How AI “Groks” Reality](https://richardaragon.substack.com/p/the-geometry-of-insight-a-guide-to)

[In the early days of AI, we thought learning was about statistics—correlations between words or pixels.](https://richardaragon.substack.com/p/the-geometry-of-insight-a-guide-to)

Feb 19 • [Richard Aragon](https://substack.com/@richardaragon)

9

![](https://substackcdn.com/image/fetch/$s_!zSRP!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5564e22-0f90-4c3a-a2cb-057dcebc3776_1024x1024.png)

[The Day We Tried to Teach Aliens Geometry — And They Laughed at Us](https://richardaragon.substack.com/p/the-day-we-tried-to-teach-aliens)

[Why our entire mathematical worldview collapses the moment we meet an intelligent species that understands time correctly](https://richardaragon.substack.com/p/the-day-we-tried-to-teach-aliens)

Nov 18, 2025 • [Richard Aragon](https://substack.com/@richardaragon)

6

6

2

![](https://substackcdn.com/image/fetch/$s_!6Z-r!,w_320,h_213,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_center/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf6cd593-d5c2-4790-8525-5b814aef2e65_1536x1024.png)

### Ready for more?

Subscribe

© 2026 Richard Aragon · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)

[Start your Substack](https://your.substack.com/publish)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)

[Substack](https://substack.com/) is the home for great culture