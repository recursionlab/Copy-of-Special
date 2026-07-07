---
title: "Statistical classification"
source: "https://en.wikipedia.org/wiki/Statistical_classification"
author:
  - "[[Contributors to Wikimedia projects]]"
published: 2005-03-07
created: 2026-04-10
description:
tags:
  - "clippings"
---
When [classification](https://en.wikipedia.org/wiki/Classification "Classification") is performed by a computer, statistical methods are normally used to develop the algorithm.

Often, the individual observations are analyzed into a set of quantifiable properties, known variously as [explanatory variables](https://en.wikipedia.org/wiki/Explanatory_variables "Explanatory variables") or *features*. These properties may variously be [categorical](https://en.wikipedia.org/wiki/Categorical_data "Categorical data") (e.g. "A", "B", "AB" or "O", for [blood type](https://en.wikipedia.org/wiki/Blood_type "Blood type")), [ordinal](https://en.wikipedia.org/wiki/Ordinal_data "Ordinal data") (e.g. "large", "medium" or "small"), [integer-valued](https://en.wikipedia.org/wiki/Integer "Integer") (e.g. the number of occurrences of a particular word in an [email](https://en.wikipedia.org/wiki/Email "Email")) or [real-valued](https://en.wikipedia.org/wiki/Real_number "Real number") (e.g. a measurement of [blood pressure](https://en.wikipedia.org/wiki/Blood_pressure "Blood pressure")). Other classifiers work by comparing observations to previous observations by means of a [similarity](https://en.wikipedia.org/wiki/Similarity_function "Similarity function") or [distance](https://en.wikipedia.org/wiki/Metric_\(mathematics\) "Metric (mathematics)") function.

An [algorithm](https://en.wikipedia.org/wiki/Algorithm "Algorithm") that implements classification, especially in a concrete implementation, is known as a **classifier**. The term "classifier" sometimes also refers to the mathematical [function](https://en.wikipedia.org/wiki/Function_\(mathematics\) "Function (mathematics)"), implemented by a classification algorithm, that maps input data to a category.

Terminology across fields is quite varied. In [statistics](https://en.wikipedia.org/wiki/Statistics "Statistics"), where classification is often done with [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression "Logistic regression") or a similar procedure, the properties of observations are termed [explanatory variables](https://en.wikipedia.org/wiki/Explanatory_variable "Explanatory variable") (or [independent variables](https://en.wikipedia.org/wiki/Independent_variable "Independent variable"), regressors, etc.), and the categories to be predicted are known as outcomes, which are considered to be possible values of the [dependent variable](https://en.wikipedia.org/wiki/Dependent_variable "Dependent variable"). In [machine learning](https://en.wikipedia.org/wiki/Machine_learning "Machine learning"), the observations are often known as *instances*, the explanatory variables are termed *features* (grouped into a [feature vector](https://en.wikipedia.org/wiki/Feature_vector "Feature vector")), and the possible categories to be predicted are *classes*. Other fields may use different terminology: e.g. in [community ecology](https://en.wikipedia.org/wiki/Community_ecology "Community ecology"), the term "classification" normally refers to [cluster analysis](https://en.wikipedia.org/wiki/Cluster_analysis "Cluster analysis").

## Relation to other problems

[Classification](https://en.wikipedia.org/wiki/Classification "Classification") and clustering are examples of the more general problem of [pattern recognition](https://en.wikipedia.org/wiki/Pattern_recognition "Pattern recognition"), which is the assignment of some sort of output value to a given input value. Other examples are [regression](https://en.wikipedia.org/wiki/Regression_analysis "Regression analysis"), which assigns a real-valued output to each input; [sequence labeling](https://en.wikipedia.org/wiki/Sequence_labeling "Sequence labeling"), which assigns a class to each member of a sequence of values (for example, [part of speech tagging](https://en.wikipedia.org/wiki/Part_of_speech_tagging "Part of speech tagging"), which assigns a [part of speech](https://en.wikipedia.org/wiki/Part_of_speech "Part of speech") to each word in an input sentence); [parsing](https://en.wikipedia.org/wiki/Parsing "Parsing"), which assigns a [parse tree](https://en.wikipedia.org/wiki/Parse_tree "Parse tree") to an input sentence, describing the [syntactic structure](https://en.wikipedia.org/wiki/Syntactic_structure "Syntactic structure") of the sentence; etc.

A common subclass of classification is [probabilistic classification](https://en.wikipedia.org/wiki/Probabilistic_classification "Probabilistic classification"). Algorithms of this nature use [statistical inference](https://en.wikipedia.org/wiki/Statistical_inference "Statistical inference") to find the best class for a given instance. Unlike other algorithms, which simply output a "best" class, probabilistic algorithms output a [probability](https://en.wikipedia.org/wiki/Probability "Probability") of the instance being a member of each of the possible classes. The best class is normally then selected as the one with the highest probability. However, such an algorithm has numerous advantages over non-probabilistic classifiers:

- It can output a confidence value associated with its choice (in general, a classifier that can do this is known as a *confidence-weighted classifier*).
- Correspondingly, it can *abstain* when its confidence of choosing any particular output is too low.
- Because of the probabilities which are generated, probabilistic classifiers can be more effectively incorporated into larger machine-learning tasks, in a way that partially or completely avoids the problem of *error propagation*.

## Frequentist procedures

Early work on statistical classification was undertaken by [Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher "Ronald Fisher"),[^1] [^2] in the context of two-group problems, leading to [Fisher's linear discriminant](https://en.wikipedia.org/wiki/Fisher%27s_linear_discriminant "Fisher's linear discriminant") function as the rule for assigning a group to a new observation.[^3] This early work assumed that data-values within each of the two groups had a [multivariate normal distribution](https://en.wikipedia.org/wiki/Multivariate_normal_distribution "Multivariate normal distribution"). The extension of this same context to more than two groups has also been considered with a restriction imposed that the classification rule should be [linear](https://en.wikipedia.org/wiki/Linear "Linear").[^3] [^4] Later work for the multivariate normal distribution allowed the classifier to be [nonlinear](https://en.wikipedia.org/wiki/Nonlinear "Nonlinear"):[^5] several classification rules can be derived based on different adjustments of the [Mahalanobis distance](https://en.wikipedia.org/wiki/Mahalanobis_distance "Mahalanobis distance"), with a new observation being assigned to the group whose centre has the lowest adjusted distance from the observation.

## Bayesian procedures

Unlike frequentist procedures, Bayesian classification procedures provide a natural way of taking into account any available information about the relative sizes of the different groups within the overall population.[^6] Bayesian procedures tend to be computationally expensive and, in the days before [Markov chain Monte Carlo](https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo "Markov chain Monte Carlo") computations were developed, approximations for Bayesian clustering rules were devised.[^7]

Some Bayesian procedures involve the calculation of [group-membership probabilities](https://en.wikipedia.org/wiki/Group-membership_probabilities "Group-membership probabilities"): these provide a more informative outcome than a simple attribution of a single group-label to each new observation.

## Binary and multiclass classification

Classification can be thought of as two separate problems – [binary classification](https://en.wikipedia.org/wiki/Binary_classification "Binary classification") and [multiclass classification](https://en.wikipedia.org/wiki/Multiclass_classification "Multiclass classification"). In binary classification, a better understood task, only two classes are involved, whereas multiclass classification involves assigning an object to one of several classes.[^8] Since many classification methods have been developed specifically for binary classification, multiclass classification often requires the combined use of multiple binary classifiers.

## Feature vectors

Most algorithms describe an individual instance whose category is to be predicted using a [feature vector](https://en.wikipedia.org/wiki/Feature_vector "Feature vector") of individual, measurable properties of the instance. Each property is termed a [feature](https://en.wikipedia.org/wiki/Feature_\(pattern_recognition\) "Feature (pattern recognition)"), also known in statistics as an [explanatory variable](https://en.wikipedia.org/wiki/Explanatory_variable "Explanatory variable") (or [independent variable](https://en.wikipedia.org/wiki/Independent_variable "Independent variable"), although features may or may not be [statistically independent](https://en.wikipedia.org/wiki/Statistically_independent "Statistically independent")). Features may variously be [binary](https://en.wikipedia.org/wiki/Binary_data "Binary data") (e.g. "on" or "off"); [categorical](https://en.wikipedia.org/wiki/Categorical_data "Categorical data") (e.g. "A", "B", "AB" or "O", for [blood type](https://en.wikipedia.org/wiki/Blood_type "Blood type")); [ordinal](https://en.wikipedia.org/wiki/Ordinal_data "Ordinal data") (e.g. "large", "medium" or "small"); [integer-valued](https://en.wikipedia.org/wiki/Integer "Integer") (e.g. the number of occurrences of a particular word in an email); or [real-valued](https://en.wikipedia.org/wiki/Real_number "Real number") (e.g. a measurement of blood pressure). If the instance is an image, the feature values might correspond to the pixels of an image; if the instance is a piece of text, the feature values might be occurrence frequencies of different words. Some algorithms work only in terms of discrete data and require that real-valued or integer-valued data be *discretized* into groups (e.g. less than 5, between 5 and 10, or greater than 10).

## Linear classifiers

A large number of [algorithms](https://en.wikipedia.org/wiki/Algorithm "Algorithm") for classification can be phrased in terms of a [linear function](https://en.wikipedia.org/wiki/Linear_function "Linear function") that assigns a score to each possible category *k* by [combining](https://en.wikipedia.org/wiki/Linear_combination "Linear combination") the feature vector of an instance with a vector of weights, using a [dot product](https://en.wikipedia.org/wiki/Dot_product "Dot product"). The predicted category is the one with the highest score. This type of score function is known as a [linear predictor function](https://en.wikipedia.org/wiki/Linear_predictor_function "Linear predictor function") and has the following general form: 
$$
{\displaystyle \operatorname {score} (\mathbf {X} _{i},k)={\boldsymbol {\beta }}_{k}\cdot \mathbf {X} _{i},}
$$
 where **X** <sub><i>i</i></sub> is the feature vector for instance *i*, **β** <sub><i>k</i></sub> is the vector of weights corresponding to category *k*, and score(**X** <sub><i>i</i></sub>, *k*) is the score associated with assigning instance *i* to category *k*. In [discrete choice](https://en.wikipedia.org/wiki/Discrete_choice "Discrete choice") theory, where instances represent people and categories represent choices, the score is considered the [utility](https://en.wikipedia.org/wiki/Utility "Utility") associated with person *i* choosing category *k*.

Algorithms with this basic setup are known as [linear classifiers](https://en.wikipedia.org/wiki/Linear_classifier "Linear classifier"). What distinguishes them is the procedure for determining (training) the optimal weights/coefficients and the way that the score is interpreted.

Examples of such algorithms include

- [Logistic regression](https://en.wikipedia.org/wiki/Logistic_regression "Logistic regression") – Statistical model for a binary dependent variable
	- [Multinomial logistic regression](https://en.wikipedia.org/wiki/Multinomial_logistic_regression "Multinomial logistic regression") – Regression for more than two discrete outcomes
- [Probit regression](https://en.wikipedia.org/wiki/Probit_regression "Probit regression") – Statistical regression where the dependent variable can take only two values
- The [perceptron](https://en.wikipedia.org/wiki/Perceptron "Perceptron") algorithm
- [Support vector machine](https://en.wikipedia.org/wiki/Support_vector_machine "Support vector machine") – Set of methods for supervised statistical learning
- [Linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis "Linear discriminant analysis") – Method used in statistics, pattern recognition, and other fields

## Algorithms

Since no single form of classification is appropriate for all data sets, a large toolkit of classification algorithms has been developed. The most commonly used include:[^9]

- [Artificial neural networks](https://en.wikipedia.org/wiki/Artificial_neural_networks "Artificial neural networks") – Computational model used in machine learning, based on connected, hierarchical functions
- [Boosting (machine learning)](https://en.wikipedia.org/wiki/Boosting_\(machine_learning\) "Boosting (machine learning)") – Ensemble learning method
- [Random forest](https://en.wikipedia.org/wiki/Random_forest "Random forest") – Tree-based ensemble machine learning methods
- [Genetic programming](https://en.wikipedia.org/wiki/Genetic_programming "Genetic programming") – Evolving computer programs with techniques analogous to natural genetic processes
	- [Gene expression programming](https://en.wikipedia.org/wiki/Gene_expression_programming "Gene expression programming") – Evolutionary algorithm
		- [Multi expression programming](https://en.wikipedia.org/wiki/Multi_expression_programming "Multi expression programming")
		- [Linear genetic programming](https://en.wikipedia.org/wiki/Linear_genetic_programming "Linear genetic programming")
- [Kernel estimation](https://en.wikipedia.org/wiki/Kernel_estimation "Kernel estimation") – Window function
	- [k-nearest neighbor](https://en.wikipedia.org/wiki/K-nearest_neighbor_algorithm "K-nearest neighbor algorithm") – Non-parametric classification method
- [Learning vector quantization](https://en.wikipedia.org/wiki/Learning_vector_quantization "Learning vector quantization")
- [Linear classifier](https://en.wikipedia.org/wiki/Linear_classifier "Linear classifier") – Statistical classification in machine learning
	- [Fisher's linear discriminant](https://en.wikipedia.org/wiki/Fisher%27s_linear_discriminant "Fisher's linear discriminant") – Method used in statistics, pattern recognition, and other fields
		- [Logistic regression](https://en.wikipedia.org/wiki/Logistic_regression "Logistic regression") – Statistical model for a binary dependent variable
		- [Naive Bayes classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier "Naive Bayes classifier") – Probabilistic classification algorithm
		- [Perceptron](https://en.wikipedia.org/wiki/Perceptron "Perceptron") – Algorithm for supervised learning of binary classifiers
- [Quadratic classifier](https://en.wikipedia.org/wiki/Quadratic_classifier "Quadratic classifier") – Statistical classifier in machine learning
- [Support vector machine](https://en.wikipedia.org/wiki/Support_vector_machine "Support vector machine") – Set of methods for supervised statistical learning
	- [Least squares support vector machine](https://en.wikipedia.org/wiki/Least_squares_support_vector_machine "Least squares support vector machine")

Choices between different possible algorithms are frequently made on the basis of quantitative [evaluation of accuracy](https://en.wikipedia.org/wiki/Classification#Evaluation_of_accuracy "Classification").

## Application domains

Classification has many applications. In some of these, it is employed as a [data mining](https://en.wikipedia.org/wiki/Data_mining "Data mining") procedure, while in others more detailed statistical modeling is undertaken.

- [Biological classification](https://en.wikipedia.org/wiki/Biological_classification "Biological classification") – The science of identifying, describing, defining and naming groups of biological organisms
- [Biometric](https://en.wikipedia.org/wiki/Biometric "Biometric") – Metrics related to human characteristics identification
- [Computer vision](https://en.wikipedia.org/wiki/Computer_vision "Computer vision") – Computerized information extraction from images
	- Medical image analysis and [medical imaging](https://en.wikipedia.org/wiki/Medical_imaging "Medical imaging") – Technique and process of creating visual representations of the interior of a body
		- [Optical character recognition](https://en.wikipedia.org/wiki/Optical_character_recognition "Optical character recognition") – Computer recognition of visual text
		- [Video tracking](https://en.wikipedia.org/wiki/Video_tracking "Video tracking") – Locating a moving object by analyzing frames of a video
- [Credit scoring](https://en.wikipedia.org/wiki/Credit_scoring "Credit scoring") – Numerical expression representing a person's creditworthiness
- [Document classification](https://en.wikipedia.org/wiki/Document_classification "Document classification") – Process of categorizing documents
- [Drug discovery](https://en.wikipedia.org/wiki/Drug_discovery "Drug discovery") and [development](https://en.wikipedia.org/wiki/Drug_development "Drug development") – Process of bringing a new pharmaceutical drug to the market
	- [Toxicogenomics](https://en.wikipedia.org/wiki/Toxicogenomics "Toxicogenomics")
		- [Quantitative structure-activity relationship](https://en.wikipedia.org/wiki/Quantitative_structure-activity_relationship "Quantitative structure-activity relationship") – Predictive chemical model
- [Geostatistics](https://en.wikipedia.org/wiki/Geostatistics "Geostatistics") – Branch of statistics focusing on spatial data sets
- [Handwriting recognition](https://en.wikipedia.org/wiki/Handwriting_recognition "Handwriting recognition") – Ability of a computer to receive and interpret intelligible handwritten input
- Internet [search engines](https://en.wikipedia.org/wiki/Search_engines "Search engines")
- [Micro-array classification](https://en.wikipedia.org/w/index.php?title=Micro-array_classification&action=edit&redlink=1 "Micro-array classification (page does not exist)")
- [Pattern recognition](https://en.wikipedia.org/wiki/Pattern_recognition "Pattern recognition") – Automated recognition of patterns and regularities in data
- [Recommender system](https://en.wikipedia.org/wiki/Recommender_system "Recommender system") – System to predict users' preferences
- [Speech recognition](https://en.wikipedia.org/wiki/Speech_recognition "Speech recognition") – Automatic conversion of spoken language into text
- [Statistical natural language processing](https://en.wikipedia.org/wiki/Statistical_natural_language_processing "Statistical natural language processing") – Processing of natural language by a computer

[^1]: Fisher, R. A. (1936). "The Use of Multiple Measurements in Taxonomic Problems". *[Annals of Eugenics](https://en.wikipedia.org/wiki/Annals_of_Eugenics "Annals of Eugenics")*. **7** (2): 179–188. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1111/j.1469-1809.1936.tb02137.x](https://doi.org/10.1111%2Fj.1469-1809.1936.tb02137.x). [hdl](https://en.wikipedia.org/wiki/Hdl_\(identifier\) "Hdl (identifier)"):[2440/15227](https://hdl.handle.net/2440%2F15227).

[^2]: Fisher, R. A. (1938). "The Statistical Utilization of Multiple Measurements". *[Annals of Eugenics](https://en.wikipedia.org/wiki/Annals_of_Eugenics "Annals of Eugenics")*. **8** (4): 376–386. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1111/j.1469-1809.1938.tb02189.x](https://doi.org/10.1111%2Fj.1469-1809.1938.tb02189.x). [hdl](https://en.wikipedia.org/wiki/Hdl_\(identifier\) "Hdl (identifier)"):[2440/15232](https://hdl.handle.net/2440%2F15232).

[^3]: Gnanadesikan, R. (1977) *Methods for Statistical Data Analysis of Multivariate Observations*, Wiley. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-471-30845-5](https://en.wikipedia.org/wiki/Special:BookSources/0-471-30845-5 "Special:BookSources/0-471-30845-5") (p. 83–86)

[^4]: [Rao, C.R.](https://en.wikipedia.org/wiki/C._R._Rao "C. R. Rao") (1952) *Advanced Statistical Methods in Multivariate Analysis*, Wiley. (Section 9c)

[^5]: [Anderson, T.W.](https://en.wikipedia.org/wiki/T._W._Anderson "T. W. Anderson") (1958) *An Introduction to Multivariate Statistical Analysis*, Wiley.

[^6]: Binder, D. A. (1978). "Bayesian cluster analysis". *[Biometrika](https://en.wikipedia.org/wiki/Biometrika "Biometrika")*. **65**: 31–38. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1093/biomet/65.1.31](https://doi.org/10.1093%2Fbiomet%2F65.1.31).

[^7]: Binder, David A. (1981). "Approximations to Bayesian clustering rules". *[Biometrika](https://en.wikipedia.org/wiki/Biometrika "Biometrika")*. **68**: 275–285. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1093/biomet/68.1.275](https://doi.org/10.1093%2Fbiomet%2F68.1.275).

[^8]: [Har-Peled, S.](https://en.wikipedia.org/wiki/Sariel_Har-Peled "Sariel Har-Peled"), Roth, D., Zimak, D. (2003) "Constraint Classification for Multiclass Classification and Ranking." In: Becker, B., [Thrun, S.](https://en.wikipedia.org/wiki/Sebastian_Thrun "Sebastian Thrun"), Obermayer, K. (Eds) *Advances in Neural Information Processing Systems 15: Proceedings of the 2002 Conference*, MIT Press. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-262-02550-7](https://en.wikipedia.org/wiki/Special:BookSources/0-262-02550-7 "Special:BookSources/0-262-02550-7")

[^9]: ["A Tour of The Top 10 Algorithms for Machine Learning Newbies"](https://builtin.com/data-science/tour-top-10-algorithms-machine-learning-newbies). *Built In*. 2018-01-20. Retrieved 2019-06-10.