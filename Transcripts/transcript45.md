
> Kenneth Stanley [00:00:00]:
>   So it goes back to these observations from Pickbreeder, which is this picture breeding website where neural networks, which were a special kind of neural network called compositional pattern producing networks, were bred
> 
>   [00:00:15]
> 
>   or evolved by people to produce images. And this is a really unusual and exotic form of training that's very different from modern deep learning. It's completely different from it, which is 1 of the important points about it. And
> 
>   [00:00:30]
> 
>   so when people were able to actually breed interesting looking pictures, there's a lot of lessons we learned from that. Actually, the novelty search algorithm and things like that came from those lessons. But there was this 1 dangling lesson that, like, just hasn't gotten out, and that's
> 
>   [00:00:45]
> 
>   what this paper does. And that that lesson was that the representations, the underlying representations of these images, which are basically represented encoded by these neural networks are absolutely incredible amazing. And there was
> 
>   [00:01:00]
> 
>   like no good explanation for how they could be as good as they are. And we noticed this very early on that like they have unbelievable modular decomposition, which means that it's almost like it was engineered by a person. You know, it's like there's a there's there's a
> 
>   [00:01:15]
> 
>   network that that generates the image of a skull, and it the network has decomposed it such that, like, there's a component of the network that's responsible for the mouth. They can do things with the mouth, like open and close the mouth, or there's another dimension that can make the mouth smile. And
> 
>   [00:01:30]
> 
>   things like that which are not it's what's really amazing. It's not data driven. Like, we're talking about dozens of iterations in terms of, like, the amount of search that's involved to get a representation like this. And so I've always there's we've
> 
>   [00:01:45]
> 
>   had many discussions over the years, like, why why is the representation so amazing in these pick breeder images? Why does it have this unbelievable modular decomposition? And and and extremely efficient and compact. And so
> 
>   [00:02:00]
> 
>   1 thing that like at 1 point I did with Joel Lehman was we were kind of just playing around to see, like, well, what if we tried to get SGD to produce the same images? Like, what what would it be different internally? The the image the way that
> 
>   [00:02:15]
> 
>   it represents these images. And it was just dramatically different. But then we did nothing with that. Like, we just kinda, like, left it. We both Joel and I knew this thing, but we didn't really do anything with that information. But I've been just mulling it for years that, like, there's something there that's
> 
>   [00:02:30]
> 
>   really important That, like, with this weird kind of open ended search process, you get these incredible representations. And then with conventional, like, objective driven SGD, which is, the the backbone of all of machine
> 
>   [00:02:45]
> 
>   learning right now, you get a completely different kind of garbage representation, just total spaghetti. And we we we used we came up with some terminology that we put in the paper to to more, like, clearly articulate what these differences are. But basically,
> 
>   [00:03:00]
> 
>   you're talking about just amazing versus garbage. And so like the the question that the paper addresses is what does this mean? Which is something I think that has endless repercussions and potential implications. Like the fact that we're basing the entire
> 
>   [00:03:15]
> 
>   field on something that produces this complete garbage under the hood. And does this mean anything? Now I think if if you just saw this by the way, the fact that it's images makes it easier to see, like the the I mean, that the representation is garbage. Like
> 
>   [00:03:30]
> 
>   the fact that it's a network that produces 1 image. Because what that means is that we can visualize every single neuron, what subcomponent it's actually computing. It's very easy because it's just a single image. So it makes it very easy to see all at once how it actually computes the image, so we can see the internal
> 
>   [00:03:45]
> 
>   representations. And if I just showed you that for SGD, like if I said, here's a skull, I made this network, reproduce this skull, and the internal representation is crap. I think it would be not like hugely resonant in the field, because it'd be like, oh, it's not
> 
>   [00:04:00]
> 
>   super surprising that it's kinda hard to understand this like really complicated entangled representation. It's just emergent from how SGD climbs these gradients. But the thing that I think makes this really intriguing, the reason that the paper is because beyond just
> 
>   [00:04:15]
> 
>   that, is that it gives you something that otherwise could never exist, which is a counterexample, that there actually do exist networks that don't have that issue. You would think that that's just intrinsic to neural representation, that somehow they just look like kind of entangled
> 
>   [00:04:30]
> 
>   messes, and that's just the way life is. But clearly, it's not how life has to be. And so because we have now actual concrete examples from Pic Breeder that show beautiful internal representation. And so I think that the the paper's trying to get at what does that mean? Like, how how should we
> 
>   [00:04:45]
> 
>   interpret this? Should we perhaps aim for algorithms that actually do achieve these kind of, you know, really amazing kinds of modular decompositions? Or should we or
> 
>   [00:05:00]
> 
>   or should we just say, well, no, that's that's just not important. Let's just forget it and dismiss the fact that we know they exist. I think that would be that seems to be a pretty premature move to say that. So so there's something here, think, deep deep
> 
>   [00:05:15]
> 
>   lesson for us to learn in the field about internal representation, which just is totally off the radar. It's way way off the radar of anything that's being discussed. You know, mechanistic interpretability is not on the same page with what we're showing here. And
> 
>   [00:05:30]
> 
>   so, of course, it it can play a role in in further, like, interpreting this result. But this is a new thing to look at and for us to contemplate and try to understand what the implications are.
> 
> Host [00:05:42]:
>   Don't we just need to have humans in the loop? I mean, wouldn't it be great
> 
>   [00:05:45]
> 
>   if we could just have these evolving topologies, right, without humans? Wouldn't it be great if the systems could themselves learn the categories, the abstractions? And is it just a matter of missing data? Or is there just
> 
>   [00:06:00]
> 
>   a fundamental gap in capability?
> 
> Kenneth Stanley [00:06:03]:
>   Yes. So it's clear that part of the explanation for these amazing representations in pick breeder is that humans were in the loop. So
> 
>   [00:06:15]
> 
>   that's part of the explanation. But the question is what's the deeper lesson? Like, what did the humans do that caused this to happen? It clearly wasn't intentional. I mean, humans weren't thinking about the underlying representation at all. They're just choosing things they like. So why does that lead to this
> 
>   [00:06:30]
> 
>   virtuous type of representation? And I think, you know, there's 1 1 really interesting lesson that this shows is that it matters not just where you get, but how you got there. You know? And that that's like something missing right
> 
>   [00:06:45]
> 
>   now, you know, because we tend to just care where you get. Like, we look at the benchmark score, you know, in the field, and it's like, that's the result. It's doing really well. It just passed the Math Olympiad. But what if it matters how you got there? And you say, you could say, well, why does it matter how you got there?
> 
>   [00:07:00]
> 
>   If it performs well, it's like the same either way. And that's what the paper's all about, basically. Is that like, you know, you can have these 2 things, these 2 networks, they both output a perfect looking skull, exactly the same skull. 1 was found in this completely different open ended way with
> 
>   [00:07:15]
> 
>   people guiding the search. Another was found objectively through SGD. And so very different trajectories through the search space we're taking, radically different. And which means that under the hood is radically different representation. And so you say, well, what does it
> 
>   [00:07:30]
> 
>   matter then? What's the underlying representation? Well, it can matter a lot how you represent the world. And so so then, like, the question is with humans, like, is that the essential ingredient? And I think, can't be. It can't be that
> 
>   [00:07:45]
> 
>   it has like, the only way to get good representation is to have a human guiding the search. There's a deeper explanation. Like, why were the humans successful at getting to these amazing representations? And it has something to do with the underlying open ended nature of what they were doing.
> 
>   [00:08:00]
> 
>   Like, in other words, on the road to getting an image of a skull, they were not thinking about skulls. And so, like, when they discovered a symmetric object, like an ancestor to the skull, they chose it even though it didn't look like a skull,
> 
>   [00:08:15]
> 
>   but that caused symmetry to be locked into the representation. You know, from then on, symmetry was a convention that was respected as they then searched through the space of symmetric objects. And somehow this hierarchical locking in over time creates an unbelievably elegant
> 
>   [00:08:30]
> 
>   hierarchy of representation. And it's it's plausible, I think, at least for me, that there are algorithms that don't have humans that could take similar trajectories through search space. Maybe not quite as, like, perfect as the human trajectories. You
> 
>   [00:08:45]
> 
>   know, I I wouldn't be surprised if we can't actually hit that ideal, but there's probably a continuum where you could come closer. And then what are the implications? You know, if the order principles that lead to your final understanding of the world matters for
> 
>   [00:09:00]
> 
>   how you represent the world, and therefore for your ability to be creative in the future, then does it matter the order in which we allow these large models to encounter the different principles that they encounter on the road to total understanding
> 
>   [00:09:15]
> 
>   of everything in the universe. And I mean, I would guess, like, this implies probably yes. It probably matters, and that opens up a huge range of possible creative opportunities for alternative ways of thinking about training that would lead to
> 
>   [00:09:30]
> 
>   better representations.
> 
> Host [00:09:31]:
>   You brought in the open endedness aspect, which is fascinating, because you're saying they weren't looking for the skull. Right? So what were they looking for? They were, composing these primitive basis functions that they have in their mind so
> 
>   [00:09:45]
> 
>   they know that symmetry is good. Where did they get the symmetry idea from? Well, it must be somehow gleaned. And so actually our function space is restricted in some very important way. We know that we have certain things we can compose, and we know that we can compose them in certain
> 
>   [00:10:00]
> 
>   topologies, and we know that invariably if we follow that trajectory, we will land on interesting things, even though we don't necessarily know exactly what we will land on.
> 
> Keith Duggar [00:10:08]:
>   Mhmm.
> 
> Kenneth Stanley [00:10:09]:
>   Yeah. Yeah. That that that that's that's how this happened. I mean, the people people
> 
>   [00:10:15]
> 
>   in general have intuitions about potential, not just about where we are right now, but that this might lead to something. And in fact, it's very complex because, like, the more people play with pick breeder, the more they get intuitions about pick breeder itself. So they start to
> 
>   [00:10:30]
> 
>   understand what might lead to what what's promising, which is different than what's aesthetically pleasing in in the moment. And so that they're they're they're both enjoying the image and predicting, like, well, where might this go? And it's not like they're predicting they're gonna get a skull, but they're predicting
> 
>   [00:10:45]
> 
>   symmetric things are really interesting and beautiful, and and and let's see what other kinds of symmetries come out of this, like they're thinking that. And so that helps to to get this kind of virtuous ordering, which causes like a a sequence of lock ins of different conventions
> 
>   [00:11:00]
> 
>   of of increasing complexity, which then creates this, like, amazing representation underneath the hood. But I wanna I wanna point out though that, like, this view of the world is so radically different from the data driven view that we live in right now.
> 
>   [00:11:15]
> 
>   You know, it's what's what's really fascinating to me about it is not data driven. Like, you know, we we think about, you know, when you say, like, eventually, if you experience enough of the world, like you say, of course, you might expect that your representation start to mirror just the way that the world is.
> 
>   [00:11:30]
> 
>   And you get this kind of isomorphism maybe between, like, the the the the organization of your brain and the organization of outside reality. Well, that's a data driven view, like, in basically almost everything we think about is data driven. I mean, the bitter lesson is sort of like a data driven
> 
>   [00:11:45]
> 
>   philosophy. But, like, this is, like, what's so interesting is this is totally contra bitter lesson. You know? Because like what you're saying here is like, we see almost nothing of the world, like, PickReader knows nothing of the world. There's no pre training at all.
> 
>   [00:12:00]
> 
>   Start with some blobs. Over a few dozen iterations, I mean, dozen is crazy. Like, it's like peanuts. Like, we're used to millions, billions, like, we we don't do dozens. That's not what we do in our field. But here we have dozens of iterations, not enough to be exposed to almost anything.
> 
>   [00:12:15]
> 
>   It actually somehow finds within this can newly constrained space of dimensions that has been discovered by humans, things like the difference between opening and closing a mouth or smiling and not smiling. And
> 
>   [00:12:30]
> 
>   like those dimensions exist now in this space of the network, but not because of data. They're whole cloth de novo discoveries, which are not data driven. So there's no bitter lesson. It's just out of nothing. And there's
> 
>   [00:12:45]
> 
>   even more crazy ones. Like, there's, like, like, the apple 1, which is in the paper. It's in the appendix. This apple has this unbelievable weight, a single weight in the apple representation, which is a single continuum that if you move along that continuum, you swing the stem of the apple back and forth, like,
> 
>   [00:13:00]
> 
>   from left to right. Maybe someday we'll put an animation over this so we could show like, I could give you the animation. But you can see the swinging stem is 1 dimension, and it's it's like three-dimensional. You know? It's not just like a 2 dimensional thing. Like, it moves like you would expect in a rotation in
> 
>   [00:13:15]
> 
>   three-dimensional space. It has a shadow underneath it. It's like a green leaf. The underlying apple, which is a symmetric object, is not disturbed at all. It's totally independent. It's been decomposed. And then there's this 1 thing which is the stem swinging. And so, you know, what I'm saying is it's
> 
>   [00:13:30]
> 
>   absolutely incredible. It's mind blowing that if you think about that as a world model, like, it's an actual true hypothesis about the world. This is the way that stems look when they swing. But this model has not been trained on anything in the world. It's never seen swinging
> 
>   [00:13:45]
> 
>   stems, let alone apples at all. I can almost guarantee you that in the training trajectory itself, there was no swinging of the stem. After all, if the stem started swinging, that would mean it already had that ability. So it's just circular to argue that.
> 
>   [00:14:00]
> 
>   This is just something that arose out of the fact that the that the representation is so elegant that it somehow has an internal hypo I think of it as a hypothesis about the world, which is correct. And you have to ask yourself, how many of our hypotheses are like that
> 
>   [00:14:15]
> 
>   instead of data driven hypotheses? Because we do sometimes have these unbelievably elegant underlying representations of the world that often are unique. Unique to an individual, not necessarily universal across human beings. Like, everyone's representation is unique. And so this is a
> 
>   [00:14:30]
> 
>   totally different way of thinking about representation and knowledge and how it comes to be.
> 
> Host [00:14:37]:
>   Yeah. And the thing I'm trying to understand is we can agree that humans have this incredible abstract
> 
>   [00:14:45]
> 
>   model of the world. We have a language of thought, and the way we understand things is through these compositions, these topological compositions of these little basis functions. Right?
> 
> Kenneth Stanley [00:14:59]:
>   Yeah. I
> 
>   [00:15:00]
> 
>   mean, I think it's true that Picrear is a kind of psychology experiment. That that is a dimension of what we're seeing. And it's true that intelligence and compression are often equated and they clearly have relationship. I I think in the in the paper, we we talk a bit about this and and even speculate that,
> 
>   [00:15:15]
> 
>   you know, that there may be something more to say than just compression, you know, in the sense of, like, the the factored aspect, how you factor matters. It's not just that it is compressed. You know, it's like if I know that a face is composed of eyes and nose and a mouth, and actually factor
> 
>   [00:15:30]
> 
>   those out, Even if you had a greater compressed version of the face that didn't factor those out, would prefer the factored version. That's still, in some sense, better. You see, then I can, you know, generate new faces in in a principled way. So I'm not I'm not
> 
>   [00:15:45]
> 
>   sure that it's always, the maximally compressed version is, like, the most so called intelligent, depending what we mean by that. There's there's multiple factors to consider, but, obviously, compression is a virtue, you know? And so this is extremely inefficient, like, representations
> 
>   [00:16:00]
> 
>   that that you see in just like a regular SGDs. It's obviously that's part of the problem. And so I think though that, like, speaking about the the human aspect of it, just to go back to that
> 
>   [00:16:15]
> 
>   for a second. It's just 1 1 thing that I think is important to to think about is just that you can extrapolate outside of pick breeder, like this this principle of searching through regularities or or finding good
> 
>   [00:16:30]
> 
>   isomorphisms with the world in some kind of sequence. Like, that's a just general way that people do discovery. So in the sense, like, the so in other words, it's not just in in this kind of, like, very almost psych test, like, environment that that kind of stuff
> 
>   [00:16:45]
> 
>   happens. Like, that's just a general aspect of human exploration, intellectual exploration. And so when we do that, you know, you can imagine like the difference between somebody who learns calculus from a textbook versus someone who invents it for themself because they were curious.
> 
>   [00:17:00]
> 
>   But they both end up knowing the same thing, you know. So they both take the test and they both get a good score on the test. But it's just pretty obvious that the person who found it through their own independent exploration is probably gonna be doing much more interesting math, like, after that test. But
> 
>   [00:17:15]
> 
>   why? It's because, like, they they went through a pick breeder like exploration process. Of course, this is easier said than done. Most people won't do that. But it's just like the way that you got there matters a lot, like all throughout life.
> 
> Host [00:17:26]:
>   If we did have a large language model that could understand
> 