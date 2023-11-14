function updateRate() {
    var valor_ratio = document.getElementById("ratio").value;           //  esto toma el balor de la etiqueta con el id "ratio"
    document.getElementById("rate_val").innerText = valor_ratio;        //  esto envia el valor de la variable "valor_ratio" a la etiqueta con el id "rate_val"
}

function compute(){
    var principal = document.getElementById("principal").value;
    var rate = document.getElementById("rate").value;
    var years = document.getElementById("years").value; 
    var interest = principal * years * rate / 100;
    var amount = parseInt(principal) + parseFloat(interest);
    var result = document.getElementById("result");
    
    var year = new Date().getFullYear() + parseInt(years);              //  toma loas años que pusistes y los suma al año actual
    
    if (principal <= 0) {
        alert("Por fabor ingrese un numero positivo !");
        document.getElementById("principal").focus();
    }
    else {                                                              // lo que esta entre las etiquetas "mark" se resalta
        result.innerHTML = "If you deposit $" + "<mark>" + principal + "</mark>" + ",\<br\> at an interest rate of " + "<mark>" + rate + "%" + "</mark>" + "\<br\> You will receive an amount of $" + "<mark>" + amount + "</mark>" + ",\<br\> in the year " + "<mark>" + year + "</mark>" + "\<br\>";
    }
}





