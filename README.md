# BOT_WS
Projeto de automatização.

# ---------
# Base
# ---------

🤖 Bot 1 – Monitor de Promoções

Você cadastra produtos, palavras-chave ou categorias.
O bot consulta APIs/lojas de tempos em tempos.
Compara o preço atual com o último.
Se caiu → gera postagem.
Se igual/subiu → só atualiza, não posta.
Posta apenas promoções reais.

🤖 Bot 2 – Criador de Postagens
Você envia o link ou termo.
O bot busca título, preço e imagem.
Insere automaticamente o link de afiliado.
Monta a postagem (imagem + legenda + botão).
Te entrega pronto ou publica no grupo.

🤖 Bot 3 – Bot Unificado (junção do 1 + 2)
Une os dois modos em um só bot.
Modo manual: você manda link/termo e recebe o post pronto (como o Bot 1).
Modo automático: você cadastra produtos/categorias e o bot posta sozinho 
quando o preço cai (como o Bot 2).
Tudo integrado em um único painel:
Cadastro de afiliados (IDs por loja).
Histórico de postagens.
Métricas de desempenho.
Flexibilidade: tanto para uso próprio quanto para oferecer a clientes.


# ----------
# API
# ----------
- Mercado Livre: https://developers.mercadolivre.com.br/pt_br/itens-e-buscas
- Shopee: https://open.shopee.com/
- Casas Bahia: https://developers.grupocasasbahia.com.br/marketplace/docs/entenda-a-api
- Aliexpress: https://openservice.aliexpress.com/doc/api.htm#/api?cid=3&path=/auth/token/security/create&methodType=GET/POST
- Magazine Luiza: https://developers.magalu.com/
- Amazon: https://developer-docs.amazon.com/sp-api/reference/getordermetrics

# ----------
# Servidor
# ----------


# ---------
# Template
# ---------
Dê uma olhada em Fritadeira Sem 
Óleo AirFryer HQ 4,8 litros Digital Preto HQ-AF4.8LDP 
por R$158,00. Compre na Shopee agora! 
https://s.shopee.com.br/9AF6RytJ53?share_channel_code=1



Notebook Gamer Dell G15-i1300-D35P 15.6" FHD 13ª Geração Intel Core i5 16GB 512GB SSD NVIDIA RTX 3050 Linux

Notebook Gamer Dell G15-i1300-D35P 15.6" FHD 13ª Geração Intel Core i5 16GB 512GB SSD NVIDIA RTX 3050 Linux

Notebook Gamer Dell G15 i5 13450HX RTX4050 6GB 16GB de RAM Tela 120Hz FULL HD HDR Teclado RGB

soluções:

combinar os dois:

1 - Tokenização e interseção de palavras
Dividir o título em tokens (palavras).
Contar quantas palavras batem entre as lojas.
Calcular uma similaridade (ex.: Jaccard ou Cosine Similarity).
Assim você mede: quanto mais palavras iguais, maior a chance de ser o mesmo produto.

2 - Identificadores únicos
Algumas lojas já disponibilizam identificadores confiáveis:
EAN/GTIN/UPC (código de barras do produto).
Modelo do fabricante.
ASIN (Amazon).
Se você conseguir extrair esse campo da API, é a melhor forma de bater os produtos sem depender do título.

Se tiver EAN/GTIN/Modelo, usa isso para “match exato”.
Caso contrário, aplica similaridade de texto (tokenização ou embeddings).
Se a similaridade ficar abaixo de um certo limite (threshold, ex.: 0.75), marca como “possível outro produto” e não compara preços.
