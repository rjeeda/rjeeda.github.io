---
layout: default
title: Introduction
---

<head>
  <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
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
Microtubules, cellular filaments composed of monomeric tubulin subunits, play key roles in the cytoskeletal structure and internal organization of cells. They are known to undergo periods of growth and shortening; the conversion from growth to shortening consists of rapid repolymerization of tubulin known as catastrophe. The dynamics of catastrophe were measured by Gardner et. al. to explore how regulatory proteins modulate this process.
<br>

We found that there is little difference in catastrophe dynamics for GFP-labeled tubulin and non-labeled tubulin, and conclude that an exponential model best describes catastrophe dynamics. Here, we discuss statistical methods used for the analysis of this data.

---
<br>

For each plot and analysis made, we include an <b>example</b> html Jupyter notebook with discussion of how we used our analysis package. The specific modules used for each plot are linked as <b>source code</b>. Full, executable notebooks of the tutorials can be found at the end of this page and the complete analysis package can be found in the GitHub repository.

---

$$\cdot \cdot \cdot$$

## Experimental Dynamics
---
### Does fluorescent protein tagging affect catastrophe dynamics?

The authors of Gardner et. al. were interested in measuring the time between the beginning of microtubule growth to the catastrophe event. In the experiment, microtubules were monitored through fluorescent labeling of tubulin, the monomeric subunit making up a microtubule. While fluorescence is an ideal activity marker because it is so easy to visualize, a consideration to be made is that fluorescent proteins are large beta-barrel proteins. For reference, the fluorescent molecule GFP is ~240 amino acids long, while tubulin is ~400 amino acids long.
<br>

Thus, it's possible that fluorescent molecules could impact the dynamics of tubulin interactions in microtubule growth and catastrophe. In order to control for this possibility, the authors measured times to catastrophe using fluorescent labels as well as using differential interference contrast (DIC) microscopy. The microscopy served as a control to ensure that times to catastrophe were not significantly affected by the use of fluorescent markers and exposure to laser light.
<br>

We visualized the times to catastrophe for both cases to see if there was a noticable difference. We included 95% confidence intervals to visualize the range of possible ECDFs for time to catastrophe for each case, as determined from bootstrap replicates.

<center>$$\cdot$$</center>
<center>{% include label_comparison_ecdf.html %}</center>
<center>$$\cdot$$</center>
<center><b>Fig. 1</b>: ECDF of times to catastrophe for labeled (True) vs. unlabeled (False) tubulin.<br>
<b>example:</b> <a href="../../../../code/MCAT_Tutorial_Part1.html"><code>tut1.html</code></a> | <b>source code:</b> <a href="../../../../MCAT_pkg/MCAT_pkg/bootstrapping.py"><code>bootstrapping.py</code></a>  </center>
<center>$$\cdot$$</center>

Due to the strong overlap, it didn't seem as though there was a significant difference in catastrophe times when considering labeled tubulin as opposed to unlabeled tubulin, at least by eye. However, we also explored further by computing confidence intervals for the plug in estimate of the mean.



<center>$$\cdot$$</center>
<center>{% include label_comparison_intervals.html %}</center>
<center>$$\cdot$$</center>
<center><b>Fig. 2</b>: Confidence intervals for time to catastrophe derived from bootstrapping.<br>
<b>example:</b> <a href="../../../../code/MCAT_Tutorial_Part1.html"><code>tut1.html</code></a> | <b>source code:</b> <a href="../../../../MCAT_pkg/MCAT_pkg/bootstrapping.py"><code>bootstrapping.py</code></a>  </center>
<center>$$\cdot$$</center>

There is also strong overlap in the confidence intervals, suggesting that the labeled and unlabeled tubulin have similar times to catastrophe. We also computed confidence intervals according to the DKW inequality.
<center>$$\cdot$$</center>
<center>{% include label_comparison_DKW.html %}</center>
<center>$$\cdot$$</center>
<center><b>Fig. 3</b>: Confidence intervals for time to catastrophe derived from DKW inequality.<br>
<b>example:</b> <a href="../../../../code/MCAT_Tutorial_Part1.html"><code>tut1.html</code></a> | <b>source code:</b> <a href="../../../../MCAT_pkg/MCAT_pkg/bootstrapping.py"><code>bootstrapping.py</code></a>  </center>
<center>$$\cdot$$</center>

This inequality acts as a bound for the confidence interval. We saw that our bootstrapping confidence intervals lie well within these bounds.


$$\cdot \cdot \cdot$$



### Hypothesis testing

To test whether the distribution of catastrophe times for microtubules with labeled tubulin is the same as that for unlabeled tubulin, we performed a hypothesis test by testing against the null hypothesis that there is no difference between the two datasets. For our analysis, we chose the Kolmogorov Smirnov test statistic, which compares two different distributions by providing a metric that combines differences in center and spread.

The null hypothesis we are testing is as follows:

<i>H0 : The distributions for the labeled tubulin and non-labeled tubulin are the same.</i>

