---
layout: default
title: Introduction
---

<head>
  <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
</head>

<header>
<img src="../../../../microtubule.png" alt="" width="1000"
         height="200">
</header>
# Microtubule Catastrophe
#### Rashi Jeeda, Joeyta Banerjee, Mei Yi You | BE/Bi103a Fall 2020

$$\cdot \cdot \cdot$$

## Abstract
---
<br>
Microtubules, cellular filaments composed of monomeric tubulin subunits, play key roles in the cytoskeletal structure and internal organization of cells. They are known to undergo periods of growth and shortening; the conversion from growth to shortening consists of rapid repolymerization of tubulin known as catastrophe. The dynamics of catastrophe were measured by Gardner et. al. to explore how regulatory proteins modulate this process. We find that there is little difference in catastrophe dynamics for GFP-labeled tubulin and non-labeled tubulin, and conclude that an exponential model best describes catastrophe dynamics. We will discuss statistical methods used for the analysis of this data.

$$\cdot \cdot \cdot$$

## Experimental Design
---
### Does fluorescent protein tagging affect catastrophe dynamics?

The authors of Gardner et. al. were interested in measuring the time between the beginning of microtubule growth to the catastrophe event. In the experiment, microtubules were monitored through fluorescent labeling of tubulin, the monomeric subunit making up a microtubule. While fluorescence is an ideal activity marker because it is so easy to visualize, a consideration to be made is that fluorescent proteins are large beta-barrel proteins. It is thus possible that the presence of the fluorescent molecule could impact the dynamics of tubulin interactions in microtubule growth and catastrophe. In order to control for this possibility, the authors measured times to catastrophe using fluorescent labels as well as using differential interference contrast (DIC) microscopy. The microscopy served as a control to ensure that times to catastrophe were not significantly affected by the use of fluorescent markers and exposure to laser light. We visualize the times to catastrophe for both cases to see if there is a noticable difference. We include 95% confidence intervals to visualize the range of possible ECDFs for time to catastrophe for each case as determined from bootstrap replicates.

<center>$$\cdot$$</center>
<center>{% include label_comparison_ecdf.html %}</center>
<center>$$\cdot$$</center>
<center><b>Fig. 1</b>: ECDF of times to catastrophe for labeled (True) vs. unlabeled (False) tubulin.<br>
<b>example:</b> <a href="../../../../code/lol.py"><code>lol.py</code></a> | <b>code:</b> <a href="../../../../code/lol.py"><code>lol.py</code></a>  </center>
<center>$$\cdot$$</center>

It doesn't seem as though there is a significant difference in catastrophe times when we measure labeled tubulin as opposed to unlabeled tubulin.

### Hypothesis testing

To test the hypothesis of whether the distribution of catastrophe times for microtubules with labeled tubulin is the same as that for unlabeled tubulin, we will be taking boostrap replicates of to calculate the Kolmogrov Smirnov test statistic for the two samples. This will allow us to compute the p-value and evaluate our null hypothesis that the two datasets come from the same distribution.

We chose to use the Kolmogorov-Smirnov test because we wanted to see if the two datasets come from the same distribution. The Kolmogrov Smirnov test is a nonparametric test that tests the equality of distributions by quantifying the difference between the empirical distribution functions of two samples. Our test statistic uses
<br>
<center> $$D=  \textrm{max} 1≤i≤N(F(xi)−i−1N,iN−F(xi)),$$ </center>
<br>
where  $$F(x)$$  is the ECDF. This is an appropriate test statistic, since we want to compare both the spreads of the distribution and the maximum difference in their values.

The null hypothesis we are testing is as follows:

H0 : The distributions for the labeled tubulin and non-labeled tubulin are the same.

<center>$$\cdot$$</center>
<center>{% include label_comparison_intervals.html %}</center>
<center>$$\cdot$$</center>
<center><b>Fig. 2</b>: Confidence intervals for time to catastrophe derived from bootstrapping.<br>
<b>example:</b> <a href="../../../../code/lol.py"><code>lol.py</code></a> | <b>code:</b> <a href="../../../../code/lol.py"><code>lol.py</code></a>  </center>
<center>$$\cdot$$</center>


Since our p-value of  ∼0.8  is a rather large value, we fail to reject the null hypothesis that the distributions for labeled and non-labeled tubulin are the same, likely without ambiguity. A large p-value means that we get a test statistic as extreme as what we saw in the actual experiment many times.

