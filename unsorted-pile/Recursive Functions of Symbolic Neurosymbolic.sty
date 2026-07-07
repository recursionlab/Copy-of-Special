



-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
- id: alford2024-neurosymbolic-abstraction
  title: "A Neurosymbolic Approach to Abstraction and Reasoning"
  author: "Simon Alford"
  year: 2024
  type: preprint
  notes: "Neurosymbolic framework for ARC-style tasks"
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

A Neurosymbolic Approach to
 Abstraction and Reasoning
 by
 Simon Alford
 B.S. Mathematics and Computer Science and Engineering
 Massachusetts Institute of Technology, 2020
 Submitted to the Department of Electrical Engineering and Computer Science
 in partial ful llment of the requirements for the degree of
 Master of Engineering in Electrical Engineering
 and Computer Science
 at the
 Massachusetts Institute of Technology
 June 2021
 ©Massachusetts Institute of Technology 2021. All rights reserved.
 Signature of Author: .............................................................
 Department of Electrical Engineering and Computer Science
 Certi ed By: .....................................................................
 Tomaso Poggio
 Eugene McDermott Professor in the Brain Sciences
 Thesis Supervisor
 Accepted By: ....................................................................
 Katrina LaCurts
 Chair, Master of Engineering Thesis Committee
 1
A Neurosymbolic Approach to Abstraction and
 Reasoning
 by
 Simon Alford
 Submitted to the Department of Electrical Engineering and Computer Science
 on May 20, 2021 in partial ful llment of the requirements for the degree of
 Master of Engineering in Electrical Engineering and Computer Science
 Abstract
 Current deep learning systems are highly specialized to whatever task they are de
signed to solve. Their application to more general domains is limited by their inability
 to form explicit, systematic knowledge and reason over it. Such an ability would be
 required for a machine to, for instance, rediscover the scienti c method, and use
 this method to learn new things. This thesis attempts to make progress on this
 front by developing an approach for the Abstraction and Reasoning Corpus (ARC),
 an arti cial intelligence benchmark consisting of a set of few-shot visual reasoning
 tasks which measures the ability for an agent to solve tasks beyond those speci ed
 by the developer. We present two approaches that address that challenges posed
 by ARC. First, we give an approach for learning abstractions on ARC. We apply a
 program synthesis system called DreamCoder to create symbolic abstractions out of
 the solutions of tasks solved so far. These abstractions enable the solving of progres
sively more di cult ARC tasks. Second, we design a reasoning algorithm for ARC
 motivated by the way humans approach solving ARC tasks. Our algorithm com
bines execution-guided program synthesis with deductive reasoning based on inverse
 semantics, enabling a bidirectional, execution-guided program synthesis algorithm
 for solving ARC tasks. Despite di culty ultimately achieving high performance on
 ARC, we believe the approach is a rm basis for a learning-based search algorithm
 for ARC, especially compared to existing brute-force approaches. We additionally
 evaluate the bidirectional algorithm on a set of 24 Game style math puzzles. We
 conclude by discussing how these two approaches can be combined as well as future
 research directions relevant to ARC and AI in general.
 Thesis Supervisor: Tomaso Poggio
 Title: Professor
 2
Contents
 Acknowledgements 5
 1 Introduction 6
 2 TheAbstractionandReasoningCorpus 10
 2.1 ChallengesofARC . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
 2.2 SolvingARC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
 3 Abstraction 12
 3.1 DreamCoder . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
 3.2 EnablingGeneralizationthroughCompression . . . . . . . . . . . . . 14
 3.3 EnablinggeneralizationonARCsymmetrytasks. . . . . . . . . . . . 15
 3.4 Neural-guidedsynthesis. . . . . . . . . . . . . . . . . . . . . . . . . . 16
 3.5 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
 4 Reasoning 19
 4.1 Execution-guidedProgramSynthesis . . . . . . . . . . . . . . . . . . 21
 4.2 Deductivereasoningviainversesemantics . . . . . . . . . . . . . . . 23
 4.3 Bidirectional,Execution-guidedProgramSynthesis . . . . . . . . . . 24
 4.4 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
 5 Discussion 31
 AAppendix 33
 A.1 AbidirectionalgrammarforARCtasks . . . . . . . . . . . . . . . . . 33
 A.1.1 Listoperations . . . . . . . . . . . . . . . . . . . . . . . . . . 34
 A.2 Code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
 3
ListofFigures
 1 FailureofMLPstogeneralizeoutsidetrainingrange . . . . . . . . . 7
 2 ARCexampletask . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
 3 ARCabstractionexamples . . . . . . . . . . . . . . . . . . . . . . . . 13
 4 ARCreasoningexamples . . . . . . . . . . . . . . . . . . . . . . . . . 13
 5 Sampletasksinvolvingapplyinganactiontowardstheleft . . . . . . 15
 6 Learnedsymmetryabstractions . . . . . . . . . . . . . . . . . . . . . 17
 7 Challengingfour-waymirrortask . . . . . . . . . . . . . . . . . . . . 17
 8 Neural-guidedsynthesis. . . . . . . . . . . . . . . . . . . . . . . . . . 18
 9 ARCtasksinvolvingdenoisingandreasoning. . . . . . . . . . . . . . 19
 10 Task173 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
 11 Task303 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
 12 ARCexecution-guidedwalkthrough . . . . . . . . . . . . . . . . . . . 22
 13 Exampleinverseandconditional inverse . . . . . . . . . . . . . . . . 23
 14 ARCsymmetrytasksusedinbidirectionalexperiment . . . . . . . . 29
 15 Task148 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
 16 Task168 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
 17 Task10bidirectionaldemo. . . . . . . . . . . . . . . . . . . . . . . . 37
 ListofTables
 1 PrimitivesusedtosolveARCsymmetrytasks. . . . . . . . . . . . . . 28
 2 Percentoftaskssolvedfor24Game . . . . . . . . . . . . . . . . . . . 30
 3 24testtaskresult . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
 4
Acknowledgements
 There are many individuals who deserve recognition for their contributions to this
 thesis. Thank you to Professor Tomaso Poggio for agreeing to take me on as a
 masters student and for providing the vibrant community in which I could pursue
 research. Thank you to Andrzej Banburski, my amazing direct advisor, who has
 helped me discover and explore my research interests and is a constant source of
 animated research conversations.
 Thank you to Anshula Gandhi, Akshay Rangamani, and Tony Wang for their
 contributions to the ARC project. Anshula and I worked side-by-side for the majority
 of the project. She contributed to practically every part of it working with her was
 a joy. Akshay helped with bidirectional project, implementing network training,
 nding hyperparameters, and providing much-appreciated organizational guidance.
 Tony also helped with the bidirectional project, implementing reinforcement learning
 and many general system contributions. His programming and research wisdom had
 a large impact.
 Thankyoutothe students Sylee Dandekar, Subhash Kantemneni, Faduma Khalif,
 and Noa Korneev, who helped program various aspects of the project and who I
 enjoyed working with tremendously. Thank you to Peter Chin, who helped advise
 and organize the project. Thank you also to Kevin Ellis, whose research is a large
 inuence and inspiration for the present thesis and who has graciously discussed
 many research ideas with me. Lastly, thank you to my family, especially my parents
 for supporting me throughout MIT, and my grandparents for cultivating my scienti c
 future.
 5
1 Introduction
 What would it take to develop generally intelligent machines? The growth and
 tremendous success of deep learning has catapulted us past many benchmarks of ar
ti cial intelligence. Reaching human and superhuman performance in object recog
nition, language generation and translation, and complex games such as Go and
 Starcraft have pushed the boundaries of what humans can do and machines cannot
 [12, 9, 5, 14, 17, 21]. To continue to make progress, we must isolate and tackle the
 ways in which humans remain superior to machines.
 One feature shared in common among the machine learning systems listed above
 is notably de cient to humans: they all in many aspects remain highly specialized
 for a speci c task, and excel only in the domain they are designed to operate in a
 sharp contrast to humans. Now, it is not the underlying neural network architectures
 which meaningfully di er from task to task. The feedforward structure of networks
 and their functional role is essentially shared between all tasks. Indeed, the successful
 application of language-model architectures to computer vision tasks and vice versa
 is a reassuring sign that task-to-task variance of minute network architectural details
 is not likely to be a roadblock to developing more general-purpose systems down the
 road.
 Instead, task-speci c specialization inhibitive to general applicability occurs in
 what might be designated the symbolic, rule-based behavior of the systems. For ex
ample, AlphaZero, DeepMinds AI for playing chess and go, uses a standard residual
 convolutional network to predict good board positions and combines this with a form
 of Monte Carlo tree search [17]. The network weights are learnable, but the search
 strategy is essentially xed. As another example, a SAT solver might be provided to
 assist a neural network with solving Sudoku puzzles[22]. This solver knows from the
 start how to work; the only learning takes place in the neural network. Importantly,
 these symbolic parts of the systems di er depending on the task.
 Why not have neural networks directly learn this aspect of the system as well?
 Unfortunately, despite their successes, neural networks have been found to struggle
 at tasks involving systematic, rule-based behavior. While e ective at learning to
 6
recognize patterns in data, networks do so in a way which fails to generalize outside
 the distribution of data on which they are trained. For example, one can train a
 recurrent neural network to classify the parity of a binary string (0 if the string con
tains an even number of ones, 1 otherwise). Given a maximum training string length
 encountered during training, the network is generally able to classify all training
 examples accurately, but upon testing with string lengths beyond those encountered
 during training, the network fails[20, 24, 13]. An even more striking version of this
 behavior can be seen in the following plot taken from [20], which shows how sim
ple three-layer multi-layer perceptrons fail to learn a simple identity function in a
 manner which generalizes beyond the training distribution.
 Figure 1: Outside the training range, error rapidly increases from zero for a neural
 network using a variety of activation functions. Taken from [20].
 This weak spot hinders the ability of neural networks to learn tasks involving
 systematic behavior such as counting, arithmetic, problem-solving, and more in a
 way which generalizes outside the training distribution. Whereas a human knows
 rules which allows them to count arbitrarily high, or add arbitrarily large numbers,
 a neural network is limited to what it has seen before it can not extrapolate to new
 data. One may ameliorate the issue by extending the range of training data, but
 this approach can only go so far. Consider GPT-3, a 175-billion-parameter natu
7
ral language model[2], which astonished the community with its ability to generate
 hyperrealistic text. Despite containing more parameters than the human brain has
 neurons and being trained on a large swath of data from the internet, GPT-3 can
 add two digit numbers with 100% accuracy, but ve digit numbers with only 10%
 accuracy. Simply increasing the amount of training data and the size of the network
 does not appear to feasible if one wishes to solve a large variety of symbolic tasks
 e ectively.
 For another example, we can consider Conways Game of Life, a cellular automa
ton where cells in a grid update their state to black or white based on the state of
 their neighbors. If we provide a network with the systematic rule for predicting
 the state of a future cell that a cells state at time t+1 depends only on the neigh
boring cell values at time t the problem is trivial for a neural network to learn, as
 it involves learning a lookup table for possible con gurations of eight Boolean cells.
 However, if instead we task a convolutional network with predicting the next state
 for an entire grid at once, without the rule, then networks fail to converge to an
 accurate prediction that properly generalizes to arbitrary grid sizes[19].
 One way to look at this failing of neural networks is that they are simply mem
orizing the training data. Symbolic reasoning, in contrast, consists of rules which
 can be applied outside the distribution: a memorized solution to addition consists of
 a cleverly represented lookup-table, while a symbolic solution consists of an explicit
 procedure which adds digit-by-digit, keeping track of the carry value as it goes a
 procedure which generalizes to arbitrary input lengths. This is how humans solve
 symbolic tasks, and there is reason to believe AI agents need to acquire this ability
 to learn such procedures if they are to succeed on symbolic tasks.
 A striking characterization of the interplay between symbolic reasoning and the
 pattern recognition done by neural networks is described in dual-process theories of
 reasoning[18, 8, 11] which suggest that our abilities stem from the interaction between
 a fast, associative system (similar to that of modern deep nets) and a slower symbolic
 system. Neural networks excel at conducting associative reasoning, but are not suited
 to conducting rule-based reasoning in their computations. Current systems fail at
 systematicity and generalization, having an inability to form declarative, systematic
 8
knowledge and reason over it to solve new problems. Such an ability would be
 required for a machine to, for example, rediscover the scienti c method, and use this
 method to learn new things. As such, it is an important problem to address in the
 design of more generally intelligent systems.
 How might we combine learning of symbolic rules with machine learning to pro
duce more capable arti cial intelligence systems? This thesis attempts to make
 progress in this direction. To begin to solve this large challenge, it is helpful to have
 a benchmark that appropriately measures the ability we are seeking. Importantly, it
 must be designed in a way to prevent developers from hard-coding the knowledge into
 the system 1. The Abstraction and Reasoning Corpus, developed by Francois Chollet
 and henceforth referred to as ARC, is an excellent test of this type of learning.
 Wepresent two approaches for solving ARC tasks designed to aid in both abstrac
tion and reasoning. In Section 2, we describe the Abstraction and Reasoning Corpus.
 We discuss the relevance of the corpus of tasks with respect to the challenges put
 forward above, and outline existing work on the dataset. In Section 3 and Section 4,
 we develop two approaches and sets of results on ARC. The rst approach involves
 learning abstractions of symbolic concepts out of the solutions of tasks solved so far
 using a program synthesis system called DreamCoder. However, the type of search
 DreamCoder uses to discover solutions is weak and does not scale to solving general
 ARC problems. To address this, the second section develops a reasoning approach
 for ARC motivated by the reasoning humans exhibit when discovering solutions to
 ARCtasks. Our approach combines execution-guided program synthesis with deduc
tive reasoning based on inverse semantics, enabling a bidirectional program synthesis
 algorithm for ARC. We present preliminary results on ARC problems with this ap
proach, as well as application to a simpler domain of solving tasks from the 24
 Game family of puzzles. We conclude in Section 5 by discussing how these two
 approaches can be combined as well as future research directions relevant to ARC
 and AI in general.
 1This is not as much of an issue for benchmarks involving object recognition, language generation,
 etc. where hard-coding a recognizer yields poor performance. In contrast, systematic tasks are by
 nature easier to program.
 9
Figure 2: An example ARC task with three shown training examples and one test
 example. The solution might be described as nd the most common object in the
 input grid .
 2 The Abstraction and Reasoning Corpus
 In 2019, Francois Chollet released a paper On the Measure of Intelligence [4]. In it,
 Chollet argues that intelligence must be measured not as skill in a particular task, but
 as skill-acquisition e ciency. General intelligent systems must also have developer
aware generalization, meaning they can learn to solve problems the developer of the
 system has not encountered before or anticipated. As part of the paper, Chollet
 introduces the Abstraction and Reasoning Corpus, a benchmark he created in line
 with his view of measuring intelligence.
 ARC consists of a training set of 400 tasks, an evaluation set of 400 tasks, and
 a private test set of 200 tasks. Each task consists of a 24 training examples and
 one or more test examples. Each training example is an input/output pair of grids.
 To solve a task, an agent must determine the relationship between input and output
 grids in the training examples, and use this to produce the correct output grid for
 each of the test examples, for which the agent is only given the input grid.
 Importantly, the tasks are unique and constructed by hand so as to prevent
 reverse engineering any synthetic generation process. In addition, they are designed
 to depend on a set of human Core Knowledge inbuilt priors such as the notion of
 10
objectness, simple arithmetic abilities, symmetry, or goal-directedness.
 Chollet hosted a Kaggle-competition and the winning solution, a hard-coded
 brute force approach, achieved only 20% performance on the private test set [1].
 At the time of writing, we are not aware of any improvements upon this mark.
 2.1 Challenges of ARC
 The Abstraction and Reasoning Corpus has a number of features which make it
 quite a challenging benchmark. To start, since each task is a few-shot problem
 whose solution is symbolic and mostly rule-based, neural networks are extremely
 poorly equipped for the benchmark. Second, the tasks in the private test set are
 not from the same distribution as the tasks in the training set. This prevents a
 developer from succeeding by hard-coding a program that can solve tasks in the
 training set unless that program learns to do so from the training set itself, or does
 so based on some sort of universal problem-solving technique that is not tailored to
 the observed idiosyncrasies of the training set. Last, the search for a solution to a
 task may be easy for humans, but for any rule-based approach, the search quickly
 explodes exponentially in a way which is infeasible without close supervision.
 2.2 Solving ARC
 As laid out in the paper, ARC is best thought of as a program synthesis benchmark.
 The most straightforward way to approach solving a task is to seek to write a pro
gram that converts the input grid to the output grid for each training example, and
 then evaluate this program on the test input grids. This is the general framework
 we will assume. Such an approach starts with a Domain Speci c Language of use
