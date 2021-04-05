
## Definition of Marcov

The next state $s_{t+1}$ of a system only depends on the current state $s_t$, rather than previous states.

define:
state is Marcov if and only if $P[s_{t+1}|s_t] = P[s_{t+1}|s_1, ..., s_t]$

Marcov property describes every state, but the most important is how to describe the states squence. Mathematically, random process is used to describe the squence of random variables. If every state of a random variable in their squence has Marcov property, this process is call Marcov Process.

## Definition of Marcov Process(MP)
MP is two element set $(S, P)$, it satisfies $S$ is a finite set and $P$ is a state transfer probability matrix, this is:
$$
  \begin{matrix}
   P_{11} & \cdots & P_{1n} \\
    \vdots & \vdots &  \vdots \\
   P_{n1} & \cdots & P_{nn}
  \end{matrix} \tag{1}
$$

Given state transfer probability matrix, we can always get the Marcov Chain. However, Marcov Process can not describe the interaction between action and environment and get reward from environment. This lead to Marcov Decision Process (MDP), which can take action(policy) and reward into Marcov Process.

## Definition of Marcov Decision Process (MDP)
 
MDP can be described as a set $(A, A, P, R, \gamma)$, where $S$ is finite state set, $A$ is finite action set, $p$ is state transfer probability, $\gamma$ is discount factor used to calculate cumulative rewards. Different from MP, state transfer probability takes action into accout, that is,

 $P^a_{ss^{\prime}} = P[S_{t+1 = s^{\prime}}|S_t = s, A_t = a]$

 Reinforcement Learning seeks to find the optimal policy in a Marcov Decision Process. Policy is a mapping from state to action, which is always denoted as $\pi$. It is the action distribution given a state $s$.
 $\pi(a|s) = p[A_t = a|S_t=s]$. If $\pi$ is definite, then the action is definte when given a state.

 For instance, a policy is $\pi_1(play|s_1) = 0.8$ means the probality of playing is 0.8 in state $s_1$, not playing is 0.2.

 Reinforcement Learning is the find an optimal policy that can give the most cumulative reward.

 When the policy $\pi$ is given, we can calculate the cumulative reward. First we define the cumulative reward as:
$$
G_t = R_{t+1} + \gamma R_{t+2} + \cdots = \sum^\infin_{k=0} \gamma_k R_{t+k+1} 

\tag{2}
$$

Assume we have some squence of states, if we start from $s_1$:
$$
s_1 \rightarrow s_2 \rightarrow s_3 \rightarrow s_4 \rightarrow s_5;
\\
s_1 \rightarrow s_2 \rightarrow s_3 \rightarrow s_5
\\
\cdots \cdots
$$

Under the given policy $\pi$, we calculate the cumulative reward $G_1$ according to $(2)$, and it may have several values. Due to the policy $\pi$ is random, the cumulative reward $G_1$ is also random. In order to evalutate $s_1, we should define how to describe the value of $s_1$. It is natural to use the cumulative reward to evaluate $s_1$. As we analyse above, the cumulative reward $G_1$ is random, and thus intractable, we instead use its expected value. The function to evalute the value of state using expected cumulative reward is called State Value Function.

## Definition if State Value Function
Generally, when an agent takes a policy, the cumulative reward is a distribution, and its expected value at state $s$ can be defined as:

$$
\upsilon_\pi (s) = E_\pi [\sum^\infin_{k=0}\gamma^kR_{t+k+1}|S_t=s] \tag{3}
$$

This function depends on policy $\pi$, as $\pi$ determines the distribution of cumulative reward $G$

We can further define the State-Action Value Function:
$$
q_\pi(s, a) = E_\pi [\sum^\infin_{k=0}\gamma^kR_{t+k+1}|S_t=s, A_t = a] \tag{4}
$$

In practice, we usually use Bellman equation to formulate State Value Function and State-Action Value Function
## Bellman Equation 

According to $(2)$ and $(3)$, we can get Bellman equation of State Value Function:
$$
\begin{aligned}
\upsilon(s) = & E[G_t|S_t = s] \\
= & E[R_{t+1} + \gamma R_{t+2} + \cdots|S_t = s] \\
= & E[R_{t+1} + \gamma (R_{t+2} + \gamma R_{t+3} + \cdots) | S_t = s] \\
= & E[R_{t+1} + \gamma G_{t+1} | s_t = s] \\
= & E[R_{t+1} + \gamma \upsilon(S_{t+1}) | S_t = s] \\  
\end{aligned} \tag{5}
$$

Similarly, the Bellman equation of State-Action Value Function is:

$$
q_\pi(s, a) = E_\pi [R_{t+1} + \gamma q(S_{t+1}) + \gamma(S_{t+1}, A_{t+1}) | S_t = s, A_t = a] \tag{6}
$$










 



