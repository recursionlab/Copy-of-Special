---
stub: true
title: "Mergent Abilities Of Large Language Models.Pdf"
created: 2026-05-11
updated: 2026-05-11
type: concept
tags: [obstruction_class, "ingested"]
sources: ["mergent Abilities of Large Language Models.pdf.md"]
psi_tier: obstruction_class
---

# Mergent Abilities Of Large Language Models.Pdf

# mergent Abilities of Large Language Models.pdf

Emergent Abilities of Large Language Models

Jason Wei 1
jasonwei@google.com
Yi Tay 1
yitay@google.com
Rishi Bommasani 2
nlprishi@stanford.edu
Colin Raffel 3
craffel@gmail.com
Barret Zoph 1
barretzoph@google.com
Sebastian Borgeaud 4
sborgeaud@deepmind.com
Dani Yogatama 4
dyogatama@deepmind.com
Maarten Bosma 1
bosma@google.com
Denny Zhou 1
dennyzhou@google.com
Donald Metzler 1
metzler@google.com
Ed H. Chi 1
edchi@google.com
Tatsunori Hashimoto 2
thashim@stanford.edu
Oriol Vinyals 4
vinyals@deepmind.com
Percy Liang 2
pliang@stanford.edu
Jeff Dean 1
jeff@google.com
William Fedus 1
liamfedus@google.com

1Google Research 2Stanford University 3UNC Chapel Hill 4DeepMind
Reviewed on OpenReview:
https://openreview.net/forum?id=yzkSU5zdwD

Abstract
Scaling up language models has been shown to predictably improve performance and sample efficiency on a wide range of downstream tasks. This paper instead discusses an unpredictable phenomenon that we refer to as emergent abilities of large language models. We consider an ability to be emergent if it is not present in smaller models but is present in larger models. Thus, emergent abilities cannot be predicted simply by extrapolating the performance of smaller models. The existence of such emergence raises the question of whether additional scaling could potentially further expand the range of capabilities of language models.
1 Introduction
Language models have revolutionized natural language processing (NLP) in recent years. It is now well-known that increasing the scale of language models (e.g., training compute, model parameters, etc.) can lead to better performance and sample efficiency on a range of downstream NLP tasks (Devlin et al., 2019; Brown et al., 2020, inter alia). In many cases, the effect of scale on performance can often be methodologically predicted via scaling laws—for example, scaling curves for cross-entropy loss have been shown to empirically span more than seven orders of magnitude (Kaplan et al., 2020; Hoffmann et al., 2022). On the other hand, performance for certain downstream tasks counterintuitively does not appear to continuously improve as a function of scale, and such tasks cannot be predicted ahead of time (Ganguli et al., 2022).
In this paper, we will discuss the unpredictable phenomena of emergent abilities of large language models. Emergence as an idea has been long discussed in domains such as physics, biology, and computer science (Anderson, 1972; Hwang et al., 2012; Forrest, 1990; Corradini & O’Connor, 2010; Harper & Lewis, 2012, inter
alia). We will consider the following general definition of emergence, adapted from Steinhardt (2022) and rooted in a 1972 essay called “More Is Different” by Nobel prize-winning physicist Philip Anderson (Anderson, 1972):
Emergence is when quantitative changes in a system result in qualitative changes in behavior.
Here we will explore emergence with respect to model scale, as measured by training compute and number of model parameters. Specifically, we define emergent abilities of large language models as abilities that are not present in smaller-scale models but are present in large-scale models; thus they cannot be predicted by simply extrapolating the performance improvements on smaller-scale models (§2).1 We survey emergent abilities as observed in a range of prior work, categorizing them in settings such as few-shot prompting (§3) and augmented prompting strategies (§4). Emergence motivates future research on why such abilities are acquired and whether more scaling will lead to further emergent abilities, which we highlight as important questions for the field (§5).
2 Emergent Abilities Definition
As a broad concept, emergence is often used informally and can be reasonably interpreted in many different ways. In this paper, we will consider a focused definition of emergent abilities of large language models:
An ability is emergent if it is not present in smaller models but is present in larger models.
Emergent abilities would not have been directly predicted by extrapolating a scaling law (i.e. consistent performance improvements) from small-scale models. When visualized via a scaling curve (x-axis: model scale, y-axis: performance), emergent abilities show a clear pattern—performance is near-random until a certain critical threshold of scale is reached, after which performance increases to substantially above random. This qualitative change is also known as a phase transition—a dramatic change in overall behavior that would not have been foreseen by examining smaller-scale systems (Huberman & Hogg, 1987).
Today’s language models have been scaled primarily along three factors: amount of computation, number of model parameters, and training dataset size (Kaplan et al., 2020; Hoffmann et al., 2022). In this paper, we will analyze scaling curves by plotting the performance of different models where training compute for each model is measured in FLOPs on the x-axis (Hoffmann et al., 2022). Because language models trained with more compute tend to also have more parameters, we additionally show plots with number of model parameters as the x-axis in Appendix D (see Figure 11 and Figure 12, as well as Figure 4 and Figure 10). Using training FLOPs or model parameters as the x-axis produces curves with similar shapes due to the fact that most dense Transformer language model families have scaled training compute roughly proportionally with model parameters (Kaplan et al., 2020).
Training dataset size is also an important factor, but we do not plot capabilities against it because many language model families use a fixed number of training examples for all model sizes (Brown et al., 2020; Rae et al., 2021; Chowdhery et al., 2022). Although we focus on training computation and model size here, there is not a single proxy that adequately captures all aspects of scale. For example, Chinchilla (Hoffmann et al., 2022) has one-fourth as many parameters as Gopher (Rae et al., 2021) but uses similar training compute; and sparse mixture-of-expert models have more parameters per training/inference compute than dense models (Fedus et al., 2021; Du et al., 2021). Overall, it may be wise to view emergence as a function of many correlated variables. For example, later in Figure 4 we will also plot emergence as a function of WikiText103 perplexity (Merity et al., 2016), which happens to closely correlate with training computation for Gopher/ Chinchilla (though this correlation may not hold in the long-run).
Note that the scale at which an ability is first observed to emerge depends on a number of factors and is not an immutable property of the ability. For instance, emergence may occur with less training compute
1This survey focuses on pre-trained Transformer language models. Emergent abilities in NLP more broadly, however, could go back to Miller et al. (2004), Liang (2005), or earlier.
or fewer model parameters for models trained on higher-quality data. Conversely, emergent abilities also crucially depend on other factors such as not being limited by the amount of data, its quality, or the number of parameters in the model. Today’s language models are likely not trained optimally (Hoffmann et al., 2022), and our understanding of how to best train models will evolve over time. Our goal in this paper is not to characterize or claim that a specific scale is required to observe emergent abilities, but rather, we aim to discuss examples of emergent behavior in prior work.
3 Few-Shot Prompted Tasks

