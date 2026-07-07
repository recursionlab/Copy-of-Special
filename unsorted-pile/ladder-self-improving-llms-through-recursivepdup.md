---
stub: true
title: "Ladder Self Improving Llms Through Recursive.P Dup"
created: 2026-05-12
updated: 2026-05-12
type: concept
tags: [tuu, "ingested"]
sources: ["LADDER SELF-IMPROVING LLMS THROUGH RECURSIVE.p_dup.md"]
psi_tier: tuu
---

# Ladder Self Improving Llms Through Recursive.P Dup

# LADDER SELF-IMPROVING LLMS THROUGH RECURSIVE.p

LADDER: SELF-IMPROVING LLMS THROUGH RECURSIVE PROBLEM DECOMPOSITION

Toby Simonds Tufa Labs

toby@tufalabs.ai

Akira Yoshiyama Tufa Labs

akira@tufalabs.ai

March 6, 2025
ABSTRACT
We introduce LADDER (Learning through Autonomous Difficulty-Driven Example Recursion), a framework which enables Large Language Models to autonomously improve their problem-solving capabilities through self-guided learning by recursively generating and solving progressively simpler variants of complex problems. Unlike prior approaches that require curated datasets or human feedback, LADDER leverages a model’s own capabilities to generate easier question variants. We demonstrate LADDER’s effectiveness on the subject of mathematical integration, improving Llama 3.2 3B’s accuracy from 1% to 82% on undergraduate-level problems and enabling Qwen2.5 7B Deepseek-R1 Distilled to achieve 73% on the MIT Integration Bee qualifying examination. We also introduce TTRL (Test-Time Reinforcement Learning), where we perform reinforcement learning on variants of test problems at inference time. TTRL enables Qwen2.5 7B Deepseek-R1 Distilled to achieve a state-of-the-art score of 90% on the MIT Integration Bee qualifying examination, surpassing OpenAI o1’s performance. These results show how self-directed strategic learning can achieve significant capability improvements without relying on architectural scaling or human supervision.
1 Introduction
Reinforcement Learning (RL) has emerged as a highly effective approach for training Large Language Models (LLMs), yet its success hinges critically on the availability of appropriate training tasks [5, 9, 10, 12]. A fundamental challenge lies in obtaining verifiable tasks that match the model’s current capabilities. For RL to be effective, tasks must form a gradient of difficulties that allows for incremental learning progress [8]. When tasks exceed the model’s current abilities, the training process not only stalls but can lead to catastrophic collapse, resulting in degraded performance. This challenge is particularly acute in domains requiring complex reasoning, where the gap between simple and advanced tasks can be substantial [4, 12].
We propose Learning through Autonomous Difficulty-Driven Example Recursion (LADDER), a framework that enables LLMs to autonomously improve their problem-solving capabilities through strategic self-guided learning. The key insight is that models can bootstrap their own learning by recursively generating and solving progressively simpler variants of complex problems. For each challenging problem, LADDER prompts the model to create multiple easier variants, forming a natural difficulty gradient. This process continues recursively, with each variant spawning simpler sub-variants, until reaching problems the model can reliably solve. The solutions to these simpler problems then provide stepping stones for tackling progressively harder variants. We demonstrate that this self-bootstrapping approach achieves dramatic improvements beyond what’s possible through standard techniques like pass@k sampling - enabling models to reliably solve problems that were previously far beyond their capabilities.
Unlike previous approaches requiring carefully curated datasets or human feedback, LADDER leverages the model’s existing capabilities to create a natural difficulty gradient, allowing for systematic improvement through reinforcement learning with verifiable rewards. The framework requires only a reliable verification mechanism - in our case, numerical integration for checking solutions. This enables the model to assess its own progress and guide its learning trajectory without human intervention.
We demonstrate LADDER’s effectiveness on mathematical integration tasks, achieving remarkable improvements across multiple benchmarks. Using this approach, we improve a Llama 3B model’s accuracy from 1% to 82% on undergraduate-level integration problems. When applied to the challenging 2025 MIT Integration Bee examination, LADDER enables a 7B parameter model to achieve 73% accuracy, significantly outperforming much larger models, such as GPT-4o (42%), and typical human performance (15-30%). These results showcase how strategic problem decomposition and verified self-learning can achieve substantial capability improvements without relying on architectural scaling or human supervision.
Building on LADDER’s self-improvement framework, we propose Test-Time Reinforcement Learning (TTRL), a novel approach that extends these principles to inference time. TTRL dynamically generates problem variants during test-time and applies reinforcement learning to refine the model’s solutions, effectively creating a micro-learning process for each test instance. By leveraging the same verification mechanisms used in training, TTRL enables the model to further improve its performance. When applied to the 2025 MIT Integration Bee, TTRL boosts accuracy from 73% - with just LADDER - to 90%, demonstrating how scaling test-time compute through strategic problem decomposition can yield substantial performance improvements. We achieve state of the art accuracy, outperforming significantly larger models, such as OpenAI’s o1.
Thus, we make the following contributions:

