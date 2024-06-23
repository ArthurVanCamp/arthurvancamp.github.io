---
date: "2014-09-01T00:00:00"
math: false
title: "Robustifying the Viterbi algorithm"
authors:
    - "Cedric De Boom"
    - "Jasper De Bock"
    - "Arthur Van Camp"
    - "Gert de Cooman"
event_pre: "the"
event: "Lecture Notes in Computer Science, Volume 8754"
event_short: "PGM 2014"
event_link: "http://www.projects.science.uu.nl/PGM/"
pages: "160 – 175"
note: ""
hdl: "1854/LU-5743565"
doi: "10.1007/978-3-319-11433-0_11"
ext_link: "https://link.springer.com/chapter/10.1007/978-3-319-11433-0_11"
resources:
    - name: ".pdf"
      src: "CDB-PGM2014-paper.pdf"
    - name: "slides"
      src: "CDB-PGM2014-slides.pdf"
---

## Abstract
We present an efficient algorithm for estimating hidden state sequences in imprecise hidden Markov models (iHMMs), based on observed output sequences.
The main difference with classical HMMs is that the local models of an iHMM are not represented by a single mass function, but rather by a set of mass functions.
We consider as estimates for the hidden state sequence those sequences that are maximal.
In this way, we generalise the problem of finding a state sequence with highest posterior probability, as is commonly considered in HMMs, and solved efficiently by the Viterbi algorithm.
An important feature of our approach is that there may be multiple maximal state sequences, typically for iHMMs that are highly imprecise.
We show experimentally that the time complexity of our algorithm tends to be linear in this number of maximal sequences, and investigate how this number depends on the local models.