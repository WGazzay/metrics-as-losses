# sigmoidF1: A Smooth F1 Score Surrogate Loss for Multilabel Classification

> Gabriel Bénédict, Hendrick Vincent Koops, Daan Odijk, Maarten de Rijke

*Abstract*

Multilabel classification is the task of attributing multiple labels to examples via predictions. 
Current models formulate a reduction of the multilabel setting into either multiple binary classifications or multiclass classification, allowing for the use of existing loss functions (sigmoid, cross-entropy, logistic, etc.). 
These multilabel classification reductions do not accommodate for the prediction of varying numbers of labels per example. Moreover, the loss functions are distant estimates of the performance metrics. 
We propose \emph{sigmoidF1}, a loss function that is an approximation of the F1 score that (i) is smooth and tractable for stochastic gradient descent, (ii) naturally approximates a multilabel metric, and (iii) estimates both label suitability and label counts. 
We show that any confusion matrix metric can be formulated with a smooth surrogate. 
We evaluate the proposed loss function on text and image datasets, and with a variety of metrics, to account for the complexity of multilabel classification evaluation. 
sigmoidF1 outperforms other loss functions on one text and two image datasets over several metrics. 
These results show the effectiveness of using inference-time metrics as loss functions for non-trivial classification problems like multilabel classification. 

## Citation

```
@article{sigmoidF1,
  author    = {Gabriel B{\'{e}}n{\'{e}}dict and
               Vincent Koops and
               Daan Odijk and
               Maarten de Rijke},
  title     = {sigmoidF1: {A} Smooth {F1} Score Surrogate Loss for Multilabel Classification},
  year      = {2021},
  url       = {https://arxiv.org/abs/2108.10566},
  eprinttype = {arXiv},
  eprint    = {2108.10566},
}
```
