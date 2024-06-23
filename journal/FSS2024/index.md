---
date: "2024-04-15T00:00:00"
math: false
title: "Inferring from an imprecise Plackett–Luce model: Application to label ranking"
authors:
    - "Loïc Adam"
    - "Arthur Van Camp"
    - "Sébastien Destercke"
    - "Benjamin Quost"
journal: "[Fuzzy Sets and Systems](https://www.sciencedirect.com/journal/fuzzy-sets-and-systems)"
volume: "482"
beginpage: "tbd"
endpage: "tbd"
note: ""
doi: "10.1016/j.fss.2024.108908"
ext_link:
resources:
    - name: ".pdf"
      src: "LA-FSS2024-paper.pdf"
---

## Abstract
The Plackett–Luce model is a popular parametric probabilistic model to define distributions between rankings of objects, modelling for instance observed preferences of users or ranked performances of algorithms.
Since such observations may be scarce (users may provide partial preferences, or not all algorithms are run for a given experiment), it may be useful to consider the case where the parameters of the Plackett–Luce model are imprecisely known.
In this paper, we first introduce the imprecise Plackett–Luce model, induced by a set of parameters (for instance, parameters with a high relative likelihood).
Given a set of possible parameters for the model, we then provide an efficient algorithm to make cautious inferences, returning sets of possible optimal rankings (for instance in the form of partial orders).
We illustrate the use of our imprecise model on label ranking, a specific kind of supervised learning.