<center>$$\cdot$$</center>
<center>{% include label_comparison_DKW.html %}</center>
<center>$$\cdot$$</center>
<center><b>Fig. 3</b>: Confidence intervals for time to catastrophe derived from DKW inequality.<br>
<b>example:</b> <a href="../../../../code/lol.py"><code>lol.py</code></a> | <b>code:</b> <a href="../../../../code/lol.py"><code>lol.py</code></a>  </center>
<center>$$\cdot$$</center>

$$\cdot \cdot \cdot$$

## Modeling the experiment
---
### Are the data Gamma distributed?

The authors of Gardner et. al. assume that the times to catastrophe were Gamma distributed. Taking a look at the handy <a href="https://distribution-explorer.github.io/">distribution explorer</a>, we can compare the story of microtubule growth to the story behind the Gamma distribution. The Gamma distribution is the amount of time we have to wait for n arrivals of a Poisson process. In this case, catastrophe is a multi-step process in which each sub-processes can be thought of as a Poisson process. So, the time for each sub-process to occur is exponentially distributed. The time you need to wait for all the multi-step processes to occur will then be Gamma distributed.

### An alternative hypothesis

Alternatively, we could consider that two biochemical processes have to happen in succession in order to trigger a catastrophe. We can model each of these processes as a Poisson process. The rate of arrivals, which corresponds biologically to the rate of the first biochemical process, is described by the variable $$\beta_1$$ while the other is described by $$\beta_2$$. In this successive Poisson model, note that the value of $$\beta_2$$ doesn't depend on the value of $$\beta_1$$. Each process happens at its own rate, but we only require that the second happens sometime after the first and that they together trigger catastrophe. To see if this model could potentially describe the catastrophe data, we generate random numbers sampled from the distribution. This allows us to simulate the story and see if it has the potential to match up with the true observations. For now, we choose various values of $$\beta_1$$ and $$\beta_2$$ by hand.

In order to simulate the successive Poisson process model, we will add the times generated by the second Poisson process to those generated by the first. This works because once we have sampled a time for the first process from the exponential distribution, it essentially becomes our new zero point when sampling for the time taken for the second process. Thus, the time taken to complete both procesesses will simply be the sum of the time of the first process and the time of the second process.

To be a bit more exact, we can analytically calculate the probability density function (PDF) of the distribution matching the story we told.
We find that the PDF simplifies to
<br>
<center>$$f(t) = \beta^2 te^{-\beta t}$$</center>
<br>


### Maximum likelihood estimation

In order to simulate catastrophe as one of the models we proposed, we need parameter values to plug into the PDF. We want to find the ideal parameters, which are the values that maximize the PDF. We define the log likelihood as the joint PDF. We want to find the set of parameters that maximizes this quantity. We do this with the help of scipy.

We do this for the Gamma distribution as well as the exponential distribution. As we can see from the ECDFs of times to catastrophe for the theoretical data, there is significant overlap with the experimental data. So, we will employ a bit more rigor to determine which model is better.

### Model comparison

We explored the question of which model was preferred by

<center>$$\cdot$$</center>
<center>{% include concentrations.html %}</center>
<center>$$\cdot$$</center>
<center><b>Fig. 3</b>: Times to catastrophe for various concentrations of tubulin. Presented as ECDF (left) and strip plot (right).<br>
<b>example:</b> <a href="../../../../code/lol.py"><code>lol.py</code></a> | <b>code:</b> <a href="../../../../code/lol.py"><code>lol.py</code></a>  </center>
<center>$$\cdot$$</center>

We also compare QQ plots of the two models.

<center>$$\cdot$$</center>
<center>{% include qq_plots.html %}</center>
<center>$$\cdot$$</center>
<center><b>Fig. 3</b>: Times to catastrophe for various concentrations of tubulin. Presented as ECDF (left) and strip plot (right).<br>
<b>example:</b> <a href="../../../../code/lol.py"><code>lol.py</code></a> | <b>code:</b> <a href="../../../../code/lol.py"><code>lol.py</code></a>  </center>
<center>$$\cdot$$</center>

We also generate predictive regression plots for each model.

<center>$$\cdot$$</center>
<center>{% include pred_reg.html %}</center>
<center>$$\cdot$$</center>
<center><b>Fig. 3</b>: Times to catastrophe for various concentrations of tubulin. Presented as ECDF (left) and strip plot (right).<br>
<b>example:</b> <a href="../../../../code/lol.py"><code>lol.py</code></a> | <b>code:</b> <a href="../../../../code/lol.py"><code>lol.py</code></a>  </center>
<center>$$\cdot$$</center>
