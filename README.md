<!-- antes de enviar a versão final, solicitamos que todos os comentários, colocados para orienta?ão ao aluno, sejam removidos do arquivo -->
<meta charset="UTF-8">

# Utilização de Técnicas de Aprendizado não Supervisionado para Classificação de Unidade Mecânicas em Maciço Rochoso

#### Aluno: [Thiago da Cruz Falcão](https://github.com/thiago85falcao/).
#### Orientador: [Leonardo Alfredo Forero Mendoza](https://github.com/link_do_github).

------

Trabalho apresentado ao curso [BI MASTER](https://ica.puc-rio.ai/bi-master) como pré-requisito para conclusão de curso e obtenção de crédito na disciplina "Projetos de Sistemas Inteligentes de Apoio à Decisão".

- [Repositório Códigos - GIT](https://github.com/thiago85falcao/Projeto_Final_BIMaster). <!-- caso não aplicável, remover esta linha -->

------

### Resumo

<!-- trocar o texto abaixo pelo resumo do trabalho, em portugu?s -->
<div class=text-justify>
A classificação de maciços rochosos é um tema da mecânica de rochas de extrema relevância para as atividades de geologia de engenharia tais como analise de estabilidade de taludes, perfuração de túneis, assentamento de fundações de grandes estruturas como barragens hidrelétricas, perfuração de poços de petróleo, entre outros.

Este trabalho tem como objetivo buscar uma alternativa para a classificação de rochas intactas propostas por Deere & miller, 1966. Onde a partir da correlação de valores das propriedades mecânicas UCS (Unconfined Compressive Strength) e E (Young's Modulus), em um gráfico bi-dimensional, os autores classificam as amostras em 15 classes diferentes. Tal classificação é feita de forma manual e não leva em conta outras propriedades intrínsecas do material que por ventura possa ser utilizada para uma melhor discretização dos grupos, fazendo com que possamos aplicar técnicas de aprendizado de máquina na tentativa de automatizar o processo de classificação e também incluir outros parâmetros que de forma manual tornam-se bastante trabalhosa a sua análise.

Para atacar o problema, foram utilizados dados de perfis elétricos que medem propriedades intrínsecas do maciço, tais como radioatividade, densidade, velocidade e porosidade. Estas propriedades foram transformadas em propriedades mecânicas através de fórmulas empíricas coletadas da literatura, em seguida foi seguido um fluxo de trabalho de análise exploratória dos dados de forma a prepara-lo para a utilização de métodos não supervisionados de aprendizado de máquina para a identificação de clusters e a classificação automática.

No primeiro momento, foram utilizados somente as propriedades de UCS e E, de tal forma que o método pudesse replicar de alguma forma a classificação de Deere & Miller, 1966.
Foram utilizados os métodos K-means, DBSCAN, Agglomerative Hierarchy, Meansshift, TSN-e e PCA através da biblioteca Scikit Learn.

Os primeiros resultados mostraram que o k-means é o método mais rápido e que melhor se ajusta a classificação manual de Deere & Miller, quando utilizamos apenas duas propriedades. Contudo este trabalho ainda carece de uma alternativa para mensuração da acurácia e/ou de qual método de fato representa grupos distintos do comportamento do maciço rochoso.
Os resultados com TSN-e e PCA, utilizando o dado RAW (perfis) mais os perfis secundários (Propriedades Mecânicas), mostraram um resultado interessante principalmente quando visualizados no gráfico 3D (UCS, E, VpVs). Em ambos os casos, as melhores reduções foram para 3 componentes, e para o TSNe, os melhores valores de perplexidade de no mínimo 50, pois os valores menores resultam em uma nuvem mais aglutinada.
Portanto, foi visualizado que a classificação tradicional de Deere&Miller, 1966. mostra uma quantidade de classes ainda muito grande para o dataset utilizado, sendo a metodologia pca/TSN-e + K-means desenvolvida por esse trabalho sugere trabalharmos com 5 classes o que pode ser um indicativo de simplificação e consequentemente possibilitar um entendimento do comportamento do maciço de forma rápida e intuitiva.

Contudo, para um melhor entendimento do comportamento de cada classe, este trabalho sugere correlacionar a classificação automática de classes, com uma propriedades medias de cada classe com uma simulação numérica que permita compreender os mecanismos de deformação do material predominantes em cada classe, para uma mesma condição de carga.</div>

------

Matrícula: 192.190.087

Pontifícia Universidade Católica do Rio de Janeiro

Curso de Pós Graduação *Business Intelligence Master*
