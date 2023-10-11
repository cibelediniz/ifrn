/*Escreva um comando que exiba o código, o nome e o percentual de comissão dos corretores em ordem decrescente de percentual de comissão.*/

SELECT [CodCorretor], [Corretor], [Comissao]
FROM [dbo].[Corretor]
ORDER BY [Comissao] DESC;


/* Escreva um comando que exiba o código e a descrição dos imóveis com uma área construída compreendida entre uma faixa (valor inicial e valor final) fornecida como parâmetro, ordenado pela descrição do imóvel. */

DECLARE @ValorInicial DECIMAL(18, 2) = 100/* valor inicial entre 100 e 200 */;
DECLARE @ValorFinal DECIMAL(18, 2) = 150/* valor final entre 100 e 200 */;

SELECT [CodImovel], [Imovel]
FROM [dbo].[Imovel]
WHERE [AreaConstruida] BETWEEN @ValorInicial AND @ValorFinal
ORDER BY [Imovel];


/*Escreva um comando que exiba o nome da zona e a quantidade de bairros cadastrados em cada zona, ordenado por nome de zona.*/

SELECT Z.[Zona], COUNT(B.[CodBairro]) AS QuantidadeDeBairros
FROM [dbo].[Zona] AS Z
LEFT JOIN [dbo].[Bairro] AS B ON Z.[CodZona] = B.[CodZona]
GROUP BY Z.[Zona]
ORDER BY Z.[Zona];


/*Escreva um comando que exiba o código, a descrição, a cidade e o estado dos imóveis ordenados por estado e cidade.*/

SELECT [CodImovel], [Imovel], [Cidade], [Estado]
FROM [dbo].[Imovel]
ORDER BY [Estado], [Cidade];


/* Escreva um comando que exiba o código, a descrição, a área construída e o preço de venda dos imóveis em ordem decrescente de preço por metro de área construída. */

SELECT [CodImovel], [Imovel], [AreaConstruida], [PrecoVenda]
FROM [dbo].[Imovel]
ORDER BY ([PrecoVenda] / [AreaConstruida]) DESC;



/* Escreva um comando que exiba as cidades e o valor total dos imóveis existentes em cada cidade, listando apenas as cidades com mais de um imóvel. */

SELECT [Cidade], SUM([PrecoVenda]) AS ValorTotal
FROM [dbo].[Imovel]
GROUP BY [Cidade]
HAVING COUNT(*) > 1;


/* Escreva um comando para apagar os corretores que não realizaram vendas. */

DELETE FROM [dbo].[Corretor]
WHERE [CodCorretor] NOT IN (SELECT DISTINCT [CodCorretor] FROM [dbo].[Venda]);


/* Escreva um comando para inserir um novo corretor. */

INSERT INTO [dbo].[Corretor] ([CodCorretor], [Corretor], [Comissao])
VALUES (6, 'NOME DO NOVO CORRETOR', 2.5);

