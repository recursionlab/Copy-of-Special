---
title: "Semantic spectrum"
source: "https://en.wikipedia.org/wiki/Semantic_spectrum"
author:
  - "[[Wikipedia]]"
published: 2005-08-03
created: 2026-05-19
description:
tags:
  - "clippings"
---
The **[semantic](https://en.wikipedia.org/wiki/Semantics "Semantics") [spectrum](https://en.wikipedia.org/wiki/Spectrum "Spectrum")**, sometimes referred to as the **ontology spectrum**, the **smart data continuum**, or **semantic precision**, is in [linguistics](https://en.wikipedia.org/wiki/Linguistics "Linguistics"), a series of increasingly precise or rather [semantically](https://en.wikipedia.org/wiki/Semantics "Semantics") expressive definitions for [data elements](https://en.wikipedia.org/wiki/Data_element "Data element") in [knowledge representations](https://en.wikipedia.org/wiki/Knowledge_representation "Knowledge representation"), especially for machine use.

At the low end of the spectrum is a simple binding of a single word or phrase and its definition. At the high end is a full [ontology](https://en.wikipedia.org/wiki/Ontology_\(computer_science\) "Ontology (computer science)") that specifies relationships between data elements using precise [URIs](https://en.wikipedia.org/wiki/URI "URI") for relationships and properties.

With increased [specificity](https://en.wikipedia.org/wiki/Specificity_\(tests\) "Specificity (tests)") comes increased precision and the ability to use tools to automatically [integrate](https://en.wikipedia.org/wiki/System_integration "System integration") systems, but also increased cost to build and maintain a [metadata registry](https://en.wikipedia.org/wiki/Metadata_registry "Metadata registry").

Some steps in the semantic spectrum include the following:

1. [Glossary](https://en.wikipedia.org/wiki/Glossary "Glossary"): A simple list of terms and their definitions. A glossary focuses on creating a complete list of the terminology of domain-specific terms and [acronyms](https://en.wikipedia.org/wiki/Acronym "Acronym"). It is useful for creating clear and unambiguous definitions for terms, and because it can be created with simple word processing tools, few technical tools are necessary.
2. [Controlled vocabulary](https://en.wikipedia.org/wiki/Controlled_vocabulary "Controlled vocabulary"): A simple list of terms, definitions and naming conventions. A controlled vocabulary frequently has some type of oversight process associated with adding or removing data element definitions to ensure consistency. Terms are often defined in relationship to each other.
3. [Data dictionary](https://en.wikipedia.org/wiki/Data_dictionary "Data dictionary"): Terms, definitions, naming conventions and one or more representations of the data elements in a computer system. Data dictionaries often define data types, validation checks such as enumerated values and the formal definitions of each of the enumerated values.
4. [Data model](https://en.wikipedia.org/wiki/Data_model "Data model"): Terms, definitions, naming conventions, representations and one or more representations of the data elements as well as the beginning of specification of the relationships between data elements including abstractions and containers.
5. [Taxonomy](https://en.wikipedia.org/wiki/Taxonomy_\(general\) "Taxonomy (general)"): A complete data model in an inheritance hierarchy where all data elements inherit their behaviors from a single "super data element". The difference between a data model and a formal taxonomy is the arrangement of data elements into a formal tree structure where each element in the tree is a formally defined concept with associated properties.
6. [Ontology](https://en.wikipedia.org/wiki/Ontology_\(computer_science\) "Ontology (computer science)"): A complete, machine-readable specification of a conceptualization using [URIs](https://en.wikipedia.org/wiki/URI "URI") (and then [IRIs](https://en.wikipedia.org/wiki/Internationalized_Resource_Identifier "Internationalized Resource Identifier")) for all data elements, properties and relationship types. The [W3C](https://en.wikipedia.org/wiki/W3C "W3C") standard language for representing ontologies is the [Web Ontology Language](https://en.wikipedia.org/wiki/Web_Ontology_Language "Web Ontology Language") (OWL). Ontologies frequently contain formal business rules formed in discrete logic statements that relate data elements to each another.

## Typical questions for determining semantic precision

The following is a list of questions that may arise in determining semantic precision.

Correctness:

How can correct syntax and semantics be enforced? Are tools (such as [XML Schema](https://en.wikipedia.org/wiki/XML_Schema_\(W3C\) "XML Schema (W3C)")) readily available to validate syntax of data exchanges?

Adequacy/Expressiveness/Scope:

Does the system represent everything that is of practical use for the purpose? Is an emphasis being placed on data that is externalized (exposed or transferred between systems)?

Efficiency:

How efficiently can the representation be searched/queried and possibly [reasoned](https://en.wikipedia.org/wiki/Automatic_reasoning "Automatic reasoning") on?

Complexity:

How steep is the [learning curve](https://en.wikipedia.org/wiki/Learning_curve "Learning curve") for defining new concepts, querying for them or constraining them? Are there appropriate tools for simplifying typical workflows? (See also: [ontology editor](https://en.wikipedia.org/wiki/Ontology_editor "Ontology editor"))

Translatability:

Can the representation easily be transformed (e.g. by [Vocabulary-based transformation](https://en.wikipedia.org/wiki/Vocabulary-based_transformation "Vocabulary-based transformation")) into an equivalent representation so that [semantic equivalence](https://en.wikipedia.org/wiki/Semantic_equivalence "Semantic equivalence") is ensured?

### Determining location on the semantic spectrum

Many organizations today are building a [metadata registry](https://en.wikipedia.org/wiki/Metadata_registry "Metadata registry") to store their data definitions and to perform [metadata publishing](https://en.wikipedia.org/wiki/Metadata_publishing "Metadata publishing"). The question of where they are on the semantic spectrum frequently arises. To determine where your systems are, some of the following questions are frequently useful.

1. Is there a centralized glossary of terms for the subject matter?
2. Does the glossary of terms include precise definitions for each terms?
3. Is there a central repository to store [data elements](https://en.wikipedia.org/wiki/Data_element "Data element") that includes data types information?
4. Is there an approval process associated with the creation and changes to data elements?
5. Are coded data elements fully enumerated? Does each enumeration have a full definition?
6. Is there a process in place to remove duplicate or redundant data elements from the metadata registry?
7. Is there one or more classification schemes used to classify data elements?
8. Are document exchanges and [web services](https://en.wikipedia.org/wiki/Web_services "Web services") created using the data elements?
9. Can the central metadata registry be used as part of a [Model-driven architecture](https://en.wikipedia.org/wiki/Model-driven_architecture "Model-driven architecture")?
10. Are there staff members trained to extract data elements that can be reused in metadata structures?

## Strategic nature of semantics

Today, much of the World Wide Web is stored as [Hypertext Markup Language](https://en.wikipedia.org/wiki/Hypertext_Markup_Language "Hypertext Markup Language"). Search engines are severely hampered by their inability to understand the meaning of published web pages. These limitations have led to the advent of the [Semantic web](https://en.wikipedia.org/wiki/Semantic_web "Semantic web") movement. [^1]

In the past, many organizations that created custom database application used isolated teams of developers that did not formally publish their data definitions. These teams frequently used internal data definitions that were incompatible with other computer systems. This made [Enterprise Application Integration](https://en.wikipedia.org/wiki/Enterprise_Application_Integration "Enterprise Application Integration") and [Data warehousing](https://en.wikipedia.org/wiki/Data_warehousing "Data warehousing") extremely difficult and costly. Many organizations today require that teams consult a centralized data registry before new applications are created.

The job title of an individual that is responsible for coordinating an organization's data is a [Data architect](https://en.wikipedia.org/wiki/Data_architect "Data architect").

## History

The first reference to this term was at the 1999 [AAAI](http://www.aaai.org/) [Ontologies Panel](https://web.archive.org/web/20070118085450/http://www.cs.vassar.edu/faculty/welty/presentations/aaai-99/). The panel was organized by Chris Welty, who at the prodding of Fritz Lehmann and in collaboration with the panelists (Fritz, [Mike Uschold](https://en.wikipedia.org/wiki/Mike_Uschold "Mike Uschold"), [Mike Gruninger](https://en.wikipedia.org/wiki/Mike_Gruninger "Mike Gruninger"), and [Deborah McGuinness](https://en.wikipedia.org/wiki/Deborah_McGuinness "Deborah McGuinness")) came up with a "spectrum" of kinds of information systems that were, at the time, referred to as ontologies. The "ontology spectrum" picture appeared in print in the introduction to *[Formal Ontology and Information Systems: Proceedings of the 2001 Conference](http://portal.acm.org/toc.cfm?id=505168&coll=GUIDE&dl=GUIDE&type=proceeding&CFID=10676962&CFTOKEN=42478708).* The ontology spectrum was also featured in a talk at the Semantics for the Web meeting in 2000 at Dagstuhl by Deborah McGuinness. McGuinness produced a [paper](http://www.ksl.stanford.edu/people/dlm/papers/ontologies-come-of-age-mit-press-\(with-citation\).htm) describing the points on that spectrum that appeared in the book that emerged (much later) from that workshop called ["Spinning the Semantic Web."](https://web.archive.org/web/20070327234919/http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=9182) Later, Leo Obrst extended the spectrum into two dimensions (which technically is not really a spectrum anymore) and added a lot more detail, which was included in his book, *The Semantic Web: A Guide to the Future of XML, Web Services, and Knowledge Management.*

The concept of the Semantic precision in [business systems](https://en.wikipedia.org/wiki/Business_system "Business system") was popularized by [Dave McComb](https://en.wikipedia.org/w/index.php?title=Dave_McComb&action=edit&redlink=1 "Dave McComb (page does not exist)") in his book *Semantics in Business Systems: The Savvy Managers Guide* published in 2003 where he frequently uses the term **Semantic Precision**.

This discussion centered around a 10 level partition that included the following levels (listed in the order of increasing semantic precision):

1. Simple Catalog of Data Elements
2. [Glossary](https://en.wikipedia.org/wiki/Glossary "Glossary") of Terms and Definitions
3. [Thesauri](https://en.wikipedia.org/wiki/Thesauri "Thesauri"), Narrow Terms, [Relationships](https://en.wikipedia.org/wiki/Relation_\(mathematics\) "Relation (mathematics)")
4. Informal " [Is-a](https://en.wikipedia.org/wiki/Is-a "Is-a") " relationships
5. Formal "Is-a" relationships
6. Formal [instances](https://en.wikipedia.org/wiki/Instantiation_principle "Instantiation principle")
7. [Frames](https://en.wikipedia.org/wiki/Frame_\(data_structure\) "Frame (data structure)") (properties)
8. [Value Restrictions](https://en.wikipedia.org/wiki/Value_restriction "Value restriction")
9. [Disjointness](https://en.wikipedia.org/wiki/Disjointness "Disjointness"), Inverse, [Part-of](https://en.wikipedia.org/wiki/Part-of "Part-of")
10. [General Logical Constraints](https://en.wikipedia.org/wiki/Constraint_logic_programming "Constraint logic programming")

Note that there was formerly a special emphasis on the adding of formal *is-a* relationships to the spectrum which has been dropped.

The company [Cerebra](http://cerebra.com/) has also popularized this concept by describing the data formats that exist within an enterprise in their ability to store semantically precise [metadata](https://en.wikipedia.org/wiki/Metadata "Metadata"). Their list includes:

1. [HTML](https://en.wikipedia.org/wiki/HTML "HTML")
2. [PDF](https://en.wikipedia.org/wiki/PDF "PDF")
3. [Word Processing](https://en.wikipedia.org/wiki/Word_Processing "Word Processing") documents
4. [Microsoft Excel](https://en.wikipedia.org/wiki/Microsoft_Excel "Microsoft Excel")
5. [Relational databases](https://en.wikipedia.org/wiki/Relational_database "Relational database")
6. [XML](https://en.wikipedia.org/wiki/XML "XML")
7. [XML Schema](https://en.wikipedia.org/wiki/XML_Schema_\(W3C\) "XML Schema (W3C)")
8. [Taxonomies](https://en.wikipedia.org/wiki/Taxonomy_\(general\) "Taxonomy (general)")
9. [Ontologies](https://en.wikipedia.org/wiki/Ontologies "Ontologies")

[^1]: Lassila, Tim Berners-Lee, James Hendler and Ora (2001-05-01). ["The Semantic Web"](https://www.scientificamerican.com/article/the-semantic-web/). *Scientific American*. Retrieved 2024-05-05.