ful functions in this case, the DSL could be based on the Core Knowledge priors
 that form the foundation of ARC. These functions are then combined to produce
 programs. For example, the solution to the task in Figure 2 could be written in
 Pythonic style as
 f(in) = get_first(sort(map(objects(in),
 11
lambda obj: freq(obj, objects(in))))
 or more simply as f(in) = most_common_element(get_objects(in)). There is
 a trade-o here: starting with a universal (fundamentally, all we need is Turing
completeness) set of functions ensures any task solution is expressible, but solution
 programs may be so long that any search for them is prohibitively expensive. On
 the other hand, introducing specialized functions to reduce the description length of
 solution programs may not generalize well to the test set.
 To ensure the rigor of the benchmark, Chollet organized a Kaggle competition
 around it. The winning solution used a brute-force approach which solves roughly
 60% of the training tasks but only 20% of of the private test tasks[10]. To this day,
 this solution remains state of the art. In the words of the winner, Unfortunately, I
 dont feel like my solution itself brings us closer to AGI .
 As one might expect, two important components underlying a proper solution to
 ARC are the ability to conduct abstraction and reasoning. We brie y showcase this
 through a few examples. Figure 3 demonstrates the way concepts are introduced and
 developed through interrelated tasks. Figure 4 shows a task whose solution requires
 multiple steps of reasoning to uncover.
 In what follows, we will design approaches that address these two necessary com
ponents.
 3 Abstraction
 Our rst approach to ARC addresses the central desire of our system: the ability
 to learn symbolic rules from data. To do so we use DreamCoder, a recent tool for
 program synthesis [7]. What follows consists of essentially applying DreamCoder as
 designed to ARC without any signi cant modi cations. We show that it is well
suited to solving ARC tasks, and crucially enables the ability of learning the types
 of abstractions found in ARC.
 12
Figure 3: Abstraction: the concept of in ation and de ation is rst introduced
 in an isolated task before being combined with other concepts (symmetry, denoising)
 in more challenging tasks. To solve the harder tasks, an agent must learn concepts
 from the simpler tasks. Each task only shows a single training example for brevity.
 Figure 4: Reasoning: this challenging task 65 cannot be solved without a sort of
 step-by-step reasoning towards a solution. Reasoning on ARC is discussed further
 in 4. Can you solve it?
 13
3.1 DreamCoder
 DreamCoder is a program synthesis engine; it solves tasks by learning to write pro
grams which convert, in this case, the input grid into the target grid. As it solves
 tasks, it learns new abstractions through compression , an algorithm which distills
 higher-level functions out of existing task solutions. This allows DreamCoder to solve
 new tasks that it would not have been able to solve with its original library. Dream
Coder also trains a neural network to learn to recognize which functions are most
 likely to solve a given task. Together, compression and neural-guided synthesis allow
 DreamCoder to gradually acquire expertise in an area. For example, it rediscovers
 laws of classical physics (including Newtons and Coulombs laws) from much simpler
 functions, by compositionally building on concepts from those learned earlier.
 As a simple example, given only an addition function, DreamCoder can learn to
 solve multiplication tasks through repeated addition. Then, during compression,
 it refactors these multiplication programs to express them in terms of a higher-level
 multiplication function. This new function can be used to solve more di cult tasks
 such as calculating exponents or factorials.
 3.2 Enabling Generalization through Compression
 The compression component of DreamCoder is crucial to our program synthesis
 approach. After each iteration of attempting to solve ARC tasks, our agent looks
 at all of the correct programs, notices structures that were similar between di erent
 solved programs, and then re-writes new, higher-level programs based on lower-level
 programs.
 Compression enables our agent to learn new techniques and behaviors based on
 the tasks it is solving, rather than being limited to the tools the developer provided
 it with. This type of generalization ability is at the heart of the ARC challenge 
creating a machine that quickly learns to solve problems its developers might not
 have anticipated.
 We demonstrate how the synthesizer can create more abstract concepts from ex
isting ones in the following experiment. First, we supply our agent with six synthetic
 14
tasks (meant to be similar to ARC tasks): drawing a line in three di erent directions,
 and moving an object in three di erent directions. The programs synthesized are
 the following:
 (lambda (rotate_cw (draw_line_down (rotate_ccw $0)))) // draw line left
 (lambda (rotate_cw (move_down (rotate_ccw $0)))) // move object left
 (lambda (rotate_ccw (draw_line_down (rotate_cw $0)))) // draw line right
 (lambda (rotate_ccw (move_down (rotate_cw $0)))) // move object right
 (lambda (rotate_cw (rotate_cw (draw_line_down (rotate_cw (rotate_cw $0)))))) // draw line up
 (lambda (rotate_cw (rotate_cw (move_down (rotate_cw (rotate_cw $0)))))) // move object up
 After running the compression algorithm, the agent creates these new abstrac
tions:
 (lambda (lambda (rotate_cw ($0 (rotate_ccw $1))))) // apply action left
 (lambda (lambda (rotate_ccw ($0 (rotate_cw $1))))) // apply action right
 (lambda (lambda (rotate_cw (rotate_cw ($0 (rotate_cw (rotate_cw $1))))))) // apply action up
 (a) An example draw line left task
 (b) An example move object left task
 Figure 5: Sample tasks involving applying an action towards the left
 Thus, instead of our agent developing tunnel-vision and just becoming more and
 more suited to doing certain kinds of trained tasks, it is able to generalize knowledge
 and can then apply this knowledge to other tasks completely unrelated to drawing
 lines or moving objects.
 3.3 Enabling generalization on ARC symmetry tasks
 In a second experiment, we demonstrate how compression-based learning enables
 developer-aware generalization on the ARC dataset. We provide DreamCoder with
 a set of ve grid-manipulation operations: ipping vertically with vertical_flip,
 rotating clockwise with rotate_cw, overlaying two grids with overlay, stacking two
 15
grids vertically with stack_vertically, and getting the left half of a grid with
 left_half. We then train our agent on a subset of 36 ARC training tasks involving
 symmetry over ve iterations of enumeration and compression. During each iteration,
 our agent attempts to solve all 36 tasks by enumerating possible programs for each
 task. It then runs compression to create new abstractions. During the next iteration,
 the agent tries to solve all tasks again within the same amount of time but equipped
 with the new abstractions. In this experiment, our agent solves 16 tasks before any
 training. After one iteration, it solves 17 in the same amount of time. After another,
 it solves 19 tasks, and after the nal iteration, it solves 22.
 After each iteration, our agent learns new abstractions which help it solve tasks
 that were previously too di cult. Thus, the DreamCoder compression framework
 enables our agent to learn interpretable, compositional abstractions not provided by
 the developer, such as ipping horizontally, rotating counter-clockwise, and stacking
 grids horizontally. It uses these new abstractions to solve progressively harder tasks.
 The most di cult tasks solved involve mirroring the input grid four ways, requiring a
 synthesized program which is extremely long when expressed in terms of the original
 functions. Such a program would be very di cult to discover without compression
 due to its length and the exponential nature of program search.
 This experiment shows a promising path towards the developer-aware generaliza
tion required to succeed on the ARC dataset. In order to solve unknown tasks in the
 test set, our agent will need to learn from the tasks themselves. As shown in this
 experiment, DreamCoder is able to learn new concepts based on tasks given, which
 enable it to solve more di cult tasks.
 3.4 Neural-guided synthesis
 Guiding program enumeration with a neural network is a commonly used program
 synthesis technique to speed up search, and is included in DreamCoders synthesis
 approach. We showcase the appropriateness of this approach for the ARC dataset by
 comparing neural-guided synthesis with brute-force enumeration on a set of arti cial
 ARC-like tasks involving sorting blocks of various sizes. Training a neural network
 16
Figure 6: Useful actions learned in the process of solving symmetry tasks. Pound
 signs represent abstractions. Abstractions may rely on others for construction; e.g.
 to stack grids horizontally, we re ect each input diagonally, stack vertically, and
 re ect the vertical stack diagonally.
 Figure 7: One of the four-way mirroring tasks and the program discovered that
 solves it. The program was discovered only after four iterations of enumeration and
 compression.
 improves the space of possible programs considered for a given task from O(n!) to
 roughly O(n) for a given program length. The network outputs a distribution over
 the set of functions using a convolutional network over the input/output grids. Doing
 so exponentially speeds up discovery of task solutions, as shown in Figure 8.
 3.5 Discussion
 It is useful to compare the learning done in our approach to that done by neural
 networks. Neural networks can also learn new concepts from training examples, but
 17
Figure 8: Using a neural net to guide synthesis exponentially improves enumera
tion time. Note: for program solution length 8, brute force did not complete in a
 reasonable time.
 their internal representation lacks structure which allows them to apply learned con
cepts compositionally to other tasks. In contrast, functions learned via compression,
 represented as programs, can naturally be composed and extended to solve harder
 tasks, while reusing concepts between tasks. This constitutes a learning paradigm
 which we view as essential to human-like reasoning.
 Even so, there are aspects of neural network functionality we can take advantage
 of. Some human priors such as object detection and denoising might be best imple
mented through neural networks rather than as functional programs. Incorporating
 neural modules into program synthesis would allow us to bene t from the advan
tages of neural networks, while also bene ting from the advantage of writing tasks
 as programs.
 There is another important caveat of the approach shown here. While e ec
tive and applicable to a wide range of tasks, the neural-guided synthesis used by
 DreamCoder is too weak to scale to the complexity of ARC tasks. To guide search,
 DreamCoder uses a neural network to predict the likelihood, given a pair of func
tions f and g, that g will be used as argument i of function f. This form of guidance
 18
Figure 9: Left: 2 tasks involving denoising. Right: 2 tasks requiring more sophisti
cated reasoning.
 enables fast enumeration of programs, but provides imperfect supervision for more
 complex problems. In particular, it does not necessarily scale well to long programs
 with many repeated operations. The tasks in ARC often require such programs. In
 the next section, we will design a new reasoning approach that incorporates neu
ral networks to provide a more powerful form of guidance in the search for correct
 programs.
 4 Reasoning
 To solve ARC tasks, we need a way to imbue our agent with the ability to reason
 towards solutions. ARC tasks have rich visual queues that guide us towards solutions.
 Without enabling our agent to take full advantage of these queues, the search over
 possible programs becomes exhaustive and impossibly large. In addition, most ARC
 tasks require several steps of reasoning before discovering the solution. How can we
 design an approach that searches for ARC solutions the way humans do?
 Let us consider some motivating examples for our approach that showcase the
 step-by-step reasoning we will emulate. To solve a task, one must answer the ques
tion: by what rule can we derive the output grid from input grid for each example?
 Consider task 173 from Figure 10. The reasoning steps to come to a solution might
 19
Figure 10: Task 173
 look something like this:
 1. Notice that the output grid is one of the objects present in the input grid.
 2. Reframe the question: for each input grid, which object do we choose?
 3. Solution: the object chosen in each case di ers from others in its vertical
 symmetry.
 Note how observations are conditional on the contents of both the input and
 output grid. In addition, it is hard to imagine discovering the solution without
 making the rst observation.
 Figure 11 shows another example, whose reasoning steps might be as follows:
 1. Notice that the output grid consists of copies of the 3x3 input grid, arranged
 in a certain arrangement among a 9x9 grid.
 2. Reframe the question: where should we place copies of the input grid?
 3. Notice that the placement of the input grid matches the outline of a color for
 each grid. For example, in the rst example, the diagonal of grids in the output
 matches the pattern of green pixels in the input.
 4. Reframe the question: what color should we arrage our grid copies along?
 20
Figure 11: Task 303
 5. Notice that the color matched is the most common color in the grid.
 Again, note how discovery of the solution essentially relies on making these indi
vidual observations one at a time (although not necessarily in this order).
 Systematizing a form of reasoning for ARC that emulates this reasoning will be
 based on the concept of execution-guided program synthesis.
 4.1 Execution-guided Program Synthesis
 Execution-guided program synthesis [6, 3] is a form of program synthesis where one
 executes partial programs to produce intermediate outputs, which help guide the
 creation of the full program. This ameliorates the need for a machine learning agent
 to internally simulate the semantics of the program being written. Humans make
 use of the same thing: for instance, it much easier to write out the result of a
 multiplication digit by digit, instead of conducting the full calculation in ones head.
 The style of execution-guided synthesis applicable to ARC most closely follows
 that used in [6]. An example of using it applied to ARC is described in Figure 12.
 This is a powerful form of neural-guided program synthesis in that each step of
 reasoning is conditioned on the entire state of the problem: input, output, and partial
 evaluations. However, it is limited to bottom-up enumeration: the leaves of the
 program are constructed (and evaluated) rst. In contrast, the motivating reasoning
 21
Figure 12: Solving ARC task 138 from the evaluation set with execution-guided
 synthesis. Conditioned on the input and output grids, the agent chooses to ip the
 input horizontally in step one. This action is executed to produce intermediate value
 i1. Next, the agent chooses to horizontally stack the intermediate value with the
 input grid, producing another value i2. Last, the agent horizontally stacks this value
 i2 with itself, correctly producing the output grid for each example and solving the
 task.
 22
Figure 13: Left: the function block is directly invertible: given a target grid in its
 codomain, one can deduce what inputs are needed to produce that target. Right:
 the function hstack (horizontal stack) is conditionally invertible: given a valid com
bination of target grid and one of the inputs of the function, one can deduce the
 second input needed to produce the target.
 steps laid out for tasks 173 and 303 involve proposing a function that is used to
 produce the output grid, and deducing the inputs required to correctly produce the
 output as new intermediate targets before discovering the complete program.
 This form of deductive reasoning involves evaluating function in reverse. It is best
 exempli ed in the FlashMeta system [15], where one leverages the inverse semantics
 of operators to deduce one or more inputs of a function given the output target and
 one or more inputs. We will incorporate this type of reasoning into an extension of
 execution-guided program synthesis to enable a reasoning approach for ARC tasks.
 4.2 Deductive reasoning via inverse semantics
 For our purposes, we can consider two cases.
 The simplest case is when the function is invertible. In this case, we can evaluate
 the inverse to produce two new targets for the search, as shown in 13. The more
 23
common situation is when a function is conditionally invertible: given one or more
 inputs to the function and the output, one can deduce the remaining inputs needed
 such that when the function is evaluated the output is produced. A surprisingly large
 number of functions are conditionally invertible; perhaps the most familiar family is
 arithmetic operators: if we know 1 + x = 5, we can deduce that x = 4. An example
 relevant to ARC is shown in 13.
 The deductive reasoning in our motivating examples also takes the form of con
ditionally invertible functions. For task 173, one might write the solution as
 out = kronecker(in, filter_color(in, most_common_color(in)))
 In step 1, we determine that the output is the Kronecker product of the input grid
 with another grid. In step 2, we deduce the second input to kronecker by means
 of its conditional invertibility 2. Likewise, given the target grid which is the second
 input to kronecker, we deduce the second argument to filter_color conditioned
 on the rst argument being the input grid.
 For task 303, one might write the solution as
 out = filter(objects(in), lambda obj: has_vertical_symmetry(obj))
 The conditional inverse of filter tells us whether objects in the rst argument
 must lter to true or false. To make this t in our deductive framework, it is con
venient to have filter take a list of Boolean values as the second argument. This
 list of Booleans can then be produced as an intermediate target by the conditional
 inverse of filter, and is satis ed by mapping has_vertical_symmetry to the list
 objects(in). More details on designing a conditionally invertible DSL for ARC can
 be found in Appendix A.1.
 4.3 Bidirectional, Execution-guided Program Synthesis
 With the addition of the deductive reasoning powered by inverse and conditional
 inverse functions, we are ready to present the bidirectional, execution-guided algo
rithm for program synthesis. Like the approach in [6, 23], we approach the synthesis
 2There are some subtleties with the conditional inverse presented. The conditional inverse of
 kronecker is unique up to changes in color of the second argument.
 24
task via reinforcement learning. We assume we have a grammar G of functions, each
 of which has an arity, a type signature, and associated inverse or conditional inverse
 functions. This includes constants of arity zero. For example, the subtraction func
tion has two conditional inverses: one which produces the rst argument conditioned
 on the second, and vice versa.
 The underlying Markov Decision Process has the following components:
 The current state is a graph of nodes. Each node represents either an input
 value, the output value, or an intermediate value resulting from the execution of an
 operation in the forwards or backwards direction, and has a corresponding program
 informing how that node is created. A node is grounded if there is a valid program
 to create that node from the operations applied so far.
 For ARC, each value is a set of examples, each of which is a grid. Applying
 an operation implicitly applies the operation to each example in the set to produce
 a new set of examples as a new value.
 An operation is a function from the grammar along with a designation of being
 applied in forwards, inverse, or as a conditional inverse (and if as a conditional inverse,
 conditioned on which input arguments). There are three types of operations: forward
 operations, inverse operations, and conditional inverse operations.
 For an inverse operation, the sole argument will be the output value. For condi
tional inverse operations, the rst argument is the output, and the other arguments
 are a subset of the inputs.
 Aforward operation applies the function to a set of grounded inputs to produce a
 new grounded node. We restrict our functions to have a single output. An invertible
 operation takes an ungrounded output and produces a new ungrounded target node
 such that grounding the target node will cause the output node to be grounded
 as well. A conditionally invertible operation takes an ungrounded output and one
 or more grounded input nodes, and produces a new ungrounded target node such
 that grounding the target node will cause the output node to be grounded as well.
 All invertible and conditionally invertible operations have a corresponding forward
 operation.
 Multiple examples are placed in the same node. When an operation is applied, it
 25
calculates the result for each example, and equality testing is done based on whether
 all examples match each other.
 For a task with n input values per example and a single output value, the initial
 state consists of n grounded value nodes and one ungrounded target node. In general,
 grounded nodes correspond to those from the bottom-up side of the search, while
 ungrounded nodes correspond to those from the top-down side of the search.
 Solving a given task thus consist of an episode in the MDP where the agent seeks
 to solve the task by grounding the output value node. Actions in the MDP correspond
 to a choice of operation and the choice of arguments for that operation. Each action
 applies a function in either the forward or backward direction. Intuitively, this
 executes a bidirectional search to try to connect the grounded nodes on one side
 with the ungrounded output node on the other.
 The reward for solving a task is R. A penalty of 1 is applied for attempting
 to apply any invalid operation. Invalid operations may be caused by a number
 of causes, including type errors, using an ungrounded node as input to a forward
 function, using a grounded node as improper input to an inverse or conditional
 inverse function, applying an operation which creates a node that already exists,
 or providing an invalid argument to an operation for example, providing 3 as the
 conditioning argument to the inverse of an integer multiplication op when the output
 is not divisible by three. We can even keep track of the type of values, and give errors
 for violating the type signature of functions.
 Unlike [6], we refrain from garbage-collecting nodes used as arguments to a for
ward operation, or correspondingly garbage-collecting nodes that are the designated
 output of an inverse or conditional inverse operation.
 Given a sequence of actions that solve a task, only the subset of the actions
 corresponding to the functions used in the nal program are important to solve
 the task. We can give a shaped reward function which gives reward R P to the
 operations used in the nal program, where P is the length of the nal program,
 and zero otherwise (unless a penalty is applicable). Dividing by the length of the
 program encourages shorter solutions. We expected this reward to work better than
 standard reward-to-go with exponential decay due to the more targeted feedback.
 26
Network and training
 The neural network receives as input a set of (node_value, node_grounded) tuples,
 chooses one of O operations to apply and selects M arguments for the operation,
 where M is the arity of the operation. Each argument is a value node from those
 provided. We can constrain our network to only choose arguments whose types
 match the type signature of the chosen operation by automatically masking invalid
 options in the same manner as [23].
 Our network architecture mirrors that used by [6], with a network for embedding
 value nodes, a deep set embedding for the set of value nodes, and a pointer network
 for choosing arguments to an operation.
 We found the combination of supervised pretraining and ne-tuning with REIN
FORCE used in [6] to work best for training the model. An important di erence
 is that generating random bidirectional programs is more complicated than random
 forward programs. To do so, we randomly apply forward operations, choose a ran
dom node among the outputs, and recover the sequence of actions used to create this
 node. We then convert this forward program into a bidirectional program by proba
bilistically converting operations at the end of the program to inverse or conditional
 inverse operations when applicable.
 For test-time search, we stick with taking episode rollouts as they are easiest to
 implement. Unlike [6], we did not yet implement a value network for our system.
 4.4 Results
 We evaluate the bidirectional algorithm on a set of 18 ARC symmetry tasks a
 subset of those used in Section 3. Here, we provide our agent with six primitives
 shown in 1. We use a convolutional neural network to embed grid example sets.
 We trained on a set of randomly generated programs evaluated on random input
 grids from the ARC training set, and ne-tuned with REINFORCE before sampling
 rollouts for ten minutes on all tasks at once. The agent is able to solve 13 of 18
 tasks, shown in Figure 14. Unfortunately, it struggles to scale to tasks requiring
 more than a few operations. The four-way mirror tasks solved at the end of the
 27
Primitive
 Description
 Inverse type
 hstack
 vstack
 rotate_cw
 rotate_ccw
 vflip
 hflip
 combine two grids horizontally two cond. inverses
 combine two grids vertically
 rotate grid clockwise
 rotate grid counterclockwise
 ip grid vertically
 ip grid horizontally
 two cond. inverses
 inverse
 inverse
 inverse
 inverse
 Table 1: Primitives used to solve ARC symmetry tasks.
 experiments in 3.3 remain unsolved, as well as two even harder tasks. For some
 reason we were not able to get the REINFORCE learning to consistently improve
 results. Here, equal performance came from using the supervised model directly,
 with REINFORCE yielding no improvement.
 To gain more insight into the performance of a forward-only search with the
 new bidirectional algorithm, we evaluate the agent in a simpler domain: solving 24
 Game problems. A 24 Game consists of four input numbers and a target number
 24. To solve the task, one must use each number once in an arithmetic expression
 that creates 24. For example, given 8, 1, 3, and 2, a solution is 24 = (2 1) 3 8.
 Solving a 24 problem requires similar reasoning to that solving ARC tasks: one
 executes various operations and tries to get closer to 24. We can use the conditional
 inverses of each arithmetic operator to facilitate a bidirectional search. For example,
 the conditional inverse of multiplication applied to 24 with 6 as one input yields 4
 as a new target. The 24 Game serves as a good alternative benchmark of the ability
 of our system, and lets us measure how important the bidirectional reasoning is to
 system performance.3
 For the supervised pretraining of our model, we train for 10,000 epochs on a
 dataset of randomly generated programs between depth one and four which yields
 50,000 training examples of actions. Programs may create any number as a target,
 324 Game is played with the rule that each number must be used exactly once in the expression
 to create 24. We relax this rule as it is not relevant for the program synthesis our agent is originally
 designed to carry out.
 28
Figure 14: 19 symmetry tasks from ARC. The rst two rows of tasks are simpler and
 manage to be solved by our agent. The last row our agent is unable to solve. One
 training example shown per task.
 29
1
 2
 3
 Depth
 Forward-only 0.232 0.801 0.516 0.340
 Bidirectional 0.953 0.929 0.877 0.853
 4
 Table 2: Percent of tasks solved for 24 Game. Forward-only denotes only using
 forward operations. Bidirectional includes conditional-inverse operations. Accuracy
 is average of three runs.
 not just 24, with the maximum allowed integer 100, and no negative or nonintegral
 numbers allowed. We then ne-tune with REINFORCE for 10,000 epochs of 1000
 actions taken each. We measure performance at the end of training as a function
 depth, and compare the full bidirectional, execution-guided algorithm with a forward
only baseline that only applies operations in the forwards direction with no inverse
 operations.
 Results are shown in Table 2. Accuracy remains fairly high as depth increases.
 This is because although tasks under depth four are generated through the applica
tion of four operations, as many as 40% remain solvable in fewer than four actions.
 Another observation is that bidirectional synthesis outperforms forward only across
 all depths. However, this should be questioned: its not clear why forward-only per
formance di ers so much between depths. In fact, for depth one tasks, there should
 be no di erence between forward-only and bidirectional approaches, since either way
 the solution takes a single action. So the disparity is likely the result of some bug
 rather than a meaningful di erence, or peculiarities with how REINFORCE is tuning
 our model.
 Besides bugs, there are a few reasons why learning to solve tasks with REIN
FORCE is not working as well as one might hope here. First, our hyperparameters
 may need to be tuned. Second, we may need to train for much longer. Compared
 to the number of examples seen during supervised training, the amount seen during
 policy gradient is quite low. This is due to the time taken to simulate the search
 graph environment while playing episodes. Last, our network architecture may need
 tuning or strengthening as well.
 30
Model
 SV depth 1 FW
 Tasks solved
 14
 SV depth 2 FW
 SV depth 3 FW
 SV depth 4 FW
 SV mixed FW
 SV depth 1 bidir
 SV depth 2 bidir
 SV depth 3 bidir
 SV depth 4 bidir
 SV mixed bidir
 74
 96
 45
 96
 66
 96
 96
 46
 96
 Model
 Tasks solved
 PG depth 1 FW
 PG depth 2 FW
 PG depth 3 FW
 PG depth 4 FW
 PG depth 1 bidir
 PG depth 2 bidir
 PG depth 3 bidir
 PG depth 4 bidir
 0
 15
 19
 12
 27
 39
 39
 38
 Table 3: Number of tasks solved out of 96 by various models. SV denotes a model
 trained in a supervised manner. FW denotes only forward operations, while bidir
 denotes an agent with bidirectional search. PG denotes a model ne-tuned with
 REINFORCE. Fine-tuned models are pretrained on supervised data of mixed depth.
 Depth refers to the number of operations to solve a task; mixed combines all four
 depths into one.
 Weadditionally measured performance of the agent on a set of 96 24 Game tasks,
 shown in Table 3. We sample tasks by taking rollouts repeatedly for 60 seconds on all
 96 tasks at once. Surprisingly, the supervised models 
without any REINFORCE
 ne-tuning 
performed best, solving all 96 tasks. The ne-tuned models may be
 over tting to a subset of the tasks that the models can solve, preventing proper
 exploration while solving the harder tasks. Incorporating entropy regularization to
 ameliorate this issue would be a good next step.
 5 Discussion
 As one of the rst documented e orts towards developing a principled learning ap
proach to the Abstraction and Reasoning Corpus, we have proposed and tested two
 directions independently. The rst addresses the abstraction required for ARC; it
 uses the compression algorithm from DreamCoder to learn abstractions of rule-based
 31
behavior to enable further pro ciency and compositional generalization on progres
sively more challenging tasks. The second addresses the reasoning required for ARC;
 it uni es execution-guided program synthesis, a bottom-up synthesis method, with
 top-down deductive reasoning via inverse semantics. This enables a bidirectional
 program synthesis algorithm well-suited to solving tasks like those seen in ARC, and
 addresses the di culties DreamCoder faces in scaling search to the level required for
 performance on ARC.
 The next important step is to combined these two approaches to create a uni ed
 system capable of both abstraction and reasoning on ARC. Neither approach is com
pletely su cient on its own. Without a strong reasoning approach, DreamCoders
 search algorithm is too weak to scale to challenging ARC tasks. But without the abil
ity to create new abstractions, the bidirectional, execution-guided synthesis is limited
 to solving tasks via whatever functions the developer provides it with. This requires
 a carefully crafted DSL, which not only goes against the spirit of ARC but inevitably
 leads to limited performance on the hidden test set, which likely builds on functions
 not seen in the training or evaluation sets. Luckily, combining the two approaches
 is very possible: new functions created by DreamCoders abstraction algorithm can
 be provided to the bidirectional search algorithm, which can use these functions to
 solve new tasks. In essence, we can replace DreamCoders neural-guided search al
gorithm with the more powerful bidirectional, execution-guided search. Tasks solved
 by the bidirectional search can be given to DreamCoders compression algorithm to
 produce new functions. We can then train the bidirectional algorithm to use these
 new functions by sampling random programs in them in a manner similar to the way
 DreamCoder does.
 In addition to learning forward functions, it would be nice if our bidirectional
 agent could learn inverses and conditional inverses of new abstractions. One ap
proach to this would be to treat these as synthesis problems of their own, sampling
 random inputs and tasking our system with creating a function which converts out
puts into inputs, perhaps conditioned on a subset of inputs. We hope to explore
 these possibilities for future work.
 There are a few other important further directions to consider for those interested
 32
in making progress on ARC. An important limit of all systems developed so far is
 their reliance on explicit programs to represent solutions to tasks. As discussed in
 Section 3.5, representing solutions with neural modules rather than programs opens
 the door to systems that are more exible and rely less on hard-coded reasoning
 systems like that described here. In the introduction, we stressed the importance
 of moving away from systems whose reasoning abilities are task-speci c and imple
mented by the developer. Yet the bidirectional algorithm proposed is an example of
 just such a thing. Generalizing the algorithm to something more widely applicable
 is an important step. For example, deductive reasoning could be implemented in the
 form of local causality-propagating systems of neural modules.
 Another direction involves addressing the vast amounts of prior knowledge hu
mans bring to a challenge like ARC. Large generative pretrained models [2, 16] o er
 a potential way to incorporate prior knowledge in this manner. It remains to be seen
 the extent to which such models can generalize to the idiosyncratic ARC environ
ment of discrete-colored grids, but the impressive improvements shown over the past
 few years indicate that betting against such models is not safe.
 The di culty of performing well on ARC without resorting to developer-provided
 brute-force solutions is a testament to its design as a measure of intelligence. Not
 only is it di cult, but its design captures the exact challenges facing us in arti
cial intelligence. We hope that the benchmark continues to receive attention and
 motivates new learning algorithms to get us closer to the development of generally
 intelligent machines.
 A Appendix
 A.1 A bidirectional grammar for ARC tasks
 A lot of e ort went into designing a set of functions suited to solving ARC tasks
 that facilitates bidirectional reasoning. While not used in the results shown here, we
 record the details to exemplify the potential of inverse semantics for ARC, and in
 the interest of assisting future work.
 33
Figure 15: Task 148
 Most of the operations in use are straightforward operations to get a list of objects,
 color in a grid, lter all but one color in a grid, set the background color, stack grids
 horizontally or vertically, and so on. We only address more interesting operations
 designed to facilitate the use of inverse functions and conditional inverse functions
 in an execution-guided setting.
 A.1.1 List operations
 Many list operations such as map, filter and sort take a function as an argument.
 Functions, however, are not well-suited for execution-guided synthesis, as one cannot
 evaluate intermediate constructions while making them. To address this, we can
 change the type signatures of the functions. To start, we allow any function to be
 vectorized, so that to map a function to a list, one can simply incrementally apply
 functions to the list. For example,
 We can modify filter to take a Boolean list as a second argument instead
 of a Boolean function, and return only the items in the rst list for whom the
 corresponding second element is true. Similarly, we can modify sort to take a list
 of integers as a second argument, and return the rst list sorted using the elements
 of the second list as keys for comparison.
 The function map is a little di erent. Given an input list and a target list, we can
 conduct a change of basis to create a new synthesis problem whose input/output
 examples are the elements of the list. For example, for task 148 (Figure 15), we might
 apply a forward operation to get a list of nine 3x3 grids, and an inverse operation to
 34
Figure 16: Task 168
 get a list of nine pixels as a new target from the output grid. By applying the map
 change of basis, we can create a new synthesis task with 36 training examples, each
 of which is a pair of a 3x3 input grid and an output pixel which is black or blue. With
 this change of basis, one can continue to construct a solution via execution-guided
 synthesis.
 There are other types of change of basis operations we can create. One example
 is to remap colors in the input and output grids based on frequency on a per-example
 basis. This is a strategy used by the winning Kaggle competition [10]. One can think
 of this as applying an invertible operation to the input grid in the forwards direction,
 and then applying its inverse to the output grid. Any invertible operation could be
 used in this manner. For example, we could rotate both the input and output grid
 clockwise4
 There is one more important operation, one that formed our original motivation
 for designing a bidirectional approach to ARC. Consider task 168 (Figure 16). To
 begin, we can get a list of objects in the input and output grids. Getting a list of ob
jects from the output can be thought of as the inverse of a function place_into_grid
 which takes a list of (positioned) objects and embeds them in a grid. If we apply a
 map change of basis, we then have a new task mapping grey shapes to colored versions
 4One way of thinking about this is that in rotating the output grid clockwise, we are applying
 the inverse, rotate counter-clockwise, in the backwards direction.
 35
of themselves. We can apply the conditional inverse color_in(grid, color) with
 the input grid supplied as the condiitoning argument to produce a new task: given a
 grid, deduce what color to color it in. If we then apply area in the forwards direction
 to get the area of each grid, then we get an association between integers and colors.
 If this were a synthesis task, the solution would be simple: it is a simple lookup: all
 identical inputs map to the same output. We can include a lookup operation which
 connects the two sides of the bidirectional search this way.
 One last example, task 10, exempli es the capabilities of bidirectional, execution
guided synthesis. In order, we can:
 • Split the input into a list of objects in the forwards direction
 • Apply add gridlines in reverse to the output to create a new target with the
 gridlines removed.
 • Apply in ate in reverse (conditioned on the in ate factor, a constant 3) to
 produce a 3x3 grid target.
 • Apply the lter conditional inverse: given the input list, and the target
 element which is a member of the list, produce a new target list of Booleans
 which is true for the element chosen and false otherwise.
 • Apply area in the forwards direction to the list of objects.
 • Apply lookup between the list of areas and the list of Booleans. The only
 object chosen is that with area four.
 A visual demonstration of this search is shown in Figure 17.
 A.2 Code
 For code access, please reach out to Simon at simonalford42@gmail.com.
 36
Figure 17: A demo of bidirectional search on task 10. The lower half shows the
 continued search after applying filter, which did not t easily in the top diagram.
 37
References
 [1] top-quarks/arc-solution.
 Accessed: 2020-10-05.
 https://github.com/top-quarks/ARC-solution.
 [2] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Ka
plan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry,
 Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger,
 Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Je rey Wu,
 Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin,
 Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish,
 Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot
 learners, 2020.
 [3] Xinyun Chen, Chang Liu, and Dawn Song. Execution-guided neural program
 synthesis. In International Conference on Learning Representations, 2019.
 [4] Francois Chollet. On the measure of intelligence, 2019.
 [5] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert:
 Pre-training of deep bidirectional transformers for language understanding,
 2019.
 [6] Kevin Ellis, Maxwell Nye, Yewen Pu, Felix Sosa, Josh Tenenbaum, and Ar
mando Solar-Lezama. Write, execute, assess: Program synthesis with a repl,
 2019.
 [7] Kevin Ellis, Catherine Wong, Maxwell Nye, Mathias Sable-Meyer, Luc Cary, Lu
cas Morales, Luke Hewitt, Armando Solar-Lezama, and Joshua B. Tenenbaum.
 Dreamcoder: Growing generalizable, interpretable knowledge with wake-sleep
 bayesian program learning, 2020.
 [8] Jonathan Evans. In two minds: Dual-process accounts of reasoning. Trends in
 cognitive sciences, 7:4549, 11 2003.
 38
[9] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learn
ing for image recognition, 2015.
 [10] icecuber . Arc-solution. https://github.com/top-quarks/ARC-solution,
 2020.
 [11] Daniel Kahneman. Thinking, fast and slow. Farrar, Straus and Giroux, 2011.
 [12] Alex Krizhevsky, Ilya Sutskever, and Geo rey E Hinton. Imagenet classi cation
 with deep convolutional neural networks. In Advances in neural information
 processing systems, pages 10971105, 2012.
 [13] Brenden M. Lake and Marco Baroni. Generalization without systematicity: On
 the compositional skills of sequence-to-sequence recurrent networks, 2018.
 [14] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A Rusu, Joel Ve
ness, Marc G Bellemare, Alex Graves, Martin Riedmiller, Andreas K Fidjeland,
 Georg Ostrovski, et al. Human-level control through deep reinforcement learn
ing. nature, 518(7540):529533, 2015.
 [15] Oleksandr Polozov and Sumit Gulwani. Flashmeta: a framework for inductive
 program synthesis. In Jonathan Aldrich and Patrick Eugster, editors, OOPSLA,
 pages 107126. ACM, 2015.
 [16] Aditya Ramesh, Mikhail Pavlov, Gabriel Goh, Scott Gray, Chelsea Voss, Alec
 Radford, Mark Chen, and Ilya Sutskever. Zero-shot text-to-image generation,
 2021.
 [17] David Silver, Julian Schrittwieser, Karen Simonyan, Ioannis Antonoglou, Aja
 Huang, Arthur Guez, Thomas Hubert, Lucas Baker, Matthew Lai, Adrian
 Bolton, et al. Mastering the game of go without human knowledge. nature,
 550(7676):354359, 2017.
 [18] Steven A. Sloman. The empirical case for two systems of reasoning. Psychological
 Bulletin, 119:322, 1996.
 39
[19] Jacob M. Springer and Garrett T. Kenyon. Its hard for neural networks to
 learn the game of life, 2020.
 [20] Andrew Trask, Felix Hill, Scott E. Reed, Jack W. Rae, Chris Dyer, and Phil
 Blunsom. Neural arithmetic logic units. CoRR, abs/1808.00508, 2018.
 [21] Oriol Vinyals, Igor Babuschkin, Wojciech M Czarnecki, Michael Mathieu, An
drew Dudzik, Junyoung Chung, David H Choi, Richard Powell, Timo Ewalds,
 Petko Georgiev, et al. Grandmaster level in starcraft ii using multi-agent rein
forcement learning. Nature, 575(7782):350354, 2019.
 [22] Po-Wei Wang, Priya L. Donti, Bryan Wilder, and Zico Kolter. Satnet: Bridging
 deep learning and logical reasoning using a di erentiable satis ability solver,
 2019.
 [23] Chenghui Zhou, Chun-Liang Li, and Barnabas Poczos. Unsupervised program
 synthesis for images using tree-structured lstm, 2020.
 [24] Lukasz Kaiser and Ilya Sutskever. Neural gpus learn algorithms, 2016.
 40

 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=














 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 id: mccarthy1960-recursive-symbolic-expressions
  title: "Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I"
  author: "John McCarthy"
  venue: "Communications of the ACM"
  volume: 3
  number: 4
  pages: "184–195"
  year: 1960
  notes: "Foundational paper introducing the LISP language (‘LISt Processor’)"
 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


 Recursive Functions of Symbolic Expressions
 and Their Computation by Machine, Part I
 John McCarthy, Massachusetts Institute of Technology, Cambridge, Mass. ∗
 April 1960
 1 Introduction
 A programming system called LISP (for LISt Processor) has been developed
 for the IBM 704 computer by the Artificial Intelligence group at M.I.T. The
 system was designed to facilitate experiments with a proposed system called
 the Advice Taker, whereby a machine could be instructed to handle declarative
 as well as imperative sentences and could exhibit “common sense” in carrying
 out its instructions. The original proposal [1] for the Advice Taker was made
 in November 1958. The main requirement was a programming system for
 manipulating expressions representing formalized declarative and imperative
 sentences so that the Advice Taker system could make deductions.
 In the course of its development the LISP system went through several
 stages of simplification and eventually came to be based on a scheme for rep
resenting the partial recursive functions of a certain class of symbolic expres
sions. This representation is independent of the IBM 704 computer, or of any
 other electronic computer, and it now seems expedient to expound the system
 by starting with the class of expressions called S-expressions and the functions
 called S-functions.
 ∗Putting this paper in LATEXpartly supported by ARPA (ONR) grant N00014-94-1-0775
 to Stanford University where John McCarthy has been since 1962. Copied with minor nota
tional changes from CACM, April 1960. If you want the exact typography, look there. Cur
rent address, John McCarthy, Computer Science Department, Stanford, CA 94305, (email:
 jmc@cs.stanford.edu), (URL: http://www-formal.stanford.edu/jmc/ )
 1
In this article, we first describe a formalism for defining functions recur
sively. We believe this formalism has advantages both as a programming
 language and as a vehicle for developing a theory of computation. Next, we
 describe S-expressions and S-functions, give some examples, and then describe
 the universal S-function apply which plays the theoretical role of a universal
 Turing machine and the practical role of an interpreter. Then we describe the
 representation of S-expressions in the memory of the IBM 704 by list structures
 similar to those used by Newell, Shaw and Simon [2], and the representation
 of S-functions by program. Then we mention the main features of the LISP
 programming system for the IBM 704. Next comes another way of describ
ing computations with symbolic expressions, and finally we give a recursive
 function interpretation of flow charts.
 We hope to describe some of the symbolic computations for which LISP
 has been used in another paper, and also to give elsewhere some applications
 of our recursive function formalism to mathematical logic and to the problem
 of mechanical theorem proving.
 2 Functions and Function Definitions
 We shall need a number of mathematical ideas and notations concerning func
tions in general. Most of the ideas are well known, but the notion of conditional
 expression is believed to be new1, and the use of conditional expressions per
mits functions to be defined recursively in a new and convenient way.
 a. Partial Functions. A partial function is a function that is defined only
 on part of its domain. Partial functions necessarily arise when functions are
 defined by computations because for some values of the arguments the com
putation defining the value of the function may not terminate. However, some
 of our elementary functions will be defined as partial functions.
 b. Propositional Expressions and Predicates. A propositional expression is
 an expression whose possible values are T (for truth) and F (for falsity). We
 shall assume that the reader is familiar with the propositional connectives ∧
 (“and”), ∨ (“or”), and ¬ (“not”). Typical propositional expressions are:
 1
 reference Kleene
 2
x <y
 (x < y)∧(b = c)
 x is prime
 Apredicate is a function whose range consists of the truth values T and F.
 c. Conditional Expressions. The dependence of truth values on the values
 of quantities of other kinds is expressed in mathematics by predicates, and the
 dependence of truth values on other truth values by logical connectives. How
ever, the notations for expressing symbolically the dependence of quantities of
 other kinds on truth values is inadequate, so that English words and phrases
 are generally used for expressing these dependences in texts that describe other
 dependences symbolically. For example, the function |x| is usually defined in
 words. Conditional expressions are a device for expressing the dependence of
 quantities on propositional quantities. A conditional expression has the form
 (p1 → e1,···,pn → en)
 where the p’s are propositional expressions and the e’s are expressions of any
 kind. It may be read, “If p1 then e1 otherwise if p2 then e2, ··· , otherwise if
 pn then en,” or “p1 yields e1,···,pn yields en.” 2
 We now give the rules for determining whether the value of
 (p1 → e1,···,pn → en)
 is defined, and if so what its value is. Examine the p’s from left to right. If
 a p whose value is T is encountered before any p whose value is undefined is
 encountered then the value of the conditional expression is the value of the
 corresponding e (if this is defined). If any undefined p is encountered before
 2
 I sent a proposal for conditional expressions to a CACM forum on what should be
 included in Algol 60. Because the item was short, the editor demoted it to a letter to the
 editor, for which CACM subsequently apologized. The notation given here was rejected for
 Algol 60, because it had been decided that no new mathematical notation should be allowed
 in Algol 60, and everything new had to be English. The if ...then...else that Algol 60
 adopted was suggested by John Backus.
 3
a true p, or if all p’s are false, or if the e corresponding to the first true p is
 undefined, then the value of the conditional expression is undefined. We now
 give examples.
 (1 < 2 →4,1>2→3)=4
 (2 < 1 →4,2>1→3,2>1→2)=3
 (2 < 1 →4,T →3)=3
 (2 < 1 → 0
 0 ,T →3)=3
 (2 < 1 →3,T → 0
 0 ) is undefined
 (2 < 1 →3,4<1→4) is undefined
 Some of the simplest applications of conditional expressions are in giving
 such definitions as
 |x| = (x < 0 →−x,T →x)
 δij = (i = j → 1,T →0)
 sgn(x) = (x < 0 → −1,x = 0→0,T →1)
 d. Recursive Function Definitions. By using conditional expressions we
 can, without circularity, define functions by formulas in which the defined
 function occurs. For example, we write
 n! = (n =0→1,T →n·(n−1)!)
 When we use this formula to evaluate 0! we get the answer 1; because of the
 way in which the value of a conditional expression was defined, the meaningless
 4
expression 0 · (0- 1)! does not arise. The evaluation of 2! according to this
 definition proceeds as follows:
 2! = (2=0→1,T →2·(2−1)!)
 = 2·1!
 = 2·(1=0→1T →·(1−1)!)
 = 2·1·0!
 = 2·1·(0 =0→1,T →0·(0−1)!)
 = 2·1·1
 = 2
 We now give two other applications of recursive function definitions. The
 greatest common divisor, gcd(m,n), of two positive integers m and n is com
puted by means of the Euclidean algorithm. This algorithm is expressed by
 the recursive function definition:
 gcd(m,n) = (m > n →gcd(n,m),rem(n,m) = 0 → m,T → gcd(rem(n,m),m))
 where rem(n,m) denotes the remainder left when n is divided by m.
 The Newtonian algorithm for obtaining an approximate square root of a
 number a, starting with an initial approximation x and requiring that an
 acceptable approximation y satisfy |y2 − a| < ϵ, may be written as
 sqrt(a, x, ϵ)
 = (|x2 −a| < ϵ → x,T → sqrt (a, 1
 2
 (x+ a
 x
 ),ϵ))
 The simultaneous recursive definition of several functions is also possible,
 and we shall use such definitions if they are required.
 There is no guarantee that the computation determined by a recursive
 definition will ever terminate and, for example, an attempt to compute n!
 from our definition will only succeed if n is a non-negative integer. If the
 computation does not terminate, the function must be regarded as undefined
 for the given arguments.
 The propositional connectives themselves can be defined by conditional
 expressions. We write
 5
p ∧q = (p→q,T →F)
 p ∨q = (p→T,T →q)
 ¬p = (p→F,T →T)
 p ⊃q = (p→q,T →T)
 It is readily seen that the right-hand sides of the equations have the correct
 truth tables. If we consider situations in which p or q may be undefined, the
 connectives ∧ and ∨ are seen to be noncommutative. For example if p is false
 and q is undefined, we see that according to the definitions given above p ∧ q
 is false, but q ∧ p is undefined. For our applications this noncommutativity is
 desirable, since p∧q is computed by first computing p, and if p is false q is not
 computed. If the computation for p does not terminate, we never get around
 to computing q. We shall use propositional connectives in this sense hereafter.
 e. Functions and Forms. It is usual in mathematics—outside of mathe
matical logic—to use the word “function” imprecisely and to apply it to forms
 such as y2+x. Because we shall later compute with expressions for functions,
 we need a distinction between functions and forms and a notation for express
ing this distinction. This distinction and a notation for describing it, from
 which we deviate trivially, is given by Church [3].
 Let f be an expression that stands for a function of two integer variables.
 It should make sense to write f(3,4) and the value of this expression should be
 determined. The expression y2+x does not meet this requirement; y2+x(3,4)
 is not a conventional notation, and if we attempted to define it we would be
 uncertain whether its value would turn out to be 13 or 19. Church calls an
 expression like y2 + x, a form. A form can be converted into a function if we
 can determine the correspondence between the variables occurring in the form
 and the ordered list of arguments of the desired function. This is accomplished
 by Church’s λ-notation.
 If E is a form in variables x1,···,xn, then λ((x1,···,xn),E) will be taken
 to be the function of n variables whose value is determined by substituting
 the arguments for the variables x1,···,xn in that order in E and evaluating
 the resulting expression. For example, λ((x,y),y2 + x) is a function of two
 variables, and λ((x,y),y2 + x)(3,4) = 19.
 The variables occurring in the list of variables of a λ-expression are dummy
 or bound, like variables of integration in a definite integral. That is, we may
 6
change the names of the bound variables in a function expression without
 changing the value of the expression, provided that we make the same change
 for each occurrence of the variable and do not make two variables the same
 that previously were different. Thus λ((x,y),y2 + x),λ((u,v),v2 + u) and
 λ((y,x),x2 + y) denote the same function.
 We shall frequently use expressions in which some of the variables are
 bound by λ’s and others are not. Such an expression may be regarded as
 defining a function with parameters. The unbound variables are called free
 variables.
 An adequate notation that distinguishes functions from forms allows an
 unambiguous treatment of functions of functions. It would involve too much
 of a digression to give examples here, but we shall use functions with functions
 as arguments later in this report.
 Difficulties arise in combining functions described by λ-expressions, or by
 any other notation involving variables, because different bound variables may
 be represented by the same symbol. This is called collision of bound variables.
 There is a notation involving operators that are called combinators for com
bining functions without the use of variables. Unfortunately, the combinatory
 expressions for interesting combinations of functions tend to be lengthy and
 unreadable.
 f. Expressions for Recursive Functions. The λ-notation is inadequate for
 naming functions defined recursively. For example, using λ’s, we can convert
 the definition
 sqrt(a, x,ϵ) = (|x2 − a| < ϵ → x,T → sqrt(a, 1
 2 (x+ a
 x ),ϵ))
 into
 sqrt = λ((a,x,ϵ),(|x2 − a| < ϵ → x,T → sqrt(a, 1
 2 (x+ a
 x ),ϵ))),
 but the right-hand side cannot serve as an expression for the function be
cause there would be nothing to indicate that the reference to sqrt within the
 expression stood for the expression as a whole.
 In order to be able to write expressions for recursive functions, we intro
duce another notation. label(a,E) denotes the expression E, provided that
 occurrences of a within E are to be interpreted as referring to the expression
 7
as a whole. Thus we can write
 label(sqrt, λ((a,x,ϵ),(|x2 − a| < ϵ → x,T → sqrt(a, 1
 2
 (x + a
 x
 ),ϵ))))
 as a name for our sqrt function.
 The symbol a in label (a,E) is also bound, that is, it may be altered
 systematically without changing the meaning of the expression. It behaves
 differently from a variable bound by a λ, however.
 3 RecursiveFunctionsof Symbolic Expressions
 We shall first define a class of symbolic expressions in terms of ordered pairs
 and lists. Then we shall define five elementary functions and predicates, and
 build from them by composition, conditional expressions, and recursive def
initions an extensive class of functions of which we shall give a number of
 examples. We shall then show how these functions themselves can be ex
pressed as symbolic expressions, and we shall define a universal function apply
 that allows us to compute from the expression for a given function its value
 for given arguments. Finally, we shall define some functions with functions as
 arguments and give some useful examples.
 a. A Class of Symbolic Expressions. We shall now define the S-expressions
 (S stands for symbolic). They are formed by using the special characters
 ·
 )
 (
 and an infinite set of distinguishable atomic symbols. For atomic symbols,
 we shall use strings of capital Latin letters and digits with single imbedded
 8
blanks.3 Examples of atomic symbols are
 A
 ABA
 APPLE PIE NUMBER 3
 There is a twofold reason for departing from the usual mathematical prac
tice of using single letters for atomic symbols. First, computer programs fre
quently require hundreds of distinguishable symbols that must be formed from
 the 47 characters that are printable by the IBM 704 computer. Second, it is
 convenient to allow English words and phrases to stand for atomic entities for
 mnemonic reasons. The symbols are atomic in the sense that any substructure
 they may have as sequences of characters is ignored. We assume only that dif
ferent symbols can be distinguished. S-expressions are then defined as follows:
 1. Atomic symbols are S-expressions.
 2. If e1 and e2 are S-expressions, so is (e1 · e2).
 Examples of S-expressions are
 AB
 (A· B)
 ((AB · C)·D)
 An S-expression is then simply an ordered pair, the terms of which may be
 atomic symbols or simpler S-expressions. We can can represent a list of arbi
trary length in terms of S-expressions as follows. The list
 (m1,m2,···,mn)
 is represented by the S-expression
 (m1 · (m2 ·(···(mn · NIL)···)))
 Here NIL is an atomic symbol used to terminate lists. Since many of the
 symbolic expressions with which we deal are conveniently expressed as lists,
 we shall introduce a list notation to abbreviate certain S-expressions. We have
 31995 remark: Imbedded blanks could be allowed within symbols, because lists were then
 written with commas between elements.
 9
l. (m) stands for (m ·NIL).
 2. (m1,···,mn) stands for (m1 · (···(mn · NIL)···)).
 3. (m1,···,mn · x) stands for (m1 · (···(mn · x)···)).
 Subexpressions can be similarly abbreviated. Some examples of these ab
breviations are
 ((AB,C),D) for ((AB ·(C ·NIL))·(D ·NIL))
 ((A,B),C,D ·E) for ((A·(B ·NIL))·(C ·(D ·E)))
 Since we regard the expressions with commas as abbreviations for those
 not involving commas, we shall refer to them all as S-expressions.
 b. Functions of S-expressions and the Expressions That Represent Them.
 Wenow define a class of functions of S-expressions. The expressions represent
ing these functions are written in a conventional functional notation. However,
 in order to clearly distinguish the expressions representing functions from S
expressions, we shall use sequences of lower-case letters for function names
 and variables ranging over the set of S-expressions. We also use brackets and
 semicolons, instead of parentheses and commas, for denoting the application
 of functions to their arguments. Thus we write
 car[x]
 car[cons[(A · B);x]]
 In these M-expressions (meta-expressions) any S-expression that occur stand
 for themselves.
 c. The Elementary S-functions and Predicates. We introduce the following
 functions and predicates:
 1. atom. atom[x] has the value of T or F according to whether x is an
 atomic symbol. Thus
 atom [X] = T
 atom [(X · A)] = F
 2. eq. eq [x;y] is defined if and only if both x and y are atomic. eq [x; y]
 = Tif x and y are the same symbol, and eq [x; y] = F otherwise. Thus
 10
eq [X; X] = T
 eq [X; A] = F
 eq [X; (X · A)] is undefined.
 3. car. car[x] is defined if and only if x is not atomic. car [(e1 · e2)] = e1.
 Thus car [X] is undefined.
 car [(X · A)] = X
 car [((X · A) · Y )] = (X ·A)
 4. cdr. cdr [x] is also defined when x is not atomic. We have cdr
 [(e1 · e2)] = e2. Thus cdr [X] is undefined.
 cdr [(X · A)] = A cdr [((X ·A)·Y)] = Y
 5. cons. cons [x; y] is defined for any x and y. We have cons [e1;e2] =
 (e1 · e2). Thus
 cons [X; A] = (X A)
 cons [(X · A);Y] = ((X ·A)Y)
 car, cdr, and cons are easily seen to satisfy the relations
 car [cons [x; y]] = x
 cdr [cons [x; y]] = y
 cons [car [x]; cdr [x]] = x, provided that x is not atomic.
 The names “car” and “cons” will come to have mnemonic significance only
 when we discuss the representation of the system in the computer. Composi
tions of car and cdr give the subexpressions of a given expression in a given
 position. Compositions of cons form expressions of a given structure out of
 parts. The class of functions which can be formed in this way is quite limited
 and not very interesting.
 d. Recursive S-functions. We get a much larger class of functions (in fact,
 all computable functions) when we allow ourselves to form new functions of
 S-expressions by conditional expressions and recursive definition. We now give
 11
some examples of functions that are definable in this way.
 1. ff[x]. The value of ff[x] is the first atomic symbol of the S-expression x
 with the parentheses ignored. Thus
 f
 f[((A · B) · C)] = A
 We have
 f
 f[x] = [atom[x] → x;T → ff[car[x]]]
 We now trace in detail the steps in the evaluation of
 f
 f [((A · B) · C)]:
 f
 f [((A · B) · C)]
 = [atom[((A·B)·C)] → ((A·B)·C);T → ff[car[((A·B)C·)]]]
 = [F →((A·B)·C);T →ff[car[((A·B)·C)]]]
 = [T →ff[car[((A·B)·C)]]]
 = ff[car[((A·B)·C)]]
 = ff[(A·B)]
 = [atom[(A·B)] → (A·B);T → ff[car[(A·B)]]]
 = [F →(A·B);T →ff[car[(A·B)]]]
 = [T →ff[car[(A·B)]]]
 = ff[car[(A·B)]]
 = ff[A]
 12
= [atom[A] → A;T →ff[car[A]]]
 = [T →A;T →ff[car[A]]]
 = A
 2. subst [x;y;z]. This function gives the result of substituting the S
expression x for all occurrences of the atomic symbol y in the S-expression z.
 It is defined by
 subst [x; y; z] = [atom [z] → [eq [z; y] → x; T → z];
 T →cons [subst [x; y; car [z]]; subst [x; y; cdr [z]]]]
 As an example, we have
 subst[(X · A);B;((A · B) · C)] = ((A· (X ·A))·C)
 3. equal [x; y]. This is a predicate that has the value T if x and y are the
 same S-expression, and has the value F otherwise. We have
 equal [x; y] = [atom [x] ∧ atom [y] ∧ eq [x; y]]
 ∨[¬ atom [x] ∧¬ atom [y] ∧ equal [car [x]; car [y]]
 ∧ equal [cdr [x]; cdr [y]]]
 It is convenient to see how the elementary functions look in the abbreviated
 list notation. The reader will easily verify that
 (i) car[(m1,m2,···,mn)] = m1
 (ii) cdr[(ms,m2,···,mn)] = (m2,···,mn)
 (iii) cdr[(m)] = NIL
 (iv) cons[m1;(m2,···,mn)] = (m1,m2,···,mn)
 (v) cons[m;NIL] = (m)
 We define
 13
null[x] = atom[x] ∧ eq[x;NIL]
 This predicate is useful in dealing with lists.
 Compositions of car and cdr arise so frequently that many expressions can
 be written more concisely if we abbreviate
 cadr[x] for car[cdr[x]],
 caddr[x] for car[cdr[cdr[x]]], etc.
 Another useful abbreviation is to write list [e1;e2;···;en]
 for cons[e1;cons[e2;···;cons[en;NIL]···]].
 This function gives the list, (e1,···,en), as a function of its elements.
 The following functions are useful when S-expressions are regarded as lists.
 1. append [x;y].
 append [x; y] = [null[x] → y; T → cons [car [x]; append [cdr [x]; y]]]
 An example is
 append [(A, B); (C, D, E)] = (A, B, C, D, E)
 2. among [x;y]. This predicate is true if the S-expression x occurs among
 the elements of the list y. We have
 among[x;y] = ¬null[y] ∧ [equal[x;car[y]] ∨ among[x;cdr[y]]]
 3. pair [x;y]. This function gives the list of pairs of corresponding elements
 of the lists x and y. We have
 pair[x; y] = [null[x]∧null[y] → NIL;¬atom[x]∧¬atom[y] → cons[list[car[x];car[y]];pair[cdr[x];cdr[y]]]
 An example is
 pair[(A,B,C);(X,(Y,Z),U)] = ((A,X),(B,(Y,Z)),(C,U)).
 14
4. assoc [x;y]. If y is a list of the form ((u1,v1),···,(un,vn)) and x is one
 of the u’s, then assoc [x;y] is the corresponding v. We have
 assoc[x;y] = eq[caar[y];x] → cadar[y];T → assoc[x;cdr[y]]]
 An example is
 assoc[X;((W,(A,B)),(X,(C,D)),(Y,(E,F)))] = (C,D).
 5. sublis[x;y]. Here x is assumed to have the form of a list of pairs
 ((u1, v1), · · ·, (un,vn)), where the u’s are atomic, and y may be any S-expression.
 The value of sublis[x;y] is the result of substituting each v for the correspond
ing u in y. In order to define sublis, we first define an auxiliary function. We
 have
 sub2[x;z] = [null[x] → z;eq[caar[x];z] → cadar[x];T → sub2[cdr[x];z]]
 and
 sublis[x; y] = [atom[y] → sub2[x;y];T → cons[sublis[x;car[y]];sublis[x;cdr[y]]]
 We have
 sublis [((X, (A, B)), (Y, (B, C))); (A, X · Y)] = (A, (A, B), B, C)
 e. Representation of S-Functions by S-Expressions. S-functions have been
 described by M-expressions. We now give a rule for translating M-expressions
 into S-expressions, in order to be able to use S-functions for making certain
 computations with S-functions and for answering certain questions about S
functions.
 The translation is determined by the following rules in rich we denote the
 translation of an M-expression E by E*.
 1. If E is an S-expression E* is (QUOTE, E).
 2. Variables and function names that were represented by strings of lower
case letters are translated to the corresponding strings of the corresponding
 uppercase letters. Thus car* is CAR, and subst* is SUBST.
 3. A form f[e1;···;en] is translated to (f∗,e∗
 1 ···,e∗
 n). Thus cons [car [x];
 cdr [x]]∗ is (CONS, (CAR, X), (CDR, X)).
 4. {[p1 → e1;···;pn → en]}∗ is (COND, (p∗
 1,e∗
 1),···,(p∗
 n · e∗
 n)).
 15
5. {λ[[x1;···;xn];E]}∗ is (LAMBDA, (x∗
 1,···,x∗
 n),E∗).
 6. {label[a;E]}∗ is (LABEL, a∗, E∗).
 With these conventions the substitution function whose M-expression is
 label [subst; λ [[x; y; z]; [atom [z] → [eq [y; z] → x; T → z]; T → cons [subst
 [x; y; car [z]]; subst [x; y; cdr [z]]]]]] has the S-expression
 (LABEL, SUBST, (LAMBDA, (X, Y, Z), (COND ((ATOM, Z), (COND,
 (EQ, Y, Z), X), ((QUOTE, T), Z))), ((QUOTE, T), (CONS, (SUBST, X, Y,
 (CAR Z)), (SUBST, X, Y, (CDR, Z)))))))
 This notation is writable and somewhat readable. It can be made easier
 to read and write at the cost of making its structure less regular. If more
 characters were available on the computer, it could be improved considerably.4
 f. The Universal S-Function apply. There is an S-function apply with the
 property that if f is an S-expression for an S-function f′ and args is a list of
 arguments of the form (arg1,···,argn), where arg1,···,argn are arbitrary S
expressions, then apply[f;args] and f′[arg1;···;argn] are defined for the same
 values of arg1,···,argn, and are equal when defined. For example,
 λ[[x; y]; cons[car[x]; y]][(A, B);(C,D)]
 =apply[(LAMBDA,(X,Y),(CONS,(CAR,X),Y));((A,B),(C,D))] = (A,C,D)
 The S-function apply is defined by
 apply[f;args] = eval[cons[f;appq[args]];NIL],
 where
 appq[m] = [null[m] → NIL;T → cons[list[QUOTE;car[m]];appq[cdr[m]]]]
 and
 eval[e; a] = [
 41995: More characters were made available on SAIL and later on the Lisp machines.
 Alas, the world went back to inferior character sets again—though not as far back as when
 this paper was written in early 1959.
 16
atom [e] → assoc [e; a];
 atom [car [e]] → [
 eq [car [e]; QUOTE] → cadr [e];
 eq [car [e]; ATOM] → atom [eval [cadr [e]; a]];
 eq [car [e]; EQ] → [eval [cadr [e]; a] = eval [caddr [e]; a]];
 eq [car [e]; COND] → evcon [cdr [e]; a];
 eq [car [e]; CAR] → car [eval [cadr [e]; a]];
 eq [car [e]; CDR] → cdr [eval [cadr [e]; a]];
 eq [car [e]; CONS] → cons [eval [cadr [e]; a]; eval [caddr [e];
 a]]; T → eval [cons [assoc [car [e]; a];
 evlis [cdr [e]; a]]; a]];
 eq [caar [e]; LABEL] → eval [cons [caddar [e]; cdr [e]];
 cons [list [cadar [e]; car [e]; a]];
 eq [caar [e]; LAMBDA] → eval [caddar [e];
 append [pair [cadar [e]; evlis [cdr [e]; a]; a]]]
 and
 and
 evcon[c;a] = [eval[caar[c];a] → eval[cadar[c];a];T → evcon[cdr[c];a]]
 evlis[m;a] = [null[m] → NIL;T → cons[eval[car[m];a];evlis[cdr[m];a]]]
 17
We now explain a number of points about these definitions. 5
 1. apply itself forms an expression representing the value of the function
 applied to the arguments, and puts the work of evaluating this expression onto
 a function eval. It uses appq to put quotes around each of the arguments, so
 that eval will regard them as standing for themselves.
 2. eval[e;a] has two arguments, an expression e to be evaluated, and a list
 of pairs a. The first item of each pair is an atomic symbol, and the second is
 the expression for which the symbol stands.
 3. If the expression to be evaluated is atomic, eval evaluates whatever is
 paired with it first on the list a.
 4. If e is not atomic but car[e] is atomic, then the expression has one of the
 forms (QUOTE,e)or(ATOM,e)or(EQ,e1,e2)or(COND,(p1,e1),···,(pn,en)),
 or (CAR,e) or (CDR,e) or (CONS,e1,e2) or (f,e1,···,en) where f is an
 atomic symbol.
 In the case (QUOTE,e) the expression e, itself, is taken. In the case of
 (ATOM,e) or (CAR,e) or (CDR,e) the expression e is evaluated and the
 appropriate function taken. In the case of (EQ,e1,e2) or (CONS,e1,e2) two
 expressions have to be evaluated. In the case of (COND,(p1,e1),···(pn,en))
 the p’s have to be evaluated in order until a true p is found, and then the
 corresponding e must be evaluated. This is accomplished by evcon. Finally, in
 the case of (f,e1,···,en) we evaluate the expression that results from replacing
 f in this expression by whatever it is paired with in the list a.
 5. The evaluation of ((LABEL,f,E),e1,···,en) is accomplished by eval
uating (E,e1,···,en) with the pairing (f,(LABEL,f,E)) put on the front of
 the previous list a of pairs.
 6. Finally, the evaluation of ((LAMBDA,(x1,···,xn),E),e1,···en) is ac
complished by evaluating E with the list of pairs ((x1,e1),···,((xn,en)) put
 on the front of the previous list a.
 The list a could be eliminated, and LAMBDA and LABEL expressions
 evaluated by substituting the arguments for the variables in the expressions
 E. Unfortunately, difficulties involving collisions of bound variables arise, but
 they are avoided by using the list a.
 51995: This version isn’t quite right. A comparison of this and other versions of eval
 including what was actually implemented (and debugged) is given in “The Influence of the
 Designer on the Design” by Herbert Stoyan and included in Artificial Intelligence and Math
ematical Theory of Computation: Papers in Honor of John McCarthy, Vladimir Lifschitz
 (ed.), Academic Press, 1991
 18
Calculating the values of functions by using apply is an activity better
 suited to electronic computers than to people. As an illustration, however, we
 now give some of the steps for calculating
 apply [(LABEL, FF, (LAMBDA, (X), (COND, (ATOM, X), X), ((QUOTE,
 T),(FF, (CAR, X))))));((A· B))] = A
 The first argument is the S-expression that represents the function ff defined
 in section 3d. We shall abbreviate it by using the letter φ. We have
 apply [φ; ( (A·B) )]
 = eval [((LABEL, FF, ψ), (QUOTE, (A·B))); NIL]
 where ψ is the part of φ beginning (LAMBDA
 = eval[((LAMBDA, (X), ω), (QUOTE, (A·B)));((FF, φ))]
 where ω is the part of ψ beginning (COND
 = eval [(COND, (π1,ϵ1),(π2,ϵ2)); ((X, (QUOTE, (A·B) ) ), (FF, φ) )]
 Denoting ((X, (QUOTE, (A·B))), (FF, φ)) by a, we obtain
 = evcon [((π1,ϵ1), (π2,ϵ2)); a]
 This involves eval [π1;a]
 = eval [( ATOM, X); a]
 = atom [eval [X; a]]
 = atom [eval [assoc [X; ((X, (QUOTE, (A·B))), (FF,φ))];a]]
 = atom [eval [(QUOTE, (A·B)); a]]
 = atom [(A·B)],
 = F
 Our main calulation continues with
 19
apply [φ; ((A·B))]
 = evcon [((π2,ϵ2,));a],
 which involves eval [π2;a] = eval [(QUOTE, T); a] = T
 Our main calculation again continues with
 apply [φ; ((A·B))]
 = eval [ϵ2;a]
 = eval [(FF, (CAR, X));a]
 = eval [Cons [φ; evlis [((CAR, X)); a]]; a]
 Evaluating evlis [((CAR, X)); a] involves
 eval [(CAR, X); a]
 = car [eval [X; a]]
 = car [(A·B)], where we took steps from the earlier computation of atom [eval [X; a]] = A,
 and so evlis [((CAR, X)); a] then becomes
 list [list [QUOTE; A]] = ((QUOTE, A)),
 and our main quantity becomes
 = eval [(φ, (QUOTE, A)); a]
 The subsequent steps are made as in the beginning of the calculation. The
 LABEL and LAMBDA cause new pairs to be added to a, which gives a new
 list of pairs a1. The π1 term of the conditional eval [(ATOM, X); a1] has the
 20
value T because X is paired with (QUOTE, A) first in a1, rather than with
 (QUOTE, (A·B)) as in a.
 Therefore we end up with eval [X; a1] from the evcon, and this is just A.
 g. Functions with Functions as Arguments. There are a number of useful
 functions some of whose arguments are functions. They are especially useful
 in defining other functions. One such function is maplist[x;f] with an S
expression argument x and an argument f that is a function from S-expressions
 to S-expressions. We define
 maplist[x;f] = [null[x] → NIL;T → cons[f[x];maplist[cdr[x];f]]]
 The usefulness of maplist is illustrated by formulas for the partial derivative
 with respect to x of expressions involving sums and products of x and other
 variables. The S-expressions that we shall differentiate are formed as follows.
 1. An atomic symbol is an allowed expression.
 2. If e1,e2,···,en are allowed expressions, ( PLUS, e1,···,en) and (TIMES,
 e1, · · ·, en) are also, and represent the sum and product, respectively, of e1,···,en.
 This is, essentially, the Polish notation for functions, except that the in
clusion of parentheses and commas allows functions of variable numbers of
 arguments. An example of an allowed expression is (TIMES, X, (PLUS, X,
 A), Y), the conventional algebraic notation for which is X(X + A)Y.
 Our differentiation formula, which gives the derivative of y with respect to
 x, is
 diff [y; x] = [atom [y] → [eq [y; x] → ONE; T → ZERO]; eq [car [Y]; PLUS]
 →cons [PLUS; maplist [cdr [y]; λ[[z]; diff [car [z]; x]]]]; eq[car [y]; TIMES] →
 cons[PLUS; maplist[cdr[y]; λ[[z]; cons [TIMES; maplist[cdr [y]; λ[[w]; ¬ eq [z;
 w] → car [w]; T → diff [car [[w]; x]]]]]]]
 The derivative of the expression (TIMES, X, (PLUS, X, A), Y), as com
puted by this formula, is
 (PLUS, (TIMES, ONE, (PLUS, X, A), Y), (TIMES, X, (PLUS, ONE,
 ZERO), Y), (TIMES, X, (PLUS, X, A), ZERO))
 Besides maplist, another useful function with functional arguments is search,
 which is defined as
 search[x;p;f;u] = [null[x] → u;p[x] → f[x];T → search[cdr[x];p;f;u]
 21
The function search is used to search a list for an element that has the property
 p, and if such an element is found, f of that element is taken. If there is no
 such element, the function u of no arguments is computed.
 4 The LISP Programming System
 The LISP programming system is a system for using the IBM 704 computer to
 compute with symbolic information in the form of S-expressions. It has been
 or will be used for the following purposes:
 l. Writing a compiler to compile LISP programs into machine language.
 2. Writing a program to check proofs in a class of formal logical systems.
 3. Writing programs for formal differentiation and integration.
 4. Writing programs to realize various algorithms for generating proofs in
 predicate calculus.
 5. Making certain engineering calculations whose results are formulas
 rather than numbers.
 6. Programming the Advice Taker system.
 The basis of the system is a way of writing computer programs to evaluate
 S-functions. This will be described in the following sections.
 In addition to the facilities for describing S-functions, there are facilities
 for using S-functions in programs written as sequences of statements along the
 lines of FORTRAN (4) or ALGOL (5). These features will not be described
 in this article.
 a. Representation of S-Expressions by List Structure. A list structure is a
 collection of computer words arranged as in figure 1a or 1b. Each word of the
 list structure is represented by one of the subdivided rectangles in the figure.
 The left box of a rectangle represents the address field of the word and the
 right box represents the decrement field. An arrow from a box to another
 rectangle means that the field corresponding to the box contains the location
 of the word corresponding to the other rectangle.
 22
An S-expression x that is not atomic is represented by a word, the address
 and decrement parts of which contain the locations of the subexpressions car[x]
 and cdr[x], respectively. If we use the symbols A, B, etc. to denote the
 locations of the association list of these symbols, then the S-expression ((A ·
 B) · (C · (E · F))) is represented by the list structure a of figure 2. Turning
 to the list form of S-expressions, we see that the S-expression (A,(B,C),D),
 which is an abbreviation for (A·((B ·(C ·NIL))·(D ·NIL))), is represented
 by the list structure of figure 2b.
 23
 It is permitted for a substructure to occur in more than one place in a list
 structure, as in figure 1b, but it is not permitted for a structure to have cycles,
 as in figure 1c. An atomic symbol is represented in the computer by a list
 structure of special form called the association list of the symbol. The address
 f
 ield of the first word contains a special constant which enables the program to
 tell that this word represents an atomic symbol. We shall describe association
 lists in section 4b.--
 Fig. 1--------------------
--
A--
 D
 C--
 A B
 (a)
 E F
B
 (b)
Figure 2
 C
 When a list structure is regarded as representing a list, we see that each term
 of the list occupies the address part of a word, the decrement part of which
 points to the word containing the next term, while the last word has NIL in
 its decrement.
 An expression that has a given subexpression occurring more than once
 can be represented in more than one way. Whether the list structure for
 the subexpression is or is not repeated depends upon the history of the pro
gram. Whether or not a subexpression is repeated will make no difference
 in the results of a program as they appear outside the machine, although it
 will affect the time and storage requirements. For example, the S-expression
 ((A·B)·(A·B)) can be represented by either the list structure of figure 3a or
 3b.----
 A B AB
 (a)--
 A B
 (b)
 Figure 3
 The prohibition against circular list structures is essentially a prohibition
 24
against an expression being a subexpression of itself. Such an expression could
 not exist on paper in a world with our topology. Circular list structures would
 have some advantages in the machine, for example, for representing recursive
 functions, but difficulties in printing them, and in certain other operations,
 make it seem advisable not to use them for the present.
 The advantages of list structures for the storage of symbolic expressions
 are:
 1. The size and even the number of expressions with which the program
 will have to deal cannot be predicted in advance. Therefore, it is difficult to
 arrange blocks of storage of fixed length to contain them.
 2. Registers can be put back on the free-storage list when they are no longer
 needed. Even one register returned to the list is of value, but if expressions
 are stored linearly, it is difficult to make use of blocks of registers of odd sizes
 that may become available.
 3. An expression that occurs as a subexpression of several expressions need
 be represented in storage only once.
 b. Association Lists6 . In the LISP programming system we put more in
 the association list of a symbol than is required by the mathematical system
 described in the previous sections. In fact, any information that we desire to
 associate with the symbol may be put on the association list. This information
 may include: the print name, that is, the string of letters and digits which
 represents the symbol outside the machine; a numerical value if the symbol
 represents a number; another S-expression if the symbol, in some way, serves
 as a name for it; or the location of a routine if the symbol represents a function
 for which there is a machine-language subroutine. All this implies that in the
 machine system there are more primitive entities than have been described in
 the sections on the mathematical system.
 For the present, we shall only describe how print names are represented
 on association lists so that in reading or printing the program can establish
 a correspondence between information on punched cards, magnetic tape or
 printed page and the list structure inside the machine. The association list of
 the symbol DIFFERENTIATE has a segment of the form shown in figure 4.
 Here pname is a symbol that indicates that the structure for the print name
 of the symbol whose association list this is hanging from the next word on
 the association list. In the second row of the figure we have a list of three
 words. The address part of each of these words points to a Word containing
 61995: These were later called property lists.
 25
six 6-bit characters. The last word is filled out with a 6-bit combination that
 does not represent a character printable by the computer. (Recall that the
 IBM 7O4 has a 36-bit word and that printable characters are each represented
 by 6 bits.) The presence of the words with character information means that
 the association lists do not themselves represent S-expressions, and that only
 some of the functions for dealing with S-expressions make sense within an
 association list.
 ...
pname--
DIFFER--
ENTIAT
 ....--
 E ??????
 Figure 4
 c. Free-Storage List. At any given time only a part of the memory reserved
 for list structures will actually be in use for storing S-expressions. The remain
ing registers (in our system the number, initially, is approximately 15,000) are
 arranged in a single list called the free-storage list. A certain register, FREE,
 in the program contains the location of the first register in this list. When
 a word is required to form some additional list structure, the first word on
 the free-storage list is taken and the number in register FREE is changed to
 become the location of the second word on the free-storage list. No provision
 need be made for the user to program the return of registers to the free-storage
 list.
 This return takes place automatically, approximately as follows (it is nec
essary to give a simplified description of this process in this report): There is
 a fixed set of base registers in the program which contains the locations of list
 structures that are accessible to the program. Of course, because list struc
tures branch, an arbitrary number of registers may be involved. Each register
 that is accessible to the program is accessible because it can be reached from
 one or more of the base registers by a chain of car and cdr operations. When
 26
the contents of a base register are changed, it may happen that the register
 to which the base register formerly pointed cannot be reached by a car − cdr
 chain from any base register. Such a register may be considered abandoned
 by the program because its contents can no longer be found by any possible
 program; hence its contents are no longer of interest, and so we would like to
 have it back on the free-storage list. This comes about in the following way.
 Nothing happens until the program runs out of free storage. When a free
 register is wanted, and there is none left on the free-storage list, a reclamation7
 cycle starts.
 First, the program finds all registers accessible from the base registers and
 makes their signs negative. This is accomplished by starting from each of the
 base registers and changing the sign of every register that can be reached from
 it by a car − cdr chain. If the program encounters a register in this process
 which already has a negative sign, it assumes that this register has already
 been reached.
 After all of the accessible registers have had their signs changed, the pro
gramgoes through the area of memory reserved for the storage of list structures
 and puts all the registers whose signs were not changed in the previous step
 back on the free-storage list, and makes the signs of the accessible registers
 positive again.
 This process, because it is entirely automatic, is more convenient for the
 programmer than a system in which he has to keep track of and erase un
wanted lists. Its efficiency depends upon not coming close to exhausting the
 available memory with accessible lists. This is because the reclamation process
 requires several seconds to execute, and therefore must result in the addition
 of at least several thousand registers to the free-storage list if the program is
 not to spend most of its time in reclamation.
 d. Elementary S-Functions in the Computer. We shall now describe the
 computer representations of atom, = , car, cdr, and cons. An S-expression
 is communicated to the program that represents a function as the location of
 the word representing it, and the programs give S-expression answers in the
 same form.
 atom. As stated above, a word representing an atomic symbol has a special
 7We already called this process “garbage collection”, but I guess I chickened out of using
 it in the paper—or else the Research Laboratory of Electronics grammar ladies wouldn’t let
 me.
 27
constant in its address part: atom is programmed as an open subroutine that
 tests this part. Unless the M-expression atom[e] occurs as a condition in a
 conditional expression, the symbol T or F is generated as the result of the
 test. In case of a conditional expression, a conditional transfer is used and the
 symbol T or F is not generated.
 eq. The program for eq[e;f] involves testing for the numerical equality of
 the locations of the words. This works because each atomic symbol has only
 one association list. As with atom, the result is either a conditional transfer
 or one of the symbols T or F.
 car. Computing car[x] involves getting the contents of the address part of
 register x. This is essentially accomplished by the single instruction CLA 0, i,
 where the argument is in index register, and the result appears in the address
 part of the accumulator. (We take the view that the places from which a
 function takes its arguments and into which it puts its results are prescribed
 in the definition of the function, and it is the responsibility of the programmer
 or the compiler to insert the required datamoving instructions to get the results
 of one calculation in position for the next.) (“car” is a mnemonic for “contents
 of the address part of register.”)
 cdr. cdr is handled in the same way as car, except that the result appears
 in the decrement part of the accumulator (“cdr” stands for “contents of the
 decrement part of register.”)
 cons. The value of cons[x;y] must be the location of a register that has x
 and y in its address and decrement parts, respectively. There may not be such
 a register in the computer and, even if there were, it would be time-consuming
 to find it. Actually, what we do is to take the first available register from the
 free-storage list, put x and y in the address and decrement parts, respectively,
 and make the value of the function the location of the register taken. (“cons”
 is an abbreviation for “construct.”)
 It is the subroutine for cons that initiates the reclamation when the free
storage list is exhausted. In the version of the system that is used at present
 cons is represented by a closed subroutine. In the compiled version, cons is
 open.
 e. Representation of S-Functions by Programs. The compilation of func
tions that are compositions of car, cdr, and cons, either by hand or by a
 compiler program, is straightforward. Conditional expressions give no trouble
 except that they must be so compiled that only the p’s and e’s that are re
28
quired are computed. However, problems arise in the compilation of recursive
 functions.
 In general (we shall discuss an exception), the routine for a recursive func
tion uses itself as a subroutine. For example, the program for subst[x;y;z] uses
 itself as a subroutine to evaluate the result of substituting into the subexpres
sions car[z] and cdr[z]. While subst[x;y;cdr[z]] is being evaluated, the result
 of the previous evaluation of subst[x;y;car[z]] must be saved in a temporary
 storage register. However, subst may need the same register for evaluating
 subst[x; y;cdr[z]]. This possible conflict is resolved by the SAVE and UN
SAVE routines that use the public push-down list 8. The SAVE routine is
 entered at the beginning of the routine for the recursive function with a re
quest to save a given set of consecutive registers. A block of registers called
 the public push-down list is reserved for this purpose. The SAVE routine has
 an index that tells it how many registers in the push-down list are already
 in use. It moves the contents of the registers which are to be saved to the
 f
 irst unused registers in the push-down list, advances the index of the list, and
 returns to the program from which control came. This program may then
 freely use these registers for temporary storage. Before the routine exits it
 uses UNSAVE, which restores the contents of the temporary registers from
 the push-down list and moves back the index of this list. The result of these
 conventions is described, in programming terminology, by saying that the re
cursive subroutine is transparent to the temporary storage registers.
 f. Status of the LISP Programming System (February 1960). A variant of
 the function apply described in section 5f has been translated into a program
 APPLY for the IBM 704. Since this routine can compute values of S-functions
 given their descriptions as S-expressions and their arguments, it serves as an
 interpreter for the LISP programming language which describes computation
 processes in this way.
 The program APPLY has been imbedded in the LISP programming system
 which has the following features:
 1. The programmer maydefine anynumber ofS-functions by S-expressions.
 these functions may refer to each other or to certain S-functions represented
 by machine language program.
 2. The values of defined functions may be computed.
 3. S-expressions may be read and printed (directly or via magnetic tape).
 81995: now called a stack
 29
4. Some error diagnostic and selective tracing facilities are included.
 5. The programmer may have selected S-functions compiled into machine
 language programs put into the core memory. Values of compiled functions
 are computed about 60 times as fast as they would if interpreted. Compilation
 is fast enough so that it is not necessary to punch compiled program for future
 use.
 6. A “program feature” allows programs containing assignment and go to
 statements in the style of ALGOL.
 7. Computation with floating point numbers is possible in the system, but
 this is inefficient.
 8. A programmer’s manual is being prepared. The LISP programming
 system is appropriate for computations where the data can conveniently be
 represented as symbolic expressions allowing expressions of the same kind as
 subexpressions. A version of the system for the IBM 709 is being prepared.
 5 Another Formalism for Functions of Sym
bolic Expressions
 There are a number of ways of defining functions of symbolic expressions which
 are quite similar to the system we have adopted. Each of them involves three
 basic functions, conditional expressions, and recursive function definitions, but
 the class of expressions corresponding to S-expressions is different, and so are
 the precise definitions of the functions. We shall describe one of these variants
 called linear LISP.
 The L-expressions are defined as follows:
 1. A finite list of characters is admitted.
 2. Any string of admitted characters in an L-expression. This includes the
 null string denoted by Λ.
 There are three functions of strings:
 1. first[x] is the first character of the string x.
 first[Λ] is undefined. For example: first[ABC] = A
 2. rest[x] is the string of characters which remains when the first character
 of the string is deleted.
 rest[Λ] is undefined. For example: rest[ABC] = BC.
 3. combine[x;y] is the string formed by prefixing the character x to the
 string y. For example: combine[A;BC] = ABC
 30
There are three predicates on strings:
 1. char[x], x is a single character.
 2. null[x], x is the null string.
 3. x =y, defined for x and y characters.
 The advantage of linear LISP is that no characters are given special roles,
 as are parentheses, dots, and commas in LISP. This permits computations
 with all expressions that can be written linearly. The disadvantage of linear
 LISP is that the extraction of subexpressions is a fairly involved, rather than
 an elementary, operation. It is not hard to write, in linear LISP, functions that
 correspond to the basic functions of LISP, so that, mathematically, linear LISP
 includes LISP. This turns out to be the most convenient way of programming,
 in linear LISP, the more complicated manipulations. However, if the functions
 are to be represented by computer routines, LISP is essentially faster.
 6 Flowcharts and Recursion
 Since both the usual form of computer program and recursive function defi
nitions are universal computationally, it is interesting to display the relation
 between them. The translation of recursive symbolic functions into computer
 programs was the subject of the rest of this report. In this section we show
 how to go the other way, at least in principle.
 The state of the machine at any time during a computation is given by the
 values of a number of variables. Let these variables be combined into a vector
 ξ. Consider a program block with one entrance and one exit. It defines and is
 essentially defined by a certain function f that takes one machine configuration
 into another, that is, f has the form ξ′ = f(ξ). Let us call f the associated
 function of the program block. Now let a number of such blocks be combined
 into a program by decision elements π that decide after each block is completed
 which block will be entered next. Nevertheless, let the whole program still have
 one entrance and one exit.
 31
?-?
 π1
 XXXz
 f1
 HHHj+
 π2
 ?
 f3
 T
 ?
 π3
 ?
 f4
 ?
 ?
 S
 f2
 Figure 5
 Wegive as an example the flowcart of figure 5. Let us describe the function
 r[ξ] that gives the transformation of the vector ξ between entrance and exit
 of the whole block. We shall define it in conjunction with the functions s(ξ),
 and t[ξ], which give the transformations that ξ undergoes between the points
 S and T, respectively, and the exit. We have
 r[ξ] = [π11[ξ] → S[f1[ξ]];T → S[f2[ξ]]]
 S[ξ] = [π21[ξ] → r[ξ];T → t[f3[ξ]]]
 t[ξ] = [π3I[ξ] → f4[ξ];π32[ξ] → r[ξ];T → t[f3[ξ]]]
 Given a flowchart with a single entrance and a single exit, it is easy to
 write down the recursive function that gives the transformation of the state
 vector from entrance to exit in terms of the corresponding functions for the
 computation blocks and the predicates of the branch. In general, we proceed
 as follows.
 In figure 6, let β be an n-way branch point, and let f1,···,fn be the
 computations leading to branch points β1,β2,···,βn. Let φ be the function
 32
thattransformsξbetweenβandtheexitof thechart,andletφ1,···,φnbe
 thecorrespondingfunctionsforβ1,···,βn.Wethenwrite
 φ[ξ]=[p1[ξ]→φ1[f1[ξ]];···;pn[ξ]→φn[ξ]]]
 @
 @@
 @
 @ @
 ?
 A
 A
 A
 AAU
 C
 C CW ?
 ....
 .....
 ..... f1 f2 fn
 β
 β1 β2
 βn
 φ1 φ2
 φn
 φ
 Figure6
 7 Acknowledgments
 Theinadequacyoftheλ-notationfornamingrecursivefunctionswasnoticed
 byN.Rochester, andhediscoveredanalternative tothe solution involving
 labelwhichhasbeenusedhere. The formof subroutine forconswhichper
mits its compositionwithother functionswas invented, inconnectionwith
 anotherprogrammingsystem, byC.GerberickandH.L.Gelernter, of IBM
 Corporation. TheLlSPprogrammingsystemwasdevelopedbyagroupin
cludingR.Brayton,D.Edwards,P.Fox,L.Hodes,D.Luckham,K.Maling,
 J.McCarthy,D.Park,S.Russell.
 ThegroupwassupportedbytheM.I.T.ComputationCenter,andbythe
 M.I.T.ResearchLaboratoryofElectronics(whichissupportedinpartbythe
 theU.S.Army(SignalCorps),theU.S.AirForce(OfficeofScientificResearch,
 AirResearchandDevelopmentCommand),andtheU.S.Navy(OfficeofNaval
 Research)).Theauthoralsowishestoacknowledgethepersonalfinancialsup
33
port of the Alfred P. Sloan Foundation.
 REFERENCES
 1. J. McCARTHY, Programs with common sense, Paper presented at the
 Symposium on the Mechanization of Thought Processes, National Physical
 Laboratory, Teddington, England, Nov. 24-27, 1958. (Published in Proceed
ings of the Symposium by H. M. Stationery Office).
 2. A. NEWELLANDJ.C.SHAW,Programmingthelogictheory machine,
 Proc. Western Joint Computer Conference, Feb. 1957.
 3. A. CHURCH, The Calculi of Lambda-Conversion (Princeton University
 Press, Princeton, N. J., 1941).
 4. FORTRAN Programmer’s Reference Manual, IBM Corporation, New
 York, Oct. 15, 1956.
 5. A. J. PERLIS AND K. SAMELS0N, International algebraic language,
 Preliminary Report, Comm. Assoc. Comp. Mach., Dec. 1958.
 34 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=














 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 id: mccarthy1960-recursive-symbolic-expressions
  title: "Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I"
  author: "John McCarthy"
  venue: "Communications of the ACM"
  volume: 3
  number: 4
  pages: "184–195"
  year: 1960
  notes: "Foundational paper introducing the LISP language (‘LISt Processor’)"
 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 
Recursive Functions of Symbolic Expressions 
Their Computation by Machine, Part I 
John McCarthytts Institute of Technology, Cambridge, Mass. 
1. 
Introduction 
A programming system called LISP (for lASt Processor) 
has been developed for the IBM 704 computer by the 
Artificial Intelligence group at M.I.T. The system was 
designed to facilitate experiments with a proposed system 
called the Advice Taker, whereby a machine could be 
instructed to handle declarative as well as imperative 
sentences and could exhibit "common sense" in carrying 
out its instructions. The original proposal It] for the Advice 
Taker was made in November 1958. The main require- 
ment was a programming system for manipulating ex- 
pressions representing formalized declarative and irnpera- 
live sentences so that the Advice Taker system could make 
deductions. 
In the course of its development the Lisp system went 
through several stages of simplification and eventually 
came to be based on a scheme for representing the partial 
recursive functions of a certain class of symbolic expres- 
sions. This representation is independent of the IBM 704 
computer, or of any other electronic computer, and it now 
seems expedient to expound the system by starting with 
the class of expressions called S-expressions and the func- 
tions called S-functions. 
In this article, we first describe a formalism for defining 
functions reeursively. We believe this formalism has ad- 
vantages both as a programming language and as vehicle 
for developing a theory of computation. Next, we describe 
S-expressions and S-functions, give some examples, and 
then describe the universM S-function apply which plays 
the theoretical role of a universal Turing machine and 
the practical role of an interpreter. Then we describe the 
representation of S-expressions in the memmT of the 
IBM 704 by list structures similar to those used by Newell, 
Shaw and Simon [2], and the representation of S-functions 
by program. Then we mention the main features of the 
Lisp programming system for the IBM 704. Next comes 
another way of describing computations with symbolic 
expressions, and finally we give a recursive function in- 
terpretation of flow charts. 
We hope to describe some of the sylnbolie computations 
for which LISP has been used in another paper, and also to 
give elsewhere some applications of our reeursive function 
formalism to mathematical logic and to the problem of 
mechanical theorem proving. 
and 
2. Functions and Function Definitions 
We shMl need a number of mathematical ideas ar:d 
notations concerning functions in general. Most of the 
ideas are well known, but the notion of conditional e,~pre~'- 
sion is believed to be new, and ihe use of conditional 
expressions permits functions to be defined recursively in a 
new and convenient way. 
a. Partial Functions. A partial function is a funct on 
that is defined only on part of its domain. Partial funetio:~s 
necessarily arise when functions are defined by eomputa~ 
tions because for some values of the arguments t:he Pomp:> 
ration defining the value of the function may not ter- 
minate. However, some of our elementary functions wilt be 
defined as partial functions. 
b. Propositional Expres.s'ions and Predicates. A t)ropo~i- 
tionM expression is an expression whose possible values 
are T (for truth) and F (for falsity). We shall assume 
that the reader is fanfiliar with the propositionM eom~ee- 
lives A ("and"), V ("or"), and ~ ("not"), Typieai 
propositional expressions are: 
x<y 
(x < y) A (b = e) 
x is prime 
A predicate is a function whose range consists of ih{: 
truth values T and F. 
e. Conditional Expressions. The dependence of truth 
values on the vahtes of quantities of other kinds is ex- 
pressed in mathematics by predicates, and the depende~ee 
of truth values on other truth values by logical comxee- 
~ives. However, the notations for expressing symbol (alE" 
the dependence of quantities of other kinds on trutt~ 
vMues is inadequate, so that English words and phrases 
are generMly used for expressing these depende~tces i:~ 
texts that, describe other dependences symbolically. I!'<~r 
example, the function Ix I is ustmlly defined in words. 
Conditional expressions are a deviee for expressing the 
dependence of quantities on propositional quantities. :\ 
conditional expression has the form 
(p: -+ el, -.- , p~ --+ e,,) 
where the p's are propositionM expressions and the e's are 
expressions of any kind. It may be read, "If p~ thexx <, 
184 
Communications of the ACM 
,iherwise if p2 then e2, - - • , otherwise if p,, then e,, ," or 
..p~ y/el(Is e3 , "" , P,, yields e,, ." 
We now give the rules :for determining whether the value 
r,f !p, --' e,, .,' , p,, --' e,) is defined, and if so what its 
value is. Examine the p's from left. to right. If a p whose 
valu~ is T is eilcountered before any p whose vahm is 
~mdefilied is eneom~tered, then the value of the conditional 
,xpressi(m is the value of the corresponding e (if this is 
left ned). If airy undefined p is ene(:mntered before a true p, 
.r if all p's are false, or if the e corresponding to the first 
true p is undefined, then the value of the conditional ex- 
pression is undefined. We now give examples. 
(t 
a~3d 
< 
2--~4,1 
> 
2--+3) 
= 
4 
(2 < 1--~ 4, 2 > 1-~3, 2 > 1--~2) = 3 
zpre;~. : 
!i 
,viii ~'e : 
O/ll/eb 
~yp e~l 
o~ the 
[ 
mde~a- 
collnf¢ ~- 
tr~t 
h 
lly F,:,~ 
worg! 
ities..'~ 
e 
e's ~?~ ~ 
tbet~ el, 
(,2 < 1-->4, T-~3) 
(2 < 1-,6, 
0 
T 
= 
3 -~3) =3 
(1 
(2 < 1--,3, T--,0 ) is nllde[illed 
(2 < I --~ 3, 4 < 1 --~ 4) is undefined 
Some of tile simplest applications of eonditionM expres- 
sia~s are in giving such definitions as 
x 
= 
(x < 0--,-x, iF--~x) 
san x ~ (x <0--,-1, 
x 
== 0--~0, T-~I) 
d. Rccursive Function DefiniHons. By using conditionM 
~:,xpressions we can, without circularity, define functions 
,v formulas in which the defined function occurs. For 
{'xample, we wrile 
l~: = (n = 0-~ 1, T--*n.(n- 
1)1) 
When we use this formula to evaluate 0 [ we get the answer 
i: because of the way in which the value of a conditional 
expression 
was defined, the meaningless expression 
~]- ~} - 
r, 
1)! does not arise. The evaluation of 2! according 
lhi:~ definition proceeds as follows: 
2! - - 
(2 = 0-* 1, T--.2.(2 
2.1! 
= 2.(1 = 0~L - 
1):) 
T-~ 1.(1 -- 1)!) 
= 
= 
2-1-0! -.1.(0 
=2.1.1 
=2 
= 
0-~I,T-~0.(0- 
1)!) 
We now give two other applications of recursive func- 
tion definitions. The greatest common divisor, gcd(m,n), 
of ~wc, positive integers m and n is computed by means of 
the Euclidean algorithm. This algorithm is expressed by 
the recursive function defirfition: 
ged(m,n) = (In > n --, ged(n,m), rem(n,m) 
= 0 -+ m, T --* ged(rem(n,m),m) ) 
where rein(n, In) denotes the remainder left when n is 
divided by m. 
The Newtonian algorithm for obtaining an approximate 
square root of a number a, starting with an initial approxi- 
mation :v and requiring that an acceptable approximation 
y satisfy l y 2 -- a I < e, may be written as 
sqrt(a, x, ~) 
= 
(Ix ~- a I < e--,x,T-~sqrt (a,~ 
1 (x + ~) e)) 
x ' 
The simultaneous reeursive definition of several func- 
tions is also possible, and we shall use such definitions if 
they are required. 
There is no guarantee that tile computation determined 
by a reeursive definition will ever terminate and, for 
example, an attempt to compute n[ from our definition 
will only succeed if n is a non-negative integer. If the com- 
putation does not terminate, the function must be regarded 
as undefined for the given arguments. 
The propositional connectives themselves can be de- 
fined by conditional expressions. We write 
p/~q= 
(p --~ q, T --~ F) 
pVq = (p -~ T, T -* q) 
~-~p = (p-~F,T--~T) 
p D q = (p-~q, T-~T) 
It is readily seen that the right-hand sides of the equa- 
tions have the correct truth tables. If we consider situa- 
tions in which p or q may be undefined, the connectives 
/~ and V are seen to be; noncommutative. For example if 
p is false and q is undefined, we see that according to the 
definitions given above p A q is false, but q A p is unde- 
fined. For our applications this noncommutativity is 
desirable, since p /~ q is computed by first computing p, 
and if p is false q is not computed. :If the computation for 
p does not terminate, we never get around to computing q. 
We shall use propositional connectives in this sense here- 
after. 
e. Functions and Forms. It is usual in mathematics-- 
outside of mathematical logic--to use the word "function" 
imprecisely and to apply it to forms such as y~ -V x. Be- 
cause we shall later compute with expressions for functions, 
we need a distinction between functions and forms and a 
notation for expressing this distinction. This distinction 
and a notation for describing it, from which we deviate 
trivially, is given by Church [3]. 
Let f be an expression that stands for a function of two 
integer variables. It should make sense to write f(3, 4) and 
the value of this expression should be determined. The 
expression y~ + x does not meet this requirement; 
Communications of the ACM 
185 
i 
'?i ¸¸¸¸ 
~!i iilili i :~i 
,!~i i? ,ii!~ 
i 
S, ~i !ii ~ ~ ~ 
!i ~ii i!ii~! 
~ i i 
ii ii? !il 
~:~i i! ~ii'~ 
, 
~ :i 
i i? i!~T i~ ' 
• 
!!!! 
that the refere~ee to sqrt within *he expression sloe :1 for ih~. 
expression as a whole. 
In order to be able to write expressio~s for I'eCursive 
functions, we introduce another ~aotation label(~ ['~ &:.. 
notes the. expression g, provided that oeeurre~ces <)f ~} 
within 8 are to be interpreted as referring to the expres,,:i<, 
as a whole. Thus we can write 
h~bel(sqrt, X((a, x, e), ( [ x'-' - a 
< e --, x, rl' -~ sqrt (a, 1 (x 
2' 
ab; 
a 
nanle 
for 
ollr 
s(tl:'t 
functiolt. 
a 
+ 
x )' ~):~) 
The symbol a ill label(a,g) is also bound thai is, i~ i; 
may be altered systematically without changing the meal- 
ing of the expression. It behqvcs, differently from a \'ariaN~ 
bound by a X, howe\'er. 
3. Reeursive Functions of S) mbolic Expressions 
{ 
0 
We shall first define a class of symbolic express ~ s :i~ 
terms of ordered pairs and lists. Then we shall define five, g 
elementary functions and predicates, and build front them ~i' 
by composition, conditional expressions, and "(ru,sv~:, 
definitions an extensive class of functions of which w~ ; 
sh'dl give a number of examples. We shall lhen show how 
these functions themselves can be expressed as syr~bol c 
expressions, and we shah define a universal ftlllCtiOtt 
' 
(P] 
g 
¢ 
that Mlows us to compute front the expression for a gi~t~ 
function its value for given arguments. Finally, we shal i 
define some functions with functions as argume~ts :u~d ill' 
giw; some useful examples. 
;i:+ 
ii 
i~ I 
a. A Class qf S!]nzbolic Expressions. We shall now <te{i~+~, { 
y~ + x(3, 4) is not a conventional no~ati(m, and if we 
attempted to define it we would be uneert%ir~ whether its 
valtte would turn out, to be i13 or 1.9. Church calls a,n expres- 
sion like ye + x a form. A form can be eot~verted into a 
ftmetion if we can determine the, eorrespondenee between 
the variables occurring in the form and the ordered list of 
arguments of the desired function. This is accomplished 
by Church's X-flotation. 
If ~;is ~ form in variables xl , -.. , x~,, then X((xt , ,.. , 
x,,), ~;) will t:>(:~ taken to be the function of n variables whose 
value is determned by substituting the arguments for lhe 
variables x~, • • - , x~, in that order in g and evaluating the 
resulting expression. For example, X((x,y),ye+x) is a 
function of two variables, and X ( (x, y), y~ +x) (3, 4:) - 19. 
The variables occurring in the list of variables of a X-ex- 
pression are dummy or bound, like, variables of integration 
in a definite integral. That is, we may change the names 
of the bound w~riables in a function expression without 
changing the vMue of the expression, provided that we 
make tile same change for each occurrence of the wu'iable 
and do not make two variM)les lhe same that previously 
were different. Thus X((x,y),y"'+x),X((u,v), v~+u) and 
X((y, x), xe+y) denote the same function. 
We shall frequently use expressions in which some of the 
wmables are bound by X's and others are not. Such art ex- 
pression may be regarded as defining a function with 
parameters. The unbound variables are (;ailed free vari- 
ables. 
An adequate notation that distinguishes functions from 
forms allows an unambiguous treatnmnt of functions of 
ftmetions. It, would involve too much of a digression to give 
examples here, but we shall use functions with functions as 
arguments later in this report. 
Difticulties arise in combining functions described by 
X-expressions, or by arty other notation involving variables, 
because different bound variables may be represented by 
the same symbol. This is called collision of bound vari- 
ables. There is a notation involving operators that are 
called eombinators for combining functions without the use 
of variables, Unfortunately, the combinatory expressions 
for interesting combinations of functions term to be lengthy 
and unreadable. 
f. 
Expressions for Recursive Functions. The X-notation is 
inadequate for naming functions defined recursively. For 
example, using X's, we can convert the definition 
sqrt(a, x, e) 
J. 
a 
( ix" -- a I < e -~ x, T -~ sqrt(a, 2(x + x ), e)) 
into 
sqrt = X((a,x,¢),(lx 2 -- a,l < e---+ x, T'---~ 
i 
a) 
sqrt (a, 2(x + x ' 
+))) 
but the right-hand side cannot serve as an expression for 
the fimetion because there would be nothing to indicate 
186 
the S-expressions (S st'rods for symbolic). They are for ~ed :' 
by ttsittg the special chara(.ters 
) 
( 
and an infinite set of distinguishable atomic symbols. For 
atomic symbols, we shall use strings of capital l,atin lette~ 
and digits with single imbedded blanks. Ex'm@es *~f 
atomic symbols are 
A 
ABA 
APPLE PIE NUMBER 3 
There is a twofold reason for departing from the usual 
mathematieM practice of using single letters for atomic 
synlbols. First, computer programs frequently requir<' 
hundreds of distinguishable symbols thai, nmst be formed 
from the 47 characters that are printable by the IBM 7N 
computer. Second, it is convenient to allow English wo~ds 
and phrases to stand for atomic entities for mnem(mic 
reasons. The symbols are atomic in the sense that any sui:- 
structure they may have as sequences of characters is it, 
nored. We assume only that= different symbols cam be 
distinguished. 
Comnumications of the ACI~'I 
t 
for iL 
p>e:ssi>¢ 
{ 
e 
m<~. 
ms 
ma ~he!~ 
"eea ~:s ve : 
'hi,e~i w, {e 
,aow h*.:~'.~ : 
s,:,,m}',~,ii~ 
we :,t~atl 
¢; 
'e :forme~ 
i~ ¸ 
~iiii! 
~' 
be, is, 
{ in Ieiter~ 
re'pitS :{ 
{ 
i" 
reqti~ 
i)e f0t:ff# 
lish ~0r45 
L airy SII~ 
'-~t ers is if.- 
is 
,ca1 
i 
S-expressi(>ns are th.el~ defined as follows: 
1. M()mic symbols are S-expressions° 
i?. If e~ alld e.., are S-expressions, so is (el'e2). 
Examples of S-expressions are 
AB 
(~v. B) 
(tAB.O)-D) 
An S-expression is then simply an ordered pair, the 
wrms of which may be atomic symbols or simpler S-expres- 
si,ms. We can represent a tist of arbitrary length in terms 
<>f S-expressions as follows. The list 
) 
: 
(m~, me, "'" ,m,,) 
is represented by the S-expression 
(m t-imp'( .... (m,,-N[L)...))) 
ilere NIL is an atomic symbol used to terminate lists. 
Si~me many of the symbolic expressions with which we 
de:~.l are conveniently expressed as lists, we shall introduce 
a lis~ imtation to abbreviate certain S-expressions. We have 
1. im) siands for (re.NIL). 
2. (m~ ,., . , m,) stands for (ml. (. -. (m,.NIL)- .-)). 
'.~. (m,, -.- , m,,.x) stands :for (mr' (---(m,,.x)... )). 
Subexpressions can be similarly abbreviated. Some 
examples of these abbreviations are 
{(AB, C), l)) for ((AB-(C-NIL)).(D.NIL)) 
(~A,B),C, I).E) for ((A.(B-NIL)).(C.(D.E))) 
Nince we regard the expressions with commas as abbre- 
viation,s for those not involving commas, we shall refer to 
~hem all as S-expressions. 
b. ["~mc~ions of S-expressions and the Expressions 77~at 
t~q,'~,~ent Them. We now define a class of functions of 
S-expressions. The expressions representing these ftmc- 
~io~s are written in a conventional functional notation. 
tIowever, in order to clearly distinguish the expressions 
rvpresenting fmmtions from S:expressions, we shall use 
~quences of lower-case letters for function names and 
variabk~s ravaging over the set of S-expressions. We also 
~ 
brackets and semicolons, instead of parentheses and 
commas, for denoting the application of functions to their 
arguments. Thus we write 
car [x] 
car [cons [(A.B); x]] 
I~ these M-expressions (meta.-expressions) any S-expres- 
sions that oeetlr stand for themselves. 
e, The tflemerttary S:functions and Predicates. We intro- 
<t~ee the following functions and predicates: 
L atom. 
atom [x] has the value of T or F, accordingly 
as x is an atomic symbol or not. Thus 
atom IX] = T 
atom [iX.A)] = F 
2. eq. 
eq Ix; 3'] is defined if "rod only if both x and y 
are atomic, eq Ix; y] = T if x and y are the same symbol, 
and eq Ix; Yl = F otherwise. Thus 
eq [X; X] = T 
eq IX; A] = F 
eq [X; (X.A)] is undefined. 
3. ear. 
car Ix] is defined if "rod only if x is not atomic. 
car [(e~.ee)] = el. Thus car [XI is undefined. 
car [(X.A)I = X 
ear [((X.A).Y)] = iX.A) 
4. edr. 
cdr Ix] is also defined when x is not atomic. 
We have cdr [(<'e~)l = <. Thus edr {X] is undefined. 
cdr [(X.A)] = A 
edr [((X.A)-Y)] =: 55 
5. cons. 
cons Ix; y] is defined for any x and y. We 
have cons [e~ ; e~] = (e1.e~). Thus 
cons [X; A1 = iX. A) 
cons [iX.A); Y] = ((X-A).Y) 
ear, cdr, and cons ,~i'e easily seen to satisfy the relations 
ear [cons [x; y]] = x 
cdr [cons {x; y]] = y 
cons [car [x]; cdr [x/1 = x, provided that x is not. atomic. 
The nantes "car" and "cons" will come to have mne- 
monic significance only when we discuss the representation 
of the system in the computer. Compositions of car and cdr 
give the subexpressions of a given expression in a given 
position. Compositions of cons form expressions of a given 
structure out of paris. The class of functions which can be 
formed in this way is quite limited and not very interesting. 
d. Recur,s@e S-functions. We gel; a nmch larger class of 
functions (in fact, all computable functions) when we 
allow ourselves to form new functions of S-expressions by 
conditional expressions and recursive definition. 
We now give some examples of functions that are de- 
finable in this way. 
1. ff [x]. 
The value of ff Ix] is the first atomic symbol 
of the S-expression x with the parentheses ignored. Thus 
ff [((A.B).C)] 
We have 
= 
a 
ff [x] = [atom [x] -~ x; T --~ff [ear [x]]l 
We now tract in detail the steps in the evaluation of 
ff [((A.B),C)]: 
ff [((A.B).C)] 
= [atom [((A.B).C)]--~ ((A.B)-C); 
T--~ ff lear [((A.B)'C)lll 
= iF "-+ ((A.B).C);T 
= -~f'f [ear [((A-B).C)]]] 
[T --~ t'f (ear I((A.B)"C)111 
Communications of the ACM 
187 
= ff [ear [((A.B).C)]] 
: 
= 
= 
= 
ff [(A.B)] 
[atom [(A.B)] -+ (A.B); T --> ff [ear [(A.B)]]] 
[F + (A.B); T -~ff [eat" [(m.*{)]]] 
[T --+ff [car [(A.B)]]] 
= ff lear [(A.B)]] 
: 
ff [A] 
= 
= 
[atom [A] --~ A; T --+ ff [ear [A]]] 
[T ~ A; T --, ff [car [A]]] 
=A 
2. subst Ix; y; z]. 
This function gives the result of 
substituting the S-expression x for all occurrences of the 
atomic symbol y in the S-expression z. It is defined by 
subst Ix; y; z] = [atom [z] --+ [eq [z; y] -+ x; T --~ z]; 
T + cons [subst Ix; y; ear [z]]; subst Ix; y; edr [z]l]] 
As an example, we have 
subst [(X.A); B; ((A-B)-C)] = ((A-(X.A))-C) 
3. equal [x; y]. 
This is a predicate that has the value 
T if x and y are the same S-expression, and has the value 
I v otherwise. We have 
equal Ix; y] = [atom [x]/~ atom [y] /~ eq Ix; y]] 
V [~-oatom [x] /~ ~atom [y] /~ equal lear [x]; car [y]] 
It is convenient to see how the elementary functions 
look in the abbreviated list notation. The reader will 
easily verify that 
(i) ear [(ml, m2, ... , m,)] = ml 
(ii) 
edr [(m,, m2, "" , m~)] = (m2, .." , m~) 
(iii) cdr [(m)] = NIL 
(iv) cons[m,;(m2,'",m,,)] 
(v) cons [m; NIL] = (m) 
We define 
null [x] = atom [x] A eq [x; NIL] 
This predicate is useful in dealing with lists. 
Compositions of ear and edr arise so frequently that 
many expressions can be written more concisely if we 
abbreviate 
eadr [x] for ear [edr [x]], 
eaddr [x] for ear [edr [edr [x]]], etc. 
Another useful abbreviation isto write list [e~ ; e= ; • • • ; e~] 
for cons [el ; cons [e2 ; • • • ; cons [e. ; NIL]-. • ]]. This func- 
tion gives the list, (e,, ..- , e.), as a hmetion of its ele- 
ments. 
188 
The following functions are useful when S-expressior~s 
are regarded as lists. 
1. append [x; y]. 
append Ix; y] = [mdI [x] -+ y; T ~ cons [ca," [x]; 
append [cdr [x]; y]]] 
An example is 
append [(A, B); (C, l), E)] = (A, B, C, D, ]i;) 
2. among [x; y]. 
This predicate is true if the S-ex- 
pression x occurs among the elements of the lis~ y. We have 
among Ix; y] = ~--mull [y] /~ [equal [x; ear [y]] 
V among [x; cdr D']]] 
3. pair Ix; y]. 
This function gives the list of pairs of 
corresponding elements of the lists x and y, We have 
pair Ix; y] = [null [x]/\ null [y] -+ NIL; --,atom [xl 
/~ ~-~atom [y] -+ cons [lisg lear Ix]; ear [y]]; 
pair [edr Ix]; cdr [y]]]] 
An example is 
pair [(A, B, C); (X, (Y, Z), U)] = ((A, X), 
(B, (Y, Z)), (C, C)) 
4. assoe [x;y]. 
/~ equal [edr [x]; edr [yl]l 
If y is a list of the form ((ut, v,), 
• • • , (m~, v~) ) and x is one of the u's, then assoe [x; Yl is 
the corresponding v. We have 
assoc [x; y] = ecl[caar [y]; x] -+ eadar [y] ; 
T --~ assoc Ix; ode [y}]] 
An example is 
assoe IX; ((W, (A, B)), (X, (C, D)), 
(Y, (E, F)))] : (C, ~)) 
5. sublis [x; y]. 
= 
(ml,m~,'",m,,) 
Here x is assumed to have the form 
of a list of pairs ((u~, v,), • .. , (u,,, v,)), where the u% 
are atomic, and y may be any S-expression. The value of 
sublis [x; y] is tile result of substituting each v for the cor- 
responding u in y. In order to define sublis, we first defi~e 
an auxiliary function. We have 
sub2 [x; z] = [null Ix] -+ z; eq [eaar [x]; z] ~ eadar [x]; 
T -+ sub2 [cdr [x]; z]] 
and 
sublis Ix; Yl = [atom [y] --~ sub2 [x; y]; 
T ~ cons [sublis [x; ear [y]]; sublis [x; edr [y]i] 
We have 
sublis [((X, (A, B)), (Y, (B, C))); (A, X.Y)] 
= (a, (a, B), B, c) 
Communications of the ACM 
~ssi0ns ~ 
:} 
x]; y]ll 
S-ex. 
% have 
,dr b']]l 
)airs of 
'e 
dr [y]]]] 
Ic, u)); 
he c0r- 
i define" 
[x]; z]l il ¸ 
e. R~¢prese,zlation of S-Functions by S-Expressions. 
S.func[ions have bem~ described by M-expressions. We 
now give a rule for t, ranslating M-expressions into S- 
expressions, ii, order to be able to use S-functions for 
making certain computations with S-functions and for 
aaswering certain questions about S-functions. 
The translation is determined by the following rules in 
which we denote ~he translation of an M-expression 8 by 
1. If g is an S-expression E* is (QUOTE, 8). 
2. Variables and function names that were represented 
by strings of lower-case letters are translated to the cor- 
responding strings of the corresponding upper-case letters. 
Thus car* is CAR, and subst* is SUBST. 
3. A form fie, ; . • • ; en] is translated to (f*, e~*, • - • , en*). 
Thus {cons {ear [x]; edr [x]l}* is (CONS, (CAR, X), 
CDR, X)). 
4. {[p, -+ e, ; ... ; p,, -+ e,]}* is (COND, (p**, e**), 
.., (p,,*. e,,*)). 
5. {X[[x, ; .." ; x,]; g]}* is (LAMBDA, (x~*, --- , x,,*), 
~;*). 
6. {label [a; a]}* is (LABEL, a*, g*). 
With these conventions the substitution function whose 
M-expression is label [subst; X[[x; y; z]; [atom [z] -+ 
[eq [y; z] -~, x; T --~ z]; T --~ cons [subst [x; y; ear [z]]; 
subst Ix; y; cdr [z]]]]l] has the S-expression 
(LABEL, SUEST, (I.MMI~DA, (X, Y, Z), (COND 
((ATOM, Z), (COND, (EQ, Y, Z), X), ((QUOTE, 
T), Z))), ((QUOTE, T), (CONS, (SUBST, X, Y, 
(CAI~ Z)), (SUBST, X, Y, (CDR, Z))))))) 
This notation is writable and somewhat readable. It can 
be made easier tO read and write at the cost of making its 
structure less regular. If more characters were available 
on the computer, it could be improved considerably. 
f. 
The Universal S-Function apply. There is an S-func- 
tion apply with the property that if f is an S-expression for 
art S-function f' and args is a list of arguments of the form 
(argl, ... , argn), where argl, ..', argn are arbitrary 
S-expressions, then apply{f; args] and f'[argl; .." ; argn] 
arc defined for the same vahms of argl, ... , argn, and are 
equal when defined. For example, 
X[[x; y]; cons [car [x]; yl] [(A, B); (C, D)] 
= apply [(LAMBDA, (X, Y), (CONS, (CAR, X), 
y)); ((A, B), (C, D))] = (A, C, D) 
The S-function apply is defined by 
apply If; args]= eval [cons If; appq [args]]; NIL] 
where 
appq [m] = {null [m] -+ NIL; 
T -~ cons {list [QUOTE; car [m]]; appq [cdr [m]]]] 
and, 
eval [e; a] = [ 
atom [e] --+ assoc [e; a]; 
atom [car [e]] --+ [ 
eq {ear [e]; QUOTE] -~ cadr [e]; 
eq [car [e]; ATOM] -÷ atom [eval [cadr [e]; a]]; 
eq [cal" [e]; EQ] --~ [eval [cadr [e]; a] = eval [cad& [e]; a]]; 
eq [car {el; CON])] --~ evcon [edr [e]; a]; 
eq [ear" [e]; CAR] --~ ear [eval [cadr [el; a]]; 
eq [car [e]; CDR] --~ cdr [eval [cadr [e]; a]]; 
eq [car {el; CONS] --~ cons [eval [eadr {el; a]; eval [eaddr {el ; 
a]]; T --+ eval [cons [assoe {ear {el; a]; 
evlis [edr [e]; all; a]]; 
eq [caar [e]; LABEL] --~ eval [cons [eaddar {el; cdr [e]]; 
cons {list [cadar {el; car [e]; a]]; 
eq [eaar [e]; LAMBDA] -+ ewd [caddar [e]; 
append [pair [ca.dar {el; evils [cdr {el; a]; a]]] 
and 
evcon [c; a] = [eval [caar [e]; a] -~ eval [eadar [c]; al; 
T --~ evcon [cdr [c]; a]] 
and 
evils [m; a] = [uull [m] --+ NIL; 
T -~ cons [eval [car [m]; a]; evlis [cdr [m]; a]]] 
We now explain a number of points about these defini- 
tions. 
1. apply itself forms an expression representing the 
value of the function applied to the arguments, and puts 
the work of evaluating this expression onto a function eval. 
It uses appq to put quotes around each of the arguments, 
so that eval will regard them as standing for themselves. 
2. eval [e; a] has two arguments, an expression e to be 
evahmted, and a list of pairs a. The first item of each pair 
is an atomic symbol, and the second is the expression for 
which the symbol stands. 
3. If the expression to be evaluated is atomic, eval 
evaluates whatever is paired with it first on the list a. 
4. If e is not atomic but car [e] is atomic, then the expres- 
' 
~' 
(ATOM, e) or 
sion has one of the forms (QUO I'E, e) or 
(EQ, el, e2) or (COND, (pl, e,),..., (P,,, e,,)), or 
(CAR, e) or (CDR, e) or (CONS, e,, e2) or (f, e,, .." , e,,) 
where f is an atomic symbol. 
In the case (QUOTE; e) the expression e, itself, is taken. 
In the case of (ATOM, e) or (CAR, e) or (CDR, e) the 
expression e is evaluated and the appropriate function 
taken. In the case of (EQ, el, e2) or (CONS, el, e~) two 
expressions have to be evaluated. In the case of (COND, 
Communications of the ACM 
18~ 
(p~, el), -.. , (p,~, e,)) the p's havo to be evaluated in 
order until a true p is found, and theH the eorresponding o 
must be evaluated. This is accomplished by eveon. Finally, 
in the case of (f, o,, ... , on) we evaluate t, he expression 
that results from replacing f in this expression by whatever 
it; is paired with in the list a. 
5. The evaluation of ((LABEI~, f, g), e~, • - • , e,,) is 'te- 
complished by evaluating (8, o~ , • .. , e~) with the pairing 
(f, (LABEL, f, 8)) put on the front of the previous list, a 
of pairs. 
6. Finally, the evaluation of ( (LA MBDA, (x~, • - - , x,~), 
~), e~, ... , e,~) is accomplished by evaluating ~; with tho 
list of pairs ((xt, o~), ... , ((xn, o,)) put on the front of 
the previous list a. 
The list a could be eliminated, and LAMBDA and 
LABEl, exprossions evaluated by substituting the argu- 
ments for the variables in. the expressions ~;. Unfortu- 
nately, difficulties involving collisions of bound variables 
arise, but they are avoided by using the list a. 
Calculating the values of functions by using apply is an 
activity better suited to electronic computers than to 
people. As an illustration, however, we now give some of 
the steps for calculating 
apply [(LABEL, FF, (LAMBDA, (X), (COND, 
((ATOM, X), X), ((QUOTE, T), 
(FF, (Ca~, X)))))); ((A.B))] = 
The first argument is tho S-expression that represents the 
function ff defined in seetion 3d. We shall abbreviate it 
by using the lettor ¢. Wo have 
apply [~; ((A-B))] 
= evaI[((LABEL, FF, ¢), (QUOTE, (A-B))); NIL] 
where ¢ is tho part of ¢ beginning (LAMBDA 
= eval[((LAMBDA, (X), ~o), (QUOTE, (A.B))); 
((FF, ¢))] 
where ca is the part of ¢ beginning (COND 
=eval [(CONI), (rr~, et), (~r~, e=)); ((X, (QUOTE, 
(A.B))), (FF, ¢))] 
Denoting ( (X, (QUOTE, ( A- B ) ) ), (FF, ¢) ) by a, 
wo obtain 
= ovoon [( (~-~, ~), (~r~, ~.) ) ; ~*1 
This involves eval [~rt ; co] 
= eval [(ATOM, X); a] 
= atom loyal iX; a]] 
= atom loyal [assoe iX; ( (X, (QUOTE, (A. B) ) ), 
(FF, ¢))]; all 
= atom [oval [(QUOTE, (A. B)); a]] 
= atom [(A.B)] 
=F 
190 
()ur main caleulation contirmes wiih 
apply [¢5; ((A. B))] 
= ore, on [((~, ~))' ~t, 
which involves oval [~ ; a] = eva[ [(Q[YOTE, T); ~] = T. :~ 
Our main calculation again eontim~es with 
apply [¢; ((A. B) )] 
= oval [e2 ; a] 
= eval [(FF, (CAR, X)); a] 
=eval [cons [4; evils [((CAR, X)); a]]; a] 
Evaluating evlis [((C, AR, X)) ; a] involves 
'k 
oval [(c~ t{, x) ,~l - 
ear [oval [X; all] 
= ear [(A'B)I, where we took steps from the earli~,r '( 
computation of a.tom loyal IX; all = A, 
and so evils it(CAR, X)) ; a] then becomes 
list [list [QUOTt!;; A]] = ((QU)rE, A)) 
and otlr main quantity becomes 
eva| [(4,, (q~Jo IL, x)); ~] 
The subsequent steps are made as in tho begimfing ,,f 
the calculation. The LABEL and LAMBDA cause i~(:~*.' ' {{:: 
pairs to be added to ~, which gives a new list; of pairs <. 
The rr, term of the conditional oval [(ATOM, X); <! h> 
the value 32 t)oeause X is paired with (Q[ O 1 E, A)tirst 
..... c 
. 
in al, rather than with (QUOIE, (A B)) as in c~. 
Therefore we end up with oval iX; a~] fl'om the .e~'co~, 
'rod this is just A. 
g. Functions with Functions as Arguments. There are a 
number of useflfl functions some of whose arguments are 
functions. They are especially useful in defining othe|" rune- 
tions. One such function is maplist ix; f] with an S-expres- 
sion argument x and an argument f that, is a function from 
S-expressions to S-expressions. Wo define 
lnaplist [x; fl = [null [xl --~ NIL; 
T --+ cons [fix]; maplist [cdr ix]; i'1 ~] 
:['he usefulness of maplist is illustrated by fornmlas for 
the partial derivative with rospeet to x of expressions i~> 
volving sums and products of x and other variables. The 
S-expressions that we shall differentiate are formed ~ 
follows. 
1. An atomic symbol is an allowed expression. 
2. If e~, e~, • • • , e, are allowed expressions, (PLUS, <, 
... , en) and (TIMES, e~, ... , e.) arc also, a.nd represeld' 
the sum and product, respectively, of e~, • • - , e,. 
This is, essentially, the Polish notation for functio~* 
except, that the inclusion of paronthe~es and eoinmas tfl" 
lows functions of variablo numbers of arguments. An exa m~ 
ple of an allowed expression is (TIMES, X (t)L[~'S' 
X, A), Y), the conventional algebraic notati(m for whicD 
is X(X + A)Y. 
t 
i' 
!i 
.... 
., 
~. 
{ 
{ 
i 
:~, 
:i~ 
~- 
:, 
, 
ii 
!i 
: 
;~ 
~ 
~, 
;:. 
Communications of the ACM 
(a) 
,arlier 
xpres, 
fl'0m ! 
x; 
l 
fill 
} 
!i 
! 
) 
f~ 
as foi: :: 
~ls lrt- tl 
ted as 
i 
which i 
i J~il;! 
~ 
Our different.fallen tormula, which gives the derivative 
of y with respecti (.() x, is 
diff [y; x] = [atom [y]---* [eq [y; x] -~, ON[i;; T --, ZEtIOI; 
eq [car [y]; PI,USI --~ cons [['LUS; maplist [cdr [y]; X[[z]; 
diff[car [z]; x]/I]; eq[car [y]; TIMES] --+ cons[PLUS; 
maplistledr[y]; X[[zl; cons [TIMES; maplist[cdr [y]; 
X[[w]; ~--~eq [z; w] -÷ car [w]; 1l' ~ diff' [car [[w]; xlll]]]] 
The derivative of the allowed expression, as computed 
by this formula, is 
(PLUS, (TIMES, ONE, (I'IA;rs, X, A), Y), 
(TIMES, X, (PLUS, ONE, ZERO), Y), 
(TIMES, X, (PLUS, X, A), ZERO)) 
Besides maplist, another useful function with functional 
arguments is search, which is defined as 
search Ix; p; f; u] --- [null Ix] --+ u; p[x] --~ f[x]; 
T -+ search [cdr [x]; p; f; u] 
The function ,search is used to search a list for an element 
that has the property p, and if such an element is found, f 
of that element is taken. If there is no such element, the 
function u of no argument is computed. 
4. The LISP Programming System 
The LISP programming system is a system for using 
the IBM 704 computer to compute with symbolic informa- 
tion in the form of S-expressions. It has been or will be 
used for the following purposes: 
1. Writing a compiler to compile LISP programs into 
machine language. 
2. Writing a program t.o check proofs in a (:lass of 
formal logical systems. 
3. Writing programs for fornml differentiation and 
integration. 
4. Writing programs to realize various algorithms for 
generating proofs in predicate calculus. 
5. Making certain engineering calculations whose re- 
sults are formulas rather than numbers. 
6. Programming the Advice Taker system. 
The basis of the system is a way of writing computer 
programs to evaluate S-functions. This will be described 
in the following sections. 
In addition to the facilities for describing S-functions, 
there are facilities for using S-flmctions in programs 
written as sequences of statements along the lines of 
FORTRAN (4) or AL(;OI; (5). These features will not be 
described in tiffs article. 
(b) 
FIG. 
I 
(c) 
a. R<'4ffe,~entalio~ of £'-P~'xpre.~,~wns b:q List Structure. A 
list structttre is a collection of computer words arranged 
as in figure la or lb. Each word of the list structure is 
represented by one of the subdivided rectangles in the 
figure. The left box of a rectangle represents the address 
field of the word and the right box represents the decre- 
ment field. An arrow from a box ~;o another rectangle 
means that the field corresponding to the box contains 
the location of the word corresponding to the other 
rectangle. 
It is permitted for a substructure to occur in more than 
one place in t~ list structm'e, as in figure lb. but it is no~ 
permitted for a sturcture to have cycles, as in figure le. 
An atomic symbol is represented in the computer by a 
list structure of special form called the association list of 
the symbol. The address field of the first word contains a 
special constant which enables the program to tell that 
this word represents an atomic symbol. We shall describe 
association lists in section 4b. 
(o) 
(b) 
l?m. 2 
An S-expression x that is not atomic is represented by 
a word, the address and decrement parts of which contain 
tile locations of the subexpressions ear[x] and edr[x], 
respectively. If we use the symbols A, B, ere, to denote 
the locations of the association list of these symbols, then 
tile S-expression ((A.B).(C.(E.F))) is represented by 
the list structure a of figure 2. Turning to the list. form of 
S-expressions, we see that, tile S-expression (A, (B, C), D), 
which is an abbreviation for (A.((B.(C-N[L)).(D- 
NIL))), is represented by tile list structure of figure 2b. 
When a list structure is regarded as representing a list, 
we see that each term of the list occupies tile address 
part of a word, the decrement part, of which points to the 
word containing the next term, while the last word has 
NIL in its decrement. 
An expression that has a given subexpression occurring 
more than once can be represented in more than one w'~y. 
Whether the list structure for the subexpression is or is not 
repeated depends upon the history of the program. 
Whether or not a subexpression is repeated will make no 
Comnumications of the XCM 
 i;ii ii!iiii!i 
..... 
/" Zil 
1.91 
difference in the results of a program as they appear out- 
side the machine, although it will affect the time and 
storage requirements. For example, tt~e S-('xpressio~ 
((A. B). (A. B)) can be represented by either the list. struc- 
ture of figure 3a or 3b. 
~o} 
{b) 
F~G. 3 
Tile prohibition against circular list, structures is es- 
sentially a prohibition against an expression being a sub- 
expression of itself. Such an expression could not exis~ ot~ 
paper in a world with our topology. Circular l:]st structures 
would have some advantages in the machine, for example, 
for representing recursive hmctions, but difficulties in 
printing them, and in certain other operations, make it 
seem advisable not to use them for the present. 
The advantages of list structures for the storage of 
symbolic expressions are: 
1. The size and even the number of expressions with 
which the program will have to deal cannot be predicted 
in advance. Therefore, it is difficult to arrange blocks of 
storage of fixed length to contain them. 
2. Registers can be put back on the free-storage list 
when they are no longer needed. Even one register re- 
turned to the list is of value, but if expressions are stored 
linearly, it is difficult to make use of blocks of registers of 
odd sizes that may become available. 
3. An expression that occurs as a subexpression of 
several expressions need be represented in storage only 
once. 
b. Association Lists. In the LIsP programming system 
we put more in the association list of a symbol than is 
required by the mathematical system described in the 
previous sections. In fact, any information that we desire 
to associate with the symbol nmy be put on the associa- 
tion list. This information may include: the print name, 
that is, the string of letters and digits which represents 
the symbol outside the machine; a numerical value if 
the symbol represents a number; another S-expression 
if the symbol, in some way, serves as a name for it; or the 
location of a routine if the symbol represents a functior~ 
for which there is a machine-language subroutine. All this 
implies that in the machine system there are more prirni- 
tive entities than have been described in the: sections on 
the mathematical system. 
~mme of the symbol who~e asso(qaEi(m list this is hangs 
from the uext~ word <m ~h(, association list. l:n the second 
row of the figure w(, have a list of three words. The address -part of each of th~c words polaris to ~ word containing 
six (i4:)it. characters. The last, uord is filled (:)~tt with a 
6.t:)iC combination that do(,s not~ represent a character 
t)rilltable by the computer. (Ilecall thai, the IBM 704 has 
a 
36-bit word a:ud that printable eh~raeters are each 
represented by 6 bits.) The presence of tile words with 
character inform~tion means that the association lists do 
~of themselves represen{; S-exl:)ressiotls, :.rod that only 
some of the rum, rictus for dealing with S-expressions make 
sense within as association list. 
[4II~ 
fro 
re~ 
iC 
ch 
rel 
re, 
st~ 
th 
CC 
h( 
ci 
F( 
S( 
p: 
I 
ll 
Cl 
tJ 
t 
S: 
c. Free-Storaf/c List. At. any given time only a part of 
the memory reserved for list, structures will actually be in 
use for storing S-expressions, The remaining registers (in 
ore' system the number, initially, is approxima{,ely 15,000) 
are arranged in a single list c.dled the fl'ee-.stora,qe liet. A 
cert:dn register, :Fm,:E, in the program contains the loca- 
ti(:m of the first register in this list. When a word is re- 
quired to form some additional list structure, the first 
word on the fl'ee-,s'torage list is taken and the number in 
register FaEE is changed to become the location of the 
second word on the free-storage list. No provision need be 
made for the user to program the return of registers to the 
free-st.orage list. 
This return takes place atttoInatieally, approximately 
as follows (it is necessary to give a simplified deseriptiol~ 
of this process in this report): There is a fixed set of base 
registers in the program which contains the locations of ~f 
list structures that, are accessible to the program. Of ] 
course, because list structures branch, an arbitrary num- 
ber of registers may be involved. Each register that is } 
accessible to the program is accessible because it can be 
reached from one or more of the base registers by a chain 
of car and edr operations. When the contents of a base 
register are changed, it may happen that the register Co 
which the base register formerly pointed cannot be reached 
by a car-cdr chain from any base register. Such a register 
may be considered abandoned by the program because its 
contents can no longer be found by any possible program; 
hence its contents are no longer of interest, and so we 
would like to have it back on the free-storage list. This ,' 
comes about in the following way. 
Nothing happens until the program runs out of free 
storage. WherJ a free register is wanted, and there :is none 
left on the free-storage list, a reclamation cycle starts. -- . -. 
. 
For the present, we shall only describe how print names 
are represented on association lists so that in reading or 
printing the program can establish a correspondence 
between information on punched cards, magr:Jetic tape or 
printed page and the list structure inside the machine. 
The association list. of the symbol DIFFEI{t~3NTIATt?] has a 
segment (ff the form shown in figure 4, Here lmame is a 
symbol that indicates that the struett~re for the. print 
Fm, 4 
t 
First, the program finds all registers accessible from the t 
base registers and makes their signs negative. This is ! 
accomplished by starting from each of the base registers i 
(:ommunications of the ACM 
192 
and changing the sign of every register that can be reached 
from it by a car-cdr chain. If the program encounters a 
register in this process which already has a negative sign, 
it assumes that this register has already been reached. 
After all of the accessible registers have had their signs 
changed, the program goes through the area of memory 
reserved for the storage of list structures and puts all the 
registers whose signs were not changed in the previous 
step back on the free-storage list, and makes the signs of 
the accessible registers positive again. 
This process, because it is entirely automatic, is more 
convenient for the programmer than a system in which 
he has to keep track of and erase unwanted lists. Its effi- 
ciency depends upon not coming close to exhausting the 
available memory with accessible lists. This is because the 
reclamation process requires several seconds to execute, 
and therefore must result in the addition of at least 
several thousand registers to the free-storage list if the 
program is not to spend most of its time in reclamation. 
d. Elementary S-Functions in the Computer. We shall 
now describe the computer representations of atom, =, 
ear, cdr, and cons. An S-expression is communicated to 
the program that represents a function as the location of 
the word representing it, and the programs give S-expres- 
sion answers in the same form. 
atom. As stated above, a word representing an atomic 
symbol has a special constant in its address part: atom is 
programmed as an open subroutine that tests this part. 
Unless the M-expression atom[e] occurs as a condition in 
a conditional expression, the symbol T or F is generated 
as the result of the test. In ease of a conditional expression, 
a conditional transfer is used and the symbol T or F is 
not generated. 
eq. 
The program for eq[e; f] involves testing for the 
numerical equality of the locations of the words. This 
works because each atomic symbol has only one association 
list. As with atom, the result is either a conditional transfer 
or one of the symbols T or F. 
car. Computing car[x] involves getting the contents 
of the _address part of register x. This is essentially accom- 
plished by the single instruction ci~a 0, i, where the argu- 
ment is in index register i, and the result appears in the 
address part of the accumulator. (We take the view that 
the places from which a function takes its arguments and 
into which it puts its results are prescribed in the defini- 
tion of the function, and it is the responsibility of the 
programmer or the compiler to insert the required data- 
moving instructions to get the results of one calculation 
in position for the next.) ("car" is a mnemonic for "con- 
tents of the _address part of register.") 
edr. edr is handled in the same way as ear, except that 
the result appears in the decrement part of the accumu- 
lator. ("edr" stands for "cgntents of the decrement part 
of register.") 
cons. The value of cons[x; y] must be the location of a 
register that has x and y in its address and decrement 
parts, respectively. There may not be such a register in 
the computer and, even if there were, it would be time- 
consuming to find it. Actually, what we do is to take the 
first available register from the free-storage list, put x and 
y in tlhe address and decrement parts, respectively, and 
make the value of the function the location of the register 
taken. ("cons" is an abbreviation for "construct.") 
It, is the subroutine for cons that initiates the reclama- 
tion when the free-storage list is exhausted. In the version 
of the system that is used at present cons is represented 
by a closed subroutine. In the compiled version, cons is 
open. 
e. Representation of S-Functions by Programs. The 
compilation of functions that are compositions of ear, 
cdr, and cons, either by hand or by a compiler program, 
is straightforward. Conditional expressions give no trouble 
except that they must be so compiled that only the p's 
and e's that are required are computed. However, prob- 
lems arise in the compilation of reeursive functions. 
In general (we shall discuss an exception), the routine 
for a recursive function uses itself as a subroutine. For 
example, the program for subst[x;y;z] uses itself as 
a subroutine to evaluate the result into the subexpres- 
sions ear[z] and cdr[z]. While subst[x;y:edr[z]] is being 
evaluated, the result of the previous evaluation of 
subst[x; y; car[z]] must be saved in a temporary storage 
register. However, subst may need the same register for 
evaluating subst[x;y;edr[z]]. This possible conflict is re- 
solved by the SAVE and UNSAVE routines that use 
the public push-down list. The SAVE routine is entered 
at the beginning of the routine for the reeursive function 
with a request to save a given set of consecutive registers. 
A block of registers called the public push-down list is 
reserved for this purpose. The SAVE routine has an index 
that tells it how many registers in the push-down list are 
already in use. It moves the contents of the registers 
which are to be saved to the first unused registers in the 
push-down list, advances the index of the list, and returns 
to the program from which control came. This program 
may then freely use these registers for temporary storage. 
Before the routine exits it uses UNSAVE, which restores 
the contents of the temporary registers from the push- 
down list and moves back the index of this list. The result 
of these conventions is described, in programming termi- 
nology, by saying that the reeursive subroutine is trans- 
parent to the temporary storage registers. 
f. Status of the LISP Programming System (February 
1960). A variant of the function apply described in section 
5f has been translated into a program APPLY for the 
IBM 704. Since this routine can compute values of S- 
functions given their descriptions as S-expressions and 
their arguments, it serves as an interpreter for the Lisp 
programming language which describes computation 
processes in this way. 
The program APPLY has been imbedded in the Lisp 
programming system which has the following features: 
1. The programmer may define any number of S-fune- 
Communications of the ACM 
193 
tions by S-expressions. These ftmctions may refer to each 
other or to certain S-functions represet~ted by machine 
language program. 
2. The vMues of defined functions may be computed. 
3. S-expressions may be read and printed (directly or 
via magnetic tape). 
4. Some error diagnostic and selective tracing facilities 
are included. 
5. The programmer may have selected S-function,s 
compiled into machine language programs put into the 
core memory. Values of compiled functions are computed 
about 60 times as fast as they would if interpreted. Corn- 
pilaf}on is fast, enough so that it is not necessary t,o punch 
compiled program for future use. 
6. A "program feature" allows programs containing 
assignment and go to staternents in the style of ALl;eL. 
7. Computation with floating point num/)ers is possible 
in the system but, this is inefficient. 
8. A programmer's manuM is being prepared. 
The Lisp programming system is appropriate for corn- 
putations where the data can conveniently be represented 
as symbolic expressions allowing expressions of the same 
kind as subexpressions. A version of the system for the 
IBM 709 is being prepared. 
5. Another Formalism for Functions of Symbolic 
Expressions 
There are a number of ways of defining functions of 
symbolic expressions which are quite similar to the system 
we have adopted. Each of them involves three basic func- 
tions, conditional expressions, and recursivc function 
definitions, but the class of exprcssions corresponding to 
S-expressions is different, and so are the precise definitions 
of the functions. We shall describe one of these variams 
called linear IASP. 
The L-expressions are defined as follows: 
1. A finite list, of Characters is admitted. 
2. Any string of admitted characters'ia an L-expression. 
This includes the null st, ring denoted by A. 
There are t,hree functions of strings: 
1. firs}Ix] is the first character of the string x. 
first[A] is undefined. 
For example: 
first[ABC] = A 
2. rest[x] is the string of characters which remains when 
the first character of the string is deleted. 
rest[A] is undefined. 
For example: 
resf[ABC] = BC 
3. eombineIx; y] is the string formed by prefixing the 
character x to the string y. 
For example: 
combine[A; BC] = ABC 
There are three predicates on strings: 
1. char[x], x is a single character. 
2. null[x], x is the null string. 
3. x = y, defined for x and y characters. 
The advantage of linear L~sP is that no characters are 
given special roles, as are parentheses, dots, and commas 
ill LISP, This permits computations with all expressions 
194 
that ca*it be writ Ien li:aearly. The disadva~.iiage of m~ea~ 
LisP is that; ~he extraction of subexpressions is a faith. I ;!: 
involved, rather than an elementary operat, ion, It Is ~)t ': si~] 
hard to write, in linear L~s>, functions that correspoad i:,., 
the basic functions of L:~se, so that, mathematically, 
linear I,Ise includes L~st,. This turns out to be the mos~ 
W~ 
g(e; 
W< 
convenient way of progr'~mming, i:n linear L:~se, the mor~, 
complicated manipulations. However, if the function> 
are to be represented by computer routines, Ltse is ess<~. 
tially faster. 
6. Flowcharts and Recurs}on 
Since both the usual form of computer program m~d re- 
cursive function definitions are universal computationally, 
i~ is interesting to display the relation between them. The 
translation of recurs}re symbolic functions inlo compuier 
programs was the subject of the rest of this report, h~ ~his 
section we show how to go the otter way, at least i~ 
prineipk. ~. 
The state of the machine at any time during a compu,a- 
lion is gNen by the values of a number of variables, l,e~ 
these variables be combined into a vector ~. Consider a 
program block with one entrance and one exit. It (teti~,es 
and is essentiMly defined by a certain function f tha~ 
takes one machine configuration into another, that is, f has 
the form ~' = f(~). Let us call f lhe associated functio,~ of 
the program block. Now let a number of such })locks i, 
combined into a program by decision elements u that (h,. 
eide after each t)lock is completed which block will }~a~ 
entered next. Nevertheless, let the whole program ~siil} 
have one entrance and one exit. 
F~c,. 5 
We give as an example the flowchart of figure 5. l,ei *~> 
describe the function r[~] that gives the transformati(m ~ 
the vector ~ between entrance and exit of the whole block. 
0g { 
{ 
I 
exi 
fn 
J~ 
' 
? 
t 
: 
i 
ih 
a[ 
p~ 
c 
t, 
(: 
Communications of the AC~! 
! 
i'airl:i We shall (:tefi,~(~ il i,~ col~junction with lhe functions - 
~[f/] and t[,~l, which give the /rausformations thai ~ under- 
2,1~{ I goes between the points S a,~d T respeclively and the exit. 
u~.l tO : 
eally, 
most 
Ill0r(, 
~ti0ns~ 
)8sell. 
t~d reL 
,nelly, 
lputei, !, 
in this 
} 
apu~a~ 
;ider ~i, 
definil 
f that! 
s, fii~ii2 
t ion 
,eks g~ 
hat di) 
will 
i 
4; 
!4 ¸ 
We h~ve 
r[~] = [~rH[~I-' ~'[f,[~ll; T -~ s[fd~]]l 
Given a flowch'trt with a single, entrance and a single 
exit, it is easy ~(, write down the recursive function that 
gives the tr'msformation of tim state vector from entrance 
to exit in terms of the corresponding functions for the 
computation blocks and the predicates of tile branch 
points. In general, we proceed as follows. 
In figure 6, let ~ be an n-way branch point, and let 
fi, ... , f, be the computations leading to branch points 
fl~, f12, '" , fl .... l~et 4) be the function that transforms 
between fl and the exit of the chart, and let (b~ , • " • , 4,~ be 
the corresponding functions for fl~,..., fl,~. We then 
write 
~[~] = [p~[~J --, ¢,[t',[}]]; ... ; p,,[}] ~ 0,,[f',,[}]]] 
Acknowledgments 
The inadequacy of tile X-notation for naming recursive 
functions was noticed by N. Rochester, and he discovered 
~n alternative to the solution involving label which has 
been used here. The form of subroutine for cons which 
permits its composition with other functions was invented, 
in connection with another programming system, by C. 
Gerberiek and H. L. Gelernter, of IBM Corporation. The 
Lisp programming system was developed by a group 
including R. Brayton, D. Edwards, P. Fox, L. Hodes, D. 
Luckham, K. MMing, J. McCarthy, D. Park, S. Russell. 
The group was supported by the M.I.T. Computation 
Center, and by the M.I.T. Research i,aboratory of Elee- 
U'onics (which is supported in part by the U.S. Army 
(Signal Corps), the U.S. Air Force (Office of Scientific 
Research, Air Research and Development Command), 
and the U.S. Navy (Office of Naval Research)). The author 
also wishes to acknowledge the personal financiM support 
of the Alfred P. Sloa.n Foun(l't,tion.. 
# 
#, 
¢ 
f2 
%_j 
#2 
FIG. 6 
... 
%_j 
REFERENCES 
1. J. McCARTHY, Programs with common sense, Paper presented 
at the Symposium on the Mechanization of Thought Proc- 
esses, National Physical Laboratory, Teddington, England, 
Nov. 24-27, 1958. (Published in Proceedings of the Sympo- 
sium by H. M. Stationery Office). 
2. A. NEWELL AND J. C. SHAW, Programming the logic theory 
machine, Proc. Western Joint Computer Conference, Feb. 
1957. 
3. A. CmmcH, The Calculi of Lambda-Conversion (Princeton 
University Press, Princeton, N. J., 1941). 
4. FORTRAN Programmer's Reference Manual, IBM Corpora- 
tion, New York, Oct. 15, 1956. 
5. A. J. PERLIS AND K. SAME, LSON, International algebraic lan- 
guage, Preliminary Report, Comm. Assoc. Comp. Mach., Dec. 
1958. 
Symbol Manipulation by Threaded Lists* 
A. J. PEltLIS AND CHARLES THORNTON, Carnegie Institute of Technology, Pittsburgh, Pa. 
Part 1: The Threaded List Language 
1. Introduction 
i! 
ilii! ¸ 
In the field variously called artificial intelligence, 
heuristic programming, automata theory, etc., many of 
bl0< 
* The work was SUl)ported in part by the Off:ice of Naval Re- 
search under contract munber Nonr.-760 (18), Nr 04(,)-141 and by 
the U. S. Army Signal (~orps under e(mtraet number l)a 36-039- 
8eq5081, File No. 0195-PH-58-91 (4461). 
i: i~;~!il 
the most interesting problems do not lend themselves 
readily to solutions formulated in the automatic program- 
ming systems now in wide use. Several new approaches 
to more adequate and natural programming systems have 
been made in the past few years. Notable among these 
are the list structure languages of the IPL family developed 
by Newell-Simon-Shaw [1] and LISP by McCarthy [2]. 
They provide great flexibility for the construction of 
highly composed programs, and are able to represent and 
process systems of arbitrarily great complexity, subject 
Communications of the AC1M 
1195 
~ 

Recursive Functions of Symbolic Expressions
 and Their Computation by Machine, Part I
 John McCarthy, Massachusetts Institute of Technology, Cambridge, Mass. ∗
 April 1960
 1 Introduction
 A programming system called LISP (for LISt Processor) has been developed
 for the IBM 704 computer by the Artificial Intelligence group at M.I.T. The
 system was designed to facilitate experiments with a proposed system called
 the Advice Taker, whereby a machine could be instructed to handle declarative
 as well as imperative sentences and could exhibit “common sense” in carrying
 out its instructions. The original proposal [1] for the Advice Taker was made
 in November 1958. The main requirement was a programming system for
 manipulating expressions representing formalized declarative and imperative
 sentences so that the Advice Taker system could make deductions.
 In the course of its development the LISP system went through several
 stages of simplification and eventually came to be based on a scheme for rep
resenting the partial recursive functions of a certain class of symbolic expres
sions. This representation is independent of the IBM 704 computer, or of any
 other electronic computer, and it now seems expedient to expound the system
 by starting with the class of expressions called S-expressions and the functions
 called S-functions.
 ∗Putting this paper in LATEXpartly supported by ARPA (ONR) grant N00014-94-1-0775
 to Stanford University where John McCarthy has been since 1962. Copied with minor nota
tional changes from CACM, April 1960. If you want the exact typography, look there. Cur
rent address, John McCarthy, Computer Science Department, Stanford, CA 94305, (email:
 jmc@cs.stanford.edu), (URL: http://www-formal.stanford.edu/jmc/ )
 1
In this article, we first describe a formalism for defining functions recur
sively. We believe this formalism has advantages both as a programming
 language and as a vehicle for developing a theory of computation. Next, we
 describe S-expressions and S-functions, give some examples, and then describe
 the universal S-function apply which plays the theoretical role of a universal
 Turing machine and the practical role of an interpreter. Then we describe the
 representation of S-expressions in the memory of the IBM 704 by list structures
 similar to those used by Newell, Shaw and Simon [2], and the representation
 of S-functions by program. Then we mention the main features of the LISP
 programming system for the IBM 704. Next comes another way of describ
ing computations with symbolic expressions, and finally we give a recursive
 function interpretation of flow charts.
 We hope to describe some of the symbolic computations for which LISP
 has been used in another paper, and also to give elsewhere some applications
 of our recursive function formalism to mathematical logic and to the problem
 of mechanical theorem proving.
 2 Functions and Function Definitions
 We shall need a number of mathematical ideas and notations concerning func
tions in general. Most of the ideas are well known, but the notion of conditional
 expression is believed to be new1, and the use of conditional expressions per
mits functions to be defined recursively in a new and convenient way.
 a. Partial Functions. A partial function is a function that is defined only
 on part of its domain. Partial functions necessarily arise when functions are
 defined by computations because for some values of the arguments the com
putation defining the value of the function may not terminate. However, some
 of our elementary functions will be defined as partial functions.
 b. Propositional Expressions and Predicates. A propositional expression is
 an expression whose possible values are T (for truth) and F (for falsity). We
 shall assume that the reader is familiar with the propositional connectives ∧
 (“and”), ∨ (“or”), and ¬ (“not”). Typical propositional expressions are:
 1
 reference Kleene
 2
x <y
 (x < y)∧(b = c)
 x is prime
 Apredicate is a function whose range consists of the truth values T and F.
 c. Conditional Expressions. The dependence of truth values on the values
 of quantities of other kinds is expressed in mathematics by predicates, and the
 dependence of truth values on other truth values by logical connectives. How
ever, the notations for expressing symbolically the dependence of quantities of
 other kinds on truth values is inadequate, so that English words and phrases
 are generally used for expressing these dependences in texts that describe other
 dependences symbolically. For example, the function |x| is usually defined in
 words. Conditional expressions are a device for expressing the dependence of
 quantities on propositional quantities. A conditional expression has the form
 (p1 → e1,···,pn → en)
 where the p’s are propositional expressions and the e’s are expressions of any
 kind. It may be read, “If p1 then e1 otherwise if p2 then e2, ··· , otherwise if
 pn then en,” or “p1 yields e1,···,pn yields en.” 2
 We now give the rules for determining whether the value of
 (p1 → e1,···,pn → en)
 is defined, and if so what its value is. Examine the p’s from left to right. If
 a p whose value is T is encountered before any p whose value is undefined is
 encountered then the value of the conditional expression is the value of the
 corresponding e (if this is defined). If any undefined p is encountered before
 2
 I sent a proposal for conditional expressions to a CACM forum on what should be
 included in Algol 60. Because the item was short, the editor demoted it to a letter to the
 editor, for which CACM subsequently apologized. The notation given here was rejected for
 Algol 60, because it had been decided that no new mathematical notation should be allowed
 in Algol 60, and everything new had to be English. The if ...then...else that Algol 60
 adopted was suggested by John Backus.
 3
a true p, or if all p’s are false, or if the e corresponding to the first true p is
 undefined, then the value of the conditional expression is undefined. We now
 give examples.
 (1 < 2 →4,1>2→3)=4
 (2 < 1 →4,2>1→3,2>1→2)=3
 (2 < 1 →4,T →3)=3
 (2 < 1 → 0
 0 ,T →3)=3
 (2 < 1 →3,T → 0
 0 ) is undefined
 (2 < 1 →3,4<1→4) is undefined
 Some of the simplest applications of conditional expressions are in giving
 such definitions as
 |x| = (x < 0 →−x,T →x)
 δij = (i = j → 1,T →0)
 sgn(x) = (x < 0 → −1,x = 0→0,T →1)
 d. Recursive Function Definitions. By using conditional expressions we
 can, without circularity, define functions by formulas in which the defined
 function occurs. For example, we write
 n! = (n =0→1,T →n·(n−1)!)
 When we use this formula to evaluate 0! we get the answer 1; because of the
 way in which the value of a conditional expression was defined, the meaningless
 4
expression 0 · (0- 1)! does not arise. The evaluation of 2! according to this
 definition proceeds as follows:
 2! = (2=0→1,T →2·(2−1)!)
 = 2·1!
 = 2·(1=0→1T →·(1−1)!)
 = 2·1·0!
 = 2·1·(0 =0→1,T →0·(0−1)!)
 = 2·1·1
 = 2
 We now give two other applications of recursive function definitions. The
 greatest common divisor, gcd(m,n), of two positive integers m and n is com
puted by means of the Euclidean algorithm. This algorithm is expressed by
 the recursive function definition:
 gcd(m,n) = (m > n →gcd(n,m),rem(n,m) = 0 → m,T → gcd(rem(n,m),m))
 where rem(n,m) denotes the remainder left when n is divided by m.
 The Newtonian algorithm for obtaining an approximate square root of a
 number a, starting with an initial approximation x and requiring that an
 acceptable approximation y satisfy |y2 − a| < ϵ, may be written as
 sqrt(a, x, ϵ)
 = (|x2 −a| < ϵ → x,T → sqrt (a, 1
 2
 (x+ a
 x
 ),ϵ))
 The simultaneous recursive definition of several functions is also possible,
 and we shall use such definitions if they are required.
 There is no guarantee that the computation determined by a recursive
 definition will ever terminate and, for example, an attempt to compute n!
 from our definition will only succeed if n is a non-negative integer. If the
 computation does not terminate, the function must be regarded as undefined
 for the given arguments.
 The propositional connectives themselves can be defined by conditional
 expressions. We write
 5
p ∧q = (p→q,T →F)
 p ∨q = (p→T,T →q)
 ¬p = (p→F,T →T)
 p ⊃q = (p→q,T →T)
 It is readily seen that the right-hand sides of the equations have the correct
 truth tables. If we consider situations in which p or q may be undefined, the
 connectives ∧ and ∨ are seen to be noncommutative. For example if p is false
 and q is undefined, we see that according to the definitions given above p ∧ q
 is false, but q ∧ p is undefined. For our applications this noncommutativity is
 desirable, since p∧q is computed by first computing p, and if p is false q is not
 computed. If the computation for p does not terminate, we never get around
 to computing q. We shall use propositional connectives in this sense hereafter.
 e. Functions and Forms. It is usual in mathematics—outside of mathe
matical logic—to use the word “function” imprecisely and to apply it to forms
 such as y2+x. Because we shall later compute with expressions for functions,
 we need a distinction between functions and forms and a notation for express
ing this distinction. This distinction and a notation for describing it, from
 which we deviate trivially, is given by Church [3].
 Let f be an expression that stands for a function of two integer variables.
 It should make sense to write f(3,4) and the value of this expression should be
 determined. The expression y2+x does not meet this requirement; y2+x(3,4)
 is not a conventional notation, and if we attempted to define it we would be
 uncertain whether its value would turn out to be 13 or 19. Church calls an
 expression like y2 + x, a form. A form can be converted into a function if we
 can determine the correspondence between the variables occurring in the form
 and the ordered list of arguments of the desired function. This is accomplished
 by Church’s λ-notation.
 If E is a form in variables x1,···,xn, then λ((x1,···,xn),E) will be taken
 to be the function of n variables whose value is determined by substituting
 the arguments for the variables x1,···,xn in that order in E and evaluating
 the resulting expression. For example, λ((x,y),y2 + x) is a function of two
 variables, and λ((x,y),y2 + x)(3,4) = 19.
 The variables occurring in the list of variables of a λ-expression are dummy
 or bound, like variables of integration in a definite integral. That is, we may
 6
change the names of the bound variables in a function expression without
 changing the value of the expression, provided that we make the same change
 for each occurrence of the variable and do not make two variables the same
 that previously were different. Thus λ((x,y),y2 + x),λ((u,v),v2 + u) and
 λ((y,x),x2 + y) denote the same function.
 We shall frequently use expressions in which some of the variables are
 bound by λ’s and others are not. Such an expression may be regarded as
 defining a function with parameters. The unbound variables are called free
 variables.
 An adequate notation that distinguishes functions from forms allows an
 unambiguous treatment of functions of functions. It would involve too much
 of a digression to give examples here, but we shall use functions with functions
 as arguments later in this report.
 Difficulties arise in combining functions described by λ-expressions, or by
 any other notation involving variables, because different bound variables may
 be represented by the same symbol. This is called collision of bound variables.
 There is a notation involving operators that are called combinators for com
bining functions without the use of variables. Unfortunately, the combinatory
 expressions for interesting combinations of functions tend to be lengthy and
 unreadable.
 f. Expressions for Recursive Functions. The λ-notation is inadequate for
 naming functions defined recursively. For example, using λ’s, we can convert
 the definition
 sqrt(a, x,ϵ) = (|x2 − a| < ϵ → x,T → sqrt(a, 1
 2 (x+ a
 x ),ϵ))
 into
 sqrt = λ((a,x,ϵ),(|x2 − a| < ϵ → x,T → sqrt(a, 1
 2 (x+ a
 x ),ϵ))),
 but the right-hand side cannot serve as an expression for the function be
cause there would be nothing to indicate that the reference to sqrt within the
 expression stood for the expression as a whole.
 In order to be able to write expressions for recursive functions, we intro
duce another notation. label(a,E) denotes the expression E, provided that
 occurrences of a within E are to be interpreted as referring to the expression
 7
as a whole. Thus we can write
 label(sqrt, λ((a,x,ϵ),(|x2 − a| < ϵ → x,T → sqrt(a, 1
 2
 (x + a
 x
 ),ϵ))))
 as a name for our sqrt function.
 The symbol a in label (a,E) is also bound, that is, it may be altered
 systematically without changing the meaning of the expression. It behaves
 differently from a variable bound by a λ, however.
 3 RecursiveFunctionsof Symbolic Expressions
 We shall first define a class of symbolic expressions in terms of ordered pairs
 and lists. Then we shall define five elementary functions and predicates, and
 build from them by composition, conditional expressions, and recursive def
initions an extensive class of functions of which we shall give a number of
 examples. We shall then show how these functions themselves can be ex
pressed as symbolic expressions, and we shall define a universal function apply
 that allows us to compute from the expression for a given function its value
 for given arguments. Finally, we shall define some functions with functions as
 arguments and give some useful examples.
 a. A Class of Symbolic Expressions. We shall now define the S-expressions
 (S stands for symbolic). They are formed by using the special characters
 ·
 )
 (
 and an infinite set of distinguishable atomic symbols. For atomic symbols,
 we shall use strings of capital Latin letters and digits with single imbedded
 8
blanks.3 Examples of atomic symbols are
 A
 ABA
 APPLE PIE NUMBER 3
 There is a twofold reason for departing from the usual mathematical prac
tice of using single letters for atomic symbols. First, computer programs fre
quently require hundreds of distinguishable symbols that must be formed from
 the 47 characters that are printable by the IBM 704 computer. Second, it is
 convenient to allow English words and phrases to stand for atomic entities for
 mnemonic reasons. The symbols are atomic in the sense that any substructure
 they may have as sequences of characters is ignored. We assume only that dif
ferent symbols can be distinguished. S-expressions are then defined as follows:
 1. Atomic symbols are S-expressions.
 2. If e1 and e2 are S-expressions, so is (e1 · e2).
 Examples of S-expressions are
 AB
 (A· B)
 ((AB · C)·D)
 An S-expression is then simply an ordered pair, the terms of which may be
 atomic symbols or simpler S-expressions. We can can represent a list of arbi
trary length in terms of S-expressions as follows. The list
 (m1,m2,···,mn)
 is represented by the S-expression
 (m1 · (m2 ·(···(mn · NIL)···)))
 Here NIL is an atomic symbol used to terminate lists. Since many of the
 symbolic expressions with which we deal are conveniently expressed as lists,
 we shall introduce a list notation to abbreviate certain S-expressions. We have
 31995 remark: Imbedded blanks could be allowed within symbols, because lists were then
 written with commas between elements.
 9
l. (m) stands for (m ·NIL).
 2. (m1,···,mn) stands for (m1 · (···(mn · NIL)···)).
 3. (m1,···,mn · x) stands for (m1 · (···(mn · x)···)).
 Subexpressions can be similarly abbreviated. Some examples of these ab
breviations are
 ((AB,C),D) for ((AB ·(C ·NIL))·(D ·NIL))
 ((A,B),C,D ·E) for ((A·(B ·NIL))·(C ·(D ·E)))
 Since we regard the expressions with commas as abbreviations for those
 not involving commas, we shall refer to them all as S-expressions.
 b. Functions of S-expressions and the Expressions That Represent Them.
 Wenow define a class of functions of S-expressions. The expressions represent
ing these functions are written in a conventional functional notation. However,
 in order to clearly distinguish the expressions representing functions from S
expressions, we shall use sequences of lower-case letters for function names
 and variables ranging over the set of S-expressions. We also use brackets and
 semicolons, instead of parentheses and commas, for denoting the application
 of functions to their arguments. Thus we write
 car[x]
 car[cons[(A · B);x]]
 In these M-expressions (meta-expressions) any S-expression that occur stand
 for themselves.
 c. The Elementary S-functions and Predicates. We introduce the following
 functions and predicates:
 1. atom. atom[x] has the value of T or F according to whether x is an
 atomic symbol. Thus
 atom [X] = T
 atom [(X · A)] = F
 2. eq. eq [x;y] is defined if and only if both x and y are atomic. eq [x; y]
 = Tif x and y are the same symbol, and eq [x; y] = F otherwise. Thus
 10
eq [X; X] = T
 eq [X; A] = F
 eq [X; (X · A)] is undefined.
 3. car. car[x] is defined if and only if x is not atomic. car [(e1 · e2)] = e1.
 Thus car [X] is undefined.
 car [(X · A)] = X
 car [((X · A) · Y )] = (X ·A)
 4. cdr. cdr [x] is also defined when x is not atomic. We have cdr
 [(e1 · e2)] = e2. Thus cdr [X] is undefined.
 cdr [(X · A)] = A cdr [((X ·A)·Y)] = Y
 5. cons. cons [x; y] is defined for any x and y. We have cons [e1;e2] =
 (e1 · e2). Thus
 cons [X; A] = (X A)
 cons [(X · A);Y] = ((X ·A)Y)
 car, cdr, and cons are easily seen to satisfy the relations
 car [cons [x; y]] = x
 cdr [cons [x; y]] = y
 cons [car [x]; cdr [x]] = x, provided that x is not atomic.
 The names “car” and “cons” will come to have mnemonic significance only
 when we discuss the representation of the system in the computer. Composi
tions of car and cdr give the subexpressions of a given expression in a given
 position. Compositions of cons form expressions of a given structure out of
 parts. The class of functions which can be formed in this way is quite limited
 and not very interesting.
 d. Recursive S-functions. We get a much larger class of functions (in fact,
 all computable functions) when we allow ourselves to form new functions of
 S-expressions by conditional expressions and recursive definition. We now give
 11
some examples of functions that are definable in this way.
 1. ff[x]. The value of ff[x] is the first atomic symbol of the S-expression x
 with the parentheses ignored. Thus
 f
 f[((A · B) · C)] = A
 We have
 f
 f[x] = [atom[x] → x;T → ff[car[x]]]
 We now trace in detail the steps in the evaluation of
 f
 f [((A · B) · C)]:
 f
 f [((A · B) · C)]
 = [atom[((A·B)·C)] → ((A·B)·C);T → ff[car[((A·B)C·)]]]
 = [F →((A·B)·C);T →ff[car[((A·B)·C)]]]
 = [T →ff[car[((A·B)·C)]]]
 = ff[car[((A·B)·C)]]
 = ff[(A·B)]
 = [atom[(A·B)] → (A·B);T → ff[car[(A·B)]]]
 = [F →(A·B);T →ff[car[(A·B)]]]
 = [T →ff[car[(A·B)]]]
 = ff[car[(A·B)]]
 = ff[A]
 12
= [atom[A] → A;T →ff[car[A]]]
 = [T →A;T →ff[car[A]]]
 = A
 2. subst [x;y;z]. This function gives the result of substituting the S
expression x for all occurrences of the atomic symbol y in the S-expression z.
 It is defined by
 subst [x; y; z] = [atom [z] → [eq [z; y] → x; T → z];
 T →cons [subst [x; y; car [z]]; subst [x; y; cdr [z]]]]
 As an example, we have
 subst[(X · A);B;((A · B) · C)] = ((A· (X ·A))·C)
 3. equal [x; y]. This is a predicate that has the value T if x and y are the
 same S-expression, and has the value F otherwise. We have
 equal [x; y] = [atom [x] ∧ atom [y] ∧ eq [x; y]]
 ∨[¬ atom [x] ∧¬ atom [y] ∧ equal [car [x]; car [y]]
 ∧ equal [cdr [x]; cdr [y]]]
 It is convenient to see how the elementary functions look in the abbreviated
 list notation. The reader will easily verify that
 (i) car[(m1,m2,···,mn)] = m1
 (ii) cdr[(ms,m2,···,mn)] = (m2,···,mn)
 (iii) cdr[(m)] = NIL
 (iv) cons[m1;(m2,···,mn)] = (m1,m2,···,mn)
 (v) cons[m;NIL] = (m)
 We define
 13
null[x] = atom[x] ∧ eq[x;NIL]
 This predicate is useful in dealing with lists.
 Compositions of car and cdr arise so frequently that many expressions can
 be written more concisely if we abbreviate
 cadr[x] for car[cdr[x]],
 caddr[x] for car[cdr[cdr[x]]], etc.
 Another useful abbreviation is to write list [e1;e2;···;en]
 for cons[e1;cons[e2;···;cons[en;NIL]···]].
 This function gives the list, (e1,···,en), as a function of its elements.
 The following functions are useful when S-expressions are regarded as lists.
 1. append [x;y].
 append [x; y] = [null[x] → y; T → cons [car [x]; append [cdr [x]; y]]]
 An example is
 append [(A, B); (C, D, E)] = (A, B, C, D, E)
 2. among [x;y]. This predicate is true if the S-expression x occurs among
 the elements of the list y. We have
 among[x;y] = ¬null[y] ∧ [equal[x;car[y]] ∨ among[x;cdr[y]]]
 3. pair [x;y]. This function gives the list of pairs of corresponding elements
 of the lists x and y. We have
 pair[x; y] = [null[x]∧null[y] → NIL;¬atom[x]∧¬atom[y] → cons[list[car[x];car[y]];pair[cdr[x];cdr[y]]]
 An example is
 pair[(A,B,C);(X,(Y,Z),U)] = ((A,X),(B,(Y,Z)),(C,U)).
 14
4. assoc [x;y]. If y is a list of the form ((u1,v1),···,(un,vn)) and x is one
 of the u’s, then assoc [x;y] is the corresponding v. We have
 assoc[x;y] = eq[caar[y];x] → cadar[y];T → assoc[x;cdr[y]]]
 An example is
 assoc[X;((W,(A,B)),(X,(C,D)),(Y,(E,F)))] = (C,D).
 5. sublis[x;y]. Here x is assumed to have the form of a list of pairs
 ((u1, v1), · · ·, (un,vn)), where the u’s are atomic, and y may be any S-expression.
 The value of sublis[x;y] is the result of substituting each v for the correspond
ing u in y. In order to define sublis, we first define an auxiliary function. We
 have
 sub2[x;z] = [null[x] → z;eq[caar[x];z] → cadar[x];T → sub2[cdr[x];z]]
 and
 sublis[x; y] = [atom[y] → sub2[x;y];T → cons[sublis[x;car[y]];sublis[x;cdr[y]]]
 We have
 sublis [((X, (A, B)), (Y, (B, C))); (A, X · Y)] = (A, (A, B), B, C)
 e. Representation of S-Functions by S-Expressions. S-functions have been
 described by M-expressions. We now give a rule for translating M-expressions
 into S-expressions, in order to be able to use S-functions for making certain
 computations with S-functions and for answering certain questions about S
functions.
 The translation is determined by the following rules in rich we denote the
 translation of an M-expression E by E*.
 1. If E is an S-expression E* is (QUOTE, E).
 2. Variables and function names that were represented by strings of lower
case letters are translated to the corresponding strings of the corresponding
 uppercase letters. Thus car* is CAR, and subst* is SUBST.
 3. A form f[e1;···;en] is translated to (f∗,e∗
 1 ···,e∗
 n). Thus cons [car [x];
 cdr [x]]∗ is (CONS, (CAR, X), (CDR, X)).
 4. {[p1 → e1;···;pn → en]}∗ is (COND, (p∗
 1,e∗
 1),···,(p∗
 n · e∗
 n)).
 15
5. {λ[[x1;···;xn];E]}∗ is (LAMBDA, (x∗
 1,···,x∗
 n),E∗).
 6. {label[a;E]}∗ is (LABEL, a∗, E∗).
 With these conventions the substitution function whose M-expression is
 label [subst; λ [[x; y; z]; [atom [z] → [eq [y; z] → x; T → z]; T → cons [subst
 [x; y; car [z]]; subst [x; y; cdr [z]]]]]] has the S-expression
 (LABEL, SUBST, (LAMBDA, (X, Y, Z), (COND ((ATOM, Z), (COND,
 (EQ, Y, Z), X), ((QUOTE, T), Z))), ((QUOTE, T), (CONS, (SUBST, X, Y,
 (CAR Z)), (SUBST, X, Y, (CDR, Z)))))))
 This notation is writable and somewhat readable. It can be made easier
 to read and write at the cost of making its structure less regular. If more
 characters were available on the computer, it could be improved considerably.4
 f. The Universal S-Function apply. There is an S-function apply with the
 property that if f is an S-expression for an S-function f′ and args is a list of
 arguments of the form (arg1,···,argn), where arg1,···,argn are arbitrary S
expressions, then apply[f;args] and f′[arg1;···;argn] are defined for the same
 values of arg1,···,argn, and are equal when defined. For example,
 λ[[x; y]; cons[car[x]; y]][(A, B);(C,D)]
 =apply[(LAMBDA,(X,Y),(CONS,(CAR,X),Y));((A,B),(C,D))] = (A,C,D)
 The S-function apply is defined by
 apply[f;args] = eval[cons[f;appq[args]];NIL],
 where
 appq[m] = [null[m] → NIL;T → cons[list[QUOTE;car[m]];appq[cdr[m]]]]
 and
 eval[e; a] = [
 41995: More characters were made available on SAIL and later on the Lisp machines.
 Alas, the world went back to inferior character sets again—though not as far back as when
 this paper was written in early 1959.
 16
atom [e] → assoc [e; a];
 atom [car [e]] → [
 eq [car [e]; QUOTE] → cadr [e];
 eq [car [e]; ATOM] → atom [eval [cadr [e]; a]];
 eq [car [e]; EQ] → [eval [cadr [e]; a] = eval [caddr [e]; a]];
 eq [car [e]; COND] → evcon [cdr [e]; a];
 eq [car [e]; CAR] → car [eval [cadr [e]; a]];
 eq [car [e]; CDR] → cdr [eval [cadr [e]; a]];
 eq [car [e]; CONS] → cons [eval [cadr [e]; a]; eval [caddr [e];
 a]]; T → eval [cons [assoc [car [e]; a];
 evlis [cdr [e]; a]]; a]];
 eq [caar [e]; LABEL] → eval [cons [caddar [e]; cdr [e]];
 cons [list [cadar [e]; car [e]; a]];
 eq [caar [e]; LAMBDA] → eval [caddar [e];
 append [pair [cadar [e]; evlis [cdr [e]; a]; a]]]
 and
 and
 evcon[c;a] = [eval[caar[c];a] → eval[cadar[c];a];T → evcon[cdr[c];a]]
 evlis[m;a] = [null[m] → NIL;T → cons[eval[car[m];a];evlis[cdr[m];a]]]
 17
We now explain a number of points about these definitions. 5
 1. apply itself forms an expression representing the value of the function
 applied to the arguments, and puts the work of evaluating this expression onto
 a function eval. It uses appq to put quotes around each of the arguments, so
 that eval will regard them as standing for themselves.
 2. eval[e;a] has two arguments, an expression e to be evaluated, and a list
 of pairs a. The first item of each pair is an atomic symbol, and the second is
 the expression for which the symbol stands.
 3. If the expression to be evaluated is atomic, eval evaluates whatever is
 paired with it first on the list a.
 4. If e is not atomic but car[e] is atomic, then the expression has one of the
 forms (QUOTE,e)or(ATOM,e)or(EQ,e1,e2)or(COND,(p1,e1),···,(pn,en)),
 or (CAR,e) or (CDR,e) or (CONS,e1,e2) or (f,e1,···,en) where f is an
 atomic symbol.
 In the case (QUOTE,e) the expression e, itself, is taken. In the case of
 (ATOM,e) or (CAR,e) or (CDR,e) the expression e is evaluated and the
 appropriate function taken. In the case of (EQ,e1,e2) or (CONS,e1,e2) two
 expressions have to be evaluated. In the case of (COND,(p1,e1),···(pn,en))
 the p’s have to be evaluated in order until a true p is found, and then the
 corresponding e must be evaluated. This is accomplished by evcon. Finally, in
 the case of (f,e1,···,en) we evaluate the expression that results from replacing
 f in this expression by whatever it is paired with in the list a.
 5. The evaluation of ((LABEL,f,E),e1,···,en) is accomplished by eval
uating (E,e1,···,en) with the pairing (f,(LABEL,f,E)) put on the front of
 the previous list a of pairs.
 6. Finally, the evaluation of ((LAMBDA,(x1,···,xn),E),e1,···en) is ac
complished by evaluating E with the list of pairs ((x1,e1),···,((xn,en)) put
 on the front of the previous list a.
 The list a could be eliminated, and LAMBDA and LABEL expressions
 evaluated by substituting the arguments for the variables in the expressions
 E. Unfortunately, difficulties involving collisions of bound variables arise, but
 they are avoided by using the list a.
 51995: This version isn’t quite right. A comparison of this and other versions of eval
 including what was actually implemented (and debugged) is given in “The Influence of the
 Designer on the Design” by Herbert Stoyan and included in Artificial Intelligence and Math
ematical Theory of Computation: Papers in Honor of John McCarthy, Vladimir Lifschitz
 (ed.), Academic Press, 1991
 18
Calculating the values of functions by using apply is an activity better
 suited to electronic computers than to people. As an illustration, however, we
 now give some of the steps for calculating
 apply [(LABEL, FF, (LAMBDA, (X), (COND, (ATOM, X), X), ((QUOTE,
 T),(FF, (CAR, X))))));((A· B))] = A
 The first argument is the S-expression that represents the function ff defined
 in section 3d. We shall abbreviate it by using the letter φ. We have
 apply [φ; ( (A·B) )]
 = eval [((LABEL, FF, ψ), (QUOTE, (A·B))); NIL]
 where ψ is the part of φ beginning (LAMBDA
 = eval[((LAMBDA, (X), ω), (QUOTE, (A·B)));((FF, φ))]
 where ω is the part of ψ beginning (COND
 = eval [(COND, (π1,ϵ1),(π2,ϵ2)); ((X, (QUOTE, (A·B) ) ), (FF, φ) )]
 Denoting ((X, (QUOTE, (A·B))), (FF, φ)) by a, we obtain
 = evcon [((π1,ϵ1), (π2,ϵ2)); a]
 This involves eval [π1;a]
 = eval [( ATOM, X); a]
 = atom [eval [X; a]]
 = atom [eval [assoc [X; ((X, (QUOTE, (A·B))), (FF,φ))];a]]
 = atom [eval [(QUOTE, (A·B)); a]]
 = atom [(A·B)],
 = F
 Our main calulation continues with
 19
apply [φ; ((A·B))]
 = evcon [((π2,ϵ2,));a],
 which involves eval [π2;a] = eval [(QUOTE, T); a] = T
 Our main calculation again continues with
 apply [φ; ((A·B))]
 = eval [ϵ2;a]
 = eval [(FF, (CAR, X));a]
 = eval [Cons [φ; evlis [((CAR, X)); a]]; a]
 Evaluating evlis [((CAR, X)); a] involves
 eval [(CAR, X); a]
 = car [eval [X; a]]
 = car [(A·B)], where we took steps from the earlier computation of atom [eval [X; a]] = A,
 and so evlis [((CAR, X)); a] then becomes
 list [list [QUOTE; A]] = ((QUOTE, A)),
 and our main quantity becomes
 = eval [(φ, (QUOTE, A)); a]
 The subsequent steps are made as in the beginning of the calculation. The
 LABEL and LAMBDA cause new pairs to be added to a, which gives a new
 list of pairs a1. The π1 term of the conditional eval [(ATOM, X); a1] has the
 20
value T because X is paired with (QUOTE, A) first in a1, rather than with
 (QUOTE, (A·B)) as in a.
 Therefore we end up with eval [X; a1] from the evcon, and this is just A.
 g. Functions with Functions as Arguments. There are a number of useful
 functions some of whose arguments are functions. They are especially useful
 in defining other functions. One such function is maplist[x;f] with an S
expression argument x and an argument f that is a function from S-expressions
 to S-expressions. We define
 maplist[x;f] = [null[x] → NIL;T → cons[f[x];maplist[cdr[x];f]]]
 The usefulness of maplist is illustrated by formulas for the partial derivative
 with respect to x of expressions involving sums and products of x and other
 variables. The S-expressions that we shall differentiate are formed as follows.
 1. An atomic symbol is an allowed expression.
 2. If e1,e2,···,en are allowed expressions, ( PLUS, e1,···,en) and (TIMES,
 e1, · · ·, en) are also, and represent the sum and product, respectively, of e1,···,en.
 This is, essentially, the Polish notation for functions, except that the in
clusion of parentheses and commas allows functions of variable numbers of
 arguments. An example of an allowed expression is (TIMES, X, (PLUS, X,
 A), Y), the conventional algebraic notation for which is X(X + A)Y.
 Our differentiation formula, which gives the derivative of y with respect to
 x, is
 diff [y; x] = [atom [y] → [eq [y; x] → ONE; T → ZERO]; eq [car [Y]; PLUS]
 →cons [PLUS; maplist [cdr [y]; λ[[z]; diff [car [z]; x]]]]; eq[car [y]; TIMES] →
 cons[PLUS; maplist[cdr[y]; λ[[z]; cons [TIMES; maplist[cdr [y]; λ[[w]; ¬ eq [z;
 w] → car [w]; T → diff [car [[w]; x]]]]]]]
 The derivative of the expression (TIMES, X, (PLUS, X, A), Y), as com
puted by this formula, is
 (PLUS, (TIMES, ONE, (PLUS, X, A), Y), (TIMES, X, (PLUS, ONE,
 ZERO), Y), (TIMES, X, (PLUS, X, A), ZERO))
 Besides maplist, another useful function with functional arguments is search,
 which is defined as
 search[x;p;f;u] = [null[x] → u;p[x] → f[x];T → search[cdr[x];p;f;u]
 21
The function search is used to search a list for an element that has the property
 p, and if such an element is found, f of that element is taken. If there is no
 such element, the function u of no arguments is computed.
 4 The LISP Programming System
 The LISP programming system is a system for using the IBM 704 computer to
 compute with symbolic information in the form of S-expressions. It has been
 or will be used for the following purposes:
 l. Writing a compiler to compile LISP programs into machine language.
 2. Writing a program to check proofs in a class of formal logical systems.
 3. Writing programs for formal differentiation and integration.
 4. Writing programs to realize various algorithms for generating proofs in
 predicate calculus.
 5. Making certain engineering calculations whose results are formulas
 rather than numbers.
 6. Programming the Advice Taker system.
 The basis of the system is a way of writing computer programs to evaluate
 S-functions. This will be described in the following sections.
 In addition to the facilities for describing S-functions, there are facilities
 for using S-functions in programs written as sequences of statements along the
 lines of FORTRAN (4) or ALGOL (5). These features will not be described
 in this article.
 a. Representation of S-Expressions by List Structure. A list structure is a
 collection of computer words arranged as in figure 1a or 1b. Each word of the
 list structure is represented by one of the subdivided rectangles in the figure.
 The left box of a rectangle represents the address field of the word and the
 right box represents the decrement field. An arrow from a box to another
 rectangle means that the field corresponding to the box contains the location
 of the word corresponding to the other rectangle.
 22
An S-expression x that is not atomic is represented by a word, the address
 and decrement parts of which contain the locations of the subexpressions car[x]
 and cdr[x], respectively. If we use the symbols A, B, etc. to denote the
 locations of the association list of these symbols, then the S-expression ((A ·
 B) · (C · (E · F))) is represented by the list structure a of figure 2. Turning
 to the list form of S-expressions, we see that the S-expression (A,(B,C),D),
 which is an abbreviation for (A·((B ·(C ·NIL))·(D ·NIL))), is represented
 by the list structure of figure 2b.
 23
 It is permitted for a substructure to occur in more than one place in a list
 structure, as in figure 1b, but it is not permitted for a structure to have cycles,
 as in figure 1c. An atomic symbol is represented in the computer by a list
 structure of special form called the association list of the symbol. The address
 f
 ield of the first word contains a special constant which enables the program to
 tell that this word represents an atomic symbol. We shall describe association
 lists in section 4b.--
 Fig. 1--------------------
--
A--
 D
 C--
 A B
 (a)
 E F
B
 (b)
Figure 2
 C
 When a list structure is regarded as representing a list, we see that each term
 of the list occupies the address part of a word, the decrement part of which
 points to the word containing the next term, while the last word has NIL in
 its decrement.
 An expression that has a given subexpression occurring more than once
 can be represented in more than one way. Whether the list structure for
 the subexpression is or is not repeated depends upon the history of the pro
gram. Whether or not a subexpression is repeated will make no difference
 in the results of a program as they appear outside the machine, although it
 will affect the time and storage requirements. For example, the S-expression
 ((A·B)·(A·B)) can be represented by either the list structure of figure 3a or
 3b.----
 A B AB
 (a)--
 A B
 (b)
 Figure 3
 The prohibition against circular list structures is essentially a prohibition
 24
against an expression being a subexpression of itself. Such an expression could
 not exist on paper in a world with our topology. Circular list structures would
 have some advantages in the machine, for example, for representing recursive
 functions, but difficulties in printing them, and in certain other operations,
 make it seem advisable not to use them for the present.
 The advantages of list structures for the storage of symbolic expressions
 are:
 1. The size and even the number of expressions with which the program
 will have to deal cannot be predicted in advance. Therefore, it is difficult to
 arrange blocks of storage of fixed length to contain them.
 2. Registers can be put back on the free-storage list when they are no longer
 needed. Even one register returned to the list is of value, but if expressions
 are stored linearly, it is difficult to make use of blocks of registers of odd sizes
 that may become available.
 3. An expression that occurs as a subexpression of several expressions need
 be represented in storage only once.
 b. Association Lists6 . In the LISP programming system we put more in
 the association list of a symbol than is required by the mathematical system
 described in the previous sections. In fact, any information that we desire to
 associate with the symbol may be put on the association list. This information
 may include: the print name, that is, the string of letters and digits which
 represents the symbol outside the machine; a numerical value if the symbol
 represents a number; another S-expression if the symbol, in some way, serves
 as a name for it; or the location of a routine if the symbol represents a function
 for which there is a machine-language subroutine. All this implies that in the
 machine system there are more primitive entities than have been described in
 the sections on the mathematical system.
 For the present, we shall only describe how print names are represented
 on association lists so that in reading or printing the program can establish
 a correspondence between information on punched cards, magnetic tape or
 printed page and the list structure inside the machine. The association list of
 the symbol DIFFERENTIATE has a segment of the form shown in figure 4.
 Here pname is a symbol that indicates that the structure for the print name
 of the symbol whose association list this is hanging from the next word on
 the association list. In the second row of the figure we have a list of three
 words. The address part of each of these words points to a Word containing
 61995: These were later called property lists.
 25
six 6-bit characters. The last word is filled out with a 6-bit combination that
 does not represent a character printable by the computer. (Recall that the
 IBM 7O4 has a 36-bit word and that printable characters are each represented
 by 6 bits.) The presence of the words with character information means that
 the association lists do not themselves represent S-expressions, and that only
 some of the functions for dealing with S-expressions make sense within an
 association list.
 ...
pname--
DIFFER--
ENTIAT
 ....--
 E ??????
 Figure 4
 c. Free-Storage List. At any given time only a part of the memory reserved
 for list structures will actually be in use for storing S-expressions. The remain
ing registers (in our system the number, initially, is approximately 15,000) are
 arranged in a single list called the free-storage list. A certain register, FREE,
 in the program contains the location of the first register in this list. When
 a word is required to form some additional list structure, the first word on
 the free-storage list is taken and the number in register FREE is changed to
 become the location of the second word on the free-storage list. No provision
 need be made for the user to program the return of registers to the free-storage
 list.
 This return takes place automatically, approximately as follows (it is nec
essary to give a simplified description of this process in this report): There is
 a fixed set of base registers in the program which contains the locations of list
 structures that are accessible to the program. Of course, because list struc
tures branch, an arbitrary number of registers may be involved. Each register
 that is accessible to the program is accessible because it can be reached from
 one or more of the base registers by a chain of car and cdr operations. When
 26
the contents of a base register are changed, it may happen that the register
 to which the base register formerly pointed cannot be reached by a car − cdr
 chain from any base register. Such a register may be considered abandoned
 by the program because its contents can no longer be found by any possible
 program; hence its contents are no longer of interest, and so we would like to
 have it back on the free-storage list. This comes about in the following way.
 Nothing happens until the program runs out of free storage. When a free
 register is wanted, and there is none left on the free-storage list, a reclamation7
 cycle starts.
 First, the program finds all registers accessible from the base registers and
 makes their signs negative. This is accomplished by starting from each of the
 base registers and changing the sign of every register that can be reached from
 it by a car − cdr chain. If the program encounters a register in this process
 which already has a negative sign, it assumes that this register has already
 been reached.
 After all of the accessible registers have had their signs changed, the pro
gramgoes through the area of memory reserved for the storage of list structures
 and puts all the registers whose signs were not changed in the previous step
 back on the free-storage list, and makes the signs of the accessible registers
 positive again.
 This process, because it is entirely automatic, is more convenient for the
 programmer than a system in which he has to keep track of and erase un
wanted lists. Its efficiency depends upon not coming close to exhausting the
 available memory with accessible lists. This is because the reclamation process
 requires several seconds to execute, and therefore must result in the addition
 of at least several thousand registers to the free-storage list if the program is
 not to spend most of its time in reclamation.
 d. Elementary S-Functions in the Computer. We shall now describe the
 computer representations of atom, = , car, cdr, and cons. An S-expression
 is communicated to the program that represents a function as the location of
 the word representing it, and the programs give S-expression answers in the
 same form.
 atom. As stated above, a word representing an atomic symbol has a special
 7We already called this process “garbage collection”, but I guess I chickened out of using
 it in the paper—or else the Research Laboratory of Electronics grammar ladies wouldn’t let
 me.
 27
constant in its address part: atom is programmed as an open subroutine that
 tests this part. Unless the M-expression atom[e] occurs as a condition in a
 conditional expression, the symbol T or F is generated as the result of the
 test. In case of a conditional expression, a conditional transfer is used and the
 symbol T or F is not generated.
 eq. The program for eq[e;f] involves testing for the numerical equality of
 the locations of the words. This works because each atomic symbol has only
 one association list. As with atom, the result is either a conditional transfer
 or one of the symbols T or F.
 car. Computing car[x] involves getting the contents of the address part of
 register x. This is essentially accomplished by the single instruction CLA 0, i,
 where the argument is in index register, and the result appears in the address
 part of the accumulator. (We take the view that the places from which a
 function takes its arguments and into which it puts its results are prescribed
 in the definition of the function, and it is the responsibility of the programmer
 or the compiler to insert the required datamoving instructions to get the results
 of one calculation in position for the next.) (“car” is a mnemonic for “contents
 of the address part of register.”)
 cdr. cdr is handled in the same way as car, except that the result appears
 in the decrement part of the accumulator (“cdr” stands for “contents of the
 decrement part of register.”)
 cons. The value of cons[x;y] must be the location of a register that has x
 and y in its address and decrement parts, respectively. There may not be such
 a register in the computer and, even if there were, it would be time-consuming
 to find it. Actually, what we do is to take the first available register from the
 free-storage list, put x and y in the address and decrement parts, respectively,
 and make the value of the function the location of the register taken. (“cons”
 is an abbreviation for “construct.”)
 It is the subroutine for cons that initiates the reclamation when the free
storage list is exhausted. In the version of the system that is used at present
 cons is represented by a closed subroutine. In the compiled version, cons is
 open.
 e. Representation of S-Functions by Programs. The compilation of func
tions that are compositions of car, cdr, and cons, either by hand or by a
 compiler program, is straightforward. Conditional expressions give no trouble
 except that they must be so compiled that only the p’s and e’s that are re
28
quired are computed. However, problems arise in the compilation of recursive
 functions.
 In general (we shall discuss an exception), the routine for a recursive func
tion uses itself as a subroutine. For example, the program for subst[x;y;z] uses
 itself as a subroutine to evaluate the result of substituting into the subexpres
sions car[z] and cdr[z]. While subst[x;y;cdr[z]] is being evaluated, the result
 of the previous evaluation of subst[x;y;car[z]] must be saved in a temporary
 storage register. However, subst may need the same register for evaluating
 subst[x; y;cdr[z]]. This possible conflict is resolved by the SAVE and UN
SAVE routines that use the public push-down list 8. The SAVE routine is
 entered at the beginning of the routine for the recursive function with a re
quest to save a given set of consecutive registers. A block of registers called
 the public push-down list is reserved for this purpose. The SAVE routine has
 an index that tells it how many registers in the push-down list are already
 in use. It moves the contents of the registers which are to be saved to the
 f
 irst unused registers in the push-down list, advances the index of the list, and
 returns to the program from which control came. This program may then
 freely use these registers for temporary storage. Before the routine exits it
 uses UNSAVE, which restores the contents of the temporary registers from
 the push-down list and moves back the index of this list. The result of these
 conventions is described, in programming terminology, by saying that the re
cursive subroutine is transparent to the temporary storage registers.
 f. Status of the LISP Programming System (February 1960). A variant of
 the function apply described in section 5f has been translated into a program
 APPLY for the IBM 704. Since this routine can compute values of S-functions
 given their descriptions as S-expressions and their arguments, it serves as an
 interpreter for the LISP programming language which describes computation
 processes in this way.
 The program APPLY has been imbedded in the LISP programming system
 which has the following features:
 1. The programmer maydefine anynumber ofS-functions by S-expressions.
 these functions may refer to each other or to certain S-functions represented
 by machine language program.
 2. The values of defined functions may be computed.
 3. S-expressions may be read and printed (directly or via magnetic tape).
 81995: now called a stack
 29
4. Some error diagnostic and selective tracing facilities are included.
 5. The programmer may have selected S-functions compiled into machine
 language programs put into the core memory. Values of compiled functions
 are computed about 60 times as fast as they would if interpreted. Compilation
 is fast enough so that it is not necessary to punch compiled program for future
 use.
 6. A “program feature” allows programs containing assignment and go to
 statements in the style of ALGOL.
 7. Computation with floating point numbers is possible in the system, but
 this is inefficient.
 8. A programmer’s manual is being prepared. The LISP programming
 system is appropriate for computations where the data can conveniently be
 represented as symbolic expressions allowing expressions of the same kind as
 subexpressions. A version of the system for the IBM 709 is being prepared.
 5 Another Formalism for Functions of Sym
bolic Expressions
 There are a number of ways of defining functions of symbolic expressions which
 are quite similar to the system we have adopted. Each of them involves three
 basic functions, conditional expressions, and recursive function definitions, but
 the class of expressions corresponding to S-expressions is different, and so are
 the precise definitions of the functions. We shall describe one of these variants
 called linear LISP.
 The L-expressions are defined as follows:
 1. A finite list of characters is admitted.
 2. Any string of admitted characters in an L-expression. This includes the
 null string denoted by Λ.
 There are three functions of strings:
 1. first[x] is the first character of the string x.
 first[Λ] is undefined. For example: first[ABC] = A
 2. rest[x] is the string of characters which remains when the first character
 of the string is deleted.
 rest[Λ] is undefined. For example: rest[ABC] = BC.
 3. combine[x;y] is the string formed by prefixing the character x to the
 string y. For example: combine[A;BC] = ABC
 30
There are three predicates on strings:
 1. char[x], x is a single character.
 2. null[x], x is the null string.
 3. x =y, defined for x and y characters.
 The advantage of linear LISP is that no characters are given special roles,
 as are parentheses, dots, and commas in LISP. This permits computations
 with all expressions that can be written linearly. The disadvantage of linear
 LISP is that the extraction of subexpressions is a fairly involved, rather than
 an elementary, operation. It is not hard to write, in linear LISP, functions that
 correspond to the basic functions of LISP, so that, mathematically, linear LISP
 includes LISP. This turns out to be the most convenient way of programming,
 in linear LISP, the more complicated manipulations. However, if the functions
 are to be represented by computer routines, LISP is essentially faster.
 6 Flowcharts and Recursion
 Since both the usual form of computer program and recursive function defi
nitions are universal computationally, it is interesting to display the relation
 between them. The translation of recursive symbolic functions into computer
 programs was the subject of the rest of this report. In this section we show
 how to go the other way, at least in principle.
 The state of the machine at any time during a computation is given by the
 values of a number of variables. Let these variables be combined into a vector
 ξ. Consider a program block with one entrance and one exit. It defines and is
 essentially defined by a certain function f that takes one machine configuration
 into another, that is, f has the form ξ′ = f(ξ). Let us call f the associated
 function of the program block. Now let a number of such blocks be combined
 into a program by decision elements π that decide after each block is completed
 which block will be entered next. Nevertheless, let the whole program still have
 one entrance and one exit.
 31
?-?
 π1
 XXXz
 f1
 HHHj+
 π2
 ?
 f3
 T
 ?
 π3
 ?
 f4
 ?
 ?
 S
 f2
 Figure 5
 Wegive as an example the flowcart of figure 5. Let us describe the function
 r[ξ] that gives the transformation of the vector ξ between entrance and exit
 of the whole block. We shall define it in conjunction with the functions s(ξ),
 and t[ξ], which give the transformations that ξ undergoes between the points
 S and T, respectively, and the exit. We have
 r[ξ] = [π11[ξ] → S[f1[ξ]];T → S[f2[ξ]]]
 S[ξ] = [π21[ξ] → r[ξ];T → t[f3[ξ]]]
 t[ξ] = [π3I[ξ] → f4[ξ];π32[ξ] → r[ξ];T → t[f3[ξ]]]
 Given a flowchart with a single entrance and a single exit, it is easy to
 write down the recursive function that gives the transformation of the state
 vector from entrance to exit in terms of the corresponding functions for the
 computation blocks and the predicates of the branch. In general, we proceed
 as follows.
 In figure 6, let β be an n-way branch point, and let f1,···,fn be the
 computations leading to branch points β1,β2,···,βn. Let φ be the function
 32
thattransformsξbetweenβandtheexitof thechart,andletφ1,···,φnbe
 thecorrespondingfunctionsforβ1,···,βn.Wethenwrite
 φ[ξ]=[p1[ξ]→φ1[f1[ξ]];···;pn[ξ]→φn[ξ]]]
 @
 @@
 @
 @ @
 ?
 A
 A
 A
 AAU
 C
 C CW ?
 ....
 .....
 ..... f1 f2 fn
 β
 β1 β2
 βn
 φ1 φ2
 φn
 φ
 Figure6
 7 Acknowledgments
 Theinadequacyoftheλ-notationfornamingrecursivefunctionswasnoticed
 byN.Rochester, andhediscoveredanalternative tothe solution involving
 labelwhichhasbeenusedhere. The formof subroutine forconswhichper
mits its compositionwithother functionswas invented, inconnectionwith
 anotherprogrammingsystem, byC.GerberickandH.L.Gelernter, of IBM
 Corporation. TheLlSPprogrammingsystemwasdevelopedbyagroupin
cludingR.Brayton,D.Edwards,P.Fox,L.Hodes,D.Luckham,K.Maling,
 J.McCarthy,D.Park,S.Russell.
 ThegroupwassupportedbytheM.I.T.ComputationCenter,andbythe
 M.I.T.ResearchLaboratoryofElectronics(whichissupportedinpartbythe
 theU.S.Army(SignalCorps),theU.S.AirForce(OfficeofScientificResearch,
 AirResearchandDevelopmentCommand),andtheU.S.Navy(OfficeofNaval
 Research)).Theauthoralsowishestoacknowledgethepersonalfinancialsup
33
port of the Alfred P. Sloan Foundation.
 REFERENCES
 1. J. McCARTHY, Programs with common sense, Paper presented at the
 Symposium on the Mechanization of Thought Processes, National Physical
 Laboratory, Teddington, England, Nov. 24-27, 1958. (Published in Proceed
ings of the Symposium by H. M. Stationery Office).
 2. A. NEWELLANDJ.C.SHAW,Programmingthelogictheory machine,
 Proc. Western Joint Computer Conference, Feb. 1957.
 3. A. CHURCH, The Calculi of Lambda-Conversion (Princeton University
 Press, Princeton, N. J., 1941).
 4. FORTRAN Programmer’s Reference Manual, IBM Corporation, New
 York, Oct. 15, 1956.
 5. A. J. PERLIS AND K. SAMELS0N, International algebraic language,
 Preliminary Report, Comm. Assoc. Comp. Mach., Dec. 1958.
 34



RECURSIVE FUNCTIONS OF SYMBOLIC EXPRESSIONS 
AND THEIR COMPUTATION BY MACHINE
 The LISP Programming. System
 J. McCarthy
 Artificial Intelligence Group 
M. I. T. Computation Center 
and
 Research Laboratory of Electronics 
, Cambridge, Massachusetts
 Reprinted from Quarterly Progress Report No. 53, Research Laboratory 
of Electronics, Massachusetts Institute of Technology, April 15, 1959.
D. 
1. 
RECURSIVE FUNCTIONS OF SYMBOLIC EXPRESSIONS AND THEIR 
COMPUTATION BY MACHINE
 Introduction
 A programming system called LISP (for LISt Processor) has been developed for the 
IBM 704 computer by the Artificial Intelligence group. The system was designed to 
~~]
 facilitate experiments with a proposed system called the Advice Taker, whereby a 
machine could be instructed to handle declarative as well as imperative sentences and J
 could exhibit "common sense" in carrying out its instructions. The original proposal (1) 
for the Advice Taker was made in November 1958. The main requirement was a pro- 
gramming system for manipulating expressions representing formalized declarative and 
imperative sentences so that the Advice Taker system could make deductions.
 In the course of its development the LISP system went through several stages of 
simplification and eventually came to be based on a scheme for representing the partial 
recursive functions of a certain class of symbolic expressions. This representation is 
independent of the IBM 704 computer, or of any other electronic computer, and it now 
seems expedient to expound the system by starting with the class of expressions called 
S-expressions and the functions called S-functions.
 In this report we first describe the class of S-expressions and S-functions. Then we 
describe the representation of S-functions by S-expressions, which enables us to prove 
that all computable partial functions have been obtained, to obtain a universal S-function, 
and to exhibit a set of questions about S-expressions which cannot be decided by an S- 
function. We describe the representation of S-functions by programs in the IBM 704 
computer, and the representation of S-expressions by list structures similar to those 
]
 / 
used by Newell, Simon, and Shaw (2).
 Although we have not carried the development of recursive function theory in terms 
of S-functions and their representation by S-expressions beyond the simplest theorems, 
it seems that formulation of this theory in terms of S-functions has important advantages. 
Devices such as Godel numbering are unnecessary, and so is the construction of parti- 
cular Turing machines. (These constructions are all artificial in terms of what is 
intended to be accomplished by them.) The advantage stems from the fact that functions 
of symbolic expressions are easily and briefly described as S-expressions, and the 
representation of S-functions by S-expressions is trivial. Moreover, a large class of 
S-expression representations of S-functions translate directly into efficient machine
 124



 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


























 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=