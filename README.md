# Godoy Auto Detailing — Website (v2, baseado no site atual)

Esta versão foi reconstruída usando o conteúdo real do seu site atual (godoyautodetailing.com): logo, preços exatos, listas completas de "What's Included", parceria SONAX, depoimentos reais do Google, FAQ e fotos reais dos carros.

## ⚠️ Importante: parte das imagens ainda está "hotlinked"

10 fotos da galeria (as que você mandou por upload: Mini, Range Rover, Porsche, Lexus, BMW M3, Volvo, Mercedes, BMW X5, Jaecoo, BMW Touring) já estão salvas localmente em `images/gallery/` — essas já são 100% independentes do site antigo.

O que ainda falta trazer pra local: logo, foto do hero, badges SONAX e as 9 fotos originais da galeria (as que vieram do site atual). Essas continuam carregando direto de `https://www.godoyautodetailing.com/assets/...`. Funciona enquanto o site atual estiver no ar, mas **antes de desligá-lo**, me manda esses arquivos (ou baixe e coloque em `images/`) que eu troco os `src` pra caminhos locais.

## O que mudou nesta versão

- **Preços reais** de cada serviço (Maintenance Valet £70, Interior Deep Clean £90, Full Deep Clean £140, Enhancement Detail £350, Ceramic Coating desde £250, Multi-Stage Correction sob orçamento) com a lista completa de "What's Included" de cada pacote.
- **Seção SONAX** dedicada, com os badges "Professional Detailer" e "Made in Germany".
- **Depoimentos reais do Google** (Franci Feitosa, Patricia Machado, Jucelino Macedo) com nota 5.0 e link para todas as avaliações.
- **Galeria** com fotos reais de trabalhos (G-Wagon, Defender, Ford Raptor, BMW, Porsche Macan, Range Rover).
- **FAQ** com as 6 perguntas do site atual, em formato accordion (clique para expandir).
- **Formulário de cotação inteligente**: o cliente preenche veículo, serviço, localização e notas, e o botão "Send via WhatsApp" monta a mensagem automaticamente e abre o WhatsApp — mesma lógica do seu site atual, mas com visual mais premium e animações de entrada.
- Design visual elevado: hero em tela cheia com a foto real de fundo, textura sutil, cards de serviço com efeito de destaque dourado no pacote mais lucrativo (Ceramic Coating), tipografia mais encorpada (Sora + Inter), microanimações ao rolar a página.

## Antes de rodar ads

- [ ] Baixar e hospedar as imagens localmente (ver aviso acima)
- [ ] Confirmar se os preços ainda são os atuais
- [ ] Conectar o domínio e publicar (Netlify, Vercel ou a hospedagem que já usa)
- [ ] Ativar o pixel do Google Ads e/ou Meta Pixel (blocos comentados no `<head>` do `index.html`)
- [ ] Testar o botão "Send via WhatsApp" e o botão flutuante no celular
- [ ] Revisar a lista de áreas cobertas (Londres & Surrey) — hoje é uma lista genérica de exemplo

## Publicar o site

**Netlify** (mais simples):
1. Crie conta grátis em netlify.com
2. Arraste a pasta `godoy-auto-detailing` para app.netlify.com/drop
3. Conecte seu domínio já existente em "Domain settings"

## Reviews do Google ao vivo (widget Elfsight) ✅ Configurado

O widget da Elfsight já está conectado no site — ele fica logo abaixo dos 3 depoimentos fixos, na seção "Reviews", e busca automaticamente as avaliações do seu Google Business Profile.

- Pra mudar o layout, cores ou quantidade de reviews exibidas, acesse seu painel em **elfsight.com** (não precisa mexer no código).
- **Pra garantir que as avaliações mais recentes apareçam primeiro**: no painel da Elfsight, vá em Settings → Content (ou "Filters/Sorting") e defina "Sort reviews by" como **Newest first**. Isso é configuração da conta, não dá pra controlar pelo código do site.
- Adicionei um cabeçalho "Latest Reviews" com indicador "Live from Google" (bolinha verde pulsando) logo acima do widget, deixando claro pro visitante que aquilo é feed ao vivo e mais atual que os 3 depoimentos fixos acima.
- O plano gratuito da Elfsight tem um limite de visualizações/mês — se o site começar a receber bastante tráfego de ads, vale considerar o upgrade pago pra não correr risco do widget parar de carregar.
- Se um dia quiser trocar o widget (outro serviço ou Google Places API), o script fica no fim do `index.html` (`elfsightcdn.com/platform.js`) e o container é a `<div id="liveReviewsSlot">` dentro da seção `#reviews`.

## Rastreamento de ads

No `<head>` do `index.html`, dois blocos comentados — descomente e coloque seu ID:
- Google Ads / GA4: substitua `G-XXXXXXXXXX`
- Meta Pixel: substitua `YOUR_PIXEL_ID`

O `js/script.js` já dispara eventos de conversão (clique no WhatsApp, no telefone, envio do formulário de cotação) automaticamente assim que os pixels estiverem ativos.
