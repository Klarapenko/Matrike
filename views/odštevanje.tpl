%rebase('osnova.tpl')

<body align="center">

       <div class="hero-body">
        <h1 class="subtitle">
            <p><b> POZOR!  </b> </p>
            <p>Prvi vnosu matrik bodi pozoren da sta enakih dimenzij. </p>
        </h1>
        </div>

</body>
     
 

<form action ="/odstevanje/" method="POST">
<div class="form-group">
  <div class="control">
    <textarea input type="text" class="textarea is-primary" placeholder="Vpiši prvo matriko:" name="matrika1" id="matrika1"></textarea>
  </div>

  <div class="control">
    <textarea input type ="text" class="textarea is-primary" placeholder="Vpiši drugo matriko:" name="matrika2" id="matrika2"></textarea>
  </div>


<div class="buttons">
  <input type="submit" class="button is-primary"  value="ODŠTEJ" >
</div>
</div>
</form>