We propose a novel framework for autonomous model improvement through recursive problem decomposition and self-guided learning via reinforcement learning with GRPO.

We develop a systematic method for generating and verifying problem variants that create natural difficulty gradients, requiring only numerical verification.

We demonstrate significant empirical improvements on mathematical reasoning tasks, improving a Llama 3B model from 2% to 82% on undergraduate integration problems and achieving 73% accuracy on the MIT Integration Bee with a 7B model, matching SoTA performance

We introduce Test-Time Reinforcement Learning (TTRL), a method for scaling compute at inference time through variant generation and reinforcement learning, boosting performance on the MIT Integration Bee from 73% to 90%.
2 Related Work
Self-Improvement and Automated Curriculum Generation in LLMs. Haluptzok et al. (2023) present a self-play setup where a code-focused LLM continually invents and solves new programming puzzles, checks solutions with a Python interpreter, and fine-tunes on correct results [3]. We build upon the generate → solve → verify → learn cycle, adding a more explicit curricular element to guide the model’s step-by-step improvement.
Recent advances such as STaR (Self-Taught Reasoner) have illustrated that LLMs can improve their reasoning skills by learning from their own generated chain-of-thoughts—effectively acting as both student and teacher [15]. Unlike traditional self-play techniques that require competitive dynamics, these methods harness the model’s intrinsic capacity to generate and evaluate intermediate reasoning steps, automatically curating training examples that progressively reduce task complexity. Our work extends this line of research by systematically transforming unsolvable problems into tractable sub-problems, thereby constructing an end-to-end self-improving framework that requires no human annotation or intervention.
Test-Time Compute Scaling and Reasoning Improvements. Recent work has explored various approaches to im-proving model performance through increased compute at inference time. "Let’s Verify Step by Step" [6] demonstrated that breaking down verification into explicit steps and allocating additional computation to each verification component can significantly improve performance. Similarly, Tree of Thoughts [14] showed how systematically exploring multiple reasoning paths during inference can lead to better problem-solving capabilities. These approaches typically focus on increasing the length and deliberation of model outputs, either through structured prompting, such as s1, or systematic exploration of solution spaces, such as self-consistency [7, 12]. Our work differs fundamentally from these approaches by introducing dynamic learning at test-time - rather than just increasing reasoning length or exploring multiple paths, TTRL enables the model to actually improve its capabilities through practice on related problems. This represents a shift from static inference-time techniques to dynamic adaptation through targeted learning.
Reinforcement Learning Approaches for LLM Self-Improvement. In recent years, reinforcement learning has emerged as a pivotal strategy for enabling language models to self-improve through iterative self-correction and feedback. Notably, OpenAI’s o1 model uses reinforcement learning to refine its chain-of-thought reasoning—learning to
2
Figure 1: Example of variant generation for an integration problem. Each level represents progressively simpler variants of the original problem. The tree structure ensures each variant has exactly one parent, maintaining a clear progression of difficulty.
“think” step by step [9]. Similarly, DeepSeek’s R1 model leverages a reinforcement learning framework that minimizes human supervision by generating and self-evaluating its own training data [2].
Importantly, recent work has shown that RL approaches may generalize much better than Supervised Fine-Tuning (SFT), which appears to memorize instead [1, 13]. RL approaches have also shown to be highly effective in generalizing to out-of-distribution tasks, particularly in competitive mathematics [13]. These results strongly suggest that reinforcement learning offers a more promising path to self-improvement than supervised fine-tuning.
These innovations underscore a paradigm shift—from externally curated curricula and human-labeled data toward autonomous, feedback-driven self-improvement in language models.
3 Methodology
3.1 Algorithm Design (LADDER & TTRL)
3.1.1 LADDER
LADDER is a structured framework designed to enhance LLM problem-solving capabilities through recursive prob-lem decomposition and reinforcement learning. We demonstrate the effectiveness of LADDER in the domain of mathematical integration. LADDER consists of the following components:

