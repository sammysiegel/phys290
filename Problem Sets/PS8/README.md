# PHYS 290 Problem Set 6

I'm thinking about what the expected value of $k$ should be for LinearFit.py.
The intercept is the standard deviation of our $\pi$ measurement when $\log(N) = 0$; that is, when $N=
1$. But that is akin to asking what the standard deviation is when I draw $x$ randomly from $[0,1]$
and compute $f(x) = 4\sqrt{1-x^2}$. We know that the standard deviation is given by 
$$\sigma^2 = \left\langle f(x)^2 \right\rangle - \left\langle f(x) \right\rangle^2.$$
Well, we know $\left\langle f \right\rangle = \pi$, and we can compute $\left\langle f^2 \right\rangle$ by the integral:
$$ \left\langle f^2 \right\rangle = \int_0^1 \left(4\sqrt{1-x^2}\right)^2\,\mathrm{d}x = 16 \int_0^1 1-x^2 \,\mathrm{d}x = 16 - \frac{16}{3}=\frac{32}{3}.$$
So $$\sigma = \sqrt{\frac{32}{3} - \pi^2} \approx 0.893$$
The intercept is $k= \log(\sigma)$, so the expected value of $k$ is $\left\langle k \right\rangle \approx -0.11$.

### Honor Code
*I affirm that I have adhered to the honor code on this assignment.*  
**Sammy Siegel**, 16 March 2023

I made use of Github Copilot to help me autocomplete comments for the code. I also used numpy and matplotlib documentation.