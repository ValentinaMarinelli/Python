<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maggiore Somma Precedenti Marinelli</title>
    <style>
        table,th, td {
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <table border-size="1px" id="tab">
        <thead>
        <tr>
            <th>Cont</th>
            <th>Numero</th>
            <th>Somma prec</th>
            <th>Max somma prec</th>
        </tr>
        </thead>
        <tbody id="tbody">

        </tbody>
    </table>
    <p> Per terminare l'inserimento inserire 0 </p>
    <label for="txtNumero"> Inserire n </label>
    <input type="text" id="txtNumero" oninput="numeri()">
    <script>
        let cont=1;
        let sommaPrec=0;
        let stringa;
        let t;
        let max;
        const numero=document.getElementById("txtNumero");
        function numeri(){
            n=Number(numero.value);
            do {
            if(isNaN(n)){
              alert("Non hai inserito un numero")
              return;
            }
            else {
                stringa=document.getElementById("tbody").innerHTML;
                t=document.getElementById("tab");
                stringa+=`<tr><td>${cont}</td>`;
                stringa+=`<td>${n}</td>`;
                stringa+=`<td>${sommaPrec}</td>`;
                cont+=1;
                sommaPrec+=n;
                if(sommaPrec>max) {
                  max = sommaPrec;
                  stringa+=`<td>${"sì"}</td></tr>`;
                }
                else
                stringa+=`<td>${"no"}</td></tr>`;
                tbody.innerHTML=stringa;
            }
        }while(n!=0);
        }
