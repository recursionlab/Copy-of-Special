---
stub: true
title: "Prefix Optimi.Pdf"
created: 2026-05-12
updated: 2026-05-12
type: concept
tags: [unclassified, "ingested"]
sources: ["Prefix-Optimi.pdf.md"]
psi_tier: unclassified
---

# Prefix Optimi.Pdf

# Prefix-Optimi.pdf

4582
Prefix-Tuning: Optimizing Continuous Prompts for Generation
Xiang Lisa Li Stanford University

xlisali@stanford.edu

Percy Liang Stanford University

pliang@cs.stanford.edu

Abstract
Fine-tuning is the de facto way of leveraging large pretrained language models for down-stream tasks. However, fine-tuning modifies all the language model parameters and there-fore necessitates storing a full copy for each task. In this paper, we propose prefix-tuning, a lightweight alternative to fine-tuning for natu-ral language generation tasks, which keeps lan-guage model parameters frozen and instead op-timizes a sequence of continuous task-specific vectors, which we call the prefix. Prefix-tuning draws inspiration from prompting for language models, allowing subsequent tokens to attend to this prefix as if it were “virtual tokens”. We apply prefix-tuning to GPT-2 for table-to-text generation and to BART for summariza-tion. We show that by modifying only 0.1% of the parameters, prefix-tuning obtains compara-ble performance in the full data setting, outper-forms fine-tuning in low-data settings, and ex-trapolates better to examples with topics that are unseen during training.
1 Introduction
Fine-tuning is the prevalent paradigm for using large pretrained language models (LMs) (Radford et al., 2019; Devlin et al., 2019) to perform down-stream tasks (e.g., summarization), but it requires updating and storing all the parameters of the LM. Consequently, to build and deploy NLP systems that rely on large pretrained LMs, one currently needs to store a modified copy of all the LM pa-rameters for each task. This can be prohibitively expensive given the size of current LMs; for exam-ple, GPT-2 has 774M parameters (Radford et al., 2019) and GPT-3 has 175B parameters (Brown et al., 2020).
A natural approach to this problem is lightweight fine-tuning, which freezes most of the pretrained parameters and only tunes a smaller set of param-eters. For example, adapter-tuning (Rebuffi et al.,
Figure 1: Fine-tuning (top) updates all LM param-eters (the red Transformer box) and requires storing a full model copy for each task. We propose prefix-tuning (bottom), which freezes the LM parameters and only optimizes the prefix (the red prefix blocks). Con-sequently, we only need to store the prefix for each task, making prefix-tuning modular and space-efficient. Note that each vertical block denote transformer activa-tions at one time step.
2017; Houlsby et al., 2019) inserts additional task-specific layers between the layers of pretrained language models. Adapter-tuning has promising performance on natural language understanding and generation benchmarks, attaining comparable performance with fine-tuning while adding only around 2–4% task-specific parameters (Houlsby et al., 2019; Lin et al., 2020).
At the limit, GPT-3 (Brown et al., 2020) can be deployed using in-context learning, which is a form of prompting, without modifying any LM parameters. In in-context learning, Brown et al. (2020) prepend a natural language task instruction (e.g., TL;DR for summarization) and a few exam-ples to the task input, and then generate the task output from the LM. However, since Transformers can only condition on a bounded-length context (e.g., 2048 tokens for GPT-3), in-context learning is restricted to very small training sets.
4583
In this paper, we propose prefix-tuning, a lightweight alternative to fine-tuning for natural lan-guage generation (NLG) tasks, inspired by prompt-ing. Consider the task of generating a textual de-scription of a data table, as shown in Figure 1, where the task input is a linearized table (e.g., “name: Starbucks | type: coffee shop”) and the out-put is a textual description (e.g., “Starbucks serves coffee.”). Prefix-tuning prepends a sequence of continuous task-specific vectors to the input, which we call a prefix, depicted by red blocks in Figure 1 (bottom). To generate each token, the LM can at-tend to the prefix as if it were a sequence of “virtual tokens”, but unlike prompting, the prefix consists entirely of free parameters which do not correspond to real tokens. In contrast to fine-tuning in Figure 1 (top), which updates all LM parameters and thus requires storing a tuned copy of the model for each task, prefix-tuning only optimizes the prefix. Con-sequently, we only need to store one copy of the large LM and a learned task-specific prefix, yield-ing a very small overhead for each additional task (e.g., 250K parameters for table-to-text).
In contrast to full fine-tuning, prefix-tuning is also modular: we train an upstream prefix which steers an unmodified LM, and therefore, a single LM can support many tasks at once. In the con-text of personalization where the tasks correspond to users (Shokri and Shmatikov, 2015; McMahan et al., 2016), we would have a separate prefix for each user trained only on that user’s data, thereby avoiding data cross-contamination. Moreover, the prefix-based architecture enables us to even pro-cess examples from multiple users/tasks in a single batch, something that is not possible with other lightweight fine-tuning approaches like adapter-tuning.
We evaluate prefix-tuning on table-to-text gen-eration using GPT-2 and abstractive summariza-tion using BART. In terms of storage, prefix-tuning stores 1000x fewer parameters than full fine-tuning. In terms of performance when trained on full datasets, prefix-tuning and fine-tuning are compara-ble for table-to-text (§6.1), while prefix-tuning suf-fers a small degradation for summarization (§6.2). In low-data settings, prefix-tuning outperforms fine-tuning on both tasks (§6.3). Prefix-tuning also ex-trapolates better to tables (for table-to-text) and arti-cles (for summarization) with unseen topics (§6.4).
2 Related Work
Fine-tuning for natural language generation. Current state-of-the-art systems for natural lan-guage generation (NLG) are based on fine-tuning pretrained LMs. For table-to-text generation, Kale (2020) fine-tunes a sequence-to-sequence model (T5; Raffel et al., 2020). For extractive and abstrac-tive summarization, researchers fine-tune masked language models (e.g., BERT; Devlin et al., 2019) and encode-decoder models (e.g., BART; Lewis et al., 2020), respectively (Zhong et al., 2020; Liu and Lapata, 2019; Raffel et al., 2020). For other conditional NLG tasks such as machine transla-tion and dialogue generation, fine-tuning is also the prevalent paradigm (Zhang et al., 2020c; Stickland et al., 2020; Zhu et al., 2020; Liu et al., 2020). In this paper, we focus on table-to-text using GPT-2 and summarization using BART, but prefix-tuning in principle can be applied to other generation tasks and pretrained models, such as masked LMs.
Lightweight fine-tuning. Prefix-tuning falls under the broad class of lightweight fine-tuning methods, which freeze most of the pretrained parameters and only tune a smaller set of param-eters. The key question is how to augment the LM architecture and decide which subset of pretrained parameters to tune. One line of research learns a task-specific parameter mask (Zhao et al., 2020; Radiya-Dixit and Wang, 2020). Another line of research inserts new modules with trainable parameters. For example, Zhang et al. (2020a) trains a “side” network that is fused with the pretrained model via summation; adapter-tuning inserts task-specific layers (adapters) between each layer of the pretrained LM (Houlsby et al., 2019; Lin et al., 2020; Rebuffi et al., 2017; Pfeiffer et al., 2020). Compared to this line of work, which tunes around 3.6% of the LM parameters, our method obtains a further 30x reduction in task-specific parameters, tuning only 0.1% while maintaining comparable performance on table-to-text tasks.
Prompting. Prompting is a way of leveraging a pretrained LM by prepending instructions and a few examples to the task input and generating the task output from the LM. For autoregressive LMs, the most successful form of prompting is GPT-3’s in-context learning (Brown et al., 2020), which uses manually designed prompts to adapt its gen-eration for different tasks in few-shot settings. For masked LMs like BERT and RoBERTa (Liu et al.,
4584
2019), prompt engineering has been explored for natural language understanding tasks (Jiang et al., 2020; Schick and Schütze, 2020). For example, AutoPrompt (Shin et al., 2020) searches for a se-quence of discrete trigger words and concatenates it with each input to elicit sentiment or factual knowledge from BERT and RoBERTa. In contrast with AutoPrompt, our method optimizes contin-uous prefixes, which are more expressive (§7.2); moreover, we focus on language generation tasks.
Continuous vectors have been used to steer LMs; for example, Subramani et al. (2020) showed that a pretrained LSTM language model can reconstruct arbitrary sentences by optimizing a continuous vec-tor for each sentence, making the vector input-specific. In contrast, prefix-tuning optimizes a task-specific prefix that applies to all instances of that task. As a result, unlike the previous work whose application is limited to sentence reconstruction, prefix-tuning can be applied to NLG tasks.
Controllable generation. Controllable genera-tion aims to steer a pretrained language model to match a sentence-level attribute (e.g., positive sentiment or sports). Such control can happen at training time: Keskar et al. (2019) pretrains the language model (CTRL) to condition on metadata such as keywords or URLs. The control can also happen at decoding time, by weighted decoding (GeDi, Krause et al., 2020) or iteratively updat-ing the past activations (PPLM, Dathathri et al., 2020). However, there is no straightforward way to apply these controllable generation techniques to enforce fine-grained control over generated con-tents, as demanded by tasks like table-to-text and summarization.
P*-tuning. Prefix tuning is an instance of a new class of methods that has emerged, which we call p*-tuning (since the other prominent instances, p-tuning and prompt-tuning, also start with p), all based on the idea of optimizing a continuous prefix or prompt. Concurrent with our work, Qin and Eis-ner (2021) learn mixtures of soft fill-in-the-blank prompts to elicit knowledge from LMs such as BERT and BART. Hambardzumyan et al. (2021) learns task-specific embeddings that adapts BERT for sentiment classification. Both works show that tuning soft prompts outperforms previous work, which optimizes over discrete prompts. P-tuning (Liu et al., 2021) shows that jointly updating the prompt embeddings and LM parameters improves
GPT-2’s performance on natural language under-standing tasks, in both few-shot and full data set-tings. In a followup work, Prompt-tuning (Lester et al., 2021) simplifies our approach and applies it to T5 (Raffel et al., 2020), demonstrating that the performance gap between fine-tuning and p*-tuning vanishes as the model size grows.
3 Problem Statement
Consider a conditional generation task where the input x is a context and the output y is a sequence of tokens. We focus on two tasks, shown in Fig-ure 2 (right): In table-to-text, x corresponds to a lin-earized data table and y is a textual description; in summarization, x is an article and y is a summary.
3.1 Autoregressive LM
Assume we have an autoregressive neural language model pφ(y | x) parametrized by φ (e.g., GPT-2; Radford et al., 2019). As shown in Figure 2 (top), let z = [x; y] be the concatenation of x and y; let Xidx denote the sequence of indices that corre-sponds to x, and Yidx denote the same for y.
The activation vector at time step i is hi ∈ Rd, where hi = [h
(1) i ; · · · ;h(n)i ] is a concatenation of
all activation layers at this time step, and h(j)i is the activation vector of the j-th layer at time step i.1
An autoregressive neural LM computes hi as a function of zi and the past activations in its left context, as follows:
hi = LMφ(zi, h<i), (1)
where the last layer of hi is used to compute the distribution for the next token: pφ(zi+1 | h≤i) = softmax(Wφ h
(n) i ) and Wφ is a matrix that maps
h (n) i to logits over the vocabulary.
3.2 Encoder-Decoder Architecture
We can also use an encoder-decoder architecture (e.g., BART; Lewis et al., 2020) to model pφ(y | x), where x is encoded by the bidirectional encoder, and the decoder predicts y autoregressively (condi-tioned on the encoded x and its left context). We use the same indexing and activation notation, as shown in Figure 2 (bottom): each hi for i ∈ Xidx is computed by the a bidirectional encoder; each hi for i ∈ Yidx is computed by an autoregressive decoder using the same equation (1).
1In GPT-2, h(n) i consists of a key-value pair, and the di-
mension of each key and value is 1024.
4585
Figure 2: An annotated example of prefix-tuning using an autoregressive LM (top) and an encoder-decoder model (bottom). The prefix activations ∀i ∈ Pidx, hi are drawn from a trainable matrix Pθ. The remaining activations are computed by the Transformer.
3.3 Fine-tuning In the full fine-tuning framework, we initialize with the pretrained parameters φ. Here pφ is a train-able language model distribution and we perform gradient updates on the following log-likelihood objective:
max φ
log pφ(y | x) = max φ
∑ i∈Yidx
log pφ(zi | h<i).
(2)
4 Prefix-Tuning
We propose prefix-tuning as an alternative to full fine-tuning for conditional generation tasks. We first provide intuition in §4.1 before defining our method formally in §4.2.
4.1 Intuition Prompting has demonstrated that conditioning on a proper context can steer the LM without changing its parameters. For example, if we want the LM to generate a word (e.g., Obama), we can prepend its common collocations as context (e.g., Barack), and the LM will assign much higher probability to the desired word. Extending this intuition beyond generating a single word or sentence, we want to find a context that steers the LM to solve an NLG task. Intuitively, the context could influence the encoding of the task input x by guiding what to ex-tract from x, and it could influence the generation of the task output y by steering the next token distri-bution. However, it’s non-obvious whether such a context exists. Using natural language task instruc-tions (e.g., “summarize the following table in one sentence”) for the context might guide a human to
solve the task, but this fails for moderately-sized pretrained LMs.2 Optimizing over the discrete in-structions might help, but discrete optimization is computationally challenging.
Instead of optimizing over discrete tokens, we can optimize the instruction as continuous word em-beddings, whose effects will be propagated upward to all Transformer activation layers and rightward to subsequent tokens. This is strictly more expres-sive than a discrete prompt which is constrained to the embeddings of real words. Prefix-tuning goes one step further in increasing expressivity by op-timizing the activations of all the layers, not just the embedding layer. As another benefit, prefix-tuning can directly modify representations deeper in the network, therefore, avoiding long computa-tion paths across the depth of the network.
4.2 Method
Prefix-tuning prepends a prefix for an autoregres-sive LM to obtain z = [PREFIX;x; y], or prepends prefixes for both encoder and decoder to obtain z = [PREFIX;x; PREFIX′; y], as shown in Figure 2. Here, Pidx denotes the sequence of prefix indices, and we use |Pidx| to denote the length of the prefix.
We follow the recurrence relation in equa-tion (1), except that the activations of the prefix indices are free parameters, given by a matrix Pθ (parametrized by θ) of dimension |Pidx| × dim(hi).
hi =
{ Pθ[i, :], if i ∈ Pidx, LMφ(zi, h<i), otherwise.
(3)
2In our preliminary experiments, GPT-2 and BART fail in this setting; the only exception is GPT-3.
4586
The training objective is the same as equation (2), but the set of trainable parameters changes: the lan-guage model parameters φ are fixed and the prefix parameters θ are the only trainable parameters.
Here, each hi is a function of the trainable Pθ. When i ∈ Pidx, this is clear because hi copies directly from Pθ. When i 6∈ Pidx, hi still depends on Pθ, because the prefix activations are always in the left context and will therefore affect any activations to the right.
4.3 Parametrization of Pθ Empirically, directly updating the Pθ parameters leads to unstable optimization and a slight drop in performance.3 So we reparametrize the matrix Pθ[i, :] = MLPθ(P ′θ[i, :]) by a smaller matrix (P ′θ) composed with a large feedforward neural network (MLPθ). Now, the trainable parameters include P ′θ and the parameters of MLPθ. Note that Pθ and P ′θ has the same number of rows (i.e., the prefix length), but different number of columns.4
Once training is complete, these reparametriza-tion parameters can be dropped, and only the prefix (Pθ) needs to be saved.
5 Experimental Setup
5.1 Datasets and Metrics
We evaluate on three standard neural generation datasets for the table-to-text task: E2E (Novikova et al., 2017), WebNLG (Gardent et al., 2017), and DART (Radev et al., 2020), as shown in Table 1. The datasets are ordered by increasing complexity and size. E2E only has 1 domain (i.e. restaurant reviews); WebNLG has 14 domains, and DART is open-domain, using open-domain tables from Wikipedia. For evaluation, we report the metrics using the official evaluation scripts (see details in Appendix A.1).
For the summarization task, we use the XSUM (Narayan et al., 2018) dataset, which is an abstrac-tive summarization dataset on news articles. We report ROUGE-1, ROUGE-2 and ROUGE-L.
5.2 Methods
For table-to-text generation, we compare prefix-tuning with three other methods: full fine-tuning
3We find in preliminary experiments that directly optimiz-ing the prefix is very sensitive to initialization.
4Pθ has dimensions |Pidx| × dim(hi) while Pθ has dimensions |Pidx| × k. We choose k = 512 for table-to-text and 800 for summarization. MLPθ maps from k to dim(hi).
#examples input length output length
E2E 50K 28.5 27.8 WebNLG 22K 49.6 30.7
DART 82K 38.8 27.3
XSUM 225K 473.3 28.1
Table 1: Datasets statistics. The input and output length is the number of BPE tokens per example. For the three table-to-text datasets, the input length is the length of linearized tables (details in Appendix A.1).
(FT-FULL), fine-tuning only the top 2 layers (FT-TOP2), and adapter-tuning (ADAPTER).5 We also report the current state-of-the-art results on these datasets: On E2E, Shen et al. (2019) uses a prag-matically informed model without pretraining. On WebNLG, Kale (2020) fine-tunes T5-large. On DART, no official models trained on this dataset version are released.6 For summarization, we com-pare against fine-tuning BART (Lewis et al., 2020).
5.3 Architectures and Hyperparameters
For table-to-text, we use GPT-2MEDIUM and GPT-2LARGE. For summarization, we use BARTLARGE. Our implementation is based on the Hugging Face Transformers (Wolf et al., 2020).
At training time, we use the AdamW optimizer (Loshchilov and Hutter, 2019) and a linear learn-ing rate scheduler, as suggested by the Hugging Face default setup. The hyperparameters we tune include the number of epochs, batch size, learning rate, and prefix length. Hyperparameter details are in the appendix. The default setting is 10 epochs, batch size 5, learning rate 5 ·10−5 and prefix length 10. The table-to-text models are trained on TITAN Xp or GeForce GTX TITAN X machines. Prefix-tuning takes 0.2 hours per epoch to train on 22K examples, whereas fine-tuning takes around 0.3 hours per epoch. The summarization models are trained on Tesla V100 machines, taking 1.25 hours per epoch on the XSUM dataset. For time effi-ciency, prefix-tuning is around 30% faster than fine-tuning. For GPU memory efficiency, prefix-tuning with batchsize 1 takes 18% of the total GPU memory, whereas fine-tuning takes 50%.
At decoding time, for table-to-text, we use beam search with beam size 5. For summarization, we use beam size 6 and length normalization 0.8. De-coding takes 1.2 seconds per sentence (without
5Same implementation as Lin et al. (2020). 6The official benchmark model is trained on v.1.0.0 while
the release dataset is v1.1.1.
4587
batching) for table-to-text, and 2.6 seconds per batch (using a batch size of 10) for summarization.
6 Main Results 6.1 Table-to-text Generation
We find that by updating only 0.1% task-specific pa-rameters,7 prefix-tuning is effective in table-to-text generation, outperforming other lightweight base-lines (ADAPTER and FT-TOP2) even by updating 30x fewer parameters and achieving a comparable performance with (full) fine-tuning. This trend holds for all datasets: E2E, WebNLG,8 and DART.
If we match the number of parameters for prefix-tuning and adapter-tuning to be 0.1%, Table 2 shows that prefix-tuning is significantly better than ADAPTER (0.1%), attaining 4.1 BLEU improve-ment per dataset on average. Even when we com-pare with fine-tuning (100%) and adapter-tuning (3.0%), which update significantly more parame-ters than prefix-tuning, prefix-tuning still achieves results comparable or better than those two systems. This demonstrates that prefix-tuning is more Pareto efficient than adapter-tuning, significantly reducing parameters while improving generation quality.
Additionally, attaining good performance on DART suggests that prefix-tuning can generalize to tables with diverse domains and a large number of relations. We will delve deeper into extrapo-lation performance (i.e., generalization to unseen categories or topics) in §6.4.
In summary, prefix-tuning is an effective and space-efficient method to adapt GPT-2 to table-to-text generation. It also maintains the performance gains when scaling up to GPT-2LARGE, suggesting it has the potential to scale to even larger models with a similar architecture, like GPT-3.
6.2 Summarization
As shown in Table 3, with 2% parameters, prefix-tuning obtains slightly lower performance than fine-tuning (36.05 vs. 37.25 in ROUGE-L). With only 0.1% parameters, prefix-tuning underperforms full fine-tuning (35.05 vs. 37.25). There are several differences between XSUM and the three table-to-text datasets which could account for why prefix-tuning has comparative advantage in table-to-text:
7250K for E2E, 250K for WebNLG, and 500K for DART versus 345M GPT-2 parameters.
8The S,U,A columns in WebNLG represents SEEN, UN-SEEN, and ALL respectively; SEEN categories appear at training time; UNSEEN categories only appears at test time; and ALL is the combination of the two.
(1) XSUM contains 4x more examples than the three table-to-text datasets on average; (2) the input articles are 17x longer than the linearized table in-put of table-to-text datasets on average; (3) summa-rization is more complex than table-to-text because it requires selecting key contents from an article.
6.3 Low-data Setting
Based on the results from table-to-text (§6.1) and summarization (§6.2), we observe that prefix-tuning has a comparative advantage when the num-ber of training examples is smaller. To explore the low-data setting more systematically, we sub-sample the full dataset (E2E for table-to-text and XSUM for summarization) to obtain small datasets of size {50, 100, 200, 500}. For each size, we sam-ple 5 different datasets and average over 2 training random seeds. Thus, we average over 10 models for each low-data setting.9
Figure 3 (right) shows that prefix-tuning outper-forms fine-tuning in low-data regimes by 2.9 BLEU on average, in addition to requiring much fewer pa-rameters, but the gap narrows as the dataset size increases.
Qualitatively, Figure 3 (left) shows 8 examples generated by both prefix-tuning and fine-tuning models trained on different data levels. While both methods tend to undergenerate (missing table con-tents) in low data regimes, prefix-tuning tends to be more faithful than fine-tuning. For example, fine-tuning (100, 200)10 falsely claims a low customer rating while the true rating is average, whereas prefix-tuning (100, 200) generates a description that is faithful to the table.
6.4 Extrapolation
We now investigate extrapolation performance to unseen topics for both table-to-text and summariza-tion. In order to construct an extrapolation setting, we split the existing datasets so that training and test cover different topics. For table-to-text, the WebNLG dataset is labeled with table topics. There are 9 categories that appear in training and dev, de-noted as SEEN and 5 categories that only appear at test time, denoted as UNSEEN. So we evaluate ex-trapolation by training on the SEEN categories and testing on the UNSEEN categories. For summa-rization, we construct two extrapolation data splits:
9We also sample a dev split (with dev size = 30% × train-ing size) for each training set. We use the dev split to choose hyperparameters and perform early stopping.
10The number in the parenthesis refers to the training size.
4588
E2E WebNLG DART BLEU NIST MET R-L CIDEr BLEU MET TER ↓ BLEU MET TER ↓ Mover BERT BLEURT
S U A S U A S U A
GPT-2MEDIUM FT-FULL 68.8 8.71 46.1 71.1 2.43 64.7 26.7 45.7 0.46 0.30 0.38 0.33 0.78 0.54 46.2 0.39 0.46 0.50 0.94 0.39 FT-TOP2 68.1 8.59 46.0 70.8 2.41 53.6 18.9 36.0 0.38 0.23 0.31 0.49 0.99 0.72 41.0 0.34 0.56 0.43 0.93 0.21 ADAPTER(3%) 68.9 8.71 46.1 71.3 2.47 60.5 47.9 54.8 0.43 0.38 0.41 0.35 0.46 0.39 45.2 0.38 0.46 0.50 0.94 0.39 ADAPTER(0.1%) 66.3 8.41 45.0 69.8 2.40 54.5 45.1 50.2 0.39 0.36 0.38 0.40 0.46 0.43 42.4 0.36 0.48 0.47 0.94 0.33 PREFIX(0.1%) 70.3 8.82 46.3 72.1 2.46 62.9 45.3 55.0 0.44 0.37 0.41 0.35 0.51 0.42 46.4 0.38 0.46 0.50 0.94 0.39
GPT-2LARGE FT-FULL 68.5 8.78 46.0 69.9 2.45 65.3 43.1 55.5 0.46 0.38 0.42 0.33 0.53 0.42 47.0 0.39 0.46 0.51 0.94 0.40 Prefix 70.3 8.85 46.2 71.7 2.47 63.4 47.7 56.3 0.45 0.39 0.42 0.34 0.48 0.40 46.7 0.39 0.45 0.51 0.94 0.40
SOTA 68.6 8.70 45.3 70.8 2.37 63.9 52.8 57.1 0.46 0.41 0.44 - - - - - - - - -
Table 2: Metrics (higher is better, except for TER) for table-to-text generation on E2E (left), WebNLG (middle) and DART (right). With only 0.1% parameters, Prefix-tuning outperforms other lightweight baselines and achieves a comparable performance with fine-tuning. The best score is boldfaced for both GPT-2MEDIUM and GPT-2LARGE.
Source name : The Eagle | type : coffee shop | food : Chinese | price : cheap | customer rating : average | area : riverside | family friendly : no | near : Burger King
Prefix (50) The Eagle is a cheap Chinese coffee shop located near Burger King. Prefix (100) The Eagle is a cheap coffee shop located in the riverside near Burger King. It
has average customer ratings. Prefix (200) The Eagle is a cheap Chinese coffee shop located in the riverside area near
Burger King. It has average customer ratings. Prefix (500) The Eagle is a coffee shop that serves Chinese food. It is located in the riverside
area near Burger King. It has an average customer rating and is not family friendly.
FT (50) The Eagle coffee shop is located in the riverside area near Burger King. FT (100) The Eagle is a cheap coffee shop near Burger King in the riverside area. It has
a low customer rating and is not family friendly. FT (200) The Eagle is a cheap Chinese coffee shop with a low customer rating. It is
located near Burger King in the riverside area. FT (500) The Eagle is a cheap Chinese coffee shop with average customer ratings. It is
located in the riverside area near Burger King.

100 200 300 400 500 training data size

32

33

34

35

36

37

RO UG

E-1

FT-full Prefix

100 200 300 400 500 training data size

10

11

12

13

14

15

RO UG

E-2

FT-full Prefix

100 200 300 400 500 training data size

0.50

0.55

0.60

BL EU

FT-full Prefix

100 200 300 400 500 training data size

0.60

0.62

0.64

0.66

RO UG

E

FT-full Prefix


[... content truncated ...]

---

*Source: `Prefix-Optimi.pdf.md` | Ingested: 2026-05-12 | Ψ-tier: unclassified*
