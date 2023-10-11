/* URI 2609 – Produtos por categoria */

SELECT Categories.name, SUM(Products.amount) as Tot
FROM Categories
JOIN Products ON Products.id_categories = Categories.id
GROUP BY Categories.name

  
/* URI 2617 – Fornecedor Ajax SA */

SELECT Products.name, Providers.name
FROM Products
JOIN Providers ON Providers.id = Products.id_providers
WHERE Providers.name LIKE 'Ajax SA';


/* URI 2618 – Produtos Importados */

SELECT Products.name, Providers.name, Categories.name
FROM Categories
JOIN Products ON Products.id_categories = Categories.id
JOIN Providers ON Providers.id = Products.id_providers
WHERE Categories.name LIKE 'Super Luxury' AND Providers.name LIKE 'Sansul SA';


/* URI 2619 – Super Luxo */

SELECT Products.name, Providers.name, Products.price 
FROM Products 
JOIN Providers ON ( Providers.id = Products.id_providers )
JOIN Categories ON ( Categories.id = Products.id_categories )
WHERE Products.price > 1000.0 AND Categories.name LIKE 'Super Luxury';


/* URI 2621 – Quantidades entre 10 e 20 */

SELECT Products.name
FROM Products
JOIN Providers ON Providers.id = Products.id_providers
WHERE Products.amount BETWEEN 10 AND 20
AND Providers.name LIKE 'P%';


/* URI 2623 – Categorias com Vários Produtos */

SELECT Products.name, Categories.name
FROM Products
JOIN Categories ON Categories.id = Products.id_categories
WHERE Products.amount > 100
AND Categories.id IN (1, 2, 3, 6, 9)
ORDER BY Categories.id;


/* URI 2989 – Departamentos e Divisões */

SELECT 
Departamento.nome AS departamento, Divisao.nome AS divisao, round(avg(salarios.salario), 2) AS media,
round(max(salarios.salario), 2) AS maior
FROM
(
  SELECT
  grupo_venc.lotacao, grupo_venc.lotacao_div, round(sum(total_vencimentos) - coalesce(sum(total_descontos), 0), 2) 
  AS salario
  FROM (
    SELECT
    Empregado.matr, Empregado.lotacao, Empregado.lotacao_div, coalesce(sum(Vencimento.valor), 0) AS total_vencimentos
    FROM Empregado
    LEFT JOIN Emp_venc ON Empregado.matr = Emp_venc.matr
    LEFT JOIN Vencimento ON Emp_venc.cod_venc = Vencimento.cod_venc
    GROUP BY Empregado.matr, Empregado.lotacao, Empregado.lotacao_div
  ) AS grupo_venc
  LEFT JOIN
  (
    SELECT
    Empregado.matr, Empregado.lotacao, Empregado.lotacao_div, coalesce(sum(Desconto.valor), 0) AS total_descontos
    FROM Empregado
    LEFT JOIN Emp_desc ON Empregado.matr = Emp_desc.matr
    LEFT JOIN Desconto ON Emp_desc.cod_desc = Desconto.cod_desc
    GROUP BY Empregado.matr, Empregado.lotacao, Empregado.lotacao_div
  ) AS grupo_desc
  ON grupo_venc.matr = grupo_desc.matr
  GROUP BY grupo_venc.matr, grupo_venc.lotacao, grupo_venc.lotacao_div
) AS salarios
INNER JOIN departamento ON salarios.lotacao = departamento.cod_dep
INNER JOIN divisao ON salarios.lotacao_div = divisao.cod_divisao
GROUP BY divisao.nome, departamento.nome
ORDER BY media DESC


/* URI 2991 – Estatísticas dos Departamentos */

SELECT Departamento.nome AS "Nome Departamento", COUNT(salarios.lotacao) AS "Numero Empregados",
ROUND(AVG(salarios.salario), 2) AS "Media Salarial", ROUND(MAX(salarios.salario), 2) AS "Maior Salario",
ROUND(MIN(salarios.salario), 2) AS "Menor Salario"
FROM
(
  SELECT grupo_venc.lotacao, ROUND(SUM(total_venc) - COALESCE(SUM(total_desc), 0), 2) AS salario
  FROM
  (
    SELECT Empregado.matr, Empregado.lotacao, COALESCE(SUM(Vencimento.valor), 0) AS total_venc
  	FROM Empregado
  	LEFT JOIN Emp_venc ON Empregado.matr = Emp_venc.matr
  	LEFT JOIN Vencimento ON Emp_venc.cod_venc = Vencimento.cod_venc
  	GROUP BY Empregado.matr, Empregado.lotacao
  ) AS grupo_venc
  LEFT JOIN 
  (
    SELECT Empregado.matr, Empregado.lotacao, COALESCE(SUM(Desconto.valor), 0) AS total_desc
    FROM Empregado
    LEFT JOIN Emp_desc ON Empregado.matr = Emp_desc.matr
    LEFT JOIN Desconto ON Emp_desc.cod_desc = Desconto.cod_desc
    GROUP BY Empregado.matr, Empregado.lotacao
  ) AS grupo_desc
  ON grupo_venc.matr = grupo_desc.matr
  GROUP BY grupo_venc.matr, grupo_venc.lotacao
) AS salarios
INNER JOIN Departamento ON salarios.lotacao = Departamento.cod_dep
GROUP BY Departamento.nome
ORDER BY "Media Salarial" DESC


/* URI 2992 – Divisões com Maiores Médias Salariais */

