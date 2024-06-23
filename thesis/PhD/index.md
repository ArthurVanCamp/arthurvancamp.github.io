---
date: "2018-01-15T00:00:00"
title: "Choice Functions as a Tool to Model Uncertainty"
authors:
    - "Arthur Van Camp"
event: "PhD Thesis at [Ghent University](https://www.ugent.be/)"
supervisor:
    - "Gert de Cooman"
    - "Enrique Miranda"
selected: false
note: ""
hdl: "1854/LU-8546928"
doi: ""
resources:
    - name: ".pdf"
      src: "AVC-PhD-dissertation-2018.pdf"
---

## Summary
This dissertation presents a study of choice functions as a tool to model uncertainty.
Choice functions constitute a very general uncertainty model that is capable of representing a rich variety of types of beliefs.
In particular, it includes as a special case _sets of desirable gambles_, the most general binary—or pairwise—choice model in imprecise probabilities.
So the field of this dissertation is `imprecise probabilities', which is an umbrella term for mathematical models that are meant to be used in situations of imprecise or incomplete information, where it may not be possible (or advisable) to use (precise) probabilities.
With our coherent choice functions, we want to be able to do everything that can be done within imprecise probabilities, such as conservative reasoning, updating and conditioning, and also to cope with structural judgements such as independence and exchangeability.

Suppose we have a subject whose beliefs we want to model.
A direct way of doing this, is by looking at the choices he makes between uncertain options.
Such choices can be captured by means of his choice function, which is a function that maps any set of options (also called _option set_) to the subset of those elements that are the chosen or preferred ones.
Equivalently, we can consider rejection functions instead of choice functions, which return the rejected (non-chosen) options from within any given option set.
Rejection functions are often easier and more intuitive to work with.

In order for a choice function to reflect rational behaviour, it needs to satisfy some rationality criteria.
Choice functions that satisfy them are called _coherent_.
The first thing we do in this dissertation, is identify a set of axioms that models rational behaviour, and is at the same time weak enough to allow for coherent choice functions to be sufficiently general and versatile.
The set of rationality axioms we consider, is based on Kadane et al.'s 2004 and Seidenfeld et al.'s 2007 account of coherent choice functions.
These authors introduce a theory of coherent choice functions that is capable of describing choices that are not necessarily determined by pairwise comparison.
Our resulting theory differs from Seidenfeld et al.'s 2007 in a number of respects.
First of all, mainly for technical reasons, we only consider _finite_ option sets, while Seidenfeld et al. 2007 also allow for possibly infinite but closed option sets.
Secondly, Seidenfeld et al. 2007 require that their choice functions should satisfy an Archimedean (continuity) axiom, which prevents them from having sets of desirable gambles as a special case.
As we are particularly interested in the connection with sets of desirable gambles, we omit their Archimedean axiom.
Furthermore, since their 'mixtures' or 'convexity' axiom is not compatible with Walley–Sen maximality [See Walley 1991 or Troffaes 2007] as a decision rule, we disregard 'convexity' as an axiom but merely regard it as an additional property that choice functions may or may not satisfy.
A final difference between Seidenfeld et al.'s 2007 approach and ours lies in the uncertain options on which the choice functions are defined.
While they use horse lotteries---which do not constitute a linear space---we use elements of an abstract pre-determined vector space as options.

As a first result, we show that under some mild conditions, the choice functions of Seidenfeld et al. 2007 can be embedded into our framework.
Since this connection is done through so-called _vector-valued gambles_ [See Zaffalon and Miranda 2017], every result we prove for coherent choice functions on vector-valued gambles can also be related to choice functions on horse lotteries that satisfy the corresponding rationality axioms.

In order to be able to _reason conservatively_ with choice functions, we introduce a partial order on them that has the interpretation of being `at most as informative as'.
The partially ordered set of all coherent choice functions forms a complete infimum-semilattice under this partial order: the infimum of any collection of coherent choice functions exists, and is itself coherent.
This is crucial: it is this property that allows for conservative reasoning with choice functions, at least in principle.
For instance, it allows us to consider the important device of _natural extension_: the unique least informative coherent extension of a partially specified choice function.
We characterise the circumstances under which the natural extension is coherent.
If it is—we say then that the partially specified choice function _avoids complete rejection_—we obtain an explicit expression for it.
The idea of natural extension has an important role in this dissertation.