Variant Generation: A structured method for generating trees of progressively simpler variants of complex problems, establishing a natural difficulty gradient.

Solution Verification: A numerical integration method to verify the solution of an integral.

Reinforcement Learning: The protocol used to train the base model on the variant trees.
LADDER is a two-step algorithm. First, the training set of integrals is collected and a tree of variants is generated for each integral as described in section 3.1.2. Second, we perform the reinforcement learning protocol described in section 3.1.4 on a base model using the set of variant trees as the training set. The resulting model should then have significantly improved and generalized mathematical integration capabilities, and can then be prompted to solve new integrals. See Algorithm 1 for LADDER pseudocode. VLADDER is the set of variants generated for all questions in the train set of integrals and ai is the answer to the ith test question.
The number of variants N generated per question is a hyperparameter, which we vary for different experiments. We experiment with LADDER in sections 3.2.1 and 3.2.2.
3.1.2 Variant Generation
The variant generation process required careful design to ensure sufficient diversity and appropriate difficulty scaling. We found that naive approaches to variant generation - simply asking the model to generate easier versions - led to repetitive patterns and limited diversity. Through experimentation, we developed a multi-stage process that dramatically improved the quality and variety of generated variants.
3
Algorithm 1 LADDER 1: Qtrain, Qtest ← train and test sets of integrals 2: N ← number of variants to generate 3: G(q, j) : generates the jth variant of integral q 4: VLADDER ← {vi,j ∈ G(Qtrain[i], j) | 1 ≤ i ≤ |Qtrain|, 1 ≤ j ≤ N} 5: πθLADDER ← GRPO(πθbase , VLADDER) 6: for i← 1, |Qtest| do 7: ai ∼ πθLADDER(· | Qtest[i]) 8: end for
Algorithm 2 TTRL 1: Qtest ← test set of integrals 2: N ← number of variants to generate 3: G(q, j) : generates the jth variant of integral q 4: for i← 1, |Qtest| do 5: VTTRL,i ← {vj ∈ G(Qtest[i], j) | 1 ≤ j ≤ N} 6: πθTTRL,i ← GRPO(πθbase , VTTRL,i) 7: ai ∼ πθTTRL,i(· | Qtest[i]) 8: end for
First, we used the base model to generate an extensive set of mathematical transformations that could be applied to integrals, categorized by their impact on problem difficulty. These included operations ranging from simple (e.g., reducing exponent values, simplifying denominators) to more complex (e.g., introducing nested functions, combining multiple function types). This transformation library served as a foundation for guiding variant generation.
Second, for each integral, we randomly sampled 3-5 transformations and provided them as explicit suggestions to the variant generation model. Critically, we found that generating variants in batches of 10 per prompt significantly improved diversity - smaller batch sizes led to more repetitive outputs, while larger batches reduced quality. To further enhance variation, we employed two key techniques:

Temperature cycling: We dynamically varied the sampling temperature between 0.8 and 1.4 across prompts. This helped balance between creativity and mathematical validity.