WITH media_salarial_div AS
(
  SELECT salarios.lotacao, salarios.lotacao_div, ROUND(AVG(salarios.salario), 2) AS media
  FROM
  (
    SELECT grupo_venc.lotacao, grupo_venc.lotacao_div, ROUND(SUM(total_venc) - COALESCE(SUM(total_desc), 0), 2) AS salario
    FROM
    (
      SELECT Empregado.matr, Empregado.lotacao, Empregado.lotacao_div, COALESCE(SUM(Vencimento.valor), 0) AS total_venc
      FROM Empregado
      LEFT JOIN Emp_venc ON Empregado.matr = Emp_venc.matr
      LEFT JOIN Vencimento ON Emp_venc.cod_venc = Vencimento.cod_venc
      GROUP BY Empregado.matr, Empregado.lotacao, Empregado.lotacao_div
    ) AS grupo_venc
    LEFT JOIN
    (
      SELECT Empregado.matr, Empregado.lotacao, Empregado.lotacao_div, COALESCE(SUM(Desconto.valor), 0) AS total_desc
      FROM Empregado
      LEFT JOIN Emp_desc ON Empregado.matr = Emp_desc.matr
      LEFT JOIN Desconto ON Emp_desc.cod_desc = Desconto.cod_desc
      GROUP BY Empregado.matr, Empregado.lotacao, Empregado.lotacao_div
    ) AS grupo_desc
    ON grupo_venc.matr = grupo_desc.matr
    GROUP BY grupo_venc.matr, grupo_venc.lotacao, grupo_venc.lotacao_div
  ) AS salarios
  GROUP BY salarios.lotacao, salarios.lotacao_div
)
SELECT Departamento.nome, Divisao.nome, media_salarial_div.media AS media
FROM media_salarial_div
INNER JOIN Departamento ON media_salarial_div.lotacao = Departamento.cod_dep
INNER JOIN Divisao ON media_salarial_div.lotacao_div = Divisao.cod_divisao
WHERE media IN (SELECT MAX(media) OVER (PARTITION BY lotacao) FROM media_salarial_div)
ORDER BY media DESC


/* URI 2997 – Pagamento dos Empregados */

SELECT Departamento.nome, Empregado.nome, comp_salarios.total_venc AS "Salario Bruto",
comp_salarios.total_desc AS "Total Desconto", comp_salarios.salario AS "Salario Liquido"
FROM
(
  SELECT grupo_venc.lotacao, grupo_venc.matr, grupo_venc.total_venc, grupo_desc.total_desc,
  ROUND(SUM(total_venc) - COALESCE(SUM(total_desc),0), 2) AS salario
  FROM
  (
    SELECT Empregado.matr, Empregado.lotacao, COALESCE(SUM(Vencimento.valor), 0) AS total_venc
    FROM Empregado
    LEFT JOIN Emp_venc ON Empregado.matr = Emp_venc.matr
    LEFT JOIN Vencimento ON Emp_venc.cod_venc = Vencimento.cod_venc
    GROUP BY Empregado.matr, Empregado.lotacao
  ) AS grupo_venc
  LEFT JOIN
  (
    SELECT Empregado.matr, Empregado.lotacao, COALESCE(SUM(Desconto.valor), 0) AS total_desc
    FROM Empregado
    LEFT JOIN Emp_desc ON Empregado.matr = Emp_desc.matr
    LEFT JOIN Desconto ON Emp_desc.cod_desc = Desconto.cod_desc
    GROUP BY Empregado.matr, Empregado.lotacao
  ) AS grupo_desc
  ON grupo_venc.matr = grupo_desc.matr
  GROUP BY grupo_venc.matr, grupo_venc.lotacao, grupo_venc.total_venc, grupo_desc.total_desc
) AS comp_salarios
INNER JOIN Departamento ON comp_salarios.lotacao = Departamento.cod_dep
INNER JOIN Empregado ON comp_salarios.matr = Empregado.matr
ORDER BY salario DESC


/* URI 2999 – Maior Salário da Divisão */

WITH salarios AS
(
  SELECT grupo_venc.matr, grupo_venc.lotacao_div, ROUND(SUM(total_venc) - COALESCE(SUM(total_desc), 0), 2) AS salario
  FROM
  (
    SELECT Empregado.matr, Empregado.lotacao_div, COALESCE(SUM(Vencimento.valor), 0) AS total_venc
    FROM Empregado
    LEFT JOIN Emp_venc ON Empregado.matr = Emp_venc.matr
    LEFT JOIN Vencimento ON Emp_venc.cod_venc = Vencimento.cod_venc
    GROUP BY Empregado.matr, Empregado.lotacao_div
  ) AS grupo_venc
  LEFT JOIN
  (
    SELECT Empregado.matr, Empregado.lotacao_div, COALESCE(SUM(Desconto.valor), 0) AS total_desc
    FROM Empregado
    LEFT JOIN Emp_desc ON Empregado.matr = Emp_desc.matr
    LEFT JOIN Desconto ON Emp_desc.cod_desc = Desconto.cod_desc
    GROUP BY Empregado.matr, Empregado.lotacao_div
  ) AS grupo_desc
  ON grupo_venc.matr = grupo_desc.matr
  GROUP BY grupo_venc.matr, grupo_venc.lotacao_div
), media_salarial_div AS
(
  SELECT lotacao_div, AVG(salario) AS salario_medio
  FROM salarios
  GROUP BY lotacao_div
)
SELECT Empregado.nome, salarios.salario
FROM salarios
INNER JOIN media_salarial_div ON salarios.lotacao_div = media_salarial_div.lotacao_div
AND salarios.salario > media_salarial_div.salario_medio
INNER JOIN Empregado ON salarios.matr = Empregado.matr
ORDER BY salarios.salario DESC