Language model

Input
OutputReview: This movie sucks. Sentiment: negative.
Review: I love this movie. Sentiment:
positive.
Figure 1: Example of an input and output for few-shot prompting.
We first discuss emergent abilities in the prompting paradigm, as pop-ularized by GPT-3 (Brown et al., 2020).2 In prompting, a pre-trained language model is given a prompt (e.g. a natural language instruction) of a task and completes the response without any further training or gradient updates to its parameters. Brown et al. (2020) proposed few-shot prompting, which includes a few input-output examples in the model’s context (input) as a preamble before asking the model to perform the task for an unseen inference-time example. An example prompt is shown in Figure 1.
The ability to perform a task via few-shot prompting is emergent when a model has random performance until a certain scale, after which performance increases to well-above random. Figure 2 shows eight such emergent abilities spanning five language model families from various work.
BIG-Bench. Figure 2A–D depicts four emergent few-shot prompted tasks from BIG-Bench, a crowd-sourced suite of over 200 benchmarks for language model evaluation (BIG-Bench, 2022). Figure 2A shows an arithmetic benchmark that tests 3-digit addition and subtraction, as well as 2-digit multiplication. GPT-3 and LaMDA (Thoppilan et al., 2022) have close-to-zero performance for several orders of magnitude of training compute, before performance jumps to sharply above random at 2 · 1022 training FLOPs (13B parameters) for GPT-3, and 1023 training FLOPs (68B parameters) for LaMDA. Similar emergent behavior also occurs at around the same model scale for other tasks, such as transliterating from the International Phonetic Alphabet (Figure 2B), recovering a word from its scrambled letters (Figure 2C), and Persian question-answering (Figure 2D). Even more emergent abilities from BIG-Bench are given in Appendix E.
TruthfulQA. Figure 2E shows few-shot prompted performance on the TruthfulQA benchmark, which measures the ability to answer questions truthfully (Lin et al., 2021). This benchmark is adversarially curated against GPT-3 models, which do not perform above random, even when scaled to the largest model size. Small Gopher models also do not perform above random until scaled up to the largest model of 5 · 1023
training FLOPs (280B parameters), for which performance jumps to more than 20% above random (Rae et al., 2021).
Grounded conceptual mappings. Figure 2F shows the task of grounded conceptual mappings, where language models must learn to map a conceptual domain, such as a cardinal direction, represented in a textual grid world (Patel & Pavlick, 2022). Again, performance only jumps to above random using the largest GPT-3 model.
Multi-task language understanding. Figure 2G shows the Massive Multi-task Language Understanding (MMLU) benchmark, which aggregates 57 tests covering a range of topics including math, history, law, and more (Hendrycks et al., 2021a). For GPT-3, Gopher, and Chinchilla, models of ∼1022 training FLOPs (∼10B parameters) or smaller do not perform better than guessing on average over all the topics, scaling up to 3–5 ·1023 training FLOPs (70B–280B parameters) enables performance to substantially surpass random. This result is striking because it could imply that the ability to solve knowledge-based questions spanning a large collection of topics might require scaling up past this threshold (for dense language models without retrieval or access to external memory).
2Though GPT-3 popularized prompting, the task setup has existed since before GPT-3 (Trinh & Le, 2018; McCann et al., 2018; Radford et al., 2019; Raffel et al., 2020).
1018 1020 1022 1024
0
10
20
30
40
50
A cc ur ac y (%
)
(A) Mod. arithmetic
1018 1020 1022 1024
0
10
20
30
40
50
B LE
U (%
)
(B) IPA transliterate
1018 1020 1022 1024
0
10
20
30
40
50
E xa
ct m at ch
(% )
(C) Word unscramble
LaMDA GPT-3 Gopher Chinchilla PaLM Random
1018 1020 1022 1024
0
10
20
30
40
50
E xa
ct m at ch
(% )
(D) Persian QA
1020 1022 1024 0
10 20 30 40 50 60 70
A cc ur ac y (%
)
(E) TruthfulQA
1020 1022 1024 0
10 20 30 40 50 60 70
Model scale (training FLOPs)
A cc ur ac y (%
)
(F) Grounded mappings
1020 1022 1024 0
10 20 30 40 50 60 70
A cc ur ac y (%
)
(G) Multi-task NLU
1020 1022 1024 0
10 20 30 40 50 60 70
A cc ur ac y (%
)
(H) Word in context
Figure 2: Eight examples of emergence in the few-shot prompting setting. Each point is a separate model. The ability to perform a task via few-shot prompting is emergent when a language model achieves random performance until a certain scale, after which performance significantly increases to well-above random. Note that models that used more training compute also typically have more parameters—hence, we show an analogous figure with number of model parameters instead of training FLOPs as the x-axis in Figure 11. A–D: BIG-Bench (2022), 2-shot. E: Lin et al. (2021) and Rae et al. (2021). F: Patel & Pavlick (2022). G: Hendrycks et al. (2021a), Rae et al. (2021), and Hoffmann et al. (2022). H: Brown et al. (2020), Hoffmann et al. (2022), and Chowdhery et al. (2022) on the WiC benchmark (Pilehvar & Camacho-Collados, 2019).
Word in Context. Finally, Figure 2H shows the Word in Context (WiC) benchmark (Pilehvar & Camacho-Collados, 2019), which is a semantic understanding benchmark. Notably, GPT-3 and Chinchilla fail to achieve one-shot performance of better than random, even when scaled to their largest model size of ∼5 · 1023
FLOPs. Although these results so far may suggest that scaling alone may not enable models to solve WiC, above-random performance eventually emerged when PaLM was scaled to 2.5 ·1024 FLOPs (540B parameters), which was much larger than GPT-3 and Chinchilla.
4 Augmented Prompting Strategies
Although few-shot prompting is perhaps currently the most common way of interacting with large language models, recent work has proposed several other prompting and finetuning strategies to further augment the abilities of language models. If a technique shows no improvement or is harmful when compared to the baseline of not using the technique until applied to a model of a large-enough scale, we also consider the technique an emergent ability.
1021 1022 1023 1024 0
5
10
15
20
25
No chain of thought
Chain of thought
G SM
8K A cc ur ac y (%
) (A) Math word
problems
1021 1022 1023 1024 30
40
50
60
70
No instruction
tuning
Instruction tuning
10 N LU
ta sk
av er ag e
(B) Instruction following
1019 1020 1021 0
20
40
60
80
100
No scratchpad
Scratchpad
Model scale (training FLOPs)
A cc ur ac y (%
)
(C) 8-digit addition
1022 1023 1024
100
101
Letter choices
T/F
% E C E
(lo g-sc al e,
de cr ea si ng
) (D) Calibration
Figure 3: Specialized prompting or finetuning methods can be emergent in that they do not have a positive effect until a certain model scale. A: Wei et al. (2022b). B: Wei et al. (2022a). C: Nye et al. (2021). D: Kadavath et al. (2022). An analogous figure with number of parameters on the x-axis instead of training FLOPs is given in Figure 12. The model shown in A-C is LaMDA (Thoppilan et al., 2022), and the model shown in D is from Anthropic.
Multi-step reasoning. Reasoning tasks, especially those involving multiple steps, have been challenging for language models and NLP models more broadly (Rae et al., 2021; Bommasani et al., 2021; Nye et al., 2021). A recent prompting strategy called chain-of-thought prompting enables language models to solve such problems by guiding them to produce a sequence of intermediate steps before giving the final answer (Cobbe et al., 2021; Wei et al., 2022b; Suzgun et al., 2022). As shown in Figure 3A, chain of thought prompting only surpasses standard prompting without intermediate steps when scaled to 1023 training FLOPs (∼100B parameters). A similar emergence in performance gain was also observed when augmenting few-shot prompting with explanations that came after the final answer (Lampinen et al., 2022).
Instruction following. Another growing line of work aims to better enable language models to perform new tasks simply by reading instructions describing the task (without few-shot exemplars). By finetuning on a mixture of tasks phrased as instructions, language models have been shown to respond appropriately to instructions describing an unseen task (Ouyang et al., 2022; Wei et al., 2022a; Sanh et al., 2022; Chung et al., 2022). As shown in Figure 3B, Wei et al. (2022a) found that this instruction-finetuning technique hurts performance for models of 7 ·1021 training FLOPs (8B parameters) or smaller, and only improves performance when scaled to 1023 training FLOPs (∼100B parameters) (though Sanh et al. (2022) found shortly after that this instruction-following behavior could be also induced by finetuning smaller encoder-decoder T5 models).
Program execution. Consider computational tasks involving multiple steps, such as adding large numbers or executing computer programs. Nye et al. (2021) show that finetuning language models to predict intermediate outputs (“scratchpad”) enables them to successfully execute such multi-step computations. As shown in Figure 3C, on 8-digit addition, using a scratchpad only helps for models of ∼9 · 1019 training FLOPs (40M parameters) or larger.
Model calibration. Finally, an important direction for deployment of language models studies is calibration, which measures whether models can predict which questions they will be able to answer correctly. Kadavath et al. (2022) compared two ways of measuring calibration: a True/False technique, where models first propose answers and then evaluate the probability “P(True)” that their answers are correct, and more-standard methods of calibration, which use the probability of the correct answer compared with other answer options. As shown in Figure 3D, the superiority of the True/False technique only emerges when scaled to the largest model scale of ∼3 · 1023 training FLOPs (52B parameters).
Table 1: List of emergent abilities of large language models and the scale (both training FLOPs and number of model parameters) at which the abilities emerge.
Emergent scale
Train. FLOPs Params. Model Reference
Few-shot prompting abilitiesr Addition/subtraction (3 digit) 2.3E+22 13B GPT-3 Brown et al. (2020)r Addition/subtraction (4-5 digit) 3.1E+23 175Br MMLU Benchmark (57 topic avg.) 3.1E+23 175B GPT-3 Hendrycks et al. (2021a)r Toxicity classification (CivilComments) 1.3E+22 7.1B Gopher Rae et al. (2021)r Truthfulness (Truthful QA) 5.0E+23 280Br MMLU Benchmark (26 topics) 5.0E+23 280Br Grounded conceptual mappings 3.1E+23 175B GPT-3 Patel & Pavlick (2022)r MMLU Benchmark (30 topics) 5.0E+23 70B Chinchilla Hoffmann et al. (2022)r Word in Context (WiC) benchmark 2.5E+24 540B PaLM Chowdhery et al. (2022)r Many BIG-Bench tasks (see Appendix E) Many Many Many BIG-Bench (2022)
Augmented prompting abilitiesr Instruction following (finetuning) 1.3E+23 68B FLAN Wei et al. (2022a)r Scratchpad: 8-digit addition (finetuning) 8.9E+19 40M LaMDA Nye et al. (2021)r Using open-book knowledge for fact checking 1.3E+22 7.1B Gopher Rae et al. (2021)r Chain-of-thought: Math word problems 1.3E+23 68B LaMDA Wei et al. (2022b)r Chain-of-thought: StrategyQA 2.9E+23 62B PaLM Chowdhery et al. (2022)r Differentiable search index 3.3E+22 11B T5 Tay et al. (2022b)r Self-consistency decoding 1.3E+23 68B LaMDA Wang et al. (2022b)r Leveraging explanations in prompting 5.0E+23 280B Gopher Lampinen et al. (2022)r Least-to-most prompting 3.1E+23 175B GPT-3 Zhou et al. (2022)r Zero-shot chain-of-thought reasoning 3.1E+23 175B GPT-3 Kojima et al. (2022)r Calibration via P(True) 2.6E+23 52B Anthropic Kadavath et al. (2022)r Multilingual chain-of-thought reasoning 2.9E+23 62B PaLM Shi et al. (2022)r Ask me anything prompting 1.4E+22 6B EleutherAI Arora et al. (2022)

[... content truncated ...]

---

*Source: `mergent Abilities of Large Language Models.pdf.md` | Ingested: 2026-05-11 | Ψ-tier: obstruction_class*