Persona-based prompting: We prompted the model to adopt different mathematical perspectives (e.g., "think like Euler focusing on series", "approach like Gauss looking for patterns").
The combination of batch generation, varied temperatures, and rotating personas proved crucial led to significantly more diverse variants. Without them the model would often converge to generating very similar and often repeating variants.
Third, to ensure sufficient coverage of the difficulty space, we applied this generation process recursively, generating a tree of variants, each a simpler integral than its parent. We found that this also helped improve variant diversity. This recursive approach helped build natural difficulty gradients - each problem could spawn multiple easier variants, which in turn could generate even simpler problems. We capped tree depth at three to maintain problem relevance. The following is an example of one root-to-leaf path in a variant tree:
Original problem: ∫
x2 + 1
x4 + 2x2 + 1 dx
Level 1 variant: ∫
x2
x4 + 1 dx
Level 2 variant: ∫
1
x2 + 1 dx
Level 3 variant: ∫
1
x2 dx
Quality control presented a significant challenge in our variant generation process. While we prompted the model to generate "easier" or "equivalent" variants, the actual difficulty of the resulting integrals often deviated substantially from the intended level. Small perturbations in coefficients or function composition could transform seemingly simple integrals into much harder ones - for instance, changing a coefficient from 1 to 2 in a rational function could introduce complex roots that make the integral significantly more challenging.
4
generation capacity. Future work could explore methods to better constrain variant generation to maintain intended difficulty levels while preserving mathematical diversity.
We apply the above three-step variant generation method to generate the sets of variant integrals in both LADDER and TTRL. VLADDER is the set of variants for all questions in the train set Qtrain and VTTRL,i is the set of variants for the ith question in the test set, Qtest[i]. See Algorithms 1 and 2.
3.1.3 Solution Verification
Integral variant generation occurs at the beginning of LADDER. Throughout the process of performing RL in LADDER we must also perform solution verification. In order to do so, we developed a robust numerical verification framework that balanced accuracy with computational efficiency. The key challenge was ensuring reliable verification across different types of integrals while handling edge cases and potential numerical instabilities.
For each candidate solution to an integral, we employed a multi-point numerical comparison approach. We randomly sampled five points from the domain [-10, 10] and evaluated both the candidate solution and the original integral over small intervals of length 0.1 centered at these points. This interval length was chosen empirically to minimize numerical integration errors while maintaining sensitivity to local solution behavior. The use of multiple small intervals, rather than a single large one, helped detect both local and global errors in the solutions.
Our verification protocol included several key components:

Singularity handling: When a sampled point was near a singularity (detected through rapid value changes or numerical overflow), we automatically resampled to a new point. This adaptive sampling ensured robust verification even for functions with challenging behavior.

Numerical precision: Solutions were deemed correct if their values exhibited a relative difference of 10−2 or less compared to numerical integration results across all test intervals. We found empirically that this tolerance level effectively balanced false positives and negatives.

Timeout management: To handle computationally intensive integrals, we implemented a 2-second timeout for each verification attempt. If timeout occurred, new evaluation points were sampled, with up to three retries before marking the solution as unverifiable.

Edge case detection: Early iterations revealed that models could exploit verification weaknesses by outputting trivial solutions (like the integration symbol itself) or degenerate forms. We added specific filters to detect and reject such cases, ensuring solutions demonstrated genuine understanding.
All numerical integrations were performed using adaptive quadrature methods, with automatic precision adjustment based on the integrand’s complexity. This approach provided reliable results even for oscillatory and highly nonlinear functions, while maintaining reasonable computational efficiency.
We note, however, that the numerical verifier may not be 100% accurate. We opted for a numerical approach rather than a symbolic one because many problems beyond integration can be numerically verified despite lacking a symbolic solver.
We apply the above solution verification in our RL Protocol in section 3.1.4 and experiments in sections 3.2.1, 3.2.2 and 3.2.3. In our MIT experiments, final benchmark results are verified directly against the official solutions.
3.1.4 Reinforcement Learning Protocol
We decided to employ Group Relative Policy Optimization (GRPO) in both LADDER and TTRL [11]. GRPO does not use a separate critic model and instead estimates the baseline from group scores, improving efficiency and reducing memory. For each question q, GRPO samples a group of outputs o1, o2, ..., oG from the old policy πθold and then optimizes the policy model πθ by maximizing the following objective:
JGRPO(θ) = E [ q ∼ P (Q), {oi}Gi=1 ∼ πθold(O | q)
] 1
G
G∑ i=1
( min
( πθ(oi | q) πθold(oi | q)
Ai, clip ( πθ(oi | q) πθold(oi | q)
, 1− ε, 1 + ε ) Ai
) − β DKL
( πθ ∥πref
)) (1)
DKL(πθ ∥πref) = πref(oi | q) πθ(oi | q)
− log (πref(oi | q)
πθ(oi | q)
) − 1 (2)
5
where ϵ and β are hyperparameters, and Ai is the advantage, computed using a group of rewards r1, r2, ..., rG corresponding to the outputs within each group:
Ai = ri −mean
( {r1, r2, . . . , rG}
) std
( {r1, r2, . . . , rG}
) (3)
We adopted a simple, rule-based reward model. The reward model is kept simple in order to be straightforward to apply to other verifiable domains in the future. The reward model consists of two rewards:

Accuracy reward: Using the solution verification method described in 3.1.3, we evaluate whether the response is correct or not. The model is required to provide the final answer in a specified format (i.e. in  tags), enabling reliable rule-based verification of correctness.

Format reward: In addition to the accuracy reward model, we employ a format reward that encourages the model to put its answer in  tags.
We perform the RL runs with a KL divergence coefficient of 0.001. Training batch size and number of epochs differ among our experiments.
3.1.5 Test-Time Reinforcement Learning
Test-Time Reinforcement Learning (TTRL) extends our LADDER framework to inference time, enabling dynamic adaptation to challenging problems directly during testing. Upon encountering a difficult integration problem, TTRL generates a focused set of related variants and conducts targeted reinforcement learning specifically for that problem. By recursively decomposing the challenging problem into simpler variants and learning from this focused curriculum, TTRL allows the model to rapidly develop problem-specific expertise without hand-crafting variants or architectural modifications. This provides a novel approach to scaling compute at test-time - rather than simply increasing output sampling or model size, TTRL leverages compute to dynamically improve the model’s problem-solving capabilities through focused practice on variants of the specific challenge at hand.
The same three components of LADDER are also used in Test-Time Reinforcement Learning (TTRL). For each question at test-time, there are two steps. First, we generate a tree of variants for the test question at hand. Second, we perform the reinforcement learning protocol described in section 3.1.4 on a base model using the variant tree as the training set. The resulting model should then have significantly improved mathematical integration capabilities tuned to the test question at hand. The test question is then answered using the tuned model, and finally the model is rolled back to its original parameters for the next test question. See Algorithm 2 for TTRL pseudocode, where VTTRL,i is the set of variants generated for the ith test question and ai is the answer to the ith test question.
As in LADDER, the number of variants generated per question is a hyperparameter, which we vary for different experiments. We experiment with TTRL in section 3.2.3.
3.2 Experiments
3.2.1 Llama 3B Experiments
We first experiment with LADDER using a Llama 3.2 3B parameter model as our base architecture to allow us to more quickly run ablation experiments. To establish our evaluation dataset, we developed a comprehensive collection of 110 indefinite integration problems, combining questions sourced from university-level mathematics curricula with synthetically generated problems using GPT-4o. To ensure appropriate difficulty calibration, we benchmarked each problem to verify it was solvable by GPT-4o but beyond the capabilities of the base Llama 3.2 3B model. This was done purposefully to benchmark performance on problems that can still be solved by an LLM but are outside the scope of Llama 3.2 3B.
We randomly split this collection into a training set of 10 problems and a test set of 100 problems. we generated approximately 500 variants for each of our 10 training problems. To validate the diversity of our variant set, we performed exact matching against our test set and found minimal overlap (only 5 matches among 5,000 variants). The small training set was deliberately chosen to demonstrate our method’s effectiveness in generating useful variants from limited examples. Approximately half of the problems were sourced from curriculum textbooks, with the remainder synthetically generated by GPT-4o. Notably, the synthetic problems were indistinguishable from curriculum-sourced ones.
6
0 100 200 300 0
20
40
60
80
100
Steps
Te st
Sc or
e (%
)
Figure 2: LADDER training progression.
0 3k 6k 9k 0
20
40
60
80
100
Number of Generated Variants
Te st
Sc or
e (%
)
Figure 3: Performance scaling w/ variant generation.
During training, models were prompted to express solutions in sympy algebraic notation without integration constants, ensuring consistent evaluation across different but mathematically equivalent expressions of the same solution. This standardization was crucial for reliable verification of solution correctness during the training process.
We performed two RL experiments with Llama 3.2 3B. The first experiment trained on only the 10 question training set (RL w/o variants). The second experiment trained on only variants generated from the 10 question training set (RL w/ variants, i.e. LADDER). Both runs used identical hyper parameters and were continued until performance plateaued.
3.2.2 MIT Integration Bee (LADDER)
Building off the findings from our Llama 3B experiemtns, we extended our methodology to the 2025 MIT Integration Bee qualifying examination, an annual competition that attracts both undergraduate and graduate students from MIT, with participants often having competitive mathematics backgrounds. The qualifying exam, which serves to select 16 finalists, contains 20 questions and has a typical qualifying threshold of 73%, though most participants score between 15-30%, with 50% to 73% out of 20 considered strong performance. Students are given 20 minutes to attempt the entire exam.
Using the DeepSeek-R1 distilled Qwen 2.5 7B model, we applied our variant generation approach to historical qualifying exams from 2010-2024. Our variant generation followed a two-level tree structure - first generating variants from each source problem, then generating additional variants from those first-level variants. We capped recursion at depth two, as preliminary experiments showed third-level variants became trivially simple and lost mathematical relevance to the original problems. With this approach we generated 9,000 variants.
Through experimentation with different difficulty distributions, we settled on prompting the model to generate 70% easier and 30% equivalent variants than their parent problems. While we initially attempted to include more challenging variants, we found this skew toward easier problems created more effective learning trajectories. Notably, many "equivalent" variants still introduced novel mathematical patterns while maintaining similar difficulty levels, contributing to the model’s generalization capabilities.
We verified that none of the 2025 exam questions appeared in our variant set, though we note this precaution was primarily for methodological rigor rather than necessity, as our model never accessed the test set or solutions during training. We apply the same hyperparameters as in the 3B experiments, except for modifying the batch size to 128.
3.2.3 MIT Integration Bee (LADDER + TTRL)
After applying LADDER, there remain certain questions which the tuned model continues to fail to answer. For each of these questions we further apply TTRL. For each unsolved problem, we generate a tree of variants following the same process illustrated in Figure 1, but limited to two levels of depth and approximately 800 total variants. Using these problem-specific variants, we conduct 100 steps of reinforcement learning with identical RL parameters as in the MIT
7
Integration Bee LADDER setup. The problem is considered "solved" if the model produces a correct solution at any point during this process, as verified by our numerical integration framework.
TTRL’s approach of on-the-fly data synthesis means it can handle novel integrals better by expanding its training set -focused on that problem - at test time. This is especially important for challenges such as the MIT Integration Bee, where many integrals are cleverly constructed and might be out-of-distribution relative to standard calculus problems. Further, TTRL provides a systematic approach to scaling performance through additional compute. Rather than simply increasing sampling or temperature parameters, TTRL enables active improvement of problem-solving capabilities through focused practice at test-time.
4 Results
Base M
od el
(pa ss@

Base M
od el
(pa ss@
10 )
RL w/o
va ria
nts
LADDER (R
L w/ v
ari an
ts) 0
20
40
60
80
100
1 2 3
82 Te
st Sc
or e
(% )
Figure 4: Comparison of LLM scores by training approach.
4.1 Llama 3B Experiments
Our experiments evaluated whether generating easier variants could enable effective reinforcement learning in mathe-matical integration tasks on Llama 3.2 3B. We tested four conditions: base model with pass@1 samping, base model with pass@10 sampling, RL without variants (only on the training set), and LADDER (RL with variants from the training set).

[... content truncated ...]

---

*Source: `LADDER SELF-IMPROVING LLMS THROUGH RECURSIVE.p_dup.md` | Ingested: 2026-05-12 | Ψ-tier: tuu*
