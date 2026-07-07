---
title: "Commons:Categories - Wikimedia Commons"
source: "https://commons.wikimedia.org/wiki/Commons:Categories"
author:
published:
created: 2026-04-10
description:
tags:
  - "clippings"
---
[Shortcuts](https://commons.wikimedia.org/wiki/Commons:Shortcuts "Commons:Shortcuts"): [COM:C](https://commons.wikimedia.org/w/index.php?title=Commons:C&redirect=no) • [COM:CAT](https://commons.wikimedia.org/w/index.php?title=Commons:CAT&redirect=no)

| ![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Commons_policy.png/40px-Commons_policy.png) | **This page is considered an [official policy](https://commons.wikimedia.org/wiki/Commons:Policies_and_guidelines "Commons:Policies and guidelines") on Wikimedia Commons.**  It has wide acceptance among editors and is considered a standard that everyone must follow. Except for minor edits (such as fixing typos, or bringing information up to date), please make use of the [discussion page](https://commons.wikimedia.org/wiki/Commons_talk:Categories "Commons talk:Categories") to propose changes to this policy. |
| --- | --- |

A **category** is a software feature of [MediaWiki](https://en.wikipedia.org/wiki/MediaWiki "w:MediaWiki"), a special page which is intended to group related pages and media. In practice, it implies that you'll associate a single subject with a given category. The category name should be enough to guess the subject, but some extra text can be useful to precisely define it. The [category](https://commons.wikimedia.org/wiki/Commons:Guide_to_layout/Category_pages "Commons:Guide to layout/Category pages") structure is the primary way to organize and find files on the Commons. It is essential that every file can be found by browsing the category structure. To allow this, each file must be put into a category directly. Each category should itself be in more general categories, forming a hierarchical structure.

1\. How to find the appropriate categories

- Find categories with the search engine (enter *cat:search terms* into the search bar at the top; see [#Categorization tips](#Categorization_tips))
- or check how similar files are categorized (some may not be categorized though)
- or start from the main topical category ([Category:Topics](https://commons.wikimedia.org/wiki/Category:Topics "Category:Topics"))
- Starting from these categories, check their parent or sub-categories to find an appropriate category. Avoid picking too general categories.

2\. Add the categories to the file

- Add them on the upload form
- or: add them manually by adding, e.g. `[[Category:Foobar]]` to the file description page (see [#Categorizing pages](#Categorizing_pages))
- or: use HotCat which can autocomplete category names (see [Help:Gadget-HotCat](https://commons.wikimedia.org/wiki/Help:Gadget-HotCat "Help:Gadget-HotCat"))
- or: use Cat-a-lot to categorize many files at once (see [Help:Gadget-Cat-a-lot](https://commons.wikimedia.org/wiki/Help:Gadget-Cat-a-lot "Help:Gadget-Cat-a-lot"))

### Principles

[Shortcut](https://commons.wikimedia.org/wiki/Commons:Shortcuts "Commons:Shortcuts")

- [COM:CATPRI](https://commons.wikimedia.org/w/index.php?title=Commons:CATPRI&redirect=no)

The main principles are:

#### Hierarchic principle

The category structure is (ideally) a [multi-hierarchy](https://en.wikipedia.org/wiki/en:Directed_acyclic_graph "w:en:Directed acyclic graph") with a single root category, [Category:CommonsRoot](https://commons.wikimedia.org/wiki/Category:CommonsRoot "Category:CommonsRoot"). All categories (except [*CommonsRoot*](https://commons.wikimedia.org/wiki/Category:CommonsRoot "Category:CommonsRoot")) should be contained in at least one other category. There should be no cycles (i.e. a category should not contain itself, directly or indirectly).

#### Modularity principle

The page (file, category) should be put in the most specific category/categories that fit(s) the page (not directly to its parent categories). A category can have more parent categories. A category can combine two (or more) different criteria; such categories are called "compound categories" or "intersection categories". E.g. the root category [Category:Churches](https://commons.wikimedia.org/wiki/Category:Churches "Category:Churches") and the root category [Category:Russia](https://commons.wikimedia.org/wiki/Category:Russia "Category:Russia") have a common subcategory [Churches in Russia](https://commons.wikimedia.org/wiki/Category:Churches_in_Russia "Category:Churches in Russia").

#### Simplicity principle

This principle suggests not to combine too many different criteria.

#### Selectivity principle

We should not classify items which are related to different subjects in the same category. There should be one category per topic; multi-subject categories should be avoided. The category name should be unambiguous and not homonymous.

#### Universality principle

Identical items should have identical names for all countries and at all levels of categorization. The categorization structure should be as systematical and unified as possible, and local dialects and terminology should be suppressed in favour of universality if possible. Analogic categorization branches should have an analogic structure.

### Types of reflected relations

The category structure should reflect a hierarchy of concepts, from the most generic one down to the very specific. The structure uses and combines more types of relation, e. g.

- [Hyponymy](https://en.wikipedia.org/wiki/en:Hypernymy_and_hyponymy "w:en:Hypernymy and hyponymy"): a sort/kind/type of… (typically in biological taxonomy)
- [Meronymy](https://en.wikipedia.org/wiki/en:Meronymy "w:en:Meronymy"): a part of…, a member of… (typically for geographical division, building/room, device/component etc.)
- Attributes:
	- Qualitative and general attributes (color, shape, size, ability or disability, nationality, technique, quality, awards…)
		- Location: where, in…, from… (place/event, place/building, place/exhibit, place/people, country/language, source/work, factory or country/product etc.)
		- Timing: when (time/event, time/depicted situation, time of birth, inception or construction, time of death, demolition or termination etc.)
- Agentive and influence relations: (creator/work, device/product, company/product, discipline or profession/their subjects and terms, parent/children, subordination, owner/property, initiator/follower, subject/other subjects dedicated to it or named after it, subject/its duplicate, imitation, depiction or symbol etc etc.)
- Modification: original/modified or modified/original (avoid cyclic structure) – renamed, rebuilt, repurposed or transformed subjects.

### Major categories

The top-most categories (the ones contained directly in CommonsRoot) divide the category structure by the purpose of the contained categories:

- **[Category:Topics](https://commons.wikimedia.org/wiki/Category:Topics "Category:Topics")** – This category is the global common root of the media files categorized by the TOPIC. ALL media files should be categorized under this category for the sake of allowing others to find them by topic. Topical categories shouldn't be included through templates.
- **[Category:Copyright statuses](https://commons.wikimedia.org/wiki/Category:Copyright_statuses "Category:Copyright statuses")** – This category is the global common root of the media files categorized by the 'LICENSE. ALL media files should be categorized under this category with the appropriate [license tag](https://commons.wikimedia.org/wiki/Commons:Copyright_tags "Commons:Copyright tags"). This type of category is added by including it in the templates.
- **[Category:Media by source](https://commons.wikimedia.org/wiki/Category:Media_by_source "Category:Media by source")** – This category is the global common root of the media files categorized by the SOURCE, where they come from (books, collections, sites, etc.). This type of category is generally added by template.
- **[Category:Media types](https://commons.wikimedia.org/wiki/Category:Media_types "Category:Media types")** – This category is the global common root of the media files categorized by the Media TYPE. Please note that this type of categorization is sometimes omitted for images, since the vast majority of files on the Commons are images of some sort.
- **[Category:Commons](https://commons.wikimedia.org/wiki/Category:Commons "Category:Commons")** – This category is the global common root of categorizing Commons maintenance tasks and pages (Commons:-, and Help:-) except for media files. The translated pages in each language should be categorized under their language categories, using the "Category:Commons- [ISO-LANGUAGE-CODE](https://en.wikipedia.org/wiki/ISO_639 "w:ISO 639") " style. The structure of [Category:Commons-en](https://commons.wikimedia.org/wiki/Category:Commons-en "Category:Commons-en") is the sample hierarchy for every other language sub category. Do not use two colons in category or page names. See [this discussion](https://commons.wikimedia.org/wiki/Category_talk:Commons_batch_uploading "Category talk:Commons batch uploading") and [Help:Namespaces](https://commons.wikimedia.org/wiki/Help:Namespaces "Help:Namespaces").

There is a sub category [Category:Commons maintenance content](https://commons.wikimedia.org/wiki/Category:Commons_maintenance_content "Category:Commons maintenance content"), which is for the special maintenance of Wikimedia Commons global common contents and which does not get translated.　ALL media files should be categorized under the first 4 categories below, but ONLY files having problems and needing to be fixed should also be in the sub-category [Category:Commons maintenance content](https://commons.wikimedia.org/wiki/Category:Commons_maintenance_content "Category:Commons maintenance content").

- **[Category:User categories](https://commons.wikimedia.org/wiki/Category:User_categories "Category:User categories")** – this is for categories that contain Commons users' galleries, images and texts, sorted by things like the language they speak. This also contains the [Category:User galleries](https://commons.wikimedia.org/wiki/Category:User_galleries "Category:User galleries"), which is for user specific (i.e. non-topic) galleries that don't need to be in English language.

You should always put your uploads into categories and/or gallery pages according to topic, so your contributions can be found and used by others.

It is rarely necessary to create a new category (there are exceptions, such as uploading a new text and see *[People](#People)* below). Before doing so, make sure you are familiar with the existing category structure, and with the customs and policies of the Commons. Please see if there exists a [category scheme](https://commons.wikimedia.org/wiki/Category:Commons_category_schemes "Category:Commons category schemes") or a [Commons project](https://commons.wikimedia.org/wiki/Category:Commons_projects "Category:Commons projects") for your topic, and follow the conventions described there.

### Category names

Category names should generally be in English (see [Commons:Language policy](https://commons.wikimedia.org/wiki/Commons:Language_policy "Commons:Language policy")). However, there are exceptions such as:

- some proper names
- biological taxa
- names for which the non-English name is most commonly used in the English language (or there is no evidence of usage of an English-language version)

[Latin alphabets](https://en.wikipedia.org/wiki/en:List_of_Latin-script_alphabets "w:en:List of Latin-script alphabets") are used in original form including diacritics and derived letters, non-Latin alphabets are transcribed to the English Latin script. Basic English characters ([ISO/IEC 646](https://en.wikipedia.org/wiki/ISO/IEC_646 "w:ISO/IEC 646")) are preferred over national variants or extension character sets (for instance, 'straight' apostrophes over 'curly'), where reasonable.

- Types or groups of objects or people should generally have names in plural form: [Category:Tools](https://commons.wikimedia.org/wiki/Category:Tools "Category:Tools"), [Category:Artists](https://commons.wikimedia.org/wiki/Category:Artists "Category:Artists"), [Category:Lakes](https://commons.wikimedia.org/wiki/Category:Lakes "Category:Lakes"), [Category:Paintings](https://commons.wikimedia.org/wiki/Category:Paintings "Category:Paintings"), [Category:Sculptures](https://commons.wikimedia.org/wiki/Category:Sculptures "Category:Sculptures"), [Category:Popes](https://commons.wikimedia.org/wiki/Category:Popes "Category:Popes") etc. and in English if possible.
- General themes or activities require a name in singular form usually: [Category:History](https://commons.wikimedia.org/wiki/Category:History "Category:History"), [Category:Weather](https://commons.wikimedia.org/wiki/Category:Weather "Category:Weather"), [Category:Music](https://commons.wikimedia.org/wiki/Category:Music "Category:Music"), [Category:Painting](https://commons.wikimedia.org/wiki/Category:Painting "Category:Painting"), [Category:Sculpture](https://commons.wikimedia.org/wiki/Category:Sculpture "Category:Sculpture"), [Category:Papacy](https://commons.wikimedia.org/wiki/Category:Papacy "Category:Papacy") etc. and in English if possible.
- A particular individual object (a specific person, building, monument, artwork, organization, event, etc.) generally uses a singular form (but not always). [Proper nouns](https://en.wikipedia.org/wiki/en:Proper_noun "w:en:Proper noun") which do not have an established English variant are not translated ad hoc but use the original form.

Categories grouping subcategories by name should generally be named "by name" rather than "by alphabet" (e.g. [Category:Ships by name](https://commons.wikimedia.org/wiki/Category:Ships_by_name "Category:Ships by name")).

We still lack internationalization for category names, but this issue should be resolved with appropriate changes to the MediaWiki software (see [T31928](https://phabricator.wikimedia.org/T31928 "phab:T31928"): *Show translated titles per user language in categories too*). Creating intermingled category structures in different languages would only make things worse.

For a general discussion of MediaWiki's category feature, see the [manual page on categories](https://www.mediawiki.org/wiki/Special:MyLanguage/Help:Categories "mw:Special:MyLanguage/Help:Categories").

### Categorizing pages

![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/HotCat_autocomplete_%28adding_a_Commons_category%29.png/250px-HotCat_autocomplete_%28adding_a_Commons_category%29.png)

HotCat can be used to add a category or multiple to a page without having to edit the wikitext. It features autocomplete and automatically resolves redirects.

To add a page (be it an image, a gallery page, or a category page) to a category, add the following code to the end of the page.

`[[Category:*Category name*]]`

For example, if you are uploading a diagram showing the orbit of comets, you could add the following to the image description page:

```
[[Category:Orbits of comets]]
```

This will make the diagram show up in the category [Orbits of comets](https://commons.wikimedia.org/wiki/Category:Orbits_of_comets "Category:Orbits of comets") (which is located underneath [Category:Astronomical diagrams](https://commons.wikimedia.org/wiki/Category:Astronomical_diagrams "Category:Astronomical diagrams")).

For information on how to find good categories for your uploads and galleries, read the section *[Find an appropriate category](#Find_an_appropriate_category)* below.

### Creating a new category

To create a new category:

1. Do a thorough search, to be sure there isn't an existing category that will serve the purpose.
2. Find images (or a gallery or other pages) which should be put in the new category. Edit this page, and at the end insert the new category reference. e.g. `[[Category:Title]]`. Save the edited page. The new category appears as a red link at the bottom of the page.
3. Click on that red link. The new, empty, category page appears for editing. You can now edit the category like any other wiki page.

A category page should contain the following information (in order of importance):

- Category-links that put it into one or more parent categories. At the bottom of the new page, insert lines of the form `[[Category:Relevant categories]]`.
- A short description text that explains what should be in the category, if the title is not clear or unambiguous enough on its own. Descriptions in particular languages can be tagged e.g. with the template `{{ab|...}}` for description in Abkhazian, `{{en|...}}` for description in English, etc., as listed in [Commons:Language templates](https://commons.wikimedia.org/wiki/Commons:Language_templates "Commons:Language templates")); or using the [{{Multilingual description}}](https://commons.wikimedia.org/wiki/Template:Multilingual_description "Template:Multilingual description") template to show only the description in the user’s preferred language if there is one.
- Interwiki or interlanguage links to the article or category with the same topic in Wikipedia by adding the appropriate sitelinks on the corresponding Wikidata page. After creating the category page, click "Add links" under "In Wikipedia" on the bottom of the sidebar to the left to add them.

See also [#How to categorize: guidance by topic](#How_to_categorize:_guidance_by_topic) for guidance on specific classes of category, e.g. categories about [#People](#People).

### Sorting categories

If a category should be sorted according to a different string than the category title, there are two ways:

**Defining a sortkey (sort string) *for all* parent categories**:

```
{{DEFAULTSORT:sortkey}}
[[Category:Parent category A]]
[[Category:Parent category B]]
```

This will sort the category into all parent categories under the specified sortkey. For instance, the title of a category about a person would not be the right sort string. For such categories, insert just before the categories a line with the correct sort string like:

```
{{DEFAULTSORT:Lastname, Firstname}}
```

**Defining a sortkey only *for one* of the parent categories**:

```
[[Category:Parent category A|sortkey]]
[[Category:Parent category B]]
```

This will also override any maybe defined DEFAULTSORT for ‘Parent category A’.

**The default sort order on Commons is:**

```
░ ! " # $ % & ' ( ) * + , - . / 0 9 : ; < = > ? @ A a Z z [ \ ] ^ _ \` { | } ~ É é 📚
```
- Here the symbol `░` should simply indicate a [space](https://en.wikipedia.org/wiki/Space_\(punctuation\) "w:Space (punctuation)") as sortkey, which is always sorted first.
- The two most commonly used sort keys on Commons are   (space) and **`*`**, after this **`!`**, **`#`**, **`+`**, **`-`**, **`.`**, **`:`**, **`?`** and **`~`** are also often used.
- The sortkey **`~`** is used to sort [templates](https://commons.wikimedia.org/wiki/Commons:Templates "Commons:Templates") at the end of the related Commons-category, see for example [Category:Transport templates](https://commons.wikimedia.org/wiki/Category:Transport_templates "Category:Transport templates") sorted in [Category:Transport](https://commons.wikimedia.org/wiki/Category:Transport "Category:Transport").
- The special sortkey `📚` ([{{Setcat}}](https://commons.wikimedia.org/wiki/Template:Setcat "Template:Setcat")) is used to sort [image sets](https://commons.wikimedia.org/wiki/Commons:Image_sets "Commons:Image sets") at the end of the related category. (See e.g. [Category:Icosahedron with colored vertices](https://commons.wikimedia.org/wiki/Category:Icosahedron_with_colored_vertices "Category:Icosahedron with colored vertices") sorted in [Category:Icosahedron](https://commons.wikimedia.org/wiki/Category:Icosahedron "Category:Icosahedron").)

→ *See also:* [Meta:Help:Sorting#Sort modes](https://meta.wikimedia.org/wiki/Help:Sorting#Sort_modes "meta:Help:Sorting") for more information.

### Renaming or moving categories

Please see [Commons:Rename a category](https://commons.wikimedia.org/wiki/Commons:Rename_a_category "Commons:Rename a category").

Pages (including category pages) are categorized according to their subject, and not to their contents, because the contents are generally not a permanent feature of the category page; in particular, you can momentarily find inappropriate contents in a category page.

Example: Assume that [Category:Spheres](https://commons.wikimedia.org/wiki/Category:Spheres "Category:Spheres") contains only pictures of crystal balls. You must not add [Category:Glass](https://commons.wikimedia.org/wiki/Category:Glass "Category:Glass") in the category page, according to the current contents, because you can have spheres made with a great variety of materials. Normally, any picture showing a glass object would be already categorized in [Category:Glass](https://commons.wikimedia.org/wiki/Category:Glass "Category:Glass") (or in a category of its substructure). So, if the [Category:Spheres](https://commons.wikimedia.org/wiki/Category:Spheres "Category:Spheres") is really crowded with crystal balls pictures, it would be a better idea to create a new category page, like Category:Glass spheres or Category:Crystal balls, categorized in [Category:Spheres](https://commons.wikimedia.org/wiki/Category:Spheres "Category:Spheres") and [Category:Glass](https://commons.wikimedia.org/wiki/Category:Glass "Category:Glass").

Generally files should only be in the most specific category that exists for certain topic. For example, files in [Category:Looking up the center of the Eiffel Tower](https://commons.wikimedia.org/wiki/Category:Looking_up_the_center_of_the_Eiffel_Tower "Category:Looking up the center of the Eiffel Tower") should not also be in [Category:Paris](https://commons.wikimedia.org/wiki/Category:Paris "Category:Paris") *(see [over-categorization](#Over-categorization) below)*. If you do not find a category that fits your purpose, you can create it – but carefully read the section about [using categories](#How_to_use_categories) first.

This does not mean that an image only belongs in one category; it just means that images should not be in *redundant* or non-specific categories. For instance, an image of a Polar Bear being rescued from an iceberg by a helicopter should be in [Category:Ursus maritimus](https://commons.wikimedia.org/wiki/Category:Ursus_maritimus "Category:Ursus maritimus"), [Category:Icebergs](https://commons.wikimedia.org/wiki/Category:Icebergs "Category:Icebergs") and [Category:Rescue helicopters](https://commons.wikimedia.org/wiki/Category:Rescue_helicopters "Category:Rescue helicopters"). It should not, however, be in [Category:Ursidae](https://commons.wikimedia.org/wiki/Category:Ursidae "Category:Ursidae"), [Category:Sea ice](https://commons.wikimedia.org/wiki/Category:Sea_ice "Category:Sea ice") or [Category:Aircraft](https://commons.wikimedia.org/wiki/Category:Aircraft "Category:Aircraft").

### Categorization tips

The categories you choose for your uploads should answer as many as possible of the following questions:

- **what? / whom?:** what or whom does the file show? What is the main subject? What are the noteworthy features of the image? For instance [Category:Automobiles](https://commons.wikimedia.org/wiki/Category:Automobiles "Category:Automobiles"), [Category:Felis silvestris catus](https://commons.wikimedia.org/wiki/Category:Felis_silvestris_catus "Category:Felis silvestris catus") or [Category:Jimmy Wales](https://commons.wikimedia.org/wiki/Category:Jimmy_Wales "Category:Jimmy Wales")
- **where?:** where was the image taken? What is the location of the subject? What is the location of the camera? This is especially important for pictures of places. E.g. [Category:Basin Street, New Orleans](https://commons.wikimedia.org/wiki/Category:Basin_Street,_New_Orleans "Category:Basin Street, New Orleans")
	also use [{{Location}}](https://commons.wikimedia.org/wiki/Template:Location "Template:Location")
- **when?:** when did the depicted events happen, or when was the image created? When was the image taken? This is especially important for historical images. An example would be [Category:Warsaw in September 1939](https://commons.wikimedia.org/wiki/Category:Warsaw_in_September_1939 "Category:Warsaw in September 1939"), [Category:April 2010 in Northern Ireland](https://commons.wikimedia.org/wiki/Category:April_2010_in_Northern_Ireland "Category:April 2010 in Northern Ireland")
- **who?:**
	- who (if anyone) is depicted? Please add one or more subcategories from [Category:People](https://commons.wikimedia.org/wiki/Category:People "Category:People")
		- who is the author? This is especially important for works of well known artists and for historical images, for example [Category:Paintings by Rembrandt](https://commons.wikimedia.org/wiki/Category:Paintings_by_Rembrandt "Category:Paintings by Rembrandt") or [Category:Photographs by Annie Leibovitz](https://commons.wikimedia.org/wiki/Category:Photographs_by_Annie_Leibovitz "Category:Photographs by Annie Leibovitz"). You can also use the pages from the [*Creator* namespace](https://commons.wikimedia.org/wiki/Category:Creator_templates "Category:Creator templates") as templates to achieve this.
- **how?:** how does the file (or the image) do that? Specifically:
	- **what view?:** what type of view does the image show? e.g. [Category:Plan views](https://commons.wikimedia.org/wiki/Category:Plan_views "Category:Plan views"), [Category:Panoramics](https://commons.wikimedia.org/wiki/Category:Panoramics "Category:Panoramics").
		- **what color?:** which is the general color? e.g. [Category:Yellow animals](https://commons.wikimedia.org/wiki/Category:Yellow_animals "Category:Yellow animals")
		- **what photography technique?:**. If the image uses a specific [technique](https://commons.wikimedia.org/wiki/Category:Photographic_techniques "Category:Photographic techniques") or [effect](https://commons.wikimedia.org/wiki/Category:Photographic_effects "Category:Photographic effects"), apply the corresponding category: e.g. [Category:Tone-mapped HDR images](https://commons.wikimedia.org/wiki/Category:Tone-mapped_HDR_images "Category:Tone-mapped HDR images"), [Category:Black and white photographs](https://commons.wikimedia.org/wiki/Category:Black_and_white_photographs "Category:Black and white photographs"), [Category:Double exposure](https://commons.wikimedia.org/wiki/Category:Double_exposure "Category:Double exposure")

The above questions cover the main aspects of the image to be categorized. For some images it makes sense to use all, for other images only one or two are reasonable. In addition there are several other aspects of the images that can be used to categorize the image:

- **what source?:** information about where the image came from. For example, [Category:Images from the German Federal Archive](https://commons.wikimedia.org/wiki/Category:Images_from_the_German_Federal_Archive "Category:Images from the German Federal Archive")
- **what format?:** information about the media type if it is unusual. For example, [Category:Audio](https://commons.wikimedia.org/wiki/Category:Audio "Category:Audio") or [Category:Animated GIF](https://commons.wikimedia.org/wiki/Category:Animated_GIF "Category:Animated GIF"), [Category:SVG](https://commons.wikimedia.org/wiki/Category:SVG "Category:SVG")
- **what software?:** information about software used to create the image. For example, [Category:Created with Hugin](https://commons.wikimedia.org/wiki/Category:Created_with_Hugin "Category:Created with Hugin")
- **what camera?:** information about the camera. For example, [Category:Taken with Nikon D80](https://commons.wikimedia.org/wiki/Category:Taken_with_Nikon_D80 "Category:Taken with Nikon D80")

This last set is useful and important but should always be done in addition of the main set of criteria.

Categorization in Wikimedia Commons is more detailed and deep than categorization in Wikipedia projects. Compared to them, Commons has more categories for individual subjects – places, people, organizations, events, terms, etc. Almost every article on a Wikipedia can have a corresponding category on Commons. However, even if there exist more images of an ordinary person or incidental event, it is practical to group them into a special category and categorize that category instead of categorizing all similar images individually to an identical set of parent categories.

### Find an appropriate category

To find appropriate categories for your uploads, you should navigate the category structure starting from a generic category. Narrow your search down to subcategories until you find the most specific category/ies that fit(s) the file you uploaded. You can navigate the category structure by following links to subcategories, or expanding the tree of subcategories by clicking on the little ▶ symbols on subcategory names. The *[Major categories](#Major_categories)* section above provides a starting point, and the *[How to categorize: guidance by topic](#How_to_categorize:_guidance_by_topic)* covers some more topics.

### Over-categorization

*for the inclusion criteria (the equivalent of [w:WP:OVERCAT](https://en.wikipedia.org/wiki/WP:OVERCAT "w:WP:OVERCAT")) see [Commons:Category inclusion criteria](https://commons.wikimedia.org/wiki/Commons:Category_inclusion_criteria "Commons:Category inclusion criteria")*

![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Over-categorization.svg/250px-Over-categorization.svg.png)

Don't place an item into a category and its parent. For example, a black and white photo of the Eiffel Tower should be placed in Black and white photographs of the Eiffel Tower. It should not be placed in both that category and the Paris category at the same time.

Over-categorization is placing a file, category or other page in several levels of the same branch in the category tree. The general rule is *always place an image in the most specific categories, and not in the levels above those.* Exceptions to this rule are explained in [the section below](#OvercatException).

Example: An image needing to be categorized shows a yellow circle. This image should be placed in [Category:Yellow circles](https://commons.wikimedia.org/wiki/Category:Yellow_circles "Category:Yellow circles"). If it is also placed in [Category:Circles](https://commons.wikimedia.org/wiki/Category:Circles "Category:Circles"), it is *over-categorized.* We already know that it's a circle, because all yellow circles are circles. Therefore, [Category:Circles](https://commons.wikimedia.org/wiki/Category:Circles "Category:Circles") is redundant. [Template:Uw-overcat](https://commons.wikimedia.org/wiki/Template:Uw-overcat "Template:Uw-overcat") can be used to advise users of this.

This applies to most files: As mentioned under the adjacent illustration, files in [Category:Black and white photographs of the Eiffel Tower](https://commons.wikimedia.org/wiki/Category:Black_and_white_photographs_of_the_Eiffel_Tower "Category:Black and white photographs of the Eiffel Tower") should not also be in [Category:Paris](https://commons.wikimedia.org/wiki/Category:Paris "Category:Paris"), files in [Category:Albert Einstein](https://commons.wikimedia.org/wiki/Category:Albert_Einstein "Category:Albert Einstein") should not be in [Category:Physicists from Germany](https://commons.wikimedia.org/wiki/Category:Physicists_from_Germany "Category:Physicists from Germany") and so on.

#### Why over-categorization is a problem

It's often assumed that the more categories an image is in, the easier it will be to find it. Another example: By that logic, every image showing a man should be in [Category:Men](https://commons.wikimedia.org/wiki/Category:Men "Category:Men"), because even if you know nothing more about the person you're looking for than that he is a man, you'll be able to find it. The result is that the top category fills up, making it necessary to go through hundreds, or in this case more likely thousands of images to find the one you want. You probably won't find what you're looking for, and what's more, those who are looking for a generic picture of a man to illustrate an article like [en:Man](https://en.wikipedia.org/wiki/Man "en:Man") will find that they've drowned out among the movie stars, scientists and politicians.

On lower levels, the problem becomes less acute, since the number of images will be smaller — they can still easily reach into the hundreds, though. But there is still a problem: Let's go back to Einstein. I know that he's a physicist, so I'll look in the [Category:Physicists](https://commons.wikimedia.org/wiki/Category:Physicists "Category:Physicists") category. I find an image of Einstein among the hundreds of images of other physicists, which I'm not too happy with, but it's the only one there. Since there was an image there, I assume that there are no more hidden elsewhere, rather than look further in [Category:Physicists from Germany](https://commons.wikimedia.org/wiki/Category:Physicists_from_Germany "Category:Physicists from Germany") and thus find [Category:Albert Einstein](https://commons.wikimedia.org/wiki/Category:Albert_Einstein "Category:Albert Einstein") where there might be a better one. So over-categorization has led to two problems: The top category is cluttered, and users will stop looking for the most relevant category since they've reached one that has a relevant image.

#### Improper categorization of categories is a cause of over-categorization

Strange as it may sound, under-categorization can be a cause of over-categorization. When a category itself is not properly categorized, it can lead users to over-categorize files belonging in that category. An example of this: [Category:Eivør Pálsdóttir](https://commons.wikimedia.org/wiki/Category:Eiv%C3%B8r_P%C3%A1lsd%C3%B3ttir "Category:Eivør Pálsdóttir") was categorized only in [Category:People by name](https://commons.wikimedia.org/wiki/Category:People_by_name "Category:People by name"). A user categorizing an image of her might then be tempted to also place the image in [Category:Female vocalists from the Faroe Islands](https://commons.wikimedia.org/wiki/Category:Female_vocalists_from_the_Faroe_Islands "Category:Female vocalists from the Faroe Islands"). The correct solution is to place the image only in [Category:Eivør Pálsdóttir](https://commons.wikimedia.org/wiki/Category:Eiv%C3%B8r_P%C3%A1lsd%C3%B3ttir "Category:Eivør Pálsdóttir") and to make that category a subcategory of [Category:Female vocalists from the Faroe Islands](https://commons.wikimedia.org/wiki/Category:Female_vocalists_from_the_Faroe_Islands "Category:Female vocalists from the Faroe Islands"). At that point, however, any images that were already placed into both categories become overcategorized and need to be manually removed from the parent category.

A related problem is erroneous categorization. Notting Hill is a district within the borough of Kensington and Chelsea in London. When it was created, [Category:Notting Hill](https://commons.wikimedia.org/wiki/Category:Notting_Hill "Category:Notting Hill") was placed directly in [Category:London](https://commons.wikimedia.org/wiki/Category:London "Category:London") instead of in the [Category:Royal Borough of Kensington and Chelsea](https://commons.wikimedia.org/wiki/Category:Royal_Borough_of_Kensington_and_Chelsea "Category:Royal Borough of Kensington and Chelsea") subcategory, where it should have been placed. A user categorizing an image of Notting Hill might then be tempted to place it both in [Category:Notting Hill](https://commons.wikimedia.org/wiki/Category:Notting_Hill "Category:Notting Hill") and in [Category:Royal Borough of Kensington and Chelsea](https://commons.wikimedia.org/wiki/Category:Royal_Borough_of_Kensington_and_Chelsea "Category:Royal Borough of Kensington and Chelsea"). Instead, each image should be placed only in the most specific categories, and those categories should in turn be placed in their most specific categories.

When you encounter improperly categorized categories, please place them in the appropriate parent categories if you are able to do so. That will not only help avoid over-categorization, but it will also make it easier to move through the category tree.

#### Exception for images with more categorized subjects

A file that depicts only one relevant subject should not be over-categorized. Where a file depicts additional relevant subjects, and the additional subjects do not have their own subcategories, consideration can be given to temporarily categorizing the image in both the subcategory and the parent category.

For example, this situation might arise in the case of a photograph of three politicians, one of whom is [Angela Merkel](https://commons.wikimedia.org/wiki/Category:Angela_Merkel "Category:Angela Merkel") (who has her own Commons category), with two other politicians who do not yet have their own categories. While the image would undoubtedly be categorized in [Category:Angela Merkel](https://commons.wikimedia.org/wiki/Category:Angela_Merkel "Category:Angela Merkel") or one of its subcategories, it would typically be considered to be over-categorization to also include it in [Category:Politicians of Germany](https://commons.wikimedia.org/wiki/Category:Politicians_of_Germany "Category:Politicians of Germany"). Users would, however, be unlikely to search for the two other politicians in the Merkel category. Ideally, we would create specific subcategories for the two other politicians (where warranted), or find other relevant subcategories (e.g. [Category:Politicians of Bavaria](https://commons.wikimedia.org/wiki/Category:Politicians_of_Bavaria "Category:Politicians of Bavaria") or [Category:Members of the FDP](https://commons.wikimedia.org/wiki/Category:Members_of_the_FDP "Category:Members of the FDP"), etc.), that would enable us to avoid over-categorization. In some circumstances, however, we may need to temporarily categorize the image in [Category:Politicians of Germany](https://commons.wikimedia.org/wiki/Category:Politicians_of_Germany "Category:Politicians of Germany") where other appropriate subcategories do not yet exist.

Countries may be categorized as part of multiple overlapping categories. For example, [Category:India](https://commons.wikimedia.org/wiki/Category:India "Category:India") is in [Category:Countries of South Asia](https://commons.wikimedia.org/wiki/Category:Countries_of_South_Asia "Category:Countries of South Asia") as well as [Category:Countries of Asia](https://commons.wikimedia.org/wiki/Category:Countries_of_Asia "Category:Countries of Asia").

Also user categories are exempted of over-categorization as those are not visible to most viewers, and project users include them for many different purposes like sorting, stats, filling values for userboxes, etc.

For some categories, there is special guidance on how best to sort content within that category. This guidance can be found in a [category scheme](https://commons.wikimedia.org/wiki/Category:Commons_category_schemes "Category:Commons category schemes") or a [Commons project](https://commons.wikimedia.org/wiki/Category:Commons_projects "Category:Commons projects") for your topic. There is also some categorizing information in this section and sometimes there is guidance at the top of the category's page, in the Category [namespace](https://meta.wikimedia.org/wiki/Namespace "meta:Namespace"). So, for instance, some guidance on categorizing content depicting people is at the top of [Category:People](https://commons.wikimedia.org/wiki/Category:People "Category:People"), and some is in the section [People](#People) below.

### Structures

Content depicting **[Structures](https://commons.wikimedia.org/wiki/Category:Structures "Category:Structures")**, e.g. [Buildings](https://commons.wikimedia.org/wiki/Category:Buildings "Category:Buildings") and [Tunnels](https://commons.wikimedia.org/wiki/Category:Tunnels "Category:Tunnels"), can be classified like this:

**Structure Category**. First check if there is already a Category for this specific structure.

- If yes: put it in there.
- If no: If you have more than two pictures: create a new Category, named after the structure. For example [Category:Rheinbrücke Emmerich](https://commons.wikimedia.org/wiki/Category:Rheinbr%C3%BCcke_Emmerich "Category:Rheinbrücke Emmerich"). Use the common name, not necessarily the English one.

Then you categorize the category (NOT each single picture!) under the following possibilities:

- Location: see [Category:Structures by country](https://commons.wikimedia.org/wiki/Category:Structures_by_country "Category:Structures by country"), for example: [Category:Structures in Germany](https://commons.wikimedia.org/wiki/Category:Structures_in_Germany "Category:Structures in Germany")
- Function: see [Category:Structures by function](https://commons.wikimedia.org/wiki/Category:Structures_by_function "Category:Structures by function"), for example: [Category:Bridges](https://commons.wikimedia.org/wiki/Category:Bridges "Category:Bridges")
- Type / construction: see [Category:Structures by type](https://commons.wikimedia.org/wiki/Category:Structures_by_type "Category:Structures by type")
- Material: see [Category:Structures by material](https://commons.wikimedia.org/wiki/Category:Structures_by_material "Category:Structures by material") for example [Category:Concrete structures](https://commons.wikimedia.org/wiki/Category:Concrete_structures "Category:Concrete structures")
- Engineer: see [Category:Structural engineers](https://commons.wikimedia.org/wiki/Category:Structural_engineers "Category:Structural engineers") for example: [Category:John A. Roebling](https://commons.wikimedia.org/wiki/Category:John_A._Roebling "Category:John A. Roebling")
- Architect: see [Category:Architects](https://commons.wikimedia.org/wiki/Category:Architects "Category:Architects") for example: [Category:Norman Foster](https://commons.wikimedia.org/wiki/Category:Norman_Foster "Category:Norman Foster")

Afterwards, categorize the image by the way the structure is depicted, such as:

- Painting or drawing: see [Category:Paintings of structures](https://commons.wikimedia.org/wiki/Category:Paintings_of_structures "Category:Paintings of structures") or [Category:Drawings of structures](https://commons.wikimedia.org/wiki/Category:Drawings_of_structures "Category:Drawings of structures")
- Postcard: see [Category:Postcards of structures](https://commons.wikimedia.org/wiki/Category:Postcards_of_structures "Category:Postcards of structures")
- By view or point of view, see [Category:Structures by view](https://commons.wikimedia.org/wiki/Category:Structures_by_view "Category:Structures by view"), with subcategories such as [Category:Structures viewed from above](https://commons.wikimedia.org/wiki/Category:Structures_viewed_from_above "Category:Structures viewed from above"), etc.

Also consider the part and the context visible:

- For parts, see categories such as [Category:Bridge elements](https://commons.wikimedia.org/wiki/Category:Bridge_elements "Category:Bridge elements"), [Category:Tunnel portals](https://commons.wikimedia.org/wiki/Category:Tunnel_portals "Category:Tunnel portals"), [Category:Interiors of towers](https://commons.wikimedia.org/wiki/Category:Interiors_of_towers "Category:Interiors of towers")
- For context, see categories such as [Category:People with structures](https://commons.wikimedia.org/wiki/Category:People_with_structures "Category:People with structures"), [Category:Trains on bridges](https://commons.wikimedia.org/wiki/Category:Trains_on_bridges "Category:Trains on bridges")

### People

Content depicting people should be put in categories which describe them, such as [Category:Economists from the United States](https://commons.wikimedia.org/wiki/Category:Economists_from_the_United_States "Category:Economists from the United States"). Start exploring at [Category:People](https://commons.wikimedia.org/wiki/Category:People "Category:People").

Please see [Commons:Suggested category scheme for people](https://commons.wikimedia.org/wiki/Commons:Suggested_category_scheme_for_people "Commons:Suggested category scheme for people") for details on how to name and organize these categories.

### Landscapes, outdoor views

Content depicting a given subject from a common vantage point are grouped in *Views of Subject from Viewpoint* categories such as [Views of Cathedral of Seville from the Giralda](https://commons.wikimedia.org/wiki/Category:Views_of_Cathedral_of_Seville_from_the_Giralda "Category:Views of Cathedral of Seville from the Giralda"). Such categories should be subcategories of both the subject's category ([Cathedral of Seville](https://commons.wikimedia.org/wiki/Category:Cathedral_of_Seville "Category:Cathedral of Seville") in this example) and the viewpoint's category ([Giralda](https://commons.wikimedia.org/wiki/Category:Giralda "Category:Giralda") in this example).

In this example, the [Views of Cathedral of Seville from the Giralda](https://commons.wikimedia.org/wiki/Category:Views_of_Cathedral_of_Seville_from_the_Giralda "Category:Views of Cathedral of Seville from the Giralda") category is not placed directly in the subject and viewpoint categories, but in [Views of the Cathedral of Seville](https://commons.wikimedia.org/wiki/Category:Views_of_the_Cathedral_of_Seville "Category:Views of the Cathedral of Seville") and [Views from Giralda](https://commons.wikimedia.org/wiki/Category:Views_from_Giralda "Category:Views from Giralda"). Such intermediate categories are often necessary to create structure and avoid [over-categorization](#over-categorization), particularly for views of a city from a vantage point located within the city. For example, [Views of Rome from the Pincio](https://commons.wikimedia.org/wiki/Category:Views_of_Rome_from_the_Pincio "Category:Views of Rome from the Pincio") needs the intermediate category [Views of Rome](https://commons.wikimedia.org/wiki/Category:Views_of_Rome "Category:Views of Rome") to avoid placing it directly in [Rome](https://commons.wikimedia.org/wiki/Category:Rome "Category:Rome"), which would constitute over-categorization.

### Texts

Texts, such as scans of books, should normally have a category for each version of the scan and each edition of the text. Thus a book published in three separate editions would have a parent category for the book, three subcategories for each text, and further subcategories for the text as a jpeg, a DjVu, etc., assuming each version had actually been uploaded. (Categories would not be created for editions not held on Commons.) This is particularly important for files in formats other than DjVu and PDF, where the category is the only practical means of keeping the scans together; see eg. [Category:The Chronicles of England, Scotland and Ireland, Holinshed, 1587](https://commons.wikimedia.org/wiki/Category:The_Chronicles_of_England,_Scotland_and_Ireland,_Holinshed,_1587 "Category:The Chronicles of England, Scotland and Ireland, Holinshed, 1587") which contains 2857 jpeg images of page scans.

### GLAMs

For categorization issues related to mass content donations from GLAMs (Galleries, Libraries, Archives & Museums), please see [Commons:Guide to batch uploading#Categories](https://commons.wikimedia.org/wiki/Commons:Guide_to_batch_uploading#Categories "Commons:Guide to batch uploading").

Currently, a bot checks if newly uploaded files are categorized in topical categories and attempts to categorize files that are not. Before 17 June 2015, [CategorizationBot](https://commons.wikimedia.org/wiki/User:CategorizationBot "User:CategorizationBot") was responsible for this job. As of June 2019, [SteinsplitterBot](https://commons.wikimedia.org/wiki/User:SteinsplitterBot "User:SteinsplitterBot") occasionally checks for uncategorized files. The workflow is the following:

1. User uploads a new file and adds categories (or not).
2. A bot checks if the file is categorized.
	- File is already categorized => ok
		- File is not categorized => the bot tags the file for [Category:Media needing categories](https://commons.wikimedia.org/wiki/Category:Media_needing_categories "Category:Media needing categories"). Today's files are in [Category:Media needing categories as of 10 April 2026](https://commons.wikimedia.org/wiki/Category:Media_needing_categories_as_of_10_April_2026 "Category:Media needing categories as of 10 April 2026")
3. Users categorize files further (e.g. category diffusion below)

*See also:* [User:CategorizationBot#Process](https://commons.wikimedia.org/wiki/User:CategorizationBot#Process "User:CategorizationBot"), [categorization statistics](https://commons.wikimedia.org/wiki/User:Multichill/Categorization_stats "User:Multichill/Categorization stats")

Other, if manual, categorization workflows are possible:

- Category filling: Use appropriate keywords in the search engine to find the files that should be in a given category, and put them there.
- Category diffusing: Go to [Category:Categories requiring diffusion](https://commons.wikimedia.org/wiki/Category:Categories_requiring_diffusion "Category:Categories requiring diffusion"), select a crowded category, create appropriate subcategories if needed, and move the files to the subcategories. Gadgets like Cat-a-lot and HotCat can help.

[Shortcut](https://commons.wikimedia.org/wiki/Commons:Shortcuts "Commons:Shortcuts")

- [COM:HIDDENCAT](https://commons.wikimedia.org/w/index.php?title=Commons:HIDDENCAT&redirect=no)

Many non-topical categories are marked with the [magic word](https://www.mediawiki.org/wiki/Special:MyLanguage/Help:Magic_words#Behavior_switches "mw:Special:MyLanguage/Help:Magic words") `__HIDDENCAT__` or [{{Hiddencat}}](https://commons.wikimedia.org/wiki/Template:Hiddencat "Template:Hiddencat") on the category page. The advantage of using the template is that there will be an additional Infobox for the user stating that:

```
"This category is not shown on its member pages unless the appropriate user preference is set."
```

An example of using `__HIDDENCAT__` is [Category:PD NASA](https://commons.wikimedia.org/wiki/Category:PD_NASA "Category:PD NASA"). An example of using the template is [Category:Wildtunis/100WikiCommonsDays](https://commons.wikimedia.org/wiki/Category:Wildtunis/100WikiCommonsDays "Category:Wildtunis/100WikiCommonsDays").

While categories are generally visible on every page, categories marked with `__HIDDENCAT__` or [{{Hiddencat}}](https://commons.wikimedia.org/wiki/Template:Hiddencat "Template:Hiddencat") are only visible:

- on the edit screen: at the end of the screen, below the edit box
- on category pages:
	- on subcategories to the hidden category: in the normal location, but on a separate line with a smaller typeface and the label "Hidden categories."
		- on parent categories: in the same way as other categories
- on file description pages and gallery pages: for logged-in users who have selected to "Show hidden categories" in their [appearance preferences](https://commons.wikimedia.org/wiki/Special:Preferences#mw-prefsection-rendering "Special:Preferences"). This is activated for all newly registered users.

This feature is generally used for template-based categories, such as license tag based categories. For example, placing [{{PD-old-100}}](https://commons.wikimedia.org/wiki/Template:PD-old-100 "Template:PD-old-100") on a file description page adds the file to [Category:Author died more than 100 years ago public domain images](https://commons.wikimedia.org/wiki/Category:Author_died_more_than_100_years_ago_public_domain_images "Category:Author died more than 100 years ago public domain images"), which is marked with `__HIDDENCAT__`.

For more details, see the [help section on hidden categories](https://www.mediawiki.org/wiki/Special:MyLanguage/Help:Categories#Hidden_categories "mw:Special:MyLanguage/Help:Categories") for Mediawiki (the software that Commons uses).

Some templates are designed for use on category pages - see [Category:Category namespace templates](https://commons.wikimedia.org/wiki/Category:Category_namespace_templates "Category:Category namespace templates"). If the category is linked to a Wikidata entry, then you can use:

- [{{Wikidata Infobox}}](https://commons.wikimedia.org/wiki/Template:Wikidata_Infobox "Template:Wikidata Infobox") which displays a summary of the topic's information that is available on Wikidata, and also auto-adds birth/death/name/monument ID categories.

Some of the more commonly used ones are [Category:Category header templates](https://commons.wikimedia.org/wiki/Category:Category_header_templates "Category:Category header templates") such as:

- [{{Category TOC}}](https://commons.wikimedia.org/wiki/Template:Category_TOC "Template:Category TOC") and [{{LargeCategoryTOC}}](https://commons.wikimedia.org/wiki/Template:LargeCategoryTOC "Template:LargeCategoryTOC") - to provide a table of contents for very large categories with many subcategories
- [{{ImageTOC}}](https://commons.wikimedia.org/wiki/Template:ImageTOC "Template:ImageTOC") and [{{FileCategoryTOC}}](https://commons.wikimedia.org/wiki/Template:FileCategoryTOC "Template:FileCategoryTOC") - to provide a table of contents for large categories with many files and few subcategories
- [{{Image template notice}}](https://commons.wikimedia.org/wiki/Template:Image_template_notice "Template:Image template notice") and [{{Autocat}}](https://commons.wikimedia.org/wiki/Template:Autocat "Template:Autocat") - for maintenance categories populated by a specific template.
- [{{Global maintenance category}}](https://commons.wikimedia.org/wiki/Template:Global_maintenance_category "Template:Global maintenance category") and [{{Local maintenance category}}](https://commons.wikimedia.org/wiki/Template:Local_maintenance_category "Template:Local maintenance category")
- [{{CatCat}}](https://commons.wikimedia.org/wiki/Template:CatCat "Template:CatCat") - for categories which should only contain other categories
- [{{MetaCat}}](https://commons.wikimedia.org/wiki/Template:MetaCat "Template:MetaCat") - like CatCat, but narrower: should only contain other categories that are grouped by a specified criterion.
	- [{{By country category}}](https://commons.wikimedia.org/wiki/Template:By_country_category "Template:By country category"), [{{By language category}}](https://commons.wikimedia.org/wiki/Template:By_language_category "Template:By language category"), [{{By century category}}](https://commons.wikimedia.org/wiki/Template:By_century_category "Template:By century category") - for specific types of meta category
- [{{CatDiffuse}}](https://commons.wikimedia.org/wiki/Template:CatDiffuse "Template:CatDiffuse") (temporary) and [{{Categorise}}](https://commons.wikimedia.org/wiki/Template:Categorise "Template:Categorise") (permanent) - for large categories which need maintenance to move files into subcategories
- [{{Category tree}}](https://commons.wikimedia.org/wiki/Template:Category_tree "Template:Category tree")
- Gadgets enabled through the [user preferences](https://commons.wikimedia.org/wiki/Special:Preferences#mw-prefsection-gadgets "Special:Preferences")
	- *Cat-a-lot*: A tool that helps with moving multiple files between categories or adding categories to search results. \[[documentation](https://commons.wikimedia.org/wiki/Special:MyLanguage/Help:Gadget-Cat-a-lot "Special:MyLanguage/Help:Gadget-Cat-a-lot") / [talk](https://commons.wikimedia.org/wiki/MediaWiki_talk:Gadget-Cat-a-lot.js "MediaWiki talk:Gadget-Cat-a-lot.js")\]
		- *HotCat*: <sup><abbr title="default gadget – enabled by default">d</abbr></sup> Easily add / remove / change a category on a page, with name suggestions. \[[documentation](https://commons.wikimedia.org/wiki/Help:Gadget-HotCat "Help:Gadget-HotCat") / [example](https://commons.wikimedia.org/wiki/File:HotCat.png "File:HotCat.png") / [talk](https://commons.wikimedia.org/wiki/MediaWiki_talk:Gadget-HotCat.js "MediaWiki talk:Gadget-HotCat.js")\]
		- *Gallery Details*: Adds a link in the toolbox to display galleries and categories (and [Newimages](https://commons.wikimedia.org/wiki/Special:NewFiles "Special:NewFiles") and [Search](https://commons.wikimedia.org/wiki/Special:Search "Special:Search") result pages) with extensive details from file description pages and links to easily mark an image without source, etc. If *Pretty log* is activated, it also works on [Log](https://commons.wikimedia.org/wiki/Special:Log "Special:Log") pages. \[[documentation](https://commons.wikimedia.org/wiki/Help:Gadget-GalleryDetails "Help:Gadget-GalleryDetails") / [talk](https://commons.wikimedia.org/wiki/MediaWiki_talk:Gadget-GalleryDetails.js "MediaWiki talk:Gadget-GalleryDetails.js")\]
		- Place categories above content, but below image on file description pages. Modifies the placement of categories on the user interface.
		- \[[talk](https://commons.wikimedia.org/wiki/MediaWiki_talk:Gadget-Searchnotincat.js "MediaWiki talk:Gadget-Searchnotincat.js")\]
- Toollabs / toolserver tools
	- [PetScan](https://petscan.wmflabs.org/) – this new version has other features
		- [English vCat](https://meta.wikimedia.org/wiki/User:Dapete/vCat#English "m:User:Dapete/vCat") – plots ancestor trees of categories. For example, [https://tools.wmflabs.org/vcat/render?wiki=commonswiki&category=Water%20wells](https://tools.wmflabs.org/vcat/render?wiki=commonswiki&category=Water%20wells) generates a graph of the parent categories of [Category:Water wells](https://commons.wikimedia.org/wiki/Category:Water_wells "Category:Water wells")
- Special pages
	- [Alphabetic lists of categories with files or other pages in them](https://commons.wikimedia.org/wiki/Special:Categories "Special:Categories") – including nonexistent categories
		- [Category tree](https://commons.wikimedia.org/wiki/Special:CategoryTree "Special:CategoryTree")
		- [Unused categories](https://commons.wikimedia.org/wiki/Special:UnusedCategories "Special:UnusedCategories") – including categories redirected with [{{Category redirect}}](https://commons.wikimedia.org/wiki/Template:Category_redirect "Template:Category redirect")
		- [Uncategorized categories](https://commons.wikimedia.org/wiki/Special:UncategorizedCategories "Special:UncategorizedCategories")
- Bookmarklets
	- [Category redirect bookmarklets](https://commons.wikimedia.org/wiki/Commons:Categories/redirect_bookmarklets "Commons:Categories/redirect bookmarklets")
		- [Bookmarklets for categorization of aircraft by registration](https://commons.wikimedia.org/wiki/Category:Aircraft_by_registration#Bookmarklets "Category:Aircraft by registration")
- Scripts, software, etc.
	- [AutoWikiBrowser](https://commons.wikimedia.org/wiki/Commons:AutoWikiBrowser "Commons:AutoWikiBrowser") (for access: [checkpage](https://commons.wikimedia.org/wiki/Commons:AutoWikiBrowser/CheckPageJSON "Commons:AutoWikiBrowser/CheckPageJSON"))
		- [pywikipediabot](https://meta.wikimedia.org/wiki/Pywikipediabot "m:Pywikipediabot") [category.py](https://meta.wikimedia.org/wiki/Pywikipediabot/category.py "m:Pywikipediabot/category.py") (for access: [request page](https://commons.wikimedia.org/wiki/Commons:Bots/Requests "Commons:Bots/Requests"))
		- [Degrandparent](https://commons.wikimedia.org/wiki/User:Waggers/degrandparent "User:Waggers/degrandparent") – a tool to remove files from a category if they are also in one or more of its subcategories.
- Bots
	- [SieBot](https://commons.wikimedia.org/wiki/User:SieBot "User:SieBot") – renames or adds categories. See [documentation](https://commons.wikimedia.org/wiki/User:CommonsDelinker/commands/documentation#Controlling_SieBot "User:CommonsDelinker/commands/documentation") – [requests](https://commons.wikimedia.org/wiki/User_talk:CommonsDelinker/commands "User talk:CommonsDelinker/commands").
		- [EuseBot](https://commons.wikimedia.org/wiki/User:EuseBot "User:EuseBot") – adds additional parent categories to categories (and galleries) depending on which category an article in English Wikipedia is in. For [requests](https://commons.wikimedia.org/wiki/User_talk:EuseBot/commands "User talk:EuseBot/commands").
		- [RussBot](https://commons.wikimedia.org/wiki/User:RussBot "User:RussBot") – clears [Non-empty category redirects](https://commons.wikimedia.org/wiki/Category:Non-empty_category_redirects "Category:Non-empty category redirects")
		- [CategorizationBot](https://commons.wikimedia.org/wiki/User:CategorizationBot "User:CategorizationBot") – adds uncategorized images into [Media needing categories](https://commons.wikimedia.org/wiki/Category:Media_needing_categories "Category:Media needing categories") – notifies uploaders, and attempts to categorize images ([Media needing category review](https://commons.wikimedia.org/wiki/Category:Media_needing_category_review "Category:Media needing category review"))
		- [Requests for work to be done](https://commons.wikimedia.org/wiki/Commons:Bots/Work_requests "Commons:Bots/Work requests")
- [MediaWiki's handbook section on categories](https://www.mediawiki.org/wiki/Help:Category "mw:Help:Category")
- [Category:Commons category schemes](https://commons.wikimedia.org/wiki/Category:Commons_category_schemes "Category:Commons category schemes")
- [Commons:Deletion policy for categories](https://commons.wikimedia.org/wiki/Commons:Deletion_policy#Categories "Commons:Deletion policy")
- [Commons:Galleries](https://commons.wikimedia.org/wiki/Commons:Galleries "Commons:Galleries")
- [Commons:Category disambiguation](https://commons.wikimedia.org/wiki/Commons:Category_disambiguation "Commons:Category disambiguation")
- [Commons:Category inclusion criteria](https://commons.wikimedia.org/wiki/Commons:Category_inclusion_criteria "Commons:Category inclusion criteria")

Backlogs and requests

- [Commons:Categories for discussion#Current requests](https://commons.wikimedia.org/wiki/Commons:Categories_for_discussion#Current_requests "Commons:Categories for discussion") – open community discussions relating to individual categories
- [Commons:Categories requiring diffusion](https://commons.wikimedia.org/wiki/Commons:Categories_requiring_diffusion "Commons:Categories requiring diffusion") – tabular listing
- [Commons:Categorization requests](https://commons.wikimedia.org/wiki/Commons:Categorization_requests "Commons:Categorization requests") – unresolved categorization tasks by difficulty and type
- [Categories with only non-existing categories](https://commons.wikimedia.org/wiki/Commons:Report_UncategorizedCategories_with_redcats "Commons:Report UncategorizedCategories with redcats") – tabular listing
- [Categories with only infobox categories](https://commons.wikimedia.org/wiki/Commons:Report_UncategorizedCategories_with_only_infobox_categories "Commons:Report UncategorizedCategories with only infobox categories") – tabular listing
- [Self-categorized categories](https://commons.wikimedia.org/wiki/Commons:Database_reports/Self-categorized_categories "Commons:Database reports/Self-categorized categories") – category loops that need fixing
- [Commons:WikiProject Minimum One Category](https://commons.wikimedia.org/wiki/Commons:WikiProject_Minimum_One_Category "Commons:WikiProject Minimum One Category") – effort to add categories to files without any nonhidden categories