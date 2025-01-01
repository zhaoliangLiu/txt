578 IEEE TRANSACTIONS ON EVOLUTIONARY COMPUTATION, VOL. 22, NO. 4, AUGUST 2018
A Level-Based Learning Swarm Optimizer
for Large-Scale Optimization
Qiang Yang, Student Member, IEEE , Wei-Neng Chen, Senior Member, IEEE , Jeremiah Da Deng, Member, IEEE ,
Yun Li, Senior Member, IEEE , Tianlong Gu, and Jun Zhang, Fellow, IEEE
Abstract —In pedagogy, teachers usually separate mixed-level
students into different levels, treat them differently and teachthem in accordance with their cognitive and learning abilities.Inspired from this idea, we consider particles in the swarm asmixed-level students and propose a level-based learning swarmoptimizer (LLSO) to settle large-scale optimization, which is stillconsiderably challenging in evolutionary computation. At ﬁrst, alevel-based learning strategy is introduced, which separates par-ticles into a number of levels according to their ﬁtness valuesand treats particles in different levels differently. Then, a newexemplar selection strategy is designed to randomly select twopredominant particles from two different higher levels in the cur-
rent swarm to guide the learning of particles. The cooperation
between these two strategies could afford great diversity enhance-ment for the optimizer. Further, the exploration and exploitationabilities of the optimizer are analyzed both theoretically andempirically in comparison with two popular particle swarmoptimizers. Extensive comparisons with several state-of-the-artalgorithms on two widely used sets of large-scale benchmarkfunctions conﬁrm the competitive performance of the proposedoptimizer in both solution quality and computational efﬁciency.Finally, comparison experiments on problems with dimension-ality increasing from 200 to 2000 further substantiate the goodscalability of the developed optimizer.
Index Terms —Exemplar selection, high-dimensional prob-
lems, large-scale optimization, level-based learning swarm opti-mizer (LLSO), particle swarm optimization (PSO).
Manuscript received December 2, 2016; revised March 14, 2017, May 30,
2017, and August 3, 2017; accepted August 14, 2017. Date of publication
September 5, 2017; date of current version July 27, 2018. This work wassupported in part by the National Natural Science Foundation of China underGrant 61622206, Grant 61379061, and Grant 61332002, in part by the Natural
Science Foundation of Guangdong under Grant 2015A030306024, in part by
the Guangdong Special Support Program under Grant 2014TQ01X550, and inpart by the Guangzhou Pearl River New Star of Science and Technology under
Grant 201506010002. (Corresponding authors: Wei-Neng Chen; Jun Zhang.)
Q. Yang is with the School of Computer Science and Engineering,
South China University of Technology, Guangzhou 510006, China, and alsowith the School of Data and Computer Science, Sun Yat-sen University,
Guangzhou 510006, China.
W.-N. Chen and J. Zhang are with the School of Computer Science and
Engineering, South China University of Technology, Guangzhou 510006,China (e-mail: cwnraul634@aliyun.com ;junzhang@ieee.org ).
J. D. Deng is with the Department of Information Science, University of
Otago, Dunedin 9054, New Zealand.
Y . Li is with the School of Computer Science and Network Security,
Dongguan University of Technology, Dongguan 523808, China.
T. Gu is with the School of Computer Science and Engineering, Guilin
University of Electronic Technology, Guilin 541004, China.
This paper has supplementary downloadable multimedia material available
athttp://ieeexplore .ieee.orgprovided by the authors. This consists of a PDF
ﬁle containing relevant material not included within the paper itself. This
material is 4.07 MB in size.
Color versions of one or more of the ﬁgures in this paper are available
online at http://ieeexplore .ieee.org.
Digital Object Identiﬁer 10.1109/TEVC.2017.2743016I. I NTRODUCTION
PARTICLE swarm optimization (PSO) has been exten-
sively researched and also has been widely applied to
solve real-world problems [ 1]–[4], since it was ﬁrst proposed
by Eberhart and Kennedy [ 5] and Kennedy and Eberhart [ 6].
Imitating the swarm behaviors of social animals, such as
bird ﬂocking, particles in the swarm traverse the whole solu-
tion space to ﬁnd the global optimum of the problem to beoptimized.
Speciﬁcally, each particle in the swarm represents a candi-
date solution and is denoted by two attributes: position and
velocity, which are updated as
v
d
i←wvd
i+c1r1/parenleftBig
pbestd
i−xd
i/parenrightBig
+c2r2/parenleftBig
nbestd
i−xd
i/parenrightBig
(1)
xd
i←xd
i+vd
i (2)
where Xi= [x1
i,..., xd
i,..., xD
i] and Vi=
[v1
i,..., vd
i,..., vD
i] are the position vector and
the velocity vector of the ith particle, respectively.
pbesti=[pbest1
i,..., pbestd
i,..., pbestD
i] is its personal
best position and nbest i=[nbest1
i,..., nbestd
i,..., nbestD
i]
is the best position of its neighbors, which are determined
by the adopted topology [ 7], [8]. As for the parameters, D
is the dimension size, wis termed as the inertia weight [ 9],
c1and c2are two acceleration coefﬁcients [ 5], and r1
as well as r2is uniformly randomized within [0 ,1].
Kennedy and Eberhart [ 6] considered the second part and the
third part in the right of ( 1) as the cognitive component and
the social component, respectively.
By means of ( 1), one particle in the swarm learns from
its own experienced knowledge and the social knowledge to
traverse the search space to seek the global optimum of theoptimized problem. However, researchers found that the above
learning strategy is not an efﬁcient way to tackle compli-
cated multimodal problems, because this strategy easily leadsto stagnation or premature convergence [ 10].
To further improve the efﬁcacy of PSO in handling com-
plicated problems, many researchers sought inspirations fromnature and human society and have proposed an ocean of novel
learning or updating strategies for PSO [ 11]–[17]. To name
a few, enlightened from the social learning in animal society,an incremental social learning strategy was put forward in [ 12]
by adopting a population size increasing approach; inspired by
the phenomenon that the interactive learning behavior takesplace among different groups in human society, Qin et al. [16]
developed an interswarm interactive learning strategy, where
1089-778X c/circlecopyrt2017 IEEE. Translations and content mining are permitted for academic research only. Personal use is also permitted, but republication/
redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.YANG et al. : LLSO FOR LARGE-SCALE OPTIMIZATION 579
two swarms dynamically learn from each other when stag-
nation is detected; inspired from the orthogonal experimentaldesign, an orthogonal learning PSO [ 13] was designed by con-
ducting orthogonal experimental design on pbest and gbest
(ornbest ) to obtain more efﬁcient exemplars for particles.
In addition, Liang et al. [11] developed a comprehensive
learning PSO (CLPSO) and further Lynn and Suganthan [ 18]
devised heterogeneous CLPSO to enhance the exploration andexploitation of CLPSO.
Although these PSO variants show better performance
than the classical PSO, they remain effective only inlow-dimensional space. When encountering high-dimensional
problems, their performance deteriorate drastically [ 19]–[22].
This phenomenon is usually a result of “the curse of dimen-
sionality” [ 20]. On the one hand, as the dimension size grows,
the search space increases exponentially. Such huge and widespace greatly challenges the search efﬁciency of the current
PSO variants [ 21], [23]. On the other hand, increasing dimen-
sionality may also bring in the explosively increased numberof local optima surrounded by capacious local areas, which
is especially common for large-scale multimodal problems.
Such phenomenon may give rise to great chance of prematureconvergence. Therefore, to solve high-dimensional problems
effectively, high diversity preservation is highly required for
EAs to escape from local traps.
Taking inspirations from nature and human society as well,
some researchers have proposed novel learning strategies for
PSO [ 21], [23], [24] to deal with large-scale optimization.
Generally, these PSO variants can preserve higher diversity
than the former PSO variants [ 11]–[16]. For consistency, they
will be elucidated in detail in the following section. Although
these PSO variants are promising for large-scale optimization,
premature convergence is still the main challenge.
To solve large-scale optimization problems more efﬁciently,
this paper proposes a level-based learning (LL) swarm opti-
mizer (LLSO) based on two motivations.
First, in education, it is common that different students
have different cognitive or learning abilities, and thus teach-
ers should treat their students differently in accordance withtheir aptitude [ 25], [26]. In particular, in the mixed-level learn-
ing methodology which has been widely used in education
practice [ 25], [26], it is suggested that students should be
grouped into different levels with tiered teaching and learn-
ing methods. Similarly, in one swarm, particles are usually in
different evolution states, and particles in different states gen-erally have different potential in exploring and exploiting the
search space. Thus, they should be treated differently as well.
Inspired from this, a LL strategy is introduced into LLSO,which groups particles into different levels based on their
ﬁtness values and treats those in different levels differently.
Second, instead of using the historically best positions (such
aspbest ,gbest ,o rnbest ) to update particles, two popular and
recent PSO variants, competitive swarm optimizer (CSO) [ 23]
and SL-PSO [ 21], directly adopt predominant particles in the
current swarm to guide the learning of particles. Since parti-
cles in the swarm are generally updated in each generation,the diversity of these two optimizers is greatly promoted and
thus they show good performance in dealing with large-scaleoptimization. However, these two optimizers utilize only one
predominant particle to replace one exemplar in (
1) to guide
the learning of particles, while the other exemplar is the mean
position of the swarm, which is shared by all particles and
thus is not beneﬁcial for further diversity enhancement. In thedeveloped LL strategy, since particles in different levels have
diverse potential in exploration and exploitation, they possess
diverse evolutionary information to evolve the swarm and thuscould be utilized as candidates to, respectively, replace the two
exemplars in ( 1) to direct the learning of particles. To this
end, a new exemplar selection method is incorporated into thelearning strategy, which ﬁrst randomly selects two different
higher levels and then selects one exemplar from each level,
so that two diverse predominant particles in the swarm could
be selected to guide the learning of particles. In this way, the
search diversity is likely promoted.
Together, the proposed LLSO directly utilizes two predom-
inant particles in the current swarm to guide the learning of
particles. In this manner, this learning strategy can enhance thediversity of the swarm. In particular, it can compromise explo-
ration and exploitation to search the space in two levels: 1) the
particle level and 2) the swarm level. In the particle level,one particle can enhance its potential in exploiting the space
by learning from the superior one between the two selected
exemplars and consolidate its potential in exploring the spacevia learning from the relatively inferior one. In the swarm
level, particles in different levels have different numbers of
exemplars in higher levels to learn from, resulting in thatparticles in lower levels focus on exploring the space, while
those in higher levels concentrate on exploiting the space. The
exploration and exploitation abilities of LLSO are both ana-
lyzed theoretically and veriﬁed empirically in comparison with
GPSO [ 6] and CSO [ 23].
To verify the efﬁciency and effectiveness of LLSO, exten-
sive experiments are conducted by comparing LLSO with sev-
eral state-of-the-art large-scale algorithms on CEC’2010 [ 27]
and CEC’2013 [ 28] large-scale benchmark sets. Furthermore,
experiments on the CEC’2010 [ 27] benchmark problems with
dimensionality increasing from 200 to 2000 are performed totestify the scalability of LLSO.
The rest of this paper is organized as follows. Various
related EAs dealing with large-scale optimization are reviewedin Section II. Section III elucidates the whole frame-
work of LLSO in detail, following which is the theoretical
analysis about its exploration and exploitation abilities inSection IV . Then, extensive experiments are conducted in
Section V to verify the effectiveness, efﬁciency, and good scal-
ability of LLSO. Finally, the conclusion and discussion aregiven in Section VI.
II. R
ELATED WORK ON LARGE -SCALE
OPTIMIZATION
Without loss of generality, in this paper, we consider the
minimization problems deﬁned as follows:
minf(X),X=/bracketleftBig
x1,x2,..., xD/bracketrightBig
(3)580 IEEE TRANSACTIONS ON EVOLUTIONARY COMPUTATION, VOL. 22, NO. 4, AUGUST 2018
where Dis the number of variables to be optimized. In addi-
tion, the function value is taken as the ﬁtness value of eachparticle.
With Dincreasing, the above deﬁned problem becomes
more and more difﬁcult to optimize, because on the onehand, the search space is exponentially increased; on the other
hand, the number of local optima surrounded by wide local
areas may be also explosively increased [ 20], [21], [23], espe-
cially for multimodal problems [ 29], [30]. So far, to locate
the global optima of high-dimensional problems efﬁciently,
researchers attempted to seek solutions from two perspectives:1) proposing cooperative coevolutionay algorithms (CCEAs),
which divide the whole decision vector into several groups and
evolve each variable group separately and 2) proposing novel
updating strategies for traditional EAs, which evolve all vari-
ables as a whole and preserve high diversity to escape fromlocal areas.
A. Cooperative Coevolutionary Algorithms
Since Potter [ 31] proposed the cooperative coevolution (CC)
framework, which adopts the divide-and-conquer techniqueto decompose problems into smaller subproblems, vari-
ous CCEAs have come into being by combining CC
with different EAs, such as cooperative coevolutionaryPSO (CCPSO) [ 32], [33], and cooperative coevolutionary
DE (DECC) [ 34].
Van den Bergh and Engelbrecht [ 32] ﬁrst combined CC
with PSO and proposed CCPSO- S
K, which randomly divides
the whole decision vector into D/Ksubcomponents with each
containing Kvariables and then utilizes the canonical PSO to
separately optimize each subcomponent. Following CCPSO-
SK, they further developed CCPSO- HK, where the classical
PSO and CCPSO- SKupdate the swarm in an alternative man-
ner. However, for different problems, the optimal number of
subcomponents is usually different. To ameliorate this issue,Li and Yao [ 33] proposed CCPSO2 by designing a group size
pool, which contains different group sizes.
Since in CCEAs, each variable group is individually opti-
mized, the interdependent variables should be placed into the
same group and optimized simultaneously [ 20]. This indicates
that the decomposition strategy is the most crucial componentfor CCEAs to achieve good performance. As a consequence,
the research on CCEAs mainly concentrates on devising
a good decomposition strategy and thus, many decomposi-tion strategies have shown up [ 20], [35]–[38]. Among these
strategies, differential grouping (DG) [ 20] and its variants,
XDG [ 37] and GDG [ 38] are the most popular ones because
they can detect variable dependency and thus can separate
variables into groups more accurately.
Though CCEAs are promising for large-scale optimization,
they encounter two limitations, which restrict their wide appli-
cation. For one thing, the performance of CCEAs seriouslyrelies on the decomposition strategy, and to detect the interde-
pendency among variables, a good decomposer usually con-
sumes a large number of function evaluations [ 20], [37], [38].
For another, a good CCEA usually costs plenty of function
evaluations, particularly when the number of variable groupsis large. This is because not only the adopted decomposition
strategy consumes a large number of function evaluations, butalso the optimization process consumes a lot of function eval-
uations to evolve variables so that satisfactory performance
can be obtained.
B. Novel Learning or Updating Strategies for EAs
From the other perspective, some researchers are devoted
to developing new learning or updating strategies, which can
preserve high diversity, to aid traditional EAs to cope with
large-scale optimization problems.
Liang and Suganthan [ 39] proposed a dynamic multiswarm
PSO, where the swarm is randomly divided into multiple small
subswarms and then the local version PSO [ 40] is utilized
to evolve each subswarm. Enlightened from the competitionin human society, Cheng and Jin [ 23] and Cheng et al. [41]
developed a novel competitive learning strategy. First, they
applied this strategy into a multiswarm PSO [ 41], where pair-
wise competition is performed between two particles randomly
selected from two swarms. After the competition, the loser
is updated by a convergence strategy, while the winner isupdated through a mutation strategy. Subsequently, they intro-
duced a CSO [ 23], where the pairwise competition is executed
among particles in a single swarm, and only the loser inone competition is updated, while the winner enters the next
generation directly. Speciﬁcally, the loser is updated as
v
d
l←r1vd
l+r2/parenleftBig
xd
w−xd
l/parenrightBig
+φr3/parenleftBig
¯xd−xd
l/parenrightBig
(4)
xd
l←xd
l+vd
l (5)
where Xl=[x1
l,..., xd
l,...xD
l] and Vl=[v1
l,..., vd
l,...vD
l]
are the position and speed of the loser, respectively; Xw=
[x1
w,..., xd
w,...xD
w] is the position of the winner; x=
[x1,..., xd,...xD] is the mean position of the swarm, r1,r2,
andr3are three random variables within [0 ,1],andφis one
parameter controlling the inﬂuence of x.
Inspired from the social learning behavior among social ani-
mals, a social learning PSO (SL-PSO) [ 21] was developed. In
this algorithm, all particles are sorted according to their ﬁtness
values and then for each particle, the ﬁrst exemplar in ( 1)i s
randomly selected from all better particles, while the secondexemplar is also the mean position of the whole swarm as CSO
displayed in ( 4). Taking further observation on SL-PSO and
CSO, we ﬁnd that these two optimizers neither utilize pbest
norgbest (ornbest ) to guide the learning of particles. Instead,
they directly adopt predominant particles in the current swarm
and the mean position of the swarm to lead particles to ﬁndthe global optima.
In addition, taking advantage of the invasive weed opti-
mization algorithm [ 42] and the quantum-behaved PSO
algorithm [ 43], Lian et al. [44] developed a quantum-behaved
invasive weed optimization algorithm, which correspondinglyadjusts and improves the quantum models of these two
algorithms.
Except for PSO variants in handling large-scale optimiza-
tion, many other EA variants were also developed. Since too
many works exist, we cannot review them all. Here, to saveYANG et al. : LLSO FOR LARGE-SCALE OPTIMIZATION 581
space, we only list some typical and recent works on large-
scale optimization. For a comprehensive review of large-scaleoptimizers, readers can refer to [ 22] and [ 45].
Hansen and Ostermeier [ 46] proposed an algorithm named
CMA-ES, which makes use of adaptive mutation parametersthrough computing a covariance matrix and correlated step
sizes in all dimensions to preserve high diversity. Although it
is promising for high-dimensional problems, it is very time-consuming owing to the computation of the covariance matrix
with time complexity O(D
2), where Dis the dimension size. To
relieve the high-computational burden, its variant called sep-CMA-ES [ 47] came up, which only computes the diagonal
elements of the covariance matrix, leading to the reduction of
complexity from O(D
2)t oO(D).
Subsequently, Molina et al. [48] proposed a memetic algo-
rithm named MA-SW-Chains, which combines a steady-stateGA with a local search method. LaTorre et al. [49], [50]
developed a multiple offspring generation framework, named
MOS, via hybridizing different algorithms to deal with differ-ent large-scale optimization problems. Brest and Mauèec [ 51]
developed a self-adaptive DE named jDElscop to solve large-
scale problems, which employs three mutation strategies anda population size reduction mechanism to evolve the popula-
tion. Zhao et al. [52] proposed another self-adaptive DE called
SaDE-modiﬁed multitrajectory search (MMTS) by hybridizingthe mutation strategy in JADE [ 53] with an MMTS algorithm.
Then, Ali et al. [54] introduced a multipopulation DE called
mDE-bES to tackle large-scale optimization. In this algo-rithm, the population is divided into independent subgroups,
and different subgroups are evolved with different mutation
strategies.
Even though numerious works exist in dealing with large-
scale optimization, falling into local optima and permatureconvergence are still the main challenges in large-scale opti-
mizaiton. In this paper, we propose an LLSO to try to alleviate
the above issue.
III. L
EVEL -BASED LEARNING SWARM OPTIMIZER
A. Motivation
When the dimension size Dbecomes larger and larger (more
than 500 [ 23]), optimization problems become more and more
difﬁcult to optimize. On the one hand, with Dincreasing, the
computational complexity of the problem becomes higher and
higher and the search space of the problem also increases
exponentially, which takes an optimizer a larger number of ﬁt-ness evaluations to locate the optima [ 21], [23]. On the other
hand, for high-dimensional multimodal problems, the number
of local optima is generally explosively increased and it islikely that these local optima are surrounded by wide local
areas, which may easily cause local traps or premature con-
vergence for optimizers [ 22], [45]. Thus, to tackle this kind of
problems efﬁciently, an optimizer is especially required to pre-
serve high diversity, so that local traps can be avoided. At the
same time, fast convergence is also a necessity for the opti-mizer, so that with limited resources, such as the restricted
number of ﬁtness evaluations, the global optimum can be fast
located. However, these two requirements conﬂict with eachother [ 23], [55]. As a consequence, a good optimizer should
make a good compromise between these two aspects to fasttraverse the search space.
In order to ﬁgure out an effective learning strategy, we seek
inspirations from nature and human society. In particular, inpedagogy, different students generally have different cogni-
tive or learning abilities, and thus teachers should treat these
students differently in accordance of their aptitude [ 25], [26].
In particular, in the mixed-level learning methodology which
has been widely used in education practice [ 25], [26], students
should be grouped into different levels with tiered teaching andlearning methods. Similarly, during the evolution, particles are
usually in different evolution states and have different poten-
tial in exploring and exploiting the search space. Thus, they
should be treated differently as well.
Moreover, taking close observation on SL-
PSO [ 21] and CSO [ 23], we ﬁnd that these two optimizers
neither utilize pbest norgbest (ornbest ) to guide the learning
of particles. Instead, they directly adopt predominant particlesin the current swarm to update particles and show good
potential in dealing with high-dimensional problems due to
the enhanced diversity. However, these two optimizers utilizeonly one predominant particle to replace one exemplar in ( 1)
to guide the learning of particles, while the other exemplar
is the mean position of the swarm, which is shared byall particles and thus is not beneﬁcial for further diversity
enhancement. Since particles in different evolution states pos-
sess diverse potential in exploring and exploiting the searchspace, they could own diverse evolutionary information to
guide the swarm to seek the optima and thus could be utilized
as candidates to replace the two exemplars in ( 1) to update
the swarm, so that the diversity could be further enhanced.
Motivated by the above phenomenon and observation, we
propose a LL strategy for PSO, leading to LLSO, which sep-
arates particles into different levels, treats them differently
and utilizes two predominant particles in the current swarmto guide the learning of particles to ﬁnd the global optima.
Accompanying with this learning strategy, a new exemplar
selection method is also developed to aid LLSO. The concreteelucidation of each component is presented as follows.
B. Level-Based Learning
During the evolution, particles are usually in different evo-
lution states, and have different potential in exploring and
exploiting the search space. To tell them apart, we ﬁrst par-
tition particles into different levels according to their ﬁtnessvalues.
Assume that NP particles are divided into NL levels with
each level denoted by L
i(1≤i≤NL). Before the partition,
particles in the swarm are ﬁrst sorted in ascending order of
ﬁtness as in SL-PSO [ 21]. Then, better particles belong to
higher levels and the higher the level is, the smaller level index
it has. So, L1is the highest level, and LNLis the lowest level.
To make it simple, we assume that all levels have the samenumber of particles. This number is called “level size” and
denoted by LS. Clearly, LS =NP/NL.
1
1Note that the whole swarm may not be equally partitioned by NP/NL. In
this situation, we just add the NP%NL particles into the lowest level.582 IEEE TRANSACTIONS ON EVOLUTIONARY COMPUTATION, VOL. 22, NO. 4, AUGUST 2018
Fig. 1. Framework of the LL strategy. First, particles in the swarm are sorted
in ascending order of ﬁtness and then they are equally partitioned into fourlevels ( L
1–L4). Then, particles in L4learn from those in L1–L3, particles in
L3learn from those in L1andL2, and particles in L2learn from those in L1.
It should be noticed that in order to protect the most promising particles frombeing wrongly updated, particles in L
1are not updated and directly enter the
next generation.
Subsequently, we take deep insight into particles in dif-
ferent levels. On the one hand, more promising positions
usually can be found around better particles in the currentswarm [ 21], [23], [56]. In other words, particles in higher lev-
els usually hold more beneﬁcial information to guide the
swarm toward the global optimum area. Consequently, par-ticles in higher levels should guide those in lower levels to
search the whole solution space, so that fast convergence can
be achieved and promising positions can be located. This isthe ﬁrst idea behind the LL strategy.
On the other hand, observing particles in different higher
levels, we ﬁnd that the higher the level that a particle belongsto, the more likely the particle may be close to the global opti-
mum area. That is, particles in different levels have different
strength in exploitation. Likewise, particles in different levelshave different strength in exploration. In general, exploration
and exploitation are in the opposite direction [ 21]. In other
words, particles having more potential in exploitation usually
have less potential in exploration, and vice versa. So a parti-
cle from a lower level should learn from those from differenthigher levels to make a compromise between exploration and
exploitation. This is the second idea behind the LL strategy.
Combining the above two together, the framework of LL is
displayed in Fig. 1. From this ﬁgure, we can see that particles
in lower levels can potentially learn from all those in higher
levels, and the number of candidate exemplars for particles indifferent levels is different. Speciﬁcally, as the level that a par-
ticle belongs to goes higher, this particle has fewer particles
in the higher levels in total to learn from, which matches theexpectation that better particles should do more exploitation
rather than exploration.
Overall, this level-based mechanism may encourage more
exploration among particles in lower levels and more exploita-
tion among those in higher levels. The effectiveness of the LL
strategy will be further reinforced by the random selection
mechanism for exemplars to be presented next.
C. Exemplar Selection
Besides the learning strategy, another key component for
PSO is the exemplar selection strategy. As aforementioned,
particles in different levels perform different roles in theevolution process. Generally, superior particles show more
potential in exploitation, so they should be used to guide thesearch direction. While for inferior particles, even though they
perform relatively badly in exploiting, they usually show more
potential in exploring more directions and larger space, whichis potentially proﬁtable for dragging particles away from local
areas. Enlightened by these, we propose a new exemplar selec-
tion method to select two different exemplars to replace pbest
andnbest in (1) to update particles.
To utilize the property that particles in different levels have
different strength in exploration and exploitation, we alloweach particle in level L
ito learn from two particles Xrl1,k1
andXrl2,k2randomly selected from two different higher levels
Lrl1and Lrl2, respectively, where rl1and rl2are randomly
selected from [1 ,i−1] and k1andk2are randomly selected
from [1 ,LS]. Then, to take advantage of the property that
superior particles have more potential in guiding the search
direction while inferior ones have more potential in helping
particles escape from local traps, with the assumption that rl1
is higher than rl2, we use the superior one between Xrl1,k1
andXrl2,k2, namely Xrl1,k1to replace pbest in (1) and use the
inferior one, namely Xrl2,k2to substitute nbest in (1).
Note that, in order to further promote the potential in
enhancing the diversity, we use randomness on both selec-
tion of two different higher levels ( rl1andrl2) and selection
of exemplars from the selected levels ( k1andk2).
On the one hand, this exemplar selection strategy provides
two exemplars from different higher levels for each parti-cle in lower levels, offering a potential compromise between
exploration and exploitation. On the other hand, the ran-
domness embedded in the level selection and the exemplar
selection may contribute to enhancing diversity, which plays
a signiﬁcant role in large-scale optimization [ 23].
D. LLSO
Combining the above two strategies together, LLSO is
developed with the update of particles deﬁned as follows:
v
d
i,j←r1vd
i,j+r2/parenleftBig
xd
rl1,k1−xd
i,j/parenrightBig
+φr3/parenleftBig
xd
rl2,k2−xd
i,j/parenrightBig
(6)
xd
i,j←xd
i,j+vd
i,j (7)
where Xi,j= [x1
i,j,..., xd
i,j,..., xD
i,j] is the posi-
tion of the jth particle from the ith level Li
and Vi,j= [v1
i,j,..., vd
i,j,..., vD
i,j] is its speed.
Xrl1,k1=[x1
rl1,k1,..., xd
rl1,k1,..., xD
rl1,k1] randomly selected
from level Lrl1and Xrl2,k2=[x1
rl2,k2,..., xd
rl2,k2,..., xD
rl2,k2]
randomly selected from level Lrl2are the two selected
exemplars with rl1andrl2denoting two different higher level
indexes selected within [1 ,i−1], and k1andk2representing
two particle indexes randomly selected within [1 ,LS]. r1,
r2, and r3are three random variables ranging within [0 ,1]
andφis the control parameter within [0 ,1] in charge of
the inﬂuence of the second exemplar. Note that rl1<rl2<i,
which indicates that Lrl1is higher than Lrl2, and both are
higher than Li, and also suggests that Xrl1,k1is better than
Xrl2,k2and both are better than Xi,j.YANG et al. : LLSO FOR LARGE-SCALE OPTIMIZATION 583
Algorithm 1 Framework of LLSO
Input :s w a r ms i z e NP, number of levels NL, level size LS, maximum
number of ﬁtness evaluations MAX_FES , control parameter φ.
Output : The ﬁnal solution xand its ﬁtness f(x)
1:fes=0;
2:Initialize the swarm randomly and calculate the ﬁtness values of
particles;
3:fes+= NP;
4:xis the best particle of the swarm and f(x) is its ﬁtness;
5:While fes<MAX_FES do
6: Sort particles in ascending order of ﬁtness and divide them
into NLlevels;
//Update particles in LNL,..., L3;
7: For i={NL,..., 3}do
8: For j={1,..., LS}do
9: S e l e c tt w ol e v e l sf r o mt h et o p( i-1) levels: rl1,rl2;
10: If(rl2<rl1)then
11: Swap ( rl1,rl2);
12: End If
13: Randomly select two particles from rl1,rl2:
Xrl1,k1,Xrl2,k2;
14: Update particle Xi,jaccording to Eq. (6) and Eq. (7);
15: Calculate the ﬁtness value f(Xi,j)of this particle;
16: If(f(Xi,j)<f(x))then
17: x=Xi,j;
18: End If
19: End for
20: fes+= LS;
21: End for
//Update the second level
22: For j={1,..., LS}do
23: Select two particles from the ﬁrst level: X1,k1,X1,k2;
24: If(f(X1,k2)<f(X1,k1))then
25: Swap ( X1,k1,X1,k2);
26: End If
27: Update particle X2,jaccording to Eq. (6) and Eq. (7);
28: Calculate the ﬁtness value f(X2,j)of this particle;
29: If(f(X2,j)<f(x))then
30: x=X2,j;
31: End If
32: End for
33: fes+= LS;
34:End While
Generally, superior particles have more potential in exploit-
ing the search space, while inferior particles have morepotential in exploring the search space. Thus, the learning
strategy displayed in ( 6) gives rise to a potential compromise
between exploration and exploitation for each particle. This isbecause the second part in the right hand of ( 6) allows one par-
ticle to promote its potential in exploitation by learning from
a superior exemplar, while the third part enables the particleto enhance its potential in exploration through learning from
a relatively inferior exemplar, and the degree of such learning
is controlled by the parameter φ.
Additionally, both second and third parts in the right hand
of (6) can be seen as the cognitive parts like in PSO ( 1).
Though there is no obvious social learning part in LLSO, actu-
ally, the social part is embedded in these two items because,
on the one hand, the two levels where the selected exem-plars come are randomly chosen from all higher levels; on
the other hand, the two exemplars are randomly selected fromthe corresponding levels. Such two random selections possibly
offer a special kind of social learning.
Obviously, ( 6) is not directly suitable for the update of par-
ticles in the ﬁrst and second levels. To deal with this situation,
we adopt different extra techniques for the two levels.
First, since the particles in the ﬁrst level are the best of the
whole swarm in the current generation and better solutions
are usually found near these ones, we just leave these particlesunchanged to preserve the most useful information and protect
them from being weakened. Thus, the particles in the ﬁrst level
directly enter the next generation.
Second, as for the particles in the second level, a similar
adaption follows. Instead of randomly choosing two exemplars
from two randomly selected higher levels, the two exemplars
for these particles are both randomly selected from the ﬁrst
level. Then, the superior one acts as the ﬁrst exemplar and theinferior one acts as the second exemplar in ( 6).
The pseudo code of LLSO is outlined in Algorithm 1, which
is simple to implement due to the maintenance of the classi-cal PSO framework. In this algorithm, lines 7–21 are for the
update of particles in levels L
NLtoL3, while lines 22–32 are
for the update of particles in the second level.
E. Differences Between LLSO and Other PSO Variants
The main unique property of LLSO is the LL mechanism
along with the exemplar selection method. It treats particles
differently and directly utilizes two predominant particles fromtwo different higher levels in the swarm to guide the learn-
ing of particles in lower levels by taking advantage of their
different strength in exploration or exploitation. Speciﬁcally,
the following characteristics make it distinguishable from the
current PSO variants.
1) Particles are grouped into different levels and those in
different levels are treated differently via learning from
different numbers (in total) of particles in higher levels.Speciﬁcally, the lower the level one particle belongs to,
the more the candidate exemplars [both exemplars in (6)]
this particle could learn from, and vice versa. Throughthis, particles in lower levels could focus on explor-
ing the search space, while those in higher levels could
concentrate on exploiting the search space. However, inmost PSO variants [ 11]–[14], [41], [57]–[59], particles
have the same number of candidate exemplars to learn
from and thus are treated equally.
2) Two current superior particles act as the exemplars
to guide the learning of inferior particles, which is
beneﬁcial for exploration enhancement. Instead of learn-ing from pbest ,nbest ,o r gbest in most PSO vari-
ants, such as hierarchical PSO [ 59], multiswarm PSO
variants [ 41], [57], [58], and new learning strategy-
based PSOs [ 11]–[14], particles in LLSO learn from the
superior ones in the current swarm. pbest ,nbest ,o rgbest
may easily lead to premature convergence [ 23], because
they may remain unchanged for many generations, espe-
cially when the evolution goes into late stages onmultimodal problems. However, particles in the swarm
are usually updated at each generation. Thus LLSO584 IEEE TRANSACTIONS ON EVOLUTIONARY COMPUTATION, VOL. 22, NO. 4, AUGUST 2018
may preserve higher diversity and thus has relatively
less probability to fall into local areas. In addition,different from CSO [ 23] and SL-PSO [ 21] which only
adopt one superior particle and the mean position of
the swarm (shared by all particles) to guide the learn-ing of particles, LLSO directly utilizes two superior
particles randomly selected from two different higher
levels to guide the learning of particles, leading to higherdiversity preservation than these two optimizers.
3) Two kinds of compromises between exploration and
exploitation exist in LLSO. Observing (6) and ( 7),
we can ﬁnd LLSO could compromise exploration and
exploitation to search the space in two aspects.
a)Particle-Level Compromise: Each particle in lower
levels can enhance its potential in exploitation
by learning from the better one between the twosuperior exemplars, and at the same time consol-
idate its potential in exploration by learning from
the relatively worse one. Thus, a compromise inexploring and exploiting the search space exists in
the learning process of each particle.
b)Swarm-Level Compromise: Particles in different
levels have different numbers of candidate exem-
plars to learn from. More speciﬁcally, particles in
the lowest level have the most candidate exem-plars to learn from, while particles in the second
level have the fewest candidate exemplars to learn
from and particles in the highest level (namely theﬁrst level) are not updated and directly enter the
next generation for preserving the best information.
Thus, we can see that particles in the lower levels
mainly concentrate on exploring the search space,
while particles in the higher levels mainly focus onexploiting the search space. Thus, a compromise in
exploring and exploiting the search space exists in
the whole swarm, which many other PSO variantsdo not have.
4) Last but not at least, two hierarchical randomness exists
in the exemplar selection. First, two higher levels arerandomly selected. Then, based on the selected levels,
one random particle is selected from each level and thus
two different particles in total are randomly selected.Together, the randomness of the level selection and that
of the particle selection cooperate with each other, and
can potentially provide particles with diverse exemplars,which beneﬁts the diversity promotion.
F . Complexity Analysis
Given a ﬁxed number of ﬁtness evaluations, the time com-
plexity of an EA [ 14], [21], [23] is generally calculated by
analyzing the extra time in each generation without consid-
ering the time of function evaluations, which is problem-dependent.
Thanks to the maintenance of the algorithmic simplicity
of PSO in LLSO, it is straightforward to compute the timecomplexity of LLSO. From Algorithm 1, we can see that it
takes O(NPlog (NP)+NP)to rank the swarm and divide theswarm into NL levels at each generation in line 6. During
the update of particles in all levels, except for those in theﬁrst level that directly enter the next generation, it takes
O(NP×D)(lines 7–32). Overall, we can see that LLSO only
takes extra O(NPlog (NP)+NP)in each generation compared
with PSO, which takes O(NP×D)in each generation.
As for the space complexity, LLSO needs much smaller
space than PSO, because it does not store the personal bestposition of each particle, which takes O(NP
×D)space.
In conclusion, LLSO remains computationally efﬁcacious
in time and is relatively more efﬁcient in space in comparisonwith the classical PSO.
G. Dynamic Version of LLSO
Comparing LLSO ( 6) with PSO ( 1), we ﬁnd that LLSO only
introduces two parameters that need ﬁne-tuning, namely the
number of levels NL and the control parameter φ.
Given the population size is NP, a small NL gives rise to
a large number of particles in each level. This may bring two
consequences: 1) promoting diversity in the exemplar selec-
tion conducted on the two selected levels, owing to the largenumber of particles in each level and 2) reducing diversity in
the level selection owing to the small number of levels. On
the contrary, a large NL brings two opposite consequences:1) enhancing diversity in the level selection, on account of
the large number of levels and 2) reducing diversity in the
exemplar selection, due to the small number of particles ineach level.
Comparing these two kinds of diversity, we consider that
they play different roles in the evolution process. Compared
with the diversity in the exemplar selection, the diversity in
the level selection is more important when the swarm exploresthe search space or when the swarm falls into local areas
and thus needs to jump out. This is because compared with
the diversity in the exemplar selection, the diversity in thelevel selection can provide particles to be updated with more
diverse exemplars that preserve diverse potential in exploration
and exploitation. On the contrary, when exploiting the searchspace, the diversity in the exemplar selection becomes more
important, which is beneﬁcial for the swarm to exploit the
search space more intensively without serious loss of diversity.
Therefore, we can see that for a single problem, the proper
NL may vary during the evolution process. Let alone that the
proper NL for different problems with different features isdifferent. This motivates us to design a dynamic setting for NL.
In this paper, for simplicity, we design a pool containing
different integers to realize the dynamism of NL, which isdenoted as S={l
1,..., ls}with sdifferent candidate numbers
of levels. Then, at each generation, LLSO will select a number
from the pool based on their probabilities, and at the end of the
generation, the performance of LLSO with this level number
is recorded to update the probability of this number. With thismechanism, LLSO can select a proper NL despite of different
features of different problems or different evolution stages for
a single problem.
In order to compute the probabilities of different level num-
bers in S, we deﬁne a record list R
s={r1,..., rs}, where eachYANG et al. : LLSO FOR LARGE-SCALE OPTIMIZATION 585
ri∈Rsis associated with each li∈S, to record the relative
performance improvement under the selected li. At the initial-
ization stage, each ri∈Rsis set to 1, and then, each riis
updated at each generation as follows [ 36]:
ri=|F−˜F|
|F|(8)
where Fis the global best ﬁtness of the last generation, while
/tildewideFis the global best ﬁtness of the current generation. Then the
probability Ps={p1,..., ps}is computed as in [ 36]
pi=e7∗ri
/summationtexts
j=1e7∗rj. (9)
Based on Ps, we conduct the roulette wheel selection to
select a number from Sas the level number in each generation.
Observing ( 8) and ( 9), we can notice that: 1) the value of
each riis within [0 ,1] since ( 8) calculates the relative per-
formance improvement using the global best ﬁtness valuesbetween two consecutive generations and 2) if the global best
ﬁtness value differs a lot between two consecutive generations,
r
iis close to 1. This indicates that the selected level number
in this generation is very appropriate and thus should have
a high probability to be selected in the next generation, which
is implied by the probability computed in (9). On the contrary,when the global best ﬁtness value differs little between two
consecutive generations, r
iis close to 0. This indicates that the
selection of the level number in this generation is not so advis-
able and thus the probability of this selection should be small,
which can be implied by the probability computed in (9) aswell. In this way, LLSO can potentially make an appropriate
choice of NL for different problems or for a single problem
at different stages.
As for our algorithm, when NL is ﬁxed, it is denoted as
LLSO; and when it uses a dynamic NL, we denote it as
DLLSO. As shown later in Section V-C, the performancecomparison between these two versions favors DLLSO.
IV . T
HEORETICAL ANALYSIS
In this section, we take investigation about LLSO by ana-
lyzing its exploration and exploitation abilities via makingcomparisons with the global PSO (GPSO) [ 6] and one recent
and popular PSO variant named CSO [ 23].
A. Exploration Ability
Exploration plays an important role when the swarm
explores the search space. Enhancing the exploration ability
of an EA is to promote the diversity of the swarm, so that it
can escape from local areas and ﬁnd the global or promising
areas easily. In particular, the exploration ability is consider-
ably important when EAs tackle multimodal problems or whenthe swarm needs to jump out of local areas, so that stagna-
tion or premature convergence can be avoided. The exploration
ability of EAs can be implied by the diversity of the exem-plars used to guide the learning or updating of particles or
individuals [ 23].To investigate the exploration ability of LLSO, we rewrite
(6)a sf o l l o w s :
v
d
i,j←r1vd
i,j+θ1/parenleftBig
p1−xd
i,j/parenrightBig
(10)
θ1=r2+φr3 (11)
p1=r2
r2+φr3xd
rl1,k1+φr3
r2+φr3xd
rl2,k2. (12)
Similarly, we can also rewrite the update formula of GPSO
[utilizing gbest to replace nbest in (1)] into ( 13) and that of
CSO ( 4)i n t o( 16)
vd
i←wvd
i+θ2/parenleftBig
p2−xd
i/parenrightBig
(13)
θ2=c1r1+c2r2 (14)
p2=c1r1
c1r1+c2r2pbestd
i+c2r2
c1r1+c2r2gbestd(15)
vd
l←r1vd
1+θ3(p3−xd
l) (16)
θ3=r2+φr3 (17)
p3=r2
r2+φr3xd
w+φr3
r2+φr3¯xd. (18)
From ( 10), (13), and ( 16), we can see that the difference
between pi(i=1,2,3)and the particle to be updated pro-
vides the main source of diversity. First, comparing ( 10)w i t h
(13) and ( 16), we can see that LLSO has potential to preserve
higher diversity. On the one hand, as for the ﬁrst part in p1,p2,
andp3, the randomly selected exemplar Xrl1,k1offers chances
for each particle in lower levels to learn from various betterparticles in LLSO. However, in GPSO, pbest of each particle
is updated only when the particle ﬁnds a better position, which
indicates that it is possible that pbest of the particle may be
unchanged for many generations. In CSO, the loser can only
learn from its corresponding winner. Therefore, in terms ofthe ﬁrst part, LLSO and CSO preserve competitive or compa-
rable diversity and both potentially own higher diversity than
GPSO.
On the other hand, as for the second part of p
i(i=1,2,3),
gbest in GPSO is updated only when the swarm ﬁnds a bet-
ter position. It is more likely that gbest remains unchanged
than pbest . In addition, gbest is shared by all particles. These
two limitations do great harm to the diversity maintenance
for GPSO [ 23]. For CSO, though the mean position of the
swarm xis updated at each generation, it is also shared by
all particles. However, in LLSO, the second exemplar Xrl2,k2
is randomly selected for each particle. Thus, in terms of the
second part, LLSO probably possesses higher diversity.
In addition, compared with other PSO variants that use nbest
to guide the learning of particles [ 7], [8] or that divide the
swarm into subswarms and then use gbest or the center of
the subswarm to guide the updating of particles [ 58], LLSO
still potentially preserves better exploration ability, because
nbest orgbest of a subswarm may remain unchanged for many
generations as well.
In short, we can see that the diversity of the exemplars used
to guide the learning of particles in LLSO is potentially higher,
which may beneﬁt for strengthening the exploration ability.Thus, LLSO can potentially ﬁnd the promising areas faster
and have greater chance to jump out of local optimum areas.586 IEEE TRANSACTIONS ON EVOLUTIONARY COMPUTATION, VOL. 22, NO. 4, AUGUST 2018
B. Exploitation Ability
With limited computational resources, such as function eval-
uations, exploitation is necessary when the swarm exploitsthe searching areas. Enhancing the exploitation ability of
an EA is to fully exploit the found promising areas fast,
so that better solutions can be located as fast as possible.The exploitation ability is very important when an EA deals
with simple unimodal functions or when the swarm ﬁnds the
global optimum areas. Generally, the exploitation ability canbe indicated by the difference between the exemplar and the
updated particle [ 23]. The smaller the difference is, the more
the particle focuses on exploiting the area.
To analyze the exploitation ability of LLSO, we assume
that for the jth particle X
i,jfrom the ith level Li, two random
exemplars Xrl1,k1andXrl2,k2are selected from two randomly
selected higher levels Lrl1and Lrl2(rl1<rl2<i). Then, we
have
f/parenleftbig
Xrl1,k1/parenrightbig
≤f/parenleftbig
Xrl2,k2/parenrightbig
≤f/parenleftbig
Xi,j/parenrightbig
. (19)
Comparing Xrl1,k1andXrl2,k2with pbest andgbest deﬁned
in PSO, we have the following formula:
⎧
⎨
⎩f(gbest)≤f/parenleftbig
pbesti,j/parenrightbig
≤f/parenleftbig
Xi,j/parenrightbig
f(gbest)≤f/parenleftbig
pbestrl1,k1/parenrightbig
≤f/parenleftbig
Xrl1,k1/parenrightbig
f(gbest)≤f/parenleftbig
pbestrl2,k2/parenrightbig
≤f/parenleftbig
Xrl2,k2/parenrightbig(20)
where pbesti,j,pbestrl1,k1andpbestrl2,k2are the personal best
positions of Xi,j,Xrl1,k1,andXrl2,k2, respectively.
When it reaches the late stages where all particles may
converge together, the following relationship holds:
pbestrl1,k1≈pbestrl2,k2≈pbesti,j≈gbest. (21)
Therefore, for GPSO, we have
/Delta1FGPSO=/vextendsingle/vextendsinglef/parenleftbig
Xi,j/parenrightbig
−f(gbest)/vextendsingle/vextendsingle
=/vextendsingle/vextendsingle/vextendsingle/vextendsinglef/parenleftbig
X
i,j/parenrightbig
−f/parenleftbigggbest+gbest
2/parenrightbigg/vextendsingle/vextendsingle/vextendsingle/vextendsingle
≈/vextendsingle/vextendsingle/vextendsingle/vextendsinglef/parenleftbig
X
i,j/parenrightbig
−f/parenleftbigggbest+pbesti,j
2/parenrightbigg/vextendsingle/vextendsingle/vextendsingle/vextendsingle
=/vextendsingle/vextendsinglef/parenleftbig
X
i,j/parenrightbig
−f/parenleftbig
p/prime
2/parenrightbig/vextendsingle/vextendsingle (22)
where p/prime
2is the expected value of p2in (15).
Similarly, for CSO and LLSO, we can derive the following:
/Delta1FCSO=/vextendsingle/vextendsinglef/parenleftbig
Xi,j/parenrightbig
−f/parenleftbig
Xwi,j/parenrightbig/vextendsingle/vextendsingle
=/vextendsingle/vextendsinglef/parenleftbig
Xi,j/parenrightbig
−f/parenleftbig
p/prime
3/parenrightbig/vextendsingle/vextendsingle (23)
/Delta1FLLSO=/vextendsingle/vextendsinglef/parenleftbig
Xi,j/parenrightbig
−f/parenleftbig
Xrl1,k1/parenrightbig/vextendsingle/vextendsingle
=/vextendsingle/vextendsinglef/parenleftbig
Xi,j/parenrightbig
−f/parenleftbig
p/prime
1/parenrightbig/vextendsingle/vextendsingle (24)
where Xwi,jis the corresponding winner of Xi,jin CSO, p/prime
3is
the expected value of p3withφ=0f o rC S Oi n( 18), and
p/prime
1is the expected value of p1withφ=0 for LLSO in ( 12).
Since Xrl1,k1is selected from level Lrl1, which is higher than
Li, where Xi,jcomes, the expected value of Xrl1,k1is better
than that of Xwi,j, which is only better than Xi,j. Therefore, we
have f(Xrl1,k1)≤f(Xwi,j).
Combining the above formula together, we can derive
/Delta1FLLSO≤/Delta1FCSO≤/Delta1FGPSO. (25)Such formula indicates that compared with GPSO and CSO,
LLSO potentially has a better exploitation ability to reﬁnesolutions within a smaller gap between two positions whose
ﬁtness values are very similar.
The above analysis has separately demonstrated that LLSO
can preserve good exploration and exploitation abilities.
However, during the evolution process, these two abilities
usually conﬂict with each other. Thus, during evolution, anEA generally needs to make a compromise between these
two abilities to search the space [ 16], [60], [61]. It should
be mentioned that such a compromise should not be ﬁxed,but be dynamically adjusted according to different features of
the problems to be optimized or different requirements in the
evolution process. In Section V-A, the good exploration and
exploitation abilities of LLSO will be veriﬁed empirically in
comparison with GPSO [ 6] and CSO [ 23].
V. E
XPERIMENTS
To verify the feasibility and efﬁciency of the proposed
LLSO, a series of experiments are conducted on two
widely used sets of large-scale optimization problems: the
CEC’2010 [ 27] and the CEC’2013 [ 28] benchmark sets. The
latter is the extension of the former through introducing new
features, such as overlapping functions. Consequently, func-
tions in the latter set are much more complicated and harderto optimize. The main properties of these two function sets
are summarized in Tables SI and SII in the supplementary
material, respectively. For details of these functions, readers
are referred to [ 27] and [ 28].
In this section, we ﬁrst empirically substantiate the good
exploration and exploitation abilities of LLSO in Section V-A.
Then, we investigate the key parameter settings for DLLSO
in Section V-B and the inﬂuence of the dynamism of NLon LLSO in Section V-C, respectively. After all the prelim-
inary investigation, we make comparisons between DLLSO
and other state-of-the-art algorithms dealing with large-scaleoptimization in Section V-D. In Section V-E, the scalability
comparison between DLLSO and the compared algorithms
is conducted on the CEC’2010 benchmark functions withdimensionality increasing from 200 to 2000. At last, the com-
putational time comparison is made between DLLSO and
some compared algorithms on the CEC’2010 problems withthe dimensionality increasing from 200 to 2000 as well.
In addition, unless otherwise stated, the maximum number
of ﬁtness evaluations is set to 3000 ×D(where Dis the dimen-
sion size). What is more, for fair comparisons, median, mean,
and standard deviation (Std) values over 30 independent runsare used to evaluate the performance of different algorithms. In
the comparisons between two different algorithms, Wilcoxon
rank sum test is performed at a signiﬁcance level of α=0.05.
Additionally, it is worth mentioning that all algorithms are
conducted on a PC with four Intel Core i5-3470 3.20-GHz
CPUs, 4-GB memory and Ubuntu 12.04 LTS 64-bit system.
A. Exploration and Exploitation Investigation in LLSO
Before experiments, it should be noted that exploration
and exploitation generally conﬂict with each other. Thus, anYANG et al. : LLSO FOR LARGE-SCALE OPTIMIZATION 587
EA generally needs to make a compromise between these two
aspects to search the space. In general, such a compromiseshould be dynamically adjusted according to different fea-
tures of problems or different requirements in the evolution
process [ 16], [60]. Besides, this compromise does not mean
that exploration and exploitation should be the same or similar
during all evolution stages or on all problems either.
When coping with unimodal problems, exploitation should
be put properly more emphasis to seek fast convergence.
However, when tackling multimodal problems, exploration
should be properly biased to avoid falling into local areas. Fora single problem, when most particles locate in local areas,
exploration should be appropriately biased to let the swarm
jump out of local areas. Nevertheless, when the swarm ﬁnds
promising areas, exploitation should be appropriately biased
to reﬁne the obtained solutions [ 16], [60].
Then, to verify that LLSO can preserve good exploration
and exploitation abilities and could compromise these two
abilities properly, we conduct comparison experiments amongLLSO, CSO, and GPSO on four CEC’2010 benchmark func-
tions (fully separable and unimodal F
1, partially separable
and multimodal F5, partially separable and unimodal F7, and
partially separable and multimodal F10) with 200 dimenisons
in regard to swarm diversity along with the global best ﬁt-
ness value. These functions are selected because we want tomake a comprehensive comparsion on various kinds of func-
tions, like fully separable, partially separable, unimodal, or
multimodal.
In this paper, the diversity is measured as follows [ 23], [62]:
D(X)=1
NPNP/summationdisplay
i=1/radicaltp/radicalvertex/radicalvertex/radicalbtD/summationdisplay
d=1/parenleftbig
xd
i−¯xd/parenrightbig2(26)
¯xd=1
NPNP/summationdisplay
i=1xd
i (27)
where D(X) represents the diversity of the swarm X, and xis
the mean position of the swarm.
Fig. 2shows the comparison results of the three algorithms
on the four functions with the maximum number of ﬁtness
evaluations set as 3000 ×D=6×105. For fairness, the pop-
ulation size is set 300 for all algorithms. From this ﬁgure, we
can obtain the following ﬁndings.
First, for unimodal functions, exploitation should be put
a little more emphasis, so that fast convergence can be
achieved. From Fig. 2(a) and (c), we can see that on the uni-
modal functions F1andF7, the exploitation is properly biased,
so that LLSO converges much faster than GPSO and CSO
with better solutions simultaneously. Speciﬁcally, on F1[see
Fig. 2(a)], the exploitation is biased much more obviously in
LLSO. GPSO maintains the highest diversity but obtains the
worst performance because of the stagnation of the swarm.CSO perserves higher diversity but slower convergence than
LLSO, because the exploitaiton is less empahsized. On F
7[see
Fig. 2(c)], exploitation is appropriately biased without serious
loss of exploration in LLSO, resulting in its good performance.
However, the exploitation is overemphasized in GPSO andthus the exploration is seriously ignored, leading to its infe-
rior performance. For CSO, the exploitation is less biased andthus slower convergence is obtained than LLSO.
Second, when it arrives at multimodal functions, explo-
ration should be dynamically and properly biased withoutserious loss of exploitation, so that premature convergence
and stagnation can be avoided. From Fig. 2(b) and (d), we
can ﬁnd that on multimodal functions F
5andF10, LLSO still
achieves better peformance than GPSO and CSO with respect
to both convergence speed and solution quality. This is because
LLSO can compromise exploration and exploitation betterthan GPSO and CSO. Speciﬁcally in GPSO, the exploita-
tion is overbiased and thus the exploration is seriously lost
on both functions, leading to its poor performance. For CSO,
the exploration is overemphasized and thus its exploitation is
very poor, resulting in its poor performance in reﬁning thesolutions.
Overall, we can see that LLSO can preserve good explo-
ration and exploitation abilities and can particulaly compro-mise these two well to search the space during the evolution.
Such a good ability beneﬁts from the proposed LL strategy,
which can offer two kinds of compromises between explo-ration and exploitation: 1) the particle-level compromise and
2) the swarm-level compromise as stated in Section III-E.
B. Parameter Settings
In LLSO, only two extra parameters are introduced: 1) the
number of levels NL and 2) the control parameter φ. Since
we have proposed a dynamic selection strategy for NL in
Section III-G, the ﬁne-tuning of the sensitive NL can be
saved by setting the pool Swith a wide range. In the
preliminary experiments, we ﬁnd DLLSO is not so sensitivetoS, if we keep Sin a wide range. In this paper, we set
S={4,6,8,10,20,50}.
Then, we turn to the setting of the control parameter
φand the swarm size NP, the common parameter in all
EAs [ 6], [21], [23], [56], which is hard to set, owing to its
dependency on the complexity of problems. Thus, to see theeffect of φand NP on DLLSO, we conduct experiments on
DLLSO with NP varying from 200 to 600 and φvarying from
0.1 to 0.6.
Table SIII in the supplementary material displays the exper-
imental results of DLLSO with different combinations of
φand NP on six 1000-D benchmark functions from the
CEC’2010 set: fully separable and unimodal function F
1,
fully separable and multimodal function F3,partially separable
and unimodal function F7, partially separable and multimodal
function F8,partially separable and unimodal function F12,
and partially separable and unimodal function F17. These func-
tions are selected, because we want to investigate the inﬂuence
of parameters on almost all kinds of problems: fully separable,
partially separable, unimodal, and multimodal.
From this table, we can see the following.
1) The smaller the swarm size is, the larger value φhas.
This is because a small swarm size cannot offer highdiversity for the swarm, thus a large φis needed to
promote the diversity by enhancing the inﬂuence of588 IEEE TRANSACTIONS ON EVOLUTIONARY COMPUTATION, VOL. 22, NO. 4, AUGUST 2018
(a) (b)
(c) (d)
Fig. 2. Swarm diversity and the global best ﬁtness value comparison among LLSO, CSO, and GPSO on four functions F1,F5,F7,a n d F10with
200 dimensions. Please note that for F1, the ﬁtness value of LLSO is not plotted after the number of ﬁtness evaluations reaches about 5 ×105. This is because
the global best ﬁtness value becomes 0, arriving at the global optimum of F1.( a ) f1:fully separable and unimodal. (b) f5:partially separable and multimodal.
(c)f7:partially separable and unimodal. (d) f10:partially separable and multimodal.
the second exemplar, which owns more potential in
exploration than the ﬁrst one in ( 6).
2) For large swarm sizes, the proper φseems to consistently
stay at 0.4 as indicated by the results of DLLSO withNP within [400 ,600].
3) When NP is within [400, 600], it seems that φmakes
no signiﬁcant difference on DLLSO when it is within[0.1,0.5]. However, when φis within [0.1, 0.5], it seems
that NP has great inﬂuence on DLLSO, especially for F
3
andF7.
In conclusion, NP =500 and φ=0.4 is adopted for
DLLSO on 1000-D problems, which also makes it fair to
compare DLLSO with CSO that adopts the same setting of
NP [ 23].
C. Effect of Dynamic Level Numbers
To investigate the effect of the dynamic selection of NL on
DLLSO, we conduct comparison experiments on two versionsof the proposed optimizer: LLSO with a ﬁxed NL and LLSO
with a dynamic NL, namely DLLSO. The former version of
LLSO is represented as “LLSO-NL,” such as LLSO with fourlevels can be denoted as “LLSO-4.”
Fig. S1 in the supplementary material shows the compari-
son results between the two versions of LLSO on eight 1000-Dbenchmark functions from the CEC’2010 set including the six
functions used in the last section (adding two extra functions
F
10and F15). In this experiment, NP =500 and φ=0.4
is adopted and the maximum number of function evaluations
varies from 5 ×105to 5×106. For LLSO-NL, the ﬁxed
numbers of levels are set to be the members in S.
From this ﬁgure, ﬁrst, we can ﬁnd that on some functions,
such as F10,F12, and F17, LLSO is not sensitive to NL,
while on some functions, such as F3,F7,F8, and F15, LLSO
is very sensitive to NL. Second, the optimal NL is different fordifferent problems, such as the optimal NL is 8 for F7, while
that number is 50 for F15. Third, comparing these two ver-
sions, we ﬁnd that DLLSO can make a good compromise to
obtain competitive solutions on almost all the eight problemsand even on some functions, such as F
10andF15, DLLSO can
obtain better solutions than the LLSO with the optimal NL.
All in all, we can ﬁnd that the dynamic selection strategy
for NL is promising for the proposed optimizer.
D. Comparisons With State-of-the-Art Methods
Subsequently, to comprehensively verify the efﬁciency and
effectiveness of DLLSO, we compare it with various state-of-the-art algorithms dealing with large-scale optimization.
Speciﬁcally, four popular algorithms, namely three PSO vari-
ants (CSO [ 23], SL-PSO
2[21], and DMS-L-PSO3[39]), and
a memetic algorithm named MA-SW-Chains4[48], concentrat-
ing on the second aspect in handling large-scale optimization
(Section II-B), and four CCEAs, namely CCPSO2 [ 33],
DECC-DG5[20], DECC-G [ 35], and MLCC6[36], focusing
on the ﬁrst aspect in large-scale optimization (Section II-A),are selected to make comparisons. For fairness, the key param-
eters in each algorithm are set as recommended in the corre-
sponding papers. We conduct the comparison experiments onboth CEC’2010 benchmark set [ 27] and CEC’2013 benchmark
set [28].
2The codes of CSO and SL-PSO can be downloaded from http://
www.surrey.ac.uk/cs/research/nice/people/yaochu_jin/ .
3The code of DMS-L-PSO can be downloaded from http://
www.ntu.edu.sg/home/epnsugan/ .
4The code of MA-SW-Chains can be downloaded from
http://sci2s.ugr.es/EAMHCO#Complementary .
5The codes of CCPSO2 and DECC-DG can be downloaded from
https://titan.csit.rmit.edu.au/ ∼e46507/publications.php .
6The codes of DECC-G and MLCC can be downloaded from
http://staff.ustc.edu.cn/ ∼ketang/codes/ .YANG et al. : LLSO FOR LARGE-SCALE OPTIMIZATION 589
TABLE I
COMPARISON RESULTS OF THE COMPARED ALGORITHMS ON 1000-D CEC’2010 F UNCTIONS WITH3×106FITNESS EV ALUATIONS
Tables Iand II, respectively, show the comparison
results among different algorithms on the two bench-
mark sets with 1000-D. The highlighted pvalues mean
that DLLSO is signiﬁcantly better than the correspond-
ing algorithms. Additionally, the symbols, “ +,” “−,” and“=,” above the pvalues represent that DLLSO is signiﬁ-
cantly better than, signiﬁcantly worse than, and equivalent
to the compared algorithms on the associated functions.Furthermore, w/l/t in the last row represents that DLLSO
wins on wfunctions, loses on lfunctions and ties on t590 IEEE TRANSACTIONS ON EVOLUTIONARY COMPUTATION, VOL. 22, NO. 4, AUGUST 2018
TABLE II
COMPARISON RESULTS OF THE COMPARED ALGORITHMS ON 1000-D CEC’2013 F UNCTIONS WITH3×106FITNESS EV ALUATIONS
functions in total in the competitions with the counterpart
methods.
As for the CEC’2010 set, from Table I, we can see that
DLLSO outperforms the compared algorithms on most ofthe 20 functions. In details, compared with CSO, SL-PSO,
MA-SW-Chains, and DMS-L-PSO, DLLSO shows its great
superiority on 13, 12, 11, and 13 functions, respectively.Compared with these algorithms, DLLSO only loses the
competition on 6, 4, 6, and 6 functions, respectively. In com-
parison with the four CCEAs (CCPSO2, DECC-G, MLCC,
and DECC-DG), DLLSO defeats them on 16, 19, 19, and
16 functions, respectively. Besides, DLLSO only loses on2, 1, 1, and 3 functions, respectively, competing with these
algorithms.
When it arrives at the CEC’2013 set where the func-
tions are more difﬁcult to optimize than those in the former
set, DLLSO consistently shows its dominance according to
Table II. Compared with DMS-L-PSO and the four CCEAs,DLLSO shows its signiﬁcant superiority on at least ten func-
tions. In comparison with CSO and SL-PSO, DLLSO defeats
them down on eight and seven functions, respectively, and only
loses the competitions on three and four functions, respec-tively. Unfortunately, on this set, DLLSO is slightly worse
than MA-SW-Chains. However, compared with this algorithm,
DLLSO is easier to understand and simpler to implement, dueto its maintenance of the framework of the classical PSO,
which leads to its superior performance to MA-SW-Chains in
computational efﬁciency that will be veriﬁed in the following
sections.
Further, we also conduct convergence behavior com-
parison between DLLSO and the compared algorithms
on the two benchmark sets to testify the superiority of
DLLSO with respect to convergece speed. Figs. S2 and S3in the supplementary material present the comparison
results on the CEC’2010 and CEC’2013 benchmark sets,
respectively.YANG et al. : LLSO FOR LARGE-SCALE OPTIMIZATION 591
TABLE III
PARAMETER SETTINGS OF DLLSO INDEALING WITH
PROBLEMS WITHDIFFERENT DIMENSION SIZES
On the CEC’2010 benchmark set, from Fig. S2, in the
supplementary material, we can observe the following.
1) DLLSO converges faster with better solutions than all
eight compared methods on four ( F3,F6,F10, and F15)
functions.
2) DLLSO achieves faster convergence with higher qual-
ity solutions than seven compared methods (except for
only one compared algorithm out of the eight com-pared methods) on six functions ( F
1,F5,F7,F11,F12,
andF14).
3) Concretely, DLLSO can apparently defeat CSO,
SL-PSO, MA-SW-Chains, DMS-L-PSO, CCPSO2,
DECC-G, MLCC, and DECC-DG with both faster con-
vergence and better solutions on 14, 12, 10, 20, 15, 17,16, and 14 functions, respectively.
Similarly, on the CEC’2013 benchmark set, from Fig. S3,
in the supplementary material, we can obtain the following.
1) DLLSO achieves great superiority to all eight compared
algorithms in both convergence and solution quality on
six functions ( F
4,F7,F8, and F13−F15).
2) Besides, on F1and F5, DLLSO achieves both better
solutions and faster convergence than seven compared
algorithms.
3) DLLSO converges faster with higher solution qual-
ity than CSO, SL-PSO, MA-SW-Chains, DMS-L-PSO,CCPSO2, DECC-G, MLCC, and DECC-DG on 9, 9, 8,
11, 9, 9, 8, and 12 functions, respectively.
In conclusion, we can see that compared with these state-of-
the-art large-scale algorithms, DLLSO can achieve competitive
or even better performance in both solution quality and con-
vergence speed. The superiority of DLLSO can be attributed tothe proposed LL strategy and the proposed exemplar selection
strategy. LL groups particles into different levels and treats
particles in different levels differently. The exemplar selectionstrategy allows particles in different levels to learn from var-
ious superior particles from different higher levels. From the
two selected superior exemplars, one particle could improveits potential in exploitation by learning from the better one,
and at the same time consolidate its potential in exploration
by learning from the inferior one. In this way, each updatedparticle may compromise exploration and exploitation in the
evolution.
Besides, the cooperation between these two strategies makes
particles in different levels learn from different numbers of
exemplars. That is, particles in lower levels have more supe-rior particles and a wider range to learn, which is beneﬁcial for
exploration, while particles in higher levels have fewer supe-
rior particles and a narrower range to learn, which is proﬁtablefor exploitation. In this manner, the whole swarm can make
a compromise in exploring and exploiting the search spacevia letting particles in higher levels concentrate on exploiting
while letting particles in lower levels focus on exploring.
In short, these two kinds of compromises in exploration and
exploitation make DLLSO achieve good performance.
E. Scalability Comparisons With State-of-the-Art
Methods
The above comparison experiments have exhibited the supe-
riority of DLLSO to several state-of-the-art methods in dealing
with 1000-D problems. To further substantiate the scalability
of DLLSO to solve higher dimensional problems, we performexperiments on the CEC’2010 problems with dimensionality
increasing from 200 to 2000.
In this series of experiments, the parameters of DLLSO are
set as shown in Table III. As for the compared algorithms,
the parameters are set as recommended in the corresponding
papers. For fairness, the maximum number of ﬁtness evalu-ations is set as 3000 ×Dwhen conducting experiments on
problems with different dimension sizes. In addition, due to
the page limit, we attach all the comparison results to the
supplementary material.
1) Comparsion Results on 200-D Problems: Table SIV in
the supplementary material presents the comparison results on
the CEC’2010 problems with 200 dimensions. From this table,
we can see that DLLSO displays its great potential and abil-ity in dealing with 200-D problems. Speciﬁcally, DLLSO can
achieve the global optimum of F
1in each run and is much
superior to CSO, SL-PSO, and the four CCEAs (CCPSO2,DECC-G, MLCC, and DECC-DG) on at least 16 functions.
Besides, DLLSO also wins the competition with MA-SW-
Chains on 12 functions. Compared with DMS-L-PSO, DLLSO
is competitive and comparable to this algorithm by defeating
it on nine functions.
2) Comparison Results on 500-D Problems: Table SV
in the supplementary material shows the comparison results
among different algorithms on 500-D problems. Observingthis table, we can ﬁnd that DLLSO, respectively, domi-
nates the eight compared algorithms on at least 11 functions.
Compared with CSO, DLLSO outperforms it on 13 functionsand only loses the competition on three functions. In compar-
ison to MA-SW-Chains and DMS-L-PSO, DLLSO performs
better than them both on 11 functions. In particular, DLLSO
obtains the global optimum of F
1in each run as well and
is much better than SL-PSO and the four CCEAs on at least15 functions.
3) Comparison Results on 800-D Problems: Table SVI in
the supplementary material displays the comparison results on800-D problems. From this table, we can observe that DLLSO
is, respectively, superior to the eight compared algorithms on at
least 12 functions. Particularly, DLLSO dominates CSO, SL-PSO, and DMS-L-PSO on 13 functions, respectively, and is
especially better than the four CCEAs on at least 17 functions.
4) Comparison Results on 2000-D Problems: Table SVII
in the supplementary material presents the comparison results
among all the compared algorithms on 2000-D problems,which are particularly harder to optimize than the aforemen-
tioned problems. From this table, we can see that DLLSO592 IEEE TRANSACTIONS ON EVOLUTIONARY COMPUTATION, VOL. 22, NO. 4, AUGUST 2018
is still much better than the compared algorithms in deal-
ing with such complicated problems. Speciﬁcally, DLLSO,respectively, wins the competition with the eight compared
methods on at least 13 functions. In particular, DLLSO is sig-
niﬁcantly superior to SL-PSO, and the four CCEAs on at least15 functions.
5) Overall Comparisons: From the above comparison
results, we can see that DLLSO has a good scalability in tack-ling problems with different dimension sizes. Particularly, as
the dimensionality increases, the number of functions on which
DLLSO can, respectively, dominate the eight compared algo-rithms increases as well (for 200-D, 500-D, 800-D, 1000-D,
and 2000-D problems, this number is 9, 11, 12, 11, and 13,
respectively).
To have a better view of the comparison results, we plot
the changes of the averaged ﬁtness value of each algorithm on
each function with the dimensionality increasing from 200 to
2000. The result is shown in Fig. S4 in the supplementary
material.
From this ﬁgure, we can ﬁnd that as expected, on most
functions, the performance of all algorithms degrades with
the dimensionality increasing, which results from the exponen-tially increased search space. However, we ﬁnd that on F
1,F3,
andF10, DLLSO always achieves the best performance as the
dimensionality increases in comparison with other algorithmsas shown in Fig. S3(a), (c), and (j) in the supplementary mate-
rial. Besides, on F
5−F7, with the dimensionality increasing,
the ability of DLLSO does not degrade but instead is improvedvia the proper parameter settings, which can be clearly seen
from Fig. S3(e)–(g) in the supplementary material.
Overall, we can conclude that DLLSO preserves good scal-
ability to solve higher dimensional problems. Such superior
scalability of DLLSO could be ascribed to the following
aspects: 1) ﬁrst, in LLSO, particles are divided into different
levels and are treated differently; and 2) second, the proposed
exemplar selection strategy affords two different superiorexemplars for each particle to learn, so that the potential in
exploitation of one particle may be promoted via learning
from the better one and the potential in exploration may beenhanced by learning from the inferior one. In addition, par-
ticles in different levels have different numbers of superior
particles to learn from, resulting in that particles in lower levelshave a wider range to learn, which is beneﬁcial for explo-
ration, and particles in higher levels have a narrower range
to learn, which is beneﬁcial for exploitation. Thus, LLSO cancompromise exploration and exploitation to search the space
from both particle level and swarm level, which beneﬁts for
achieving competitive performance with the state-of-the-artmethods.
F . Time Comparisons With State-of-the-Art Methods
The above experiments have demonstrated the superiority of
DLLSO to other algorithms with respect to solution quality. To
further validate the competitive efﬁciency of DLLSO in tack-
ling large-scale optimization, we conduct computational costcomparison between DLLSO and three compared algorithms,
namely CSO, SL-PSO, and MA-SW-Chains. These algorithmsare selected because on the one hand, they were all imple-
mented with C codes; on the other hand, they all contributeto the second aspect in handling large-scale optimization as
stated in Section II-B. By this means, fair comparison can be
obtained.
In the experiments, we record the computing time of
each compared algorithm on the CEC’2010 benchmark func-
tions with the dimensionality increasing from 200 to 2000.Table SVIII and Fig. S5 in the supplementary material present
the time comparison results among the four algorithms on each
function with different dimension sizes.
From Table SVIII and Fig. S5, in the supplementary mate-
rial, we can see that both DLLSO and CSO are much more
efﬁcient than the other two algorithms (SL-PSO and MA-SW-
Chains). In details, the computational cost of MA-SW-Chains
is the highest. This is because MA-SW-Chains employs manycomplicated local search methods. Compared with DLLSO
and CSO, SL-PSO needs much more time, because it needs
to compute the mean position of the swarm, to sort the swarmand to compute the learning probability for each particle, the
combination of which leads to its higher computational cost
than CSO and DLLSO.
Compared with CSO, we ﬁnd that DLLSO takes nearly
the same time as CSO. However, it is interesting to ﬁnd
that when dealing with low-dimensional problems, CSO isslightly more efﬁcient than DLLSO. Nevertheless, with the
dimensionality increasing, the difference between the compu-
tational cost of DLLSO and CSO becomes less and less, andeven when it comes to 2000-D, DLLSO is a bit more efﬁ-
cient than CSO. This is because CSO needs to compute the
mean position of the whole swarm, which takes O(NP×D)
at each generation. Thus, as the dimensionality increases,
except for the computation time of ﬁtness functions, theextra computational cost of CSO increases faster than that of
DLLSO.
Together, we can see that with respect to the computational
cost, DLLSO is also very competitive or even superior to state-
of-the-art algorithms, due to its maintenance of the classical
PSO framework, which is very easy to understand and simpleto implement.
To summarize, we can conclude that the proposed DLLSO
is competitive, effective and efﬁcient in dealing with large-scale optimization in both solution quality and computational
cost.
VI. C
ONCLUSION
In this paper, we have proposed a LL strategy and an
exemplar selection strategy, the combination of which leads
to a new optimizer named LLSO. Besides, to deal with
the challenge that the optimal number of levels is problem-
dependent, we further added a dynamic selection strategy for
the number of levels, leading to DLLSO, a dynamic ver-sion of LLSO. Various experiments have been conducted
to demonstrate the efﬁciency and effectiveness of DLLSO
in tackling large-scale optimization with respect to solu-tion quality, convergence speed, scalability, and computational
cost.YANG et al. : LLSO FOR LARGE-SCALE OPTIMIZATION 593
Though DLLSO shows good performance in coping with
large-scale optimization, the obtained solutions to some func-tions are still far from the global optima, which is the common
issue for the state-of-the-art algorithms as well, as seen in
Tables Iand II. Therefore, how to further improve DLLSO
to obtain solutions as near the global optima as possible
is the ﬁrst direction for future investigation. In addition,
since dividing the whole swarm into levels is only associ-ated with the population, whether the proposed LL strategy
and the exemplar selection strategy are promising for other
population-based EAs, such as DE, is another direction forfuture investigation.
R
EFERENCES
[1] L.-Y . Chuang, C.-H. Yang, J.-H. Tsai, and C.-H. Yang, “Operon predic-
tion using chaos embedded particle swarm optimization,” IEEE/ACM
Trans. Comput. Biol. Bioinformat. , vol. 10, no. 5, pp. 1299–1309,
Sep./Oct. 2013.
[2] P. Faria, J. Soares, Z. Vale, H. Morais, and T. Sousa, “Modiﬁed par-
ticle swarm optimization applied to integrated demand response and
DG resources scheduling,” IEEE Trans. Smart Grid , vol. 4, no. 1,
pp. 606–616, Mar. 2013.
[3] X. Wen et al. , “A maximal clique based multiobjective evolutionary algo-
rithm for overlapping community detection,” IEEE Trans. Evol. Comput. ,
vol. 21, no. 3, pp. 363–377, Jun. 2017.
[4] Y .-H. Jia et al. , “A dynamic logistic dispatching system with set-based
particle swarm optimization,” IEEE Trans. Syst., Man, Cybern., Syst. ,
to be published.
[5] R. C. Eberhart and J. Kennedy, “A new optimizer using particle swarm
theory,” in Proc. Int. Symp. MHS , Nagoya, Japan, 1995, pp. 39–43.
[6] J. Kennedy and R. C. Eberhart, “Particle swarm optimization,” in Proc.
IEEE Int. Conf. Neural Netw. , vol. 4. 1995, pp. 1942–1948.
[7] J. Kennedy and R. Mendes, “Population structure and particle swarm
performance,” in Proc. IEEE Congr. Evol. Comput. , Honolulu, HI, USA,
2002, pp. 1671–1676.
[8] J. Kennedy, “Small worlds and mega-minds: Effects of neighborhood
topology on particle swarm performance,” in Proc. IEEE Congr. Evol.
Comput. , Washington, DC, USA, 1999, pp. 1931–1938.
[9] Y . Shi and R. Eberhart, “A modiﬁed particle swarm optimizer,” in Proc.
IEEE Congr. Evol. Comput. , Anchorage, AK, USA, 1998, pp. 69–73.
[10] K. E. Parsopoulos and M. N. Vrahatis, “On the computation of all global
minimizers through particle swarm optimization,” IEEE Trans. Evol.
Comput. , vol. 8, no. 3, pp. 211–224, Jun. 2004.
[11] J. J. Liang, A. K. Qin, P. N. Suganthan, and S. Baskar, “Comprehensive
learning particle swarm optimizer for global optimization of multimodalfunctions,” IEEE Trans. Evol. Comput. , vol. 10, no. 3, pp. 281–295,
Jun. 2006.
[12] M. A. M. de Oca, T. Stutzle, K. V . den Enden, and M. Dorigo,
“Incremental social learning in particle swarms,” IEEE Trans. Syst.,
Man, Cybern. B, Cybern. , vol. 41, no. 2, pp. 368–384, Apr. 2011.
[13] Z.-H. Zhan, J. Zhang, Y . Li, and Y .-H. Shi, “Orthogonal learning par-
ticle swarm optimization,” IEEE Trans. Evol. Comput. , vol. 15, no. 6,
pp. 832–847, Dec. 2011.
[14] Z. Ren, A. Zhang, C. Wen, and Z. Feng, “A scatter learning particle
swarm optimization algorithm for multimodal problems,” IEEE Trans.
Cybern. , vol. 44, no. 7, pp. 1127–1140, Jul. 2014.
[15] J. Li, J. Zhang, C. Jiang, and M. Zhou, “Composite particle swarm opti-
mizer with historical memory for function optimization,” IEEE Trans.
Cybern. , vol. 45, no. 10, pp. 2350–2363, Oct. 2015.
[16] Q. Qin, S. Cheng, Q. Zhang, L. Li, and Y . Shi, “Particle swarm optimiza-
tion with interswarm interactive learning strategy,” IEEE Trans. Cybern. ,
vol. 46, no. 10, pp. 2238–2251, Oct. 2016.
[17] W.-N. Chen et al. , “Particle swarm optimization with an aging leader and
challengers,” IEEE Trans. Evol. Comput. , vol. 17, no. 2, pp. 241–258,
Apr. 2013.
[18] N. Lynn and P. N. Suganthan, “Heterogeneous comprehensive learning
particle swarm optimization with enhanced exploration and exploita-tion,” Swarm Evol. Comput. , vol. 24, pp. 11–24, Oct. 2015.
[19] Y . Liu, X. Yao, Q. Zhao, and T. Higuchi, “Scaling up fast evolutionary
programming with cooperative coevolution,” in Proc. IEEE Congr. Evol.
Comput. , Seoul, South Korea, 2001, pp. 1101–1108.
[20] M. N. Omidvar, X. Li, Y . Mei, and X. Yao, “Cooperative co-evolution
with differential grouping for large scale optimization,” IEEE Trans.
Evol. Comput. , vol. 18, no. 3, pp. 378–393, Jun. 2014.
[21] R. Cheng and Y . Jin, “A social learning particle swarm optimization
algorithm for scalable optimization,” Inf. Sci. , vol. 291, pp. 43–60,
Jan. 2015.[22] S. Mahdavi, M. E. Shiri, and S. Rahnamayan, “Metaheuristics in large-
scale global continues optimization: A survey,” Inf. Sci. , vol. 295,
pp. 407–428, Feb. 2015.
[23] R. Cheng and Y . Jin, “A competitive swarm optimizer for large
scale optimization,” IEEE Trans. Cybern. , vol. 45, no. 2, pp. 191–204,
Feb. 2015.
[24] Q. Yang et al. , “Segment-based predominant learning swarm optimizer
for large-scale optimization,” IEEE Trans. Cybern. , vol. 47, no. 9,
pp. 2896–2910, Sep. 2017.
[25] T. O’Brien and D. Guiney, Differentiation in Teaching and Learning:
Principles and Practice . London, U.K.: Wiley, 2001.
[26] J. C. Richards and W. A. Renandya, Methodology in Language Teaching:
An Anthology of Current Practice . Cambridge, U.K.: Cambridge Univ.
Press, 2002.
[27] K. Tang, X. Li, P. N. Suganthan, Z. Yang, and T. Weise, “Benchmark
functions for the CEC’2010 special session and competition on large-
scale global optimization,” Nat. Inspired Comput. Appl. Lab., Univ. Sci.
Technol. China, Anhui, China, Tech. Rep., 2010.
[28] X. Li, K. Tang, M. N. Omidvar, Z. Yang, and K. Qin, “Benchmark
functions for the CEC’2013 special session and competition on large-scale global optimization,” Evol. Comput. Mach. Learn. Group, RMITUniv., Melbourne, VIC, Australia, Tech. Rep., 2013.
[29] Q. Yang et al. , “Multimodal estimation of distribution algorithms,” IEEE
Trans. Cybern. , vol. 47, no. 3, pp. 636–650, Mar. 2017.
[30] Q. Yang et al. , “Adaptive multimodal continuous ant colony opti-
mization,” IEEE Trans. Evol. Comput. , vol. 21, no. 2, pp. 191–205,
Apr. 2017.
[31] M. A. Potter, “The design and analysis of a computational model
of cooperative coevolution,” Ph.D. dissertation, Dept. Comput. Sci.,
George Mason Univ., Fairfax, V A, USA, 1997.
[32] F. Van den Bergh and A. P. Engelbrecht, “A cooperative approach to
particle swarm optimization,” IEEE Trans. Evol. Comput. , vol. 8, no. 3,
pp. 225–239, Jun. 2004.
[33] X. Li and X. Yao, “Cooperatively coevolving particle swarms for
large scale optimization,” IEEE Trans. Evol. Comput. , vol. 16, no. 2,
pp. 210–224, Apr. 2012.
[34] Y .-J. Shi, H.-F. Teng, and Z.-Q. Li, “Cooperative co-evolutionary dif-
ferential evolution for function optimization,” in Advances in Natural
Computation . Heidelberg, Germany: Springer, 2005, pp. 1080–1088.
[35] Z. Yang, K. Tang, and X. Yao, “Large scale evolutionary opti-
mization using cooperative coevolution,” Inf. Sci. , vol. 178, no. 15,
pp. 2985–2999, 2008.
[36] Z. Yang, K. Tang, and X. Yao, “Multilevel cooperative coevolution
for large scale optimization,” in Proc. IEEE Congr. Evol. Comput. ,
Hong Kong, 2008, pp. 1663–1670.
[37] Y . Sun, M. Kirley, and S. K. Halgamuge, “Extended differential group-
ing for large scale global optimization with direct and indirect variable
interactions,” in Proc. Conf. Genet. Evol. Comput. , Madrid, Spain, 2015,
pp. 313–320.
[38] Y . Mei, M. N. Omidvar, X. Li, and X. Yao, “A competitive divide-
and-conquer algorithm for unconstrained large-scale black-box optimiza-tion,” ACM Trans. Math. Softw. , vol. 42, no. 2, pp. 1–24, 2016.
[39] J. J. Liang and P. N. Suganthan, “Dynamic multi-swarm particle swarm
optimizer with local search,” in Proc. IEEE Congr. Evol. Comput. ,
Edinburgh, U.K., 2005, pp. 522–528.
[40] J. Kennedy and R. Mendes, “Population structure and particle swarm
performance,” in Proc. IEEE Congr. Evol. Comput. , vol. 3. Honolulu,
HI, USA, 2002, pp. 1671–1676.
[41] R. Cheng, C. Sun, and Y . Jin, “A multi-swarm evolutionary framework
based on a feedback mechanism,” in Proc. IEEE Congr. Evol. Comput. ,
Cancún, Mexico, 2013, pp. 718–724.
[42] A. R. Mehrabian and C. Lucas, “A novel numerical optimization algo-
rithm inspired from weed colonization,” Ecol. Informat. , vol. 1, no. 4,
pp. 355–366, 2006.
[43] J. Sun, W. Xu, and B. Feng, “A global search strategy of quantum-
behaved particle swarm optimization,” in Proc. IEEE Conf. Cybern.
Intell. Syst. , Singapore, 2004, pp. 111–116.
[44] K. Lian, X.-Y . Peng, and A. Ouyang, “An efﬁcient and effective algo-
rithm for large scale global optimization problems,” Int. J. Pattern
Recognit. , vol. 29, no. 4, pp. 1–22, 2015.
[45] A. LaTorre, S. Muelas, and J.-M. Peña, “A comprehensive compari-
son of large scale global optimizers,” Inf. Sci. , vol. 316, pp. 517–549,
Sep. 2015.
[46] N. Hansen and A. Ostermeier, “Completely derandomized self-
adaptation in evolution strategies,” Evol. Comput. , vol. 9, no. 2,
pp. 159–195, 2001.
[47] R. Ros and N. Hansen, “A simple modiﬁcation in CMA-ES achieving
linear time and space complexity,” in Parallel Problem Solving From
Nature—PPSN X . Heidelberg, Germany: Springer, 2008, pp. 296–305.
[48] D. Molina, M. Lozano, and F. Herrera, “MA-SW-chains: Memetic algo-
rithm based on local search chains for large scale continuous globaloptimization,” in Proc. IEEE Congr. Evol. Comput. , Barcelona, Spain,
2010, pp. 1–8.594 IEEE TRANSACTIONS ON EVOLUTIONARY COMPUTATION, VOL. 22, NO. 4, AUGUST 2018
[49] A. LaTorre, S. Muelas, and J. M. Peña, “Multiple offspring sampling in
large scale global optimization,” in Proc. IEEE Congr. Evol. Comput. ,
Brisbane, QLD, Australia, 2012, pp. 1–8.
[50] A. LaTorre, S. Muelas, and J.-M. Peña, “Large scale global optimization:
Experimental results with MOS-based hybrid algorithms,” in Proc. IEEE
Congr. Evol. Comput. , 2013, pp. 2742–2749.
[51] J. Brest and M. S. Mauè ˇcec, “Self-adaptive differential evolution algo-
rithm using population size reduction and three strategies,” Soft Comput. ,
vol. 15, no. 11, pp. 2157–2174, 2011.
[52] S.-Z. Zhao, P. N. Suganthan, and S. Das, “Self-adaptive differential
evolution with multi-trajectory search for large-scale optimization,” Soft
Comput. , vol. 15, no. 11, pp. 2175–2185, 2011.
[53] J. Zhang and A. C. Sanderson, “JADE: Adaptive differential evolution
with optional external archive,” IEEE Trans. Evol. Comput. , vol. 13,
no. 5, pp. 945–958, Oct. 2009.
[54] M. Z. Ali, N. H. Awad, and P. N. Suganthan, “Multi-population differen-
tial evolution with balanced ensemble of mutation strategies for large-scale global optimization,” Appl. Soft Comput. , vol. 33, pp. 304–327,
Aug. 2015.
[55] M. Campos, R. A. Krohling, and I. Enriquez, “Bare bones particle swarm
optimization with scale matrix adaptation,” IEEE Trans. Cybern. , vol. 44,
no. 9, pp. 1567–1578, Sep. 2014.
[56] R. A. Krohling and E. Mendel, “Bare bones particle swarm optimization
with Gaussian or Cauchy jumps,” in Proc. IEEE Congr. Evol. Comput. ,
Trondheim, Norway, 2009, pp. 3285–3291.
[57] S.-Z. Zhao, J. J. Liang, P. N. Suganthan, and M. F. Tasgetiren, “Dynamic
multi-swarm particle swarm optimizer with local search for large scaleglobal optimization,” in Proc. IEEE Congr. Evol. Comput. , Hong Kong,
2008, pp. 3845–3852.
[58] J. Kennedy, “Stereotyping: Improving particle swarm performance
with cluster analysis,” in Proc. IEEE Congr. Evol. Comput. , 2000,
pp. 1507–1512.
[59] S. Janson and M. Middendorf, “A hierarchical particle swarm optimizer
and its adaptive variant,” IEEE Trans. Syst., Man, Cybern. B, Cybern. ,
vol. 35, no. 6, pp. 1272–1282, Dec. 2005.
[60] Y . V . Pehlivanoglu, “A new particle swarm optimization method
enhanced with a periodic mutation strategy and neural networks,” IEEE
Trans. Evol. Comput. , vol. 17, no. 3, pp. 436–452, Jun. 2013.
[61] C. Segura, C. A. C. Coello, E. Segredo, and A. H. Aguirre, “A novel
diversity-based replacement strategy for evolutionary algorithms,” IEEE
Trans. Cybern. , vol. 46, no. 12, pp. 3233–3246, Dec. 2016.
[62] O. Olorunda and A. P. Engelbrecht, “Measuring exploration/exploitation
in particle swarms using swarm diversity,” in Proc. IEEE Congr. Evol.
Comput. , Hong Kong, 2008, pp. 1128–1134.
Qiang Yang (S’14) received the M.S. degree from
Sun Yat-sen University, Guangzhou, China, in 2014,where he is currently pursuing the Ph.D. degree.
He is currently a Research Assistant with the
School of Computer Science and Engineering, South
China University of Technology, Guangzhou. Hiscurrent research interests include evolutionary com-putation algorithms and their applications on real-
world problems, large-scale optimization algorithms,
multimodal optimization algorithms, distributed evo-lutionary algorithms, and their applications on
real-world problems.
Wei-Neng Chen (S’07–M’12–SM’17) received the
bachelor’s and Ph.D. degrees from Sun Yat-senUniversity, Guangzhou, China, in 2006 and 2012,respectively.
He is currently a Professor with the School
of Computer Science and Engineering, SouthChina University of Technology, Guangzhou. He
has published over 70 papers in international jour-
nals and conferences, including over 20 papers inthe IEEE T
RANSACTIONS . His current research
interests include swarm intelligence algorithms and
their applications in cloud computing, operations research, and software
engineering.
Dr. Chen was a recipient of the IEEE Computational Intelligence Society
Outstanding Dissertation Award in 2016, and the National Science Fund for
Excellent Young Scholars in 2016.
Jeremiah Da Deng (M’00) received the B.E.
degree from the University of Electronic Scienceand Technology of China, Chengdu, China, in1989, and the M.Eng. and D.Eng. degrees from
the South China University of Technology (SCUT),
Guangzhou, China, in 1992 and 1995, respec-tively, the latter co-supervised by the University ofHong Kong, Hong Kong.
Since 1995, he has been a Lecturer with SCUT,
and then joined the University of Otago, Dunedin,New Zealand, in 1999, as a Post-Doctoral Research
Fellow, where he is currently an Associate Professor with the Department of
Information Science. He has published around 100 refereed research papersin international conference proceedings and journals. His current researchinterests include machine learning, pattern recognition, and modeling and
optimization of computer networks.
Yun Li (S’87–M’90–SM’17) received the B.S.
degree in radio electronics science from Sichuan
University, Chengdu, China, in 1984, the M.Eng.
degree in electronic engineering from the Universityof Electronic Science and Technology of China,Chengdu, in 1987, and the Ph.D. degree in par-
allel processing for control engineering from the
University of Strathclyde, Glasgow, U.K., in 1990.
From 1989 to 1990, he was with the U.K. National
Engineering Laboratory, Glasgow, and Industrial
Systems and Control Ltd., Glasgow. He joined the
University of Glasgow, Glasgow, as a Lecturer in 1991. He served as the two-year Founding Director of the University of Glasgow Singapore, Singapore,
from 2011 to 2013. He developed one of the world’s ﬁrst 30 evolutionary
computation courses in 1995 and the popular online interactive coursewareGA demo in 1997. He has supervised over 30 Ph.D. students in computationalintelligence and has 250 publications.
Prof. Li established Evolutionary Computation Workgroups for the IEEE
Control System Society and the European Network of Excellence inEvolutionary Computing (EvoNet) in 1998. He served on the ManagementBoard of EvoNet from 2000 to 2005. He is a Chartered Engineer in the U.K.
Tianlong Gu received the M.Eng. degree from
Xidian University, Xi’an, China, in 1987, and thePh.D. degree from Zhejiang University, Hangzhou,
China, in 1996.
From 1998 to 2002, he was a Research Fellow
with the School of Electrical and ComputerEngineering, Curtin University of Technology, Perth,
WA, Australia, and a Post-Doctoral Fellow with
the School of Engineering, Murdoch University,Perth. He is currently a Professor with the School
of Computer Science and Engineering, Guilin
University of Electronic Technology, Guilin, China. His current researchinterests include formal methods, data and knowledge engineering, softwareengineering, and information security protocol.
Jun Zhang (M’02–SM’08–F’17) received the Ph.D.
degree in electrical engineering from the CityUniversity of Hong Kong, Hong Kong, in 2002.
From 2004 to 2016, he was a Professor with
Sun Yat-sen University, Guangzhou, China. Since2016, he has been with South China Universityof Technology, Guangzhou, where he is currently
a Cheung Kong Chair Professor. His current research
interests include computational intelligence, cloudcomputing, big data, high performance computing,data mining, wireless sensor networks, operations
research, and power electronic circuits. He has authored seven research books
and book chapters, and over 100 technical papers in the above areas.
Prof. Zhang was a recipient of the China National Funds for Distinguished
Young Scientists from the National Natural Science Foundation of China in
2011, and the First-Grade Award in Natural Science Research from theMinistry of Education, China, in 2009. He is currently an AssociateEditor of the IEEE T
RANSACTIONS ON EVOLUTIONARY COMPUTATION ,
the IEEE T RANSACTIONS ON INDUSTRIAL ELECTRONICS , and the IEEE
TRANSACTIONS ON CYBERNETICS . He is the Founding and Current
Chair of the IEEE Guangzhou Subsection, the IEEE Beijing (Guangzhou)Section Computational Intelligence Society Chapters, and the ACM
Guangzhou Chapter.