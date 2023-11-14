function actualizar_ratio() {
    var valor_ratio = document.getElementById("ratio").value;           //  esto toma el balor de la etiqueta con el id "ratio"
    document.getElementById("valor_ratio").innerText = valor_ratio;        //  esto envia el valor de la variable "valor_ratio" a la etiqueta con el id "valor_ratio"
}

function calcular(){
    var principal = document.getElementById("principal").value;
    var ratio = document.getElementById("ratio").value;
    var años = document.getElementById("años").value; 
    var interes = principal * años * ratio / 100;
    var cantidad = parseInt(principal) + parseFloat(interes);
    var resultado = document.getElementById("resultado");
    
    var year = new Date().getFullYear() + parseInt(años);              //  toma loas años que pusistes y los suma al año actual
    
    if (principal <= 0) {
        alert("Por fabor ingrese un numero positivo !");
        document.getElementById("principal").focus();
    }
    else {                                                              // lo que esta entre las etiquetas "mark" se resalta
        resultado.innerHTML = "Si depositastes $" + "<mark>" + principal + "</mark>" + ",\<br\> a una tasa de interés del " + "<mark>" + ratio + "%" + "</mark>" + "\<br\> Tendras en total $" + "<mark>" + cantidad + "</mark>" + ",\<br\> para el año " + "<mark>" + year + "</mark>" + "\<br\>";
    }
}





