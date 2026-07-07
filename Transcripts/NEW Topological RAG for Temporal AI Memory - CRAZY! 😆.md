# NEW Topological RAG for Temporal AI Memory - CRAZY! 😆

[![](https://yt3.ggpht.com/EocTonB0FyVFCLmoHoSBsCBtS4LutlIUQC7FdjY6e5Rfm5vQGEBgLIWGj9WkD73qxA1UZeO577Q=s48-c-k-c0x00ffffff-no-rj)](https://www.youtube.com/@code4AI)

[Discover AI](https://www.youtube.com/@code4AI)

88.4K subscribers

Join

Subscribe

214

Share

Ask

Save

Download

5,008 views May 19, 2026 [#topology](https://www.youtube.com/hashtag/topology) [#time](https://www.youtube.com/hashtag/time) [#airesearch](https://www.youtube.com/hashtag/airesearch)

Memory is highly volatile (Read-Write-Merge). A user says "I like Python" on Monday, and "Actually, I'm switching to Rust" on Friday. If you use a flat vector database, a traditional RAG will retrieve both statements equally and get confused. H-MEM (Memory RAG): NEW H-MEM solves this by using its Temporal-Semantic Tree. Memory requires understanding the exact relational topology of the user's life. NEW H-MEM extracts these entities into a Knowledge Graph, ensuring the RAG system can traverse explicit topological edges (multi-hop reasoning) rather than just guessing based on vector closeness. all rights w/ authors: H-MEM: A Novel Memory Mechanism for Evolving and Retrieving Agent Memory via a Hybrid Structure Jiawei Yu1, Yixiang Fang1∗ , Xilin Liu2, Yuchi Ma2 1The Chinese University of Hong Kong, Shenzhen 2Huawei Cloud Computing Technologies CO., LTD. arXiv:2605.15701 [#topology](https://www.youtube.com/hashtag/topology) [#time](https://www.youtube.com/hashtag/time) [#airesearch](https://www.youtube.com/hashtag/airesearch) [#artificialintelligence](https://www.youtube.com/hashtag/artificialintelligence) [#temporal](https://www.youtube.com/hashtag/temporal)


## Transcript

Hello community. So great that you are back. You may say this is the latest in EI memory for artificial intelligence.

Absolutely. We do have here AI memory but now with the additional complexity

here in time because what we want we want a temporal semantic structure here.

And if we have a query here, we build now fragments here and those fragments

interact at the same time with a temporal tree dynamic that we're going to build. And this is interwoven on sub

queries with a knowledge graph. You see here the activation of the node of the knowledge graph that are relevant for a

particular time slot here in our temporal tree structure. And then we bring it all together with a tiny little

bit of mathematics. And this is here really the very latest in AI memory

development. So ready set go. This is a beautiful new study by the Chinese

University of Hong Kong Shenzen and the Huawei cloud computing technology May 15, 2026. Hm. A novel memory mechanism

for evolving and retrieving agent memory via a hybrid structure. So they say we

have a problem now that cannot only we will build something a novel memory

structure that cannot only effectively model the evolution of the agent memory

over a long period of time and this is really here about long time periods. You know really robotic structures that you

have a conversation about 10 20 minutes but they also have build a structure

that is easy to retrieve. So this is now a rack system for memory. Let's have a

look at this. So how we build it? Today I also showed you we built here a temporal tree structure that we will

interwo we we will inter interact here a little bit the temporal and the semantic

complexity in a tree structure that allows you the short-term memory data to evolve progressively into the long-term

memory data where the later provides the summarized information about the former

and in the same time we have to build here a knowledge graph. So simultaneously we are constructing a

knowledge graph to capture here the relationship the edges between the entities here that are living in our

memory structure. So if you have a feeling that your memory becomes a little bit more complex a little bit

more dynamic and a little bit more mathematically oriented absolutely AI is

science and this paper shows it more than any other paper. So it offers an effective memory retrieval approach.

This is the bonus the cherry on top of the cake by exploiting here this particular hybrid structure that we're

going to build of the tree for the time and the graph for the relational structures. So let's have a look what we

have up until now. All the different methods you have here. They have an explanation how do they work. They are

vectorbased. Yes. They have a memory evolution. They have multihop reasoning capabilities. Yes. No. And you see the

very last line here is our new system HM. It's a hybrid of a tree and a graph structure. Structure based. They're

gentic vector-based. Has a memory evolution and has multihop reasoning for long reasoning traces for long

conversation. we are in here for this long problem here where all the other AI

models just crash and crumble and now they say hey we found a solution. So

let's have a look. So this is kind of a memory evolution here. This denotes you

the temporal window based consolidation from the short-term memory to the long-term memory summaries that are

created by OI. While the multihop reasoning denotes here an entity or relation level traversal across the

graph to different memory fragments that are also defined and harbored here by

our EI system. So careful this I saw at the beginning

if you just combine the indexes this is not something new now that I want to show you in a video but this is not it

is not a tree index that you just append to a graph index. It is really that we

do have a dynamic coupling of the temporal semantic memory evolution that

is now based with an entity centered multihop reasoning capability of the

memory. So you might say hey now it gets a little bit interesting no because we

have skills and skills. So we have here reasoning and interwoven skill

dependencies and now we go for the memory. It is not anymore a simple memory markdown fell.

So how do we build this? How can we do the coupling? The tree structure of HM organizes the memory data both

temporarily and semantically where each tree I showed you this in the video.

Each tree note retains here the memory information regarding a specific

semantic topic or even a subtopic but this is defined within a predefined time

window. Let's say this is my conversation with the eye on Monday or for a robot. This is the interaction

that is happening here in the time the robot is I don't know positioned in a kitchen. So we have semantic and time

here together. So each leaf node of our temporal tree structure stores now what

it is an event of the agent's original memory fragment a substructure with

reduced complexity containing now a semantic topic. Let's say a message in a conversation. Let's say maybe it's

physics or whatever generated at a particular timestamp while the upper level nodes store now

the memory summaries of some fine grained semantic topics in their lower

levels. This means converging their respective time windows.

So this is a little bit disappointing because here we just have a memory compactification. No, and we have

summaries. We have all the problems that we have with AI summary generation. But okay, let's go with this. This is what

the orers here go. Now to enable a memory evolution, it performs now a

temporal and semantic consolidation. And this is yet beautiful because think about we are working with two different

topological elements. On the one side we have a tree structure and on the other side we have a knowledge graph. So how

do they come together? So we are here in the tree structure. So today is given two tree nodes whose time windows are

very close and you see immediately what we are going to go in the same level if the semantic similarity between the

memory data exceeds here a predefined threshold. Now the semantic similarity you know from our vector store this is

nothing else than the cosine similarity and exceeds a predefined threshold. This is an absolute value that I say okay if

epsilon is greater than whatever then I would consider that this is here really

the sematic similarity is high and I have to take this into account. This means then the two tree nodes could

share here the same parent node whose memory summary now of the parent node

preserves now kind of hopefully the consolidated information of these two

nodes. So you see exactly we have a hierarchical memory building. Now a lot

of information of the very fine nitty-gritty detailed information can get lost in this way. Yeah. But let's

see how far we come with this particular idea. So we have here the temporal tree and it is also a cosine similarity

semantic closeness tree structure that allows not a short-term memory to evolve

progressively into a long-term memory. But we have both we have the complete time development and this is what why we

need to form. We couldn't do this in a graph structure but we can do some beautiful things in graph theory. A

graph structure of HMAP maintains now the knowledge graph of the entities and their relations their edges that are

extracted here from the memory data and normally not the old memory data but we will go with memory fragments here that

we split up the memory in some chunks like you know maybe here from vector uh from the classical rag here in the

vector stores here we have here memory data effectively recording the entity

centered information beyond the temporal order and capturing ing now multihop

relationship between entities that live on different memory fragments. So this

is what we need to graph for. We have different memory fragments here in different topological subspaces and now

we need this for our complex reasoning trace. If we have multi-hop

relationships and this goes now beyond the temporal order and now we have to bring them together because each

topological element or each topological subspace has some benefit to offer to us. The tree the time and the knowledge

graph simply the relational density here. So let's use both the tree and the graph

structures complement each other and this hybrid structure overcomes here the issue on relying on a single index that

is the current prevailing system here and the existing research on existing publications. So very nice. We have

something completely new. Not a single merging, not a single uh index

compactification. But we really use here the how say how

the beauty of the topology for the tree and the graph for their structures.

And what we is here the bonus as I told you includes an effective retrieval method. So how is this in the video you

saw that the the lightning bolt that comes down from the query it it dissipated in multiple channels. So same

idea here no give me a query Q it's first first step here decomposes the

complexity of a high complex query into lower complexity subqueries you know we

classical do this with almost everything and then we generate a retrieval workflow for each subquery.

Okay, split it up, make it little chunks that we can work with that we have the

complexity engines to deal with their particular task and then define the workflow for each one of them. So then

for each subquery it locates some original memory fragments and multihop

relevant entities in the graphs. So this is now again a kind of a search process

where we need the graph structure for. Yeah. Now could theoretically go

something wrong or we do not catch all the important um entities in the graph?

Yes, of course. But there's also a high probability working here with graph theory and with mathematics that we get

here I don't know let's say the most interesting other nodes the other sub

networks here on the graph that might carry here additional information. You will see this in the result how this

increases the performance compared to the classical methods. Okay. And afterwards it searches here the

relevant evidence from the tree in a bottom up manner. This is now that we jump over to the tree which is then used

for completing here the rack process for the memory the memory fragments and here

the complete compactification here to feed all this information just from the

memory into the context window of our LLM. I mean think about this. This is

amazing. If we have our query, everything goes down diverges. We have topological

structure evolving here between the tree structure and a graph structure in subn

networks that are just crazy, just amazing. But let's do this. Let's see what

happens if we go with this. So just to make sure where we are, we do have the classical rag pro process here from the

vector store you know I don't know five six seven years ago now where we have facts new data new knowledge here

because yeah the LLM needed new knowledge from what happened yesterday

then about two weeks ago I started to show you the rack process here if we have 10,000 skills on a whatever skill

bank here on the internet and Now you have to search for particular skills that are optimal that you need.

Hopefully the LLM knows that you need the skill number 12, 24 and 128 for your

particular job. So then you have the retrieve and augment process here from

the skill databases. And today now we have a new rack process for the pure

memory because you don't want to start your EI fresh from a blank sheet of paper. You want to have the conversation

that you had in the last 3 months with your AI system. So you need here the complete complexity of all your

discussion in the last 3 months that is now inscribed in the memory but in a way

that it uses not up all the available token in the context window.

Think about this. This is here our little context window. I thought about I imagined here it is a horizontal bar but

here you have Gemini build me here this image. It's a little box. Okay, let's go

with this. So what we have? We have our memory and MD file. Yeah. And then we

have all our instruction and we have here from the system ROM to the user whatever. Then we have let's say 10

skills that we downloaded here the markdown files. Then we have a process where we build from the skills adaptive

skills. We have some self-generating skills optimized for your particular job. So they stuck here on the memory

and the foundation and then you have a conversation and then you have further instruction and then you have further

sequences that you provide. Then you have few short examples in the context window and my goodness no it fills up

like crazy and 100% capacity full and we have not even started to harmonize the

representation of the memory with the complexity of the skills and I showed you in one of my last video that if you

find here a coherent representation in a mathematical space where those two work

beautifully together you can really compactify an excel accelerate here the reasoning process but more about this

later coming back to this paper of today HMM. So here you see it. We have here a

hybrid structure that is here if you want our knowledge network here our knowledge graph and then we have here

three structures building up and we have here the time component going here from the left side

to the right side and yeah this is a hybrid structure. So let's see we have the entities here in our knowledge

graph. Beautiful. Then memory summary is the exact opposite here. Okay here we

have the memory summary. We understand here everything that happened in the last 3 months from our conversation with

your personal AI system. Then we have a memory event you see here those here is

the particular time slot. Then we have the memory fragment that is stored in particular time slot here and this

constitutes if you want the short-term memory and then over aggregation and summarization and compactification

we built here over our temporal axis here the long-term memory. Beautiful.

As I told you, not a simple index add-on, a simple um construction here,

but they really have here a fine grained way how to build this up. So, they give

us here an example. We have a user here, beautiful and a lamp and lamb dishes

here and whatever and lamb stew. Okay, so the user says, I don't like lambs, so I order chicken instead. And the AI says

then I will avoid suggesting any further lamb dishes. Beautiful. So we have now

our if you want fragment use it on like a lamb user order chicken rice over lamp and whatever. So you see you just build

this up this complexity over the time over the relationship that you have in

your knowledge graph and over the fragment and the summarization here over the memory fragment and the short-term

memory elements. There is nothing complex about this in a mathematical

level. However, you will see the training this we have a lot of predefined hyperparameter. So we need a

lot of training to have here the complexity satisfied of the knowledge graph and the complexity of the temporal

tree structure. Okay. So officially we have the offline

indexing and you know this already we talked about this. Now this is the tree construct. So we build a temporal

semantic tree in an incremental manner. Assume that the tree has L levels where the leaf nodes are at the first level

and each level has two hyperparameters alpha level and beta level where alpha level is the similarity threshold

between the node and its child node. So you see we have here the linguistic complexity and the linguistic similarity

of our expression and betal is simply the size of the time window that we are

working here. time interval that we are recording here and we are calculating here and at each level L the newly

inserted node is now assigned to a corresponding temporal window. So this

is the way to do it with the size B2L according here to the time stamp and only the existing nodes within the same

temporal window and this is important are considered now as candidates for the

semantic consolidation. So this is the way to do it. So this means within this

temporal window now we compute pair wise semantic similarities between the newly inserted nodes and the existing lower

level nodes. So this is a very simple approach to handle this and now comes

the interesting part because you know at the same time in parallel we build the graph incrementally builds here the knowledge

graph. First it extract here the entities the places the persons all the relation between all the objects here

from each original memory fragment f that has been defined here at this level I second the extracted entities are

normalized and resolved into the entity nodes this is the classical um methodology that you know through here

whatever text normalization lamatization token overlap fuzzy string matching yeah I have a lot of videos here years ago on

this and if a resolved entity exactly matches an existing entity node and

their types are compatible, it is simply now merged into the node. You don't want to have a dduplication going on in your

graph. Otherwise, if it's new, if it's brand new, if it's interesting, new knowledge, it's kept as a new entity

node and some associated edges may be inserted and defined and have some

additional information. and we build up a complex topology given here the complexity of the domain that we're

working with. If you're working let's say in theoretical physics it might be a little bit more complex. It might be a

little bit not so easy to build if you work here just in social media and you

sort here the I don't know the food images of yesterday. Okay, this was the offline indexing and

now as I told you we have the bonus the jerry on the cake the online retrieval. This is now if you wanted to rag for

memory in my very simple simplification in my simple words. So given here query Q hm identifies relevant memory evidence

by searching now over this hybrid structure. So this is rag for memory we have the agentic rack of workflow over

the if you want memory manifold. Now the orers go with here a simplified

version. They go here with a retrieval planning. Okay. Then the evidence retrieval and the generation process. So

let's have a look. Now planning is clear. Now llm reasoner breaks here the complexity human query my query into

dependent subqueries here from K equal 1 to capital K. Crucially it classifies

here the required memory scope for each subquery either and this is here the simplest you can think of. No short. So

evaluate only leave nodes long evaluate only upper tier abstracted summaries or

you have mixed. So we have a classification and now we have the multihop graph expansion. So seed

entities are now extracted from our QK and matched here in the knowledge graph

and the system traverses now over all the edges to retrieve now a particular

semantic specifically linguistic relevant subgraph of topologically

relevant entities. There's nothing new. We all know how to

do this but the combination is absolutely fascinating. And then we have the bottomup tree search. No. So we have

now retrieved the entities from the graph. They are mapped back to the source fragments at the leaves of the

tree and using this as anchors the algorithm searches now upwards through

the temporal semantic tree constrained here by the short long scope to extract here the optimal mix of raw effects and

highlevel summaries. And hopefully, fingers crossed, the learning process of

this AI system was so brilliant from your training pre-training data and

after training data that this system really got the optimal mix of the raw

effects of the knowledge and of the highlevel summaries of your memory complexity that you built up over the

last three months. Tiny tiny little bit of mathematics.

Unfortunately, how you can build this, how you can do here your objective function, how you

can do the training of this system. Now, the simplest way honestly the simplest way you can do it is here you just add

here elements factors. So once the algorithm got us here candidate set of memory evidence, we have now what we

think we can put into the context window of our LLM. This is what the rack comes

back here from the wilderness and tell us look what I found. So it must now

rank and filter those chunks of memory elements into a final context window for

the generation for the generation LLM. So it scores now each piece of memory

against the particular subquery that from my master query that I defined as a human at the inference time t using now

an objective function. And this objective function has now three elements. And yeah, we have a theta 1, a

2, a three. These are simply hyperparameters that hopefully will be learned and will be optimized in the

learning process here. But what is really interesting is what are the elements that they add up here. So the

first is the semantic similarity. And you might say of course no this is the standard coen similarity between the

dense embedding representation of the memory and the query. This is what we do

with the normal rack when we have an incoming query and we have here some vector representation of I don't know

whatever it is 10,000 books and then we just go for a co similarity between the

embedding representation great this is s this is simple what is t and what is r

now t turns out the temporal relevance I told you we're looking here for the temporal development here of the memory

dynamics now this is rather complex here. So if the query Q subquery QK

contains a timebased constraint, it is mapped to a time interval L subK. The

candidate memory M spines now the time intervals L subm on temporal relevance

optimizes both the discrete intersection and the continuous translation between the intervals with this beautiful

mathematical formula. And we have epsilon here that prohibits here something mathematically to happen that

we don't want here. Beautiful. We have a formula for this. Great.

What else is missing now? Now missing is that you don't want to have noise that now really disturbs your system. So all

the irrelevant noise mmatmatically should fade out here after retrieval

pipeline. But at the same point you want that the most important information in

the memory complexity are now reinforced and are really brought back into the context of internet.

So you also want highly reinforced abstraction that they remain highly

ranked here in the vector space. So they are sure to make it here into your prompt. So they call it the order called

this here the memory robustness or and this function here if you want models

here the memory retention using a dynamically modulating forgetting curve.

Now forget about it. There are so many possibilities how to achieve this. You

have here a mathematically a function that if you want penalizes here the retrieval here of unreinforced memory.

So you have exactly what we set out to do. The irrelevant noise will mathematically fade out and highly

reinforced abstraction will remain dominant and transferred here to the context meter of our LLM. Beautiful.

Now the artist give us here their M configuration. I always like this. Now, the first I was a little bit

disappointed because they go with a GPD4 omni mini and a GPD 4.1 mini as a

backbone LLMs which I thought okay but then I thought okay never mind this is a

level where we have our tiny local I don't know 3B models here so let's go

with this and see if this methodology on this simpler GPD4 omni models really

provide an increase in the performance of those LLMs And they say for the semantic retrieval

and the evidence reranking the default configuration uses here the embedding here from Q13 and the Q13 reanker here

the 4B. Okay, you can go with any espert system that you prefer. Maybe I have

built for the physics my own embeddings and my own ranker and reranker but as you like and they have a lighter

configuration here with the embedding and the reranker not the 4 billion but the uh 0.6 six billion structure

whatever they go here with eight Nvidia or takes a 5000 GPUs each with 24 GB of

RAM. So this is here you can rent this in the cloud here. This is not so expensive. I think currently the price

for a cloud A5000 is about $2 an hour. So eight times you have an idea

benchmarks. Let's have a look at this. So on what do you evaluate this because

this is not interesting. uh this is now here some long-term agent memory benchmark. You really want to have a

long ongoing conversation or complexity here in a robotic task or whatever. And they decided to go here with two

standard locomo and long memory evaluation. And then the interesting thing, the closer to the

reality is real talk. But okay, so we have 1,500 question whatever here we have 500 question

standard. Beautiful. Let's do this. So yeah, GBD4 Omni Mini is it hurts but

okay. So whatever you imagine, imagine here a tiny little three billion local

LLM. You know I think this is about the same performance that you see how it optimizes and you go here from the old

methods here like me zero or me 3 m OS zap here and you see yes it really

brings an improvement and you see for H memory here almost here always here the

best performance here on the complete line and if you go with GBD 4.1 mini

you'll see okay there's a little bit of a fluctuation but also you have the bold numbers here on Hm. So for the benchmark

of locom beautiful it works here with let's say currently tiny mouse and it

really brings here an improvement. If you look at the overall accum um

accuracy here gives you a feeling where we are. We go from 60% to 70% to 77% to

85% and now here and imagine here this is for Omni Mini we are at 88%. So yeah,

this really kind of seems to work now. And here we have a GBD 4.1 mini. We go

here best was 90. Now we have 93 almost

the other benchmark here. Okay, you got it. What is really interesting is here real talk the the close to the real

situation. And if you see here the jump, yeah, it is still there. But yeah, you

see accuracy overall we go from 75 from 76% here to 78%. Okay, there is a little

tiny improvement. But do you know the complexity? If we have a a small

dimensional space for this, it's okay. So this means if we have to build a graph with just I don't know thousand

10,000 nodes, it's okay. But imagine you have to build here topological elements

or a knowledge graph with millions tens of millions of node and then you have to

build here the temporal trees also with a complexity. I think the computational

cost I have not done this but the computational cost I can imagine will be quite heavy. So all of this just to go

here two percentage points. So this is interesting but also think about what we

have here to do our context window of all the alm it is filling up before we

even start a conversation which should be here in this um face bundles but yeah

uh Gemini decided to make here something else. Okay whatever. Yeah, as I told

you, we have all the memory, all the system instruction, all the different skills that you need, all the coding,

all the language, all the reasoning complexities. No, and then the interval from dependency, the rag for the skills,

and now we have a rag for the memory complexity. Then we have the rag for databases, for

new facts, for knowledge. And then whatever a few short example you provide here and the context window fills up so

fast and then you have maybe a conversation of 1 2 3 4 5 days no and

then you have to have somehow a memory compactification because you want to go on over months in your work with your

work EI if you want. So I think we have not solved it at all. We just added

complexity. We added what we know how to do. We know how to do a knowledge graph.

We know how to build tree structures. And now we've used them together. Made

it a lot more complex for highdimensional data. It gets extreme intensive to calculate all of this. And

I think this will fill up a context window even I don't know of 250k or up maybe up to 1 million token here rather

fast before we even can start to work with this AI and we can provide here the complexity and all the instrument and

here the experimental data into the context window of the LLM. So I'm not

sure. I think this shows us that it's not the solution. And you said what is

the way out? And honestly I don't know. But I have some ideas and there are some research going on globally in China in

Japan in Korea all over the world in the US even in Europe. You're not going to believe this where people are kind of

aware of this complexity and they are trying to find a new solution to this

problem. Yeah. Because have I told you that all of this what we have here we even have not started to harmonize the

skills with the memory complexity on a topological element like a manifold structure as I have shown you in my last

three videos. No, this is still missing. We have not even touched it that we have to optimize these elements together to

bring in a coherent base element. No. Yeah, I think this would be all a topic

here for one of the next video. I hope you enjoyed it. I hope you had some new information. Would be great to see you

in my next video.