We used bootstrapping to generate “trials” to compare to our test set, assuming that all sampled data sets come from the same generative distribution as the test set. By computing the test statistic for each of these and comparing it to the test statistic for our particular data set, we can obtain a p-value. The p-value represents the probability of getting a test statistic at least as extreme as the one in our sample when performing many trials or runs of the experiment. We obtained a p-value of 0.8, which means that the value of the KS test statistic for bootstrapped samples is as extreme as that for the actual experiment 80% of the time. This led us to conclude that we fail to reject the null hypothesis that there is no difference in the distribution of the two conditions.
<br>

<b>example:</b> <a href="../../../../code/MCAT_Tutorial_Part1.html"><code>tut1.py</code></a>

---
<br>

<b>So, all in all, it's pretty likely that the catastrophe times for labeled and unlabled tubulin come from the same generative distribution.</b>

<br>

$$\cdot \cdot \cdot$$


## Modeling the experiment
---
### Could the data be Gamma distributed?

The authors of Gardner et. al. assume that the times to catastrophe were Gamma distributed. Taking a look at the handy <a href="https://distribution-explorer.github.io/">distribution explorer</a>, we can compare the story of microtubule growth to the story behind the Gamma distribution. The Gamma distribution is the amount of time we have to wait for n arrivals of a Poisson process. In this case, catastrophe is a multi-step process in which each sub-processes can be thought of as a Poisson process. So, the time for each sub-process to occur is exponentially distributed. The time you need to wait for all the multi-step processes to occur will then be Gamma distributed. The number of arrivals is given by the parameter $$\alpha$$ while the time for all arrivals to occur is given by $$\beta$$. The PDF is given by

$$f(y; \alpha, \beta) = \frac{1}{\Gamma(\alpha)} \frac{(\beta y)^{\alpha}}{y}e^{-\beta y}$$


### An alternative hypothesis

Alternatively, we could consider that two biochemical processes have to happen in succession in order to trigger a catastrophe. We can model each of these processes as a Poisson process. The rate of arrivals, which corresponds biologically to the rate of the first biochemical process, is described by the variable $$\beta_1$$ while the other is described by $$\beta_2$$. In this successive Poisson model, note that the value of $$\beta_2$$ doesn't depend on the value of $$\beta_1$$. In order to simulate the successive Poisson process model, we will add the times generated by the second Poisson process to those generated by the first. This works because once we have sampled a time for the first process from the exponential distribution, it essentially becomes our new zero point when sampling for the time taken for the second process. Thus, the time taken to complete both processes will simply be the sum of the time of the first process and the time of the second process.

We can analytically calculate the probability density function (PDF) of the distribution matching the story we told.
We find that the PDF simplifies to
<br>
<center> $$f(t;\beta_1, \beta_2) = \frac{\beta_1 \beta_2}{\beta_2 - \beta_1} (e^{-\beta_1 t} - e^{-\beta_2 t})$$</center>
<br>

More detailed information about considerations we made when doing calculations for this model can be found in <a href="../../../../code/MCAT_Tutorial_Part2.html"><code>tut2.py</code></a>

### Maximum likelihood estimation

For each of these potential models (gamma and exponential), we need to determine the parameters that will allow the model to best fit our data. For the gamma distribution, this is ɑ and β, and for the exponential distribution, it is the two successive values of beta. We determine these estimates by maximizing the log likelihood for the parameters given our data set, which is the same as maximizing the likelihood but is computationally simpler. Rather than determining the parameters analytically, we generated estimates using bootstrapping by maximizing the log likelihood over multiple trials and averaging over the individual results.

With the parameters estimates gained from maximum likelihood estimation, we can generate data sets from the appropriate distribution using these parameters and compare the ECDF to the experimental ECDF to loosely estimate how well our model fits the data.


<center>$$\cdot$$</center>
<center>{% include MLE_comparison.html %}</center>
<center>$$\cdot$$</center>
<center><b>Fig. 4</b>: Experimental vs Theoretical ECDFs of Catastrophe Times. Experimental shown with interval; theoretical overlaid as line.<br>
<b>example:</b> <a href="../../../../code/MCAT_Tutorial_Part2.html"><code>tut2.py</code></a> | <b>source code:</b> <a href="../../../../MCAT_pkg/MCAT_pkg/MLE_analysis.py"><code>MLE_analysis.py</code></a>  </center>
<center>$$\cdot$$</center>

This can tell whether the model is reasonable, but does not necessarily give us enough information to determine which model is better.

$$\cdot \cdot \cdot$$

### Model comparison

We explored the question of which model was preferred by solely focusing on the data from the fluorescent tagged tubulin, since we found through hypothesis testing that there was not a significant difference between the two conditions. Within this experimental condition, the experimenters also repeated the process for multiple different concentrations of tubulin.


<center>$$\cdot$$</center>
<center>{% include concentrations.html %}</center>
<center>$$\cdot$$</center>
<center><b>Fig. 5</b>: Times to catastrophe for various concentrations of tubulin. Presented as ECDF (left) and strip plot (right).<br>
<b>example:</b> <a href="../../../../code/MCAT_Tutorial_Part2.html"><code>tut2.py</code></a> | <b>source code:</b> <a href="../../../../MCAT_pkg/MCAT_pkg/exploratory_analysis.py"><code>exploratory_analysis.py</code></a> </center>
<center>$$\cdot$$</center>


