<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bolletta V2 Marinelli</title>
    <style>
        table,th, td {
            border: 1px solid black;
        }
    </style>
</head>
<body> 
    <p> Inserire codice cliente <input type="number" id="codice"></p>
    <p> Inserire consumo in kw  <input type="number" id="consumo"></p>
    <input type="text" name="" id="iva" disabled value="0.22">IVA<br>
    <input type="text" name="" id="costokw" disabled value="0.03">Costo KW<br>
    <input type="text" name="" id="canone" disabled value="20">Canone<br>
    <button id="add" onclick="btnInserisci()">Inserisci</button><br>
    <button id="add" onclick="btnMostra()">Mostra</button><br>

    <table border-size="1px" id="tab">
        <thead>
        <tr>
            <th>Codice</th>
            <th>Consumo*Costo KWH</th>
            <th>Canone</th>
            <th>Iva</th>
            <th>Totale</th>
        </tr>
        </thead>
        <tbody>

        </tbody>
    </table>
    <script>
            let codCliente;
            let consumo;
            let iva;
            let costokw;
            let canone;
            let totCons;
            let totIva;
            let totale;

            let t=document.getElementById("tab");;
            let tbody=t.children[1];
            let stringa=tbody.innerHTML;

            function btnInserisci(){
                do {
                    codCliente=document.getElementById("codice").value;
                    if(codCliente=="" || isNaN(codCliente)) {
                      alert("Errore")
                      return;
                    }
                }while(codCliente=="" || isNaN(codCliente));
                do {
                    consumo=parseInt(document.getElementById("consumo").value);
                    if(consumo=="" || isNaN(consumo)) {
                      alert("Errore")
                      return;
                    }
                }while(consumo=="" || isNaN(consumo));
                iva=parseFloat(document.getElementById("iva").value);
                costokw=parseFloat(document.getElementById("costokw").value);
                canone=parseFloat(document.getElementById("canone").value);
                totCons=consumo*costokw;
                totIva=totCons*iva;
                totale=totCons+canone+totIva;
                stringa+=`<tr><td>${codCliente}</td>`;
                stringa+=`<td>${consumo}*${costokw}=${totCons.toFixed(2)}</td>`;
                stringa+=`<td>${canone}</td>`;
                stringa+=`<td>${totCons}*${iva*100}%=${totIva.toFixed(2)}</td>`;
                stringa+=`<td>${totale.toFixed(2)}€</td></tr>`;
                document.getElementById("codice").value="";
                document.getElementById("consumo").value="";
            }

            function btnMostra(){
                tbody.innerHTML=stringa;
                
            }

    </script>
</body>
</html>
