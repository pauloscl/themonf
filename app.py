<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Calculadora de Investimento de Juros Compostos</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" integrity="sha384-0evHe/X+9Au7w6QOoIjz55eTHy2E9jlsq2107QpaqtFx27TVE8BNspGFF6ea90uV" crossorigin="anonymous">
</head>
<body>
  <div class="container">
    <h1>Calculadora de Investimento de Juros Compostos</h1>
    <form action="/" method="POST">
      <div class="mb-3">
        <label for="principal" class="form-label">Valor Inicial (R$):</label>
        <input type="number" class="form-control" id="principal" name="principal" required>
      </div>
      <div class="mb-3">
        <label for="taxa" class="form-label">Taxa de Juros (% a.a.):</label>
        <input type="number" class="form-control" id="taxa" name="taxa" required>
      </div>
      <div class="mb-3">
        <label for="anos" class="form-label">Prazo (anos):</label>
        <input type="number" class="form-control" id="anos" name="anos" required>
      </div>
      <button type="submit" class="btn btn-primary">Calcular</button>
    </form>
    <hr>
    {% if montante %}
      <h2>Montante Acumulado: R$ {{ montante:.2f }}</h2>
    {% endif %}
  </div>
  <footer class="text-center mt-5">
    <p>Desenvolvido por Paulo Sérgio da Themonf Technology</p>
  </footer>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW521D2" crossorigin="anonymous"></script>
</body>
</html>