We used three different metrics to compare the two models. The first of these, the QQ plot, uses quantiles of the experimental dataset, overlaid with the theoretical results using our model, to visualize how well our models fit the data. If our model is mostly contained within the quantiles, that implies it is a good fit.


<center>$$\cdot$$</center>
<center>{% include qq_plots.html %}</center>
<center>$$\cdot$$</center>
<center><b>Fig. 6</b>: Q-Q plot for each theoretical model.<br>
<b>example:</b> <a href="../../../../code/MCAT_Tutorial_Part2.html"><code>tut2.py</code></a> | <b>source code:</b> <a href="../../../../MCAT_pkg/MCAT_pkg/model_assessment.py"><code>model_assessment.py</code></a> </center>
<center>$$\cdot$$</center>

We also generate predictive regression plots for each model. Predictive ECDFs overlay the results of the experimental ECDF with the results we would get using each of our models. The two curves should be aligned very closely if the model fits the data.

<center>$$\cdot$$</center>
<center>{% include pred_reg.html %}</center>
<center>$$\cdot$$</center>
<center><b>Fig. 7</b>: Predictive ECDFs for each theoretical model.<br>
<b>example:</b> <a href="../../../../code/MCAT_Tutorial_Part2.html"><code>tut2.py</code></a> | <b>source code:</b> <a href="../../../../MCAT_pkg/MCAT_pkg/model_assessment.py"><code>model_assessment.py</code></a> </center>
<center>$$\cdot$$</center>

For a more quantitative metric, we also calculated the Akaike Information Criterion for each of our datasets, which is found using the log likelihood value for the parameters. This criterion can loosely be interpreted as a distance metric between the theoretical and empirical distributions, so a smaller value implies a better fit. The AIC can be calculated as

$$\text{AIC} = -2\ell(\theta^*;\text{data}) + 2p$$

for a set of parameters $$\theta$$ with MLE $$\theta^*$$ and a model with log-likelihood $$\ell(\theta;\text{data})$$, where $$p$$ is the number of free parameters.

For the exponential distribution, we found that AIC = 9327.39, and for the gamma distribution, AIC = 9278.35.

<b>example:</b> <a href="../../../../code/MCAT_Tutorial_Part2.html"><code>tut2.py</code></a>

---
<br>

<b>Based on this calculation, and the plots above, we found that the gamma distribution model is closer than the exponential distribution model to the experimental results.</b>

$$\cdot \cdot \cdot$$


## Data and Code
---
<br>

- The data sets for the analyses shown above can be downloaded at the following links:
<br>
<a href="https://s3.amazonaws.com/bebi103.caltech.edu/data/gardner_time_to_catastrophe_dic_tidy.csv">Times to Catastrophe for Labeled and Unlabeled Tubulin</a>
<br>
<a href="https://s3.amazonaws.com/bebi103.caltech.edu/data/gardner_mt_catastrophe_only_tubulin.csv">Times to Catastrophe for Various Concentrations of Tubulin</a>

- A walkthrough of the analysis shown above is available in two parts in the following Jupyter notebooks, along with tips and examples for using the package created for the analysis pipeline.
<br>
<a href="../../../../code/MCAT_Tutorial_Part1.html"><code>MCAT_Tutorial_Part1.html</code></a> | <a href="../../../../code/MCAT_Tutorial_Part1.ipynb"><code>MCAT_Tutorial_Part1.ipynb</code></a> (Experimental Dynamics)
<br>
<a href="../../../../code/MCAT_Tutorial_Part1.html"><code>MCAT_Tutorial_Part1.html</code></a> | <a href="../../../../code/MCAT_Tutorial_Part2.ipynb"><code>MCAT_Tutorial_Part2.ipynb</code></a> (Modeling Catastrophe)

- The analysis package can be downloaded here:
<br>
<a href="../../../../MCAT_pkg"><code>MCAT_pkg</code></a>

- The original paper can be found here:
<br>
<a href="https://www.cell.com/cell/fulltext/S0092-8674(11)01287-6?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS0092867411012876%3Fshowall%3Dtrue">Gardner et. al. 2011</a>

- All other code and figures shown above can be found in the GitHub repository for this website:
<br>
<a href="https://github.com/rjeeda/rjeeda.github.io">GitHub</a>

$$\cdot \cdot \cdot$$



## Acknowledgements
---
<br>

We thank the publishers of Gardner et. al. for sharing their data, the BeBi103 TA's for their guidance, the makers of Poole for this website template, <a href="https://github.com/atisor73">Rosita Fu</a> and <a href="https://github.com/gchure">Griffin Chure</a> for design inspiration, and of course, <a href="https://github.com/justinbois">Justin Bois</a> for his assistance, insight, and useful code!

Website header generated using <a href="https://ccsb.scripps.edu/cellpaint/">CellPAINT 2.0.</a>