Our motivation for using choice functions instead of sets of desirable gambles—which are those uncertain options that the subject strictly prefers to the status quo in a pairwise comparison—is that choice functions are versatile enough to represent choices that are not necessarily based on pairwise comparisons of the options only.
We relate both models (choice functions and sets of desirable gambles) to one another through a compatibility relation: an option *u* belongs to a set of desirable gambles if and only if the status quo represented by *0* is rejected from the option set *{0,u}* consisting of *u* and *0*.
Interestingly, given a coherent choice function, there is exactly one coherent set of desirable gambles that is compatible with it, but conversely, given a coherent set of desirable gambles, there are in general multiple compatible coherent choice functions.
This shows that choice functions are indeed more general than sets of desirable gambles.
We will illustrate this with a type of belief that can be modelled satisfactorily using choice functions, but not using sets of desirable gambles.

Seidenfeld et al.'s 2007 set of rationality axioms for choice allows for a representation theorem of coherent choice functions: every coherent choice function can be written as an infimum of (choice functions corresponding to) probability–utility pairs belonging to an arbitrary set.
This is a very powerful result, that immediately also shows that their maximal choice functions—the maximal elements of the partially ordered set of all coherent choice functions under the partial order of being 'at most as informative as'—are those that correspond to a single probability-utility pair.
Our axiomatisation does not allow for such a representation: we show by means of a counterexample that even restricting ourselves to the class of coherent choice functions that also satisfy the additional 'convexity' property considered in Seidenfeld 2007, does not suffice.

Once the basic properties of our coherent choice functions, and the natural extension of local assessments are in place, we move to the study of structural assessments.
By `structural' assessment, we mean an assessment about the general properties or structure of the choice function.
This contrasts with 'direct' or 'local' assessments, of which a partially specified choice function constitutes an example.
The first kind of structural assessment we study is that of _indifference_.
Consider a set of options _I_ that the subject assesses as being indifferent to the option that represents the status quo.
_I_ is then called the subject's set of indifferent options.
To be indifferent between two options means that these two options are considered to be equivalent to each other, in the sense that the subject is willing to swap one for another.
We introduce a compatibility relation between coherent choice functions and sets of indifferent options, and identify the least informative coherent choice function that is compatible with a given set of indifferent options.
As it turns out, choice functions that describe indifference are simpler, in the sense that they correspond to a unique representing choice function on a lower dimensional domain.
We connect our account of indifference with an earlier characterisation by Seidenfeld et al. 1990.

As mentioned, with our theory of choice we want to be able to deal with _conditioning or updating_.
If we have a choice function describing the subject's beliefs about an uncertain variable *X*, we need a procedure that takes new information such as '*X* assumes a value in the non-empty set *E*' into account.
Our proposed procedure for conditioning preserves coherence, and, due to the connection of our choice functions with sets of desirable gambles, it has no problems with conditioning on events of probability (in the set of probabilities associated with a choice function) zero.
We take this one step further and consider a multivariate context, where we have a finite number of uncertain variables assuming values in non-empty finite possibility spaces.
We introduce an obvious procedure for marginalisation—given a coherent choice function describing the subject's beliefs of a set of variables, how can we derive a choice function about a subset of them?—and some kind of inverse operation—given a coherent choice function describing the subject's beliefs of a set of variables, how can we extend it to a coherent choice function about a superset of variables, in a least informative manner?
Our previously introduced conditioning rule can be made to deal with a multivariate context.
Finally, we investigate another type of structural assessment: that of irrelevance, which is an asymmetric variant of independence.
We characterise choice functions that satisfy such assessments, and find the least informative coherent one, called the _irrelevant natural extension_.

This dissertation culminates in our study of _exchangeability_, where we find occasion to use most of the previously introduced concepts.
Exchangeability is a structural assessment about a sequence of variables that is important for statistical inference purposes.
Loosely speaking, making a judgement of exchangeability means that the order in which the variables are observed is not relevant.
We derive de Finetti-like representation theorems for finite exchangeable sequences.
We take also this one step further and consider a countable sequence of variables, for which we also find a de Finetti-like representation theorem.
We consider conditioning on observing a finite number of these variables, show that this conserves exchangeability, and show that counting occurrences provides a sufficient statistic for this type of inference.

We conclude by looking back at what has been achieved, and looking ahead at a number of interesting problems that still remain. 

## Promotors
Prof. dr. ir. Gert de Cooman

Prof. dr. Enrique Miranda

## Members of the examination board
prof. dr. Seamus Bradley

prof. dr. ir. Jasper De Bock (secretary)

prof. dr. Hennie De Schepper

prof. dr. Teddy Seidenfeld

prof. dr. ir. Luc Taerwe (chairman)

dr. ir. Lode Wylleman