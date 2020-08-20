%rebase('osnova.tpl')

<body align="center">
  <div class="hero-body">
    <h1 class="subtitle">
    <p><b> POZOR!</b> </p>
    <p>Prvi vnosu matrike bodi pozoren da je ta kvadratna. </p>
    <p>Torej, da je število stolpcev enako številu vrstic.</p>
    </h1>
  </div>
</body>

<form action ="/racunanje_sledi/" method="POST">
  <div class="form-group">
    <div class="control">
      <textarea input type="text" class="textarea is-primary" placeholder="Vpiši KVADRATNO matriko:" name="matrika1"  ></textarea>
    </div>

    <div class="buttons">
      <input type="submit" class="button is-primary"  value="IZRAČUNAJ SLED" >
    </div>
  </div>
</